<!-- hand-written -->
# Deepening blueprint: F1.5 From Derivations to Mathematical Prose (fd1 Chapter 8), D (stage S1; revised at S2 round 1; reconciled with the delivered Chapters 2–7 and frozen at S2 round 2, 2026-10-25)

**What this is.** A **delta** blueprint (stage S1) that deepens Chapter 8 of *Logic and Proof* under the final layout. It is written **on R5**. The frozen revision blueprint `ch05-revision.md` (R5, S2 passed 2026-10-12) was never drafted: `fd1/src/ch08-from-derivations-to-prose/` is still the R1 text that D2 moved and swept (commit `034a2ae`). The drafter therefore executes R5 §4.0–§4.7 **as content**, then the additions of this file, in one pass. Where this file and R5 disagree, this file wins, and every such point is listed (§2, "R5 items superseded"). The drafter needs: this file; R5 (for everything this file does not change); the current section files; `authoring/STYLE.md` (§12, with §12.8 and §12.13 as amended by D1); `DRAFTING.md` (with `\purpose`, `\taut` and the Diagrams templates of `latex/book-diagrams.sty`); and `NOTATION.md`.

**Line numbers** are those of the current files at commit `034a2ae`, written `01:263` for `01-connective-rhetoric.md` line 263, `ix:11` for `index.md`. D2 changed no line count in this chapter, so R5's line numbers (taken at `da6e12e`) are the same lines. They were spot-checked: 01:83, 01:380, 02:139, 03:13, 03:42, 06:28, 07:34, 07:123.

**Inputs.**
- The deepening plan (`plan.md` §3.0 devices; §3.6 "Chapter 6", which is now Chapter 8, 6.k → 8.k; and its binding *Critic review*).
- `layout-final.md`: §1.3, Part III, Chapter 8; §3, size and Time; §4.1, the migration table; §6.1, what of R5 stands; §2, the dependency rules.
- `labelmap.json`: 72 entries land in 8.x, all from 5.x, and none leaves.
- `gap-matrix.md`, for **techniques only**: rows 1.9, 1.12, 2.12, 3.6, 7.4, 7.5, 7.7, 7.8, 7.10, 9.1 and 9.2, and the device rows "stock characters / dialogues" and "dialogue extraction".
- STATUS rows touching F1.5.
- `fd1/authoring/ledger/ch08.yaml`: 81 items, all passed at S5–S8 (2026-10-11).

Every example, drill, exercise, figure and answer below was written for this book, in mathematical dress, with school mathematics first. No text, example, exercise or figure is taken from any of the twelve books or closely paraphrased (plan, binding rule 3). The classic named items used here are told in fd1's own words and numbers. They are the barber, the "and so on" of an iteration, the two-node Kripke model, the double-negation translation and Glivenko's theorem.

**Binding rules for this deepening.**
1. **No label is lost, renamed or moved.** All 72 anchors of the chapter keep their names, their sections and the content of every cited block (§3.1): 69 block labels and the 3 heading ids `what-the-sentence-does-not-say`, `one-extra-rule` and `what-a-proof-provides`. R5's eight new labels are created as R5 says. This file adds 29 labels and one heading id (§3.2). No label moves in or out of the chapter (`labelmap.json`).
2. **Cited content stays.** `exm-not-allowed-catalogue` is cited 110 times outside the chapter. (N1)–(N10) stay verbatim and (N11) as R5 splits it (§4.6, "The (N11) decision"). (N12)–(N14) are **appended** inside the same enumerate. Nothing else in the block changes. The following are kept as R5 keeps them: `def-levels-of-proof` and `def-silent-steps` verbatim; `exm-rhetoric-universal`, `-existential` (R5's two phrases), `-induction`; `exr-connective-rhetoric-c1` (frozen); `thm-irrational-power-rational`; `prp-log2-9-irrational`.
3. **Final numbering everywhere.** Every pointer is written in the final layout's numbering (§6). Chapter 8 is the last chapter of the volume. It points back into Chapters 1–7, within itself, and forward only to later volumes, in the three Looking-ahead boxes R5 placed (8.3, 8.6, 8.7). The new optional Section 8.8 has no Looking-ahead box.
4. **Critic review C1 (soundness for predicate logic).** Chapter 8 cites first-order soundness only through the statement under the heading `#from-counter-models-to-non-derivability` in Section 7.2, as a black box. It never cites `thm-first-order-soundness` or `cor-counter-model`, which are in the optional Section 7.3. Every "the soundness statement for predicate logic in Section 7.2" (06:14, 07:18, 07:77, 07:258; R5 moves 06:14's into fold F5.6-a) links that heading if the engine resolves heading ids (fd2's S3 note says this is untested). Otherwise it stays prose: "Section 7.2, 'From counter-models to non-derivability'". This is the one `b` edge of `F1.5: {s: [F1.8], b: [F1.6]}`.
5. **Critic review C2 (TAUT).** TAUT is named only as the propositional rule of 4.8 (`def-rule-taut`) and its extension to the propositional skeleton of 6.3 (`def-propositional-skeleton`, `prp-taut-skeleton`). It is never a licence for a first-order validity (§4.3, item 2). A law used on a part under a quantifier is credited to 6.2's syntactic `prp-replacement` and never to completeness. One existing solution does this silently, 8.7 R1 at 07:462, and gets one clause (§4.7, item 4). TAUT is a classical licence: it rests on completeness, whose proof uses LEM (@lem-atom-splitting). So it is excluded wherever a task or a theorem says "without RAA": 8.7's definition of an intuitionistic derivation (§4.7, item 5), 8.7 B5, `thm-kripke-soundness`, 8.8 B2 and C1 (S2 round 1).
6. **Critic review C3, smaller correction 1, and the trunk.**
   - Chapter 8 uses no group example and nothing from 7.5's second-pass half.
   - Every Γ in Chapter 8, including 8.8's, is a finite list, as in `def-derivable`.
   - "Definitional extension" (smaller correction 6, now in 5.8) is collected as a dictionary row in 8.2.
7. **Non-derivability wording (G10).** Chapter 8 comes after 4.7 and 7.2, so a propositional "not derivable" may cite `cor-refuting-row`.
   - A claim that something is **not derivable without RAA** is proved only in the optional 8.8 (Kripke models) or in 4.7's optional `thm-raa-independent`. Everywhere else it is "stated without proof", as R1 already words it.
   - **Derive-or-break lists hold only settled claims.** The verdict-withheld items of 8.6 (B3) and 8.8 (B2) contain only claims whose verdict this file settles with a derivation, a counterexample or a Kripke countermodel.
   - 8.7 has no derive-or-break list, since "breaking" without RAA needs 8.8.

---

## 1. The volume-wide devices, as applied to Chapter 8

Chapter 8 has **no rule sections** (R5 §1), so the devices are used where they fit (STYLE §12.13: "other fd1 sections use the ones that fit").

D1. **Purpose-annotated assumptions** (§12.13.1). `fd1/config/config.json` already sets `"fitch-purposes": "infer"`, so every derivation in Chapter 8 prints "asm, for →I", "asm, for ¬I", "asm, for RAA", "asm, for ∨E", "asm, for ∃E", "asm, for ↔I" and "asm, for ∀I" (bounded ∀I) with no edits.
- 8.1 gains the **spoken purposes** paragraph: each annotation read aloud as its prose opening (§4.1, item 1). This is the plan's "spoken assumption purposes" row, and the seam that ch01-deepen §6 records ("8.1's 'spoken assumption purposes' row reads 1.4's annotation").
- 8.4's first self-explanation question reads the annotation (§4.4, item 1).
- `\purpose` is written by hand only in partial derivations. There is one exception: R5's scaffolded 8.3 B2, whose blanks (ii)–(ix) ask for the very closing justifications that a purpose would print. Its assumptions get **no** `\purpose`, and S4 accepts `check_fitch.py --purposes` notes on that one block (§10).

D2. **Rule-instance galleries: not adopted.** There is no rule card per section (R5 §1, D10). Each dictionary row already has its own analysis sentence and annotated example, which do the gallery's work. The look-alike's work is done by the Not-allowed blocks (D3).

D3. **"Not allowed" blocks** (§12.13.3), adapted to prose: a `::: {.warning}` titled `[Not allowed: …]`, three to five wrong **sentences**, each tagged with the catalogue entry (N1)–(N14) or the item of `def-silent-steps` it breaks.
- One block each in 8.1 (connective phrasing), 8.2 (quantifier phrasing) and 8.8 (misreadings of forcing).
- 8.3, 8.5 and 8.6 get none:
  - 8.3's warning "Level 3 is not level 0 with steps missing at random" and 8.5's two warnings already play the part.
  - 8.6's catalogue is the master list.
- Pointers from 8.1 and 8.2 to entries of 8.6 are pointers **within the chapter**, which R5 allows. They are tags, never reasons. Chapter 1 recorded the deviation that kept such tags out of Chapter 1 (ch01-deepen D3), and the reason does not apply here.

D4. **The counterexample set.** It returns twice, by name.
- In 8.6 the two-column check says that a line which follows and is false has a false line above it.
- In 8.8 a Kripke countermodel is "a stage that forces every member of Γ and not ψ", and the text says once that this is the counterexample set Γ, ¬ψ read at a stage, for logic without RAA. That sentence is the last link of the thread of layout §1.2: break it (1.1) → inconsistent (3.2) → refuting row (4.5–4.6) → soundness (4.7) → counter-model (7.2) → theory (7.4) → here, stages.

D5. **Derive-or-break items with the verdict withheld:** two.
- 8.6 B3, "Correct, or which entry?": five short proofs, verdict withheld, look-alikes seeded.
- 8.8 B2, "Derive without RAA, or break with a Kripke model": seven claims.

Binding rule 7 governs both.

D6. **Drill banks of 12: this blueprint's choice, not a STYLE floor.** Every section has an `[A2: Drill]` of **12 parts**, answered in one folded solution, one or two lines a part.
- R5's four banks grow: 8.1 from 10 to 12, 8.2 from 10 to 12, 8.3 from 8 to 12, 8.6 from 8 to 12.
- Four banks are new: 8.4, 8.5, 8.7, 8.8.
- In all, 8 banks and 96 parts; the 84 parts of 8.1–8.7 are core.
- **Deviation from layout-final, recorded as a choice.** STYLE §12.8 sets its bank size (15 in Chapters 1–2, 12 elsewhere) for **rule sections**, and Chapter 8 has none (D2; R5 §1). Layout §3 and §10 decision 7 give prose sections banks of 8, and that would meet the layout's Time target (§5: about 33.8 h). This file nevertheless gives every section 12 parts, matching the author's choice of the heavier workload (2026-10-12) that set §12.8's numbers. The cost is about +3.5 core hours (§5). It is an S9 judgment call (§10): banks of 8 are the fallback, and nothing else in this file depends on the bank size.
- The ramp in a prose section: recognise the rule a phrase carries → decide silent or spoken → judge a step (face, costume, entry, legal or not) → construct (write the sentence, the skeleton, the column).

D7. **One fixed key and reading back.** Chapter 8 translates no sentences of its own; 6.1 and 3.3 own translation and extraction. The "reading back" check is the core of 8.1–8.3, prose against derivation, and needs no new device. 8.4 recalls 3.3's argument extraction in one sentence (§4.4, item 2).

D8. **Chapter close** (§12.13.5). `index.md` ends with `## Summary` and `## Terms`, gains the "Minimum for fd2" line (layout G14), and gets the "What you need" line of layout §1.3 (§4.0). The Terms list is written for merging into `src/glossary.md` in the whole-volume pass.

D9. **"Used later" marker.** One item: 8.2 B3 (`exr-quantifier-rhetoric-b3`, "6 divides n exactly when 2 and 3 do"), which 8.5 B4's solution cites by label. A later exercise may cite an earlier one (STYLE §6), and no proof in the text rests on it.

D10. **Pictures where the structure is spatial** (DRAFTING, Diagrams):
- R5's four 8.2 pictures, drawn with the templates where they fit (§4.2, item 5);
- one new flowchart in 8.6 ("checking one line");
- two Kripke models in 8.8 (`structure` template).

Every new figure is given below in full. It is a raw LaTeX block with the `tikzpicture` written out, with no colours and no white fills.

D11. **Not adopted in Chapter 8, with reasons.**
- (a) Galleries (D2).
- (b) The plan's "non-mathematical argument annotated line by line" for 8.4 [Co]: the mathematical register rules it out, and 3.3 owns argument extraction (layout §6.1).
- (c) The plan's inline "(Why?)" prompt, for the reason of ch01-deepen D11(a).
- (d) A C item on the disjunction property (gap-matrix row 9.1). Its proof needs completeness for Kripke models, which 8.8 only states. 8.8 states the property in a remark, without proof.
- (e) Snapshots: there are no rule sections (R5 §1).

---

## 2. Section map, and what each section gains

| § | Title | File | Status | Main line: R5 budget → final budget | What this file adds (details in §4) |
|---|---|---|---|---|---|
| index | From Derivations to Mathematical Prose | `index.md` | — | R5 ≤ 1,100 → ≤ 1,300 | "What you need" per layout; Minimum for fd2; roadmap bullet for 8.8; two named moves; Summary; Terms; Time recomputed |
| 8.1 | The Connective Rules in Prose | `01-connective-rhetoric.md` | core | ≤ 4,750 → ≤ 5,000 | spoken purposes; constructive-dilemma row; `## Equivalent conditions, by a cycle` (`exm-rhetoric-cycle`); Not allowed; three folds; A2 to 12; B4 |
| 8.2 | The Quantifier Rules in Prose | `02-quantifier-rhetoric.md` | core | ≤ 3,700 → ≤ 4,200 | `## Definitions, descriptions and sets` ("we define", "the limit", double inclusion, `exm-rhetoric-double-inclusion`); the two "stronger" rows; Not allowed; A2 to 12; B3 (used later) |
| 8.3 | Four Levels of One Proof | `03-levels-of-abbreviation.md` | core | ≤ 4,000 → ≤ 4,200 | silent steps tied to TAUT (4.8, 6.3); `## It suffices to show, as a column` (`exm-suffices-column`); one fold; A2 to 12; B3 |
| 8.4 | Reading a Proof: Self-Explanation | `04-reading-proofs.md` | core | ≤ 2,000 → ≤ 2,200 | the purpose in question 1; `## Naming the unstated fact` (3.3 recalled); A2 (new, 12); B3 |
| 8.5 | Writing a Proof | `05-writing-proofs.md` | core | ≤ 2,600 → ≤ 2,800 | `## Generalising a proof` (`exm-generalise-proof`); one fold; A2 (new, 12); B4; C3 (√2 → √3, not √4) |
| 8.6 | Checking Proofs, and What Is Not Allowed | `06-checking-proofs.md` | core | ≤ 2,600 → ≤ 3,000 | flowchart; (N12)–(N14) appended; two new families; improper but valid; traditional names; A2 to 12; B3 (verdict withheld); R1 (a dialogue) |
| 8.7 | The Dispute over Excluded Middle | `07-excluded-middle.md` | core | ≤ 3,800 → ≤ 3,900 | `## Which laws survive without RAA {#laws-without-raa}`; stated claims point to 8.8; one fold; A2 (new, 12); B5 |
| 8.8 | Stages of Knowledge: Kripke Models | `08-kripke-models.md` (**new**) | **optional** | — → ≤ 3,600 | the whole section (§4.8) |

The budgets are those of layout §1.3, except the index (D8; layout ≤ 1,000) and 8.1 (layout ≤ 4,900; S2 round 1 re-estimated it from the quoted text, §4.1). Each stays at or under STYLE's 5,000.

**R5 items superseded by this file** (layout §6.1 lists the first four):
- (i) "Chapter 5" → Chapter 8, everywhere. R5 already writes Sections 8.x in its quoted text; its section labels "5.1"–"5.7" and fold ids "F5.x-y" are internal names. The drafter titles R5's folds as R5 says, and the new folds are named F8.x-y.
- (ii) R5 §4.0 item 5, "What you need": replaced (§4.0, item 2).
- (iii) R5 §5's budgets of 8.1, 8.2, 8.4 and 8.6, its exercise totals and its Time line: replaced by §2 and §5.
- (iv) R5 §4.0 item 6's "about 31 hours … 47": replaced by §5.
- (v) R5 §1 item 5, "drill banks only in 8.1, 8.2, 8.3, 8.6, 8–10 parts": replaced by D6.
- (vi) R5 §4.0 item 7: the roadmap gains an eighth bullet, for 8.8.
- (vii) R5 §4.7's "stated without proof" sentences that 8.8 now proves gain a pointer (§4.7, item 2).
- (viii) R5 §4.7's "B4 … its solution 07:24–28 verbatim": part (b) is recomputed against the delivered Chapters 3–7 (§4.7, item 6; S2 round 1).
- (ix) R5 §4.1 item 14's "01:264–304 verbatim": 01:304 moves verbatim into fold F8.1-f (§4.1, item 6; S2 round 1).

Nothing else in R5 changes.

---

## 3. Labels

### 3.1 Every label now in the chapter (72): all kept, in place

All 72 anchors (`labelmap.json`, every one "5.k → 8.k") keep their names and sections. The 9 cited outside the chapter keep their content (layout §4.3). Each is listed with its citation count outside the chapter:

| Label | Citations outside |
|---|---|
| `exm-not-allowed-catalogue` | 110 |
| `def-levels-of-proof` | 6 |
| `exm-rhetoric-induction` | 4 |
| `exr-connective-rhetoric-c1` | 3 |
| `def-silent-steps` | 3 |
| `exm-rhetoric-universal` | 1 |
| `exm-rhetoric-existential` | 1 |
| `thm-irrational-power-rational` | 1 |
| `prp-log2-9-irrational` | 1 |

R5 §3.1 gives each label's R5 status. The table below lists only the blocks that **this file** changes beyond R5.

| Label | Where | Change by this file | Cited outside |
|---|---|---|---|
| `exm-not-allowed-catalogue` | 06:28 | entries (N12), (N13), (N14) **appended** after (N11) inside the same enumerate; (N1)–(N11) as R5 leaves them | 110 (all cite (N1)–(N11) by number; unchanged) |
| `exr-connective-rhetoric-a2` (R5 new) | 8.1 | 10 → 12 parts | — |
| `exr-quantifier-rhetoric-a2` (R5 new) | 8.2 | 10 → 12 parts | — |
| `exr-levels-of-abbreviation-a2` (R5 new) | 8.3 | 8 → 12 parts | — |
| `exr-levels-of-abbreviation-b2` | 03:384 | R5's scaffold printed **without** `\purpose` (D1) | — |
| `exr-checking-proofs-a2` (R5 new) | 8.6 | 8 → 12 parts | — |
| `exr-excluded-middle-b1` | 07:265 | solution's last sentence (07:304): "(we state this without proof)" → "(the optional Section 8.8 proves it with a two-stage model)", a prose pointer, since 8.8 is later | — |
| `exr-excluded-middle-r1` | 07:447 | solution 07:462 gains one clause crediting `prp-replacement` (Critic C2) | — |
| `exr-excluded-middle-r3` | 07:511 | solution 07:558's first sentence gains "(the optional Section 8.8 proves it with a two-stage model)" | — |
| prose 07:11–16 | 8.7 | the table cell 07:15 gains a prose pointer to the optional Section 8.8 (§4.7, item 2) | — |
| prose 05:165 | 8.5 | moves verbatim into fold F8.5-c (it sits after `exm-subset-bounded-above` in R5's order) | — |
| prose 03:80 and 03:82 | 8.3 | move verbatim into fold F8.3-d | — |
| prose 01:241, its last three sentences | 8.1 | move verbatim into fold F8.1-d | — |
| prose 01:304 (the costumes' "one smell" paragraph) | 8.1 | moves verbatim into fold F8.1-f (S2 round 1, budget) | — |
| prose 02:124 | 8.2 | moves verbatim into fold F8.2-b | — |
| prose 07:212 and the Lean block 07:214–221 | 8.7 | move verbatim into fold F8.7-c | — |

Label prefixes follow the file stem and never change. New exercises use the existing stems (`connective-rhetoric`, `quantifier-rhetoric`, `levels-of-abbreviation`, `reading-proofs`, `writing-proofs`, `checking-proofs`, `excluded-middle`) and, for the new file, `kripke-models`.

### 3.2 New labels

R5's eight are created as R5 §3.2 says: `exr-connective-rhetoric-a2`, `-b3`; `exr-quantifier-rhetoric-a2`; `exr-levels-of-abbreviation-a2`, `-c3`; `exr-reading-proofs-c2`; `exr-checking-proofs-a2`; `exr-excluded-middle-b4`. This file adds **29 labels and 1 heading id**. A grep of `fd1/src`, `fd2/src`, `fd3/src`, `fd4/src` and `an1/src` on 2026-10-13 finds none of them.

| § | Label | Kind | Main line, fold or exercises |
|---|---|---|---|
| 8.1 | `exm-rhetoric-cycle` | worked example (TFAE by a cycle) | main |
| 8.1 | `exr-connective-rhetoric-b4` | B item | exercises |
| 8.2 | `exm-rhetoric-double-inclusion` | worked example | main |
| 8.2 | `exr-quantifier-rhetoric-b3` | B item, used later | exercises |
| 8.3 | `exm-suffices-column` | worked example, two parts | main |
| 8.3 | `exr-levels-of-abbreviation-b3` | B item | exercises |
| 8.4 | `exr-reading-proofs-a2`, `-b3` | drill; B item | exercises |
| 8.5 | `exm-generalise-proof` | worked example | main |
| 8.5 | `exr-writing-proofs-a2`, `-b4`, `-c3` | drill; B; C | exercises |
| 8.6 | `exr-checking-proofs-b3`, `-r1` | B item (verdict withheld); R item | exercises |
| 8.7 | `laws-without-raa` | heading id of the new subsection | main |
| 8.7 | `exr-excluded-middle-a2`, `-b5` | drill; B item | exercises |
| 8.8 | `def-kripke-model`, `def-forcing` | definitions | main |
| 8.8 | `lem-heredity` | lemma (statement main, proof fold) | main + fold |
| 8.8 | `thm-kripke-soundness` | theorem (statement and rule table main, proof fold) | main + fold |
| 8.8 | `cor-kripke-countermodel` | corollary with proof | main |
| 8.8 | `exm-two-stage-model`, `exm-three-stage-model` | worked examples | main |
| 8.8 | `exr-kripke-models-a1`, `-a2`, `-b1`, `-b2`, `-c1`, `-c2` | exercises | exercises |

The 8.8 results carry no `.optional` class of their own: the section is the optional unit, as in 7.3 (03:3). The drafter greps again before creating each label (DRAFTING, "Labels").

**Planned labels of other units that this file cites.** Each is fixed in layout §1.4. **All are delivered under these names and in these sections** (S2 round 2: grepped in `fd1/src/ch04–ch06`), so S8 only re-greps them.
- `def-rule-taut` (4.8)
- `thm-monotonicity` (4.9, second pass; cited only in a fold)
- `thm-barber` (5.6)
- `exm-extensionality-logical-half` (5.7)
- `def-definite-description` and `prp-definitional-extension` (5.8)
- `prp-replacement` (6.2)
- `def-propositional-skeleton` and `prp-taut-skeleton` (6.3)

### 3.3 Bookkeeping (coordinator, S4)

- `fd1/authoring/ledger/ch08.yaml`:
  - R5 §3.3's re-keys: `exm-rhetoric-conjunction` → `exr-connective-rhetoric-b3`, and `exr-reading-proofs-c1` → `-c2`, each with a new entry for the reused label.
  - New entries for R5's eight labels and this file's 29.
  - `exm-not-allowed-catalogue` changes hash. Its S5–S8 verdicts go stale and the block is re-reviewed; (N1)–(N11) are diffed against the current text at S4.
  - Every touched block goes stale by hash, as in R5.
- `fd1/verify/ch08/` (D2 moved it from `ch05`):
  - R5's sidecars.
  - New, for this file's blocks:
    - `exm-rhetoric-cycle.py`: the parity of \( n \), \( n^2 \) and \( n^2 + 2n \) on \( |n| \le 200 \); the identities.
    - `exm-rhetoric-double-inclusion.py`: \( x^2 \le 2x \iff 0 \le x \le 2 \), exactly on rationals and on a grid.
    - `exm-suffices-column.py`: \( x^2 - 6x + 10 = (x - 3)^2 + 1 \); \( \abs{(2n + 1)/(n + 1) - 2} = 1/(n + 1) \).
    - `exm-generalise-proof.py`: one of \( n \), \( n + 1 \), \( n + 2 \) divisible by 3, for \( |n| \le 300 \); \( 17 = 3 \cdot 5 + 2 \).
    - `exr-connective-rhetoric-b4.py`
    - `exr-quantifier-rhetoric-b3.py`
    - `exr-levels-of-abbreviation-b3.py`
    - `exr-reading-proofs-b3.py`: the identity; the claim at \( x = -3 \) and on \( [-2, 10] \).
    - `exr-writing-proofs-b4.py`
    - `exr-writing-proofs-c3.py`: squares mod 3 and mod 4; \( n = 2 \).
    - `exr-checking-proofs-b3.py`
    - `exr-excluded-middle-b5.py`: a truth-table check that each sequent is valid; derivations by `check_fitch.py`.
    - `def-kripke-model.py` (first named `kripke.py`): a finite Kripke-model checker. It evaluates forcing at every stage of every model in 8.8 and in the 8.7 table, checks heredity on all formulas up to depth 4 over \( p, q, r \) in each model, and confirms every forced/not-forced claim of §4.8. D0 (h) built a finite-structure checker for S3/S6; `kripke.py` reuses its reachability code if present.
  - Updated: `exm-not-allowed-catalogue.py` ((N12)–(N14) instances), and the four extended A2 scripts.
  - The new A2 banks of 8.4, 8.5, 8.7 and 8.8 get scripts only where a part has values (each is named in §4).
- `authoring/STATUS.md`: the promise rows of §6.2.
- The F1.5 row of the chapter table records "R5 + D".

---

## 4. Per-section plans

Budgets: **main line** = `prose_words` of `tools/check_structure.py`, outside `.second-reading` folds and before `## Exercises`. The "now" figures were measured on the current files with everything from `## Exercises` on cut, on 2026-10-13: 8.1 4,401; 8.2 3,129; 8.3 4,064; 8.4 1,895; 8.5 2,413; 8.6 2,240; 8.7 3,781; total 21,923. These equal R5's. The "R5" figure is R5's budget; the "expected" figure is after R5 and this file.

### 4.0 `index.md`

**Budget:** ≤ 1,300 words (R5 ≤ 1,100; layout ≤ 1,000). The addition is the Summary (~170) and the Terms (≤ 220), which every deepened index carries, as ch01's does (1,246 words). Index pages are not counted for Time. Fold ≤ 300 (R5's F5.0-a, extended by item 2).

R5 §4.0 is executed, with these changes.

1. **Motivating question** (new, one italic sentence after R5's second hook, before "The chapter in one paragraph"): "*The question of this chapter: when a proof is written in sentences, where did its boxes go, and how does a reader find them again?*" (It restates the hook's "Where did the boxes go?" of ix:7, which R5 cuts with the analysis paragraph.)
2. **What you need** (layout §1.3 replaces R5 §4.0 item 5's lead). The first sentence: "**What you need.** Chapters 1–6, core. From Chapter 7, only the statement in Section 7.2 under 'From counter-models to non-derivability', that a derivation with the quantifier rules never leads from true premises to a false conclusion; Sections 8.6 and 8.7 use it as a fact." Then R5's four bullets, unchanged. Then fold F5.0-a, `title="Every earlier result this chapter cites"`: ix:11 from "From Chapters 1 and 2:" to its end, verbatim, with R5's one change, and two sentences appended:
   - "From Chapter 7: the statement of Section 7.2 named above (its proof is the optional Section 7.3)."
   - "For the optional Section 8.8: structural induction (@thm-structural-induction) and the proof of @thm-soundness."
3. **Time** (recomputed by the drafter from the delivered text, §5). The expected line is "About 35 hours on the core track (all of A, one B and one C per section, the exit checks); about 65 hours for everything." The drafter does not shade it down (STYLE §11.9).
4. **Minimum for fd2** (new, one line, after Time; layout G14): "**Minimum for fd2.** Chapters 1–6 and 8, core; Chapter 7 (Sections 7.1–7.2) before *Sets and Functions*, Chapter 3."
5. **Roadmap.** R5's seven bullets, with these changes:
   - The 8.1 bullet adds "the spoken purpose of a box; the constructive dilemma and equivalent conditions proved by a cycle" after "the classical rules".
   - The 8.2 bullet adds "definitions, 'the' and double inclusion" after "unique existence".
   - The 8.3 bullet adds "; which silent steps are truth-functional; 'it suffices to show' written as a column" before "; how to check".
   - The 8.4 bullet adds "; naming the unstated fact".
   - The 8.5 bullet adds "; generalising a proof".
   - The 8.6 bullet becomes "Two questions for every line; the catalogue (N1)–(N14) in seven families; four student proofs checked line by line (and, in a fold, the errors' traditional names)."
   - The 8.7 bullet adds "; which laws survive without the rule".
   - Eighth bullet (new): "**Stages of knowledge: Kripke models** (optional). A semantics in which knowledge grows by stages; the rules without RAA are sound for it, and two or three stages show which laws need RAA."
6. **Named moves.** R5's six (ix:27-32), verbatim, then two more:
   - "**Write the reductions as a column.** Each 'it suffices to show' is one row with its reason; read upwards, the column is the proof. (Section 8.3)"
   - "**Generalise by a fresh name.** Replace the particular object by a new letter, and keep only the lines that still hold for it. (Section 8.5)"
7. **`## Summary`** (new, ~170 words, four to six sentences; STYLE §12.13.5). The points, in order:
   - A written proof is a derivation in sentences. Every rule has its phrases, and "let", "suppose", "choose" and "in either case" are the boxes, spoken (8.1–8.2).
   - The chapter named four levels of one proof (@def-levels-of-proof), and fixed by one principle which steps plain prose may leave unsaid (@def-silent-steps). A doubtful sentence is checked by expanding it to a skeleton.
   - It gave a habit for reading (self-explanation), a procedure for writing, and, for checking, two questions and a catalogue of fourteen errors (@exm-not-allowed-catalogue).
   - It ended with the one rule mathematicians have disputed. Without RAA, excluded middle has no derivation (the optional @thm-raa-independent) and yet cannot be refuted (@prp-not-not-excluded-middle). An irrational power of an irrational number can be shown rational with or without a named witness (@thm-irrational-power-rational, @prp-log2-9-irrational). The optional Section 8.8 proves, with stages of knowledge, which classical laws need the rule.
   - What is open is what the logic is for. *Sets and Functions* writes its proofs at levels 2 and 3 with these tools, and its first question is what a set is.
8. **`## Terms`** (new, ≤ 220 words, alphabetical, each line ≤ 9 words, every entry linked):
   - **BHK reading**: a proof as a construction of what it claims (@what-a-proof-provides).
   - **costume**: a direct or contrapositive proof dressed as contradiction (@exm-costume-direct).
   - **double inclusion**: \( A = B \) shown as \( A \subseteq B \) and \( B \subseteq A \) (@exm-rhetoric-double-inclusion).
   - **forcing** (optional): what a stage of knowledge makes true (@def-forcing).
   - **heredity** (optional): what a stage forces, every later stage forces (@lem-heredity).
   - **intuitionistic logic**: the rules of this book without RAA (@one-extra-rule).
   - **Kripke model** (optional): stages of knowledge, with atoms that stay known (@def-kripke-model).
   - **levels of proof**: derivation, skeleton, annotated prose, plain prose (@def-levels-of-proof).
   - **not-allowed catalogue**, (N1)–(N14): recurring errors, each with the rule broken (@exm-not-allowed-catalogue).
   - **self-explanation**: naming each line's warrant, never paraphrasing it (@exm-self-explanation).
   - **silent step**: a step plain prose may leave unwritten (@def-silent-steps).
   - **skeleton**: level 1, the boxes and the logical lines (@def-levels-of-proof).
   - **TFAE by a cycle**: several conditions shown equivalent by a loop of implications (@exm-rhetoric-cycle).

**Sidecar:** none (the Summary repeats no value).

### 4.1 Section 8.1: The Connective Rules in Prose (`01-connective-rhetoric.md`)

**Budget:** main line ≤ 5,000 (now 4,401; R5 ≤ 4,750; layout ≤ 4,900; expected about 4,970); folds ≤ 850 (R5 ≤ 450, plus F8.1-d ~110, F8.1-e ~220, F8.1-f ~63). No Looking-ahead box (R5).

**The estimate (S2 round 1).** The S1 figure, "expected ~4,890", did not add up: R5 puts 8.1 at about 4,745, and the S1 additions measured about +645 against F8.1-d's −110, for about 5,390. The estimate below is built from the text quoted in this section, by `prose_words`-style counts of each passage:
- R5's main line, about 4,745;
- F8.1-d (item 5), −110; F8.1-f (item 6), −63;
- the purpose paragraph (item 1), +120; its Quick check moves to A2 (h) and costs no main-line words;
- the dilemma row (item 2), +45; the S1 sentence appended to 01:137 is dropped;
- the cycle subsection (item 3): lead +40, row +25, Quick check +55. `exm-rhetoric-cycle` (~145) and its commentary (~75) go into fold F8.1-e;
- Not allowed (item 4), +110.

That is about 4,970, under STYLE's 5,000 and about 70 over the layout's 4,900, a deviation recorded in §2 and §5. Had `exm-rhetoric-cycle` stayed on the main line, 8.1 would come to about 5,115, over STYLE's cap. **Fallback** if S3 still measures 8.1 over 5,000: the Not-allowed block drops its last line, the (N7) case (about −25; three lines remain, D3's minimum), and the purpose paragraph drops its last sentence (about −17).

R5 §4.1 is executed in full. Additions, in the order of the file:

1. **The purpose of a box, spoken** (new paragraph, ~120 words, at the end of R5's new `## The rule card`, after its Quick check, under the bold lead-in `**The purpose of a box, spoken.**`) [technique: LB, purpose-annotated assumptions; plan §3.0.1]. Text:

   "Since Section 1.4 every derivation in this book has printed, beside an assumption, the rule that will close its box: 'asm, for →I', 'asm, for ¬I', and so on. Prose says the same thing with the sentence that opens the box. 'Suppose \( P \)' is asm, for →I. 'Suppose \( P \); … this is impossible', or 'if \( P \) were true', is asm, for ¬I. 'Suppose, for a contradiction, that not \( P \)' is asm, for RAA. 'Case 1: \( P \)' is asm, for ∨E. 'Choose \( a \) such that \( P(a) \)' is asm, for ∃E. '\( (\Rightarrow) \) Suppose \( P \)' is asm, for ↔I. 'Let \( x \in A \)' is asm, for ∀I, its bounded form. A box whose purpose the reader cannot hear is a box the writer did not open in words."

   No Quick check follows it on the main line (S2 round 1, budget). Its check, the √5 opening, is A2 (h).

2. **Constructive dilemma** (a new row in the table of `## Disjunction and cases`, 01:130–135, after the DS row; plus one sentence appended to 01:137) [technique: LB, Hu — derived rules heard in prose; ch01-deepen §6 seam].

   Row: | constructive dilemma (@exm-constructive-dilemma; the derived rule CD of Section 2.3, @exr-derived-rules-b4) | "if \( P \) then \( R \), and if \( Q \) then \( S \); since \( P \) or \( Q \), we get \( R \) or \( S \)"; "in the first case …, in the second …, so \( R \) or \( S \)" | never the split or the two implications; the closing "so \( R \) or \( S \)" yes |

   No sentence is appended to 01:137 (S2 round 1, budget): the row's first column cites the worked example, whose reading in Section 1.6 the row abbreviates.

3. **`## Equivalent conditions, by a cycle`** (new subsection, ~120 words on the main line and ~220 in fold F8.1-e, after `## The biconditional`, 01:219–242, and before `## The three faces of "by contradiction"`) [technique: LB — TFAE by a cycle; gap-matrix row 3.6].

   Lead: "Theorems often say that several conditions are equivalent ('the following are equivalent', TFAE). Proving each pair both ways would take six implications for three conditions. A **cycle** takes three."

   Table row: | TFAE by a cycle (@prp-equivalence-cycle) | "the following are equivalent"; "we prove (i) ⇒ (ii) ⇒ (iii) ⇒ (i)" | never any arrow of the cycle, the last one included |

   Then **fold F8.1-e** `title="A cycle, worked"` (new, S2 round 1, budget; ~220 words), a sibling after the table, holding **`exm-rhetoric-cycle`** and its commentary. The main line keeps the lead, the row and the Quick check, which teach the move with the fold closed (STYLE §12.0's test); B4 is then the reader's first full cycle on the main track. A worked example in a fold is numbered, labelled and citable as on the main line (§12.0), and nothing outside 8.1 cites it.

   **`exm-rhetoric-cycle`** `[Three conditions, one cycle]` (S2 round 1: replaced; the S1 version used the conditions \( n \), \( n^2 \), \( n^3 \) odd, a pattern too close to a published exercise). Statement: "Let \( n \) be an integer. Prove that the following are equivalent: (i) \( n \) is odd; (ii) \( n^2 \) is odd; (iii) \( n^2 + 2n \) is odd. Tag the steps that carry the logic."

   Solution: "By @prp-equivalence-cycle it suffices to prove (i) ⇒ (ii), (ii) ⇒ (iii) and (iii) ⇒ (i).
   - (i) ⇒ (ii) is the direction \( (\Rightarrow) \) of @thm-odd-iff-square-odd.
   - (ii) ⇒ (iii): Suppose \( n^2 \) is odd [asm, for →I], say \( n^2 = 2a + 1 \) [∃E]. Then \( n^2 + 2n = 2(a + n) + 1 \), which is odd [∃I, witness \( a + n \)].
   - (iii) ⇒ (i): Suppose \( n^2 + 2n \) is odd. By (E1), \( n \) is even or odd [∨E].
     - If \( n \) is even, say \( n = 2k \), then \( n^2 + 2n = 2(2k^2 + 2k) \) is even. So \( n^2 + 2n \) is even and odd, which (E2) forbids [¬E]: this case cannot occur [⊥E].
     - If \( n \) is odd, there is nothing more to show.
     - So \( n \) is odd.

   The cycle closes."

   Then, still inside F8.1-e, after the solution (~75 words): "Three implications did the work of six. The last arrow, (iii) ⇒ (i), is the one a hurried writer omits. Without it the proof shows only (i) ⇒ (ii) ⇒ (iii), and no condition later in the chain gives back an earlier one. The case split in (iii) ⇒ (i) uses no RAA: the impossible case reaches the goal by ⊥E, as in @exm-rhetoric-contradiction's case version." (The Quick check below asks for the point of its second sentence with the fold closed.)

   **Quick check (new):** "To prove four conditions (i)–(iv) equivalent, a writer proves (i) ⇒ (ii), (ii) ⇒ (iii), (iii) ⇒ (iv) and (iv) ⇒ (ii). Is that enough?" *Solution:* No. (ii), (iii) and (iv) are shown equivalent, but nothing leads back to (i): (ii) ⇒ (i) is never shown. A fifth implication (ii) ⇒ (i) would do, or (iv) ⇒ (i) in place of (iv) ⇒ (ii).

4. **Not allowed** (new warning, ~100 words, the last block of the main line, after the warning 01:306–308; R5 places no Looking-ahead box here). `[Not allowed: connective steps in prose]`. Each line is a sentence that might appear in a proof, then its tag:
   - "Suppose \( x \ge 1 \); then \( x^3 \ge x \). Hence \( x^3 \ge x \) for every real \( x \)." The line \( x^3 \ge x \) belongs to a box that has closed; outside it only "if \( x \ge 1 \), then \( x^3 \ge x \)" is available. (N10). False at \( x = \tfrac12 \).
   - "To prove \( \abs{x} < 1 \), suppose, for a contradiction, that \( \abs{x} > 1 \)." The negation of \( \abs{x} < 1 \) is \( \abs{x} \ge 1 \). (N11)(a).
   - "Suppose \( n \) is odd. Then \( n^2 \) is odd." as the whole proof of "if \( n^2 \) is even, then \( n \) is even". It breaks the never-silent item "the announcement of a contrapositive" (@def-silent-steps). Without the announcement the reader sees a box that opens with neither the hypothesis nor the conclusion of the goal. (S2 round 1: the S1 tag "(N5)" was wrong. (N5) is a box that opens with the conclusion, and this text proves the contrapositive, which is valid.)
   - "Case 1: \( x \ge 0 \), so \( \abs{x} = x \ge 0 \). In either case \( \abs{x} \ge 0 \)." There is one case and no disjunction: (N7).

5. **Fold F8.1-d** `title="The hypothesis \( x \ge 0 \), direction by direction"` (new, after the solution of `exm-rhetoric-biconditional`, as a sibling): 01:241's last three sentences verbatim, from "The hypothesis \( x \ge 0 \) does a job in each" to the end (~110 words). The solution keeps its first sentence ("The labels … opens the second."). This is part of the budget trade for items 1–4, and it is an edge-case discussion (STYLE §12.3).

6. **Fold F8.1-f** `title="The smell the two tests share"` (new, S2 round 1, budget; a sibling after the second costume test, 01:302): 01:304 verbatim (~63 words). The two tests stay on the main line, and each is complete without the paragraph, which compares them (a long justification, STYLE §12.0). No exercise needs it.

**Quick checks:** R5's four, plus the cycle check: five in ~4,970 words, about one per 995 (STYLE §12.7: one per 800–1,000).

**Exercises.**
- **A1, B1, B2, B3 (R5), C1 (frozen), C2:** as R5.
- **A2: Drill** (`exr-connective-rhetoric-a2`): R5's ten parts plus two, **12 parts**, in this order (R5 letters in brackets). Stem as R5: "Name the rule each phrase carries, and say whether plain prose may leave it out." Parts (h) and (l) ask a different question and say so in their own words.
  (a) [a] … (g) [g]: R5's parts and answers.
  (h) **new** (S2 round 1: the S1 Quick check on the purpose paragraph, moved here) "A proof that \( \sqrt 5 \) is irrational opens: 'Suppose, for a contradiction, that \( \sqrt 5 \) is rational.' Which annotation would its derivation print beside that assumption?" — "asm, for ¬I". The goal, "\( \sqrt 5 \) is irrational", is the negation "\( \sqrt 5 \) is not rational". The box assumes the positive statement and is closed by ¬I, whatever the words "for a contradiction" suggest: Section 2.5's distinction, face (i) of "The three faces". (No fact about \( \sqrt 5 \) is needed.)
  (i) [h] (j) [i] (k) [j]: R5's parts and answers.
  (l) **new** "Four conditions are to be shown equivalent. How many implications does a cycle need, and how many would proofs of every ordered pair need?" — Four for a cycle. Twelve for every ordered pair (\( 4 \cdot 3 \)), that is, six biconditionals.
- **B4** (new, `exr-connective-rhetoric-b4`) `[B4: Two integers of the same parity]` [technique: LB — TFAE by a cycle] (S2 round 1: replaced; the S1 item, \( 3 \mid n \), \( 9 \mid n^2 \), \( 3 \mid n^2 \), closely paraphrased a published exercise). Statement: "Let \( a \) and \( b \) be integers. Prove that the following are equivalent, by a cycle: (i) \( a + b \) is even; (ii) \( a - b \) is even; (iii) \( a \) and \( b \) are both even or both odd. Say which arrow closes the cycle, and tag the logical steps of that arrow."

  *Solution.* By @prp-equivalence-cycle, three implications suffice.
  - (i) ⇒ (ii): Suppose \( a + b \) is even; choose \( k \) with \( a + b = 2k \) [∃E]. Then \( a - b = (a + b) - 2b = 2(k - b) \), so \( a - b \) is even, with the witness \( k - b \) [∃I].
  - (ii) ⇒ (iii): Suppose \( a - b \) is even, and choose \( j \) with \( a - b = 2j \) [∃E]. By (E1), \( b \) is even or odd [∨E].
    - If \( b = 2m \) [∃E], then \( a = 2(j + m) \) is even [∃I], so both are even [∧I, then ∨I].
    - If \( b = 2m + 1 \) [∃E], then \( a = 2(j + m) + 1 \) is odd [∃I], so both are odd [∧I, then ∨I].
  - (iii) ⇒ (i), the closing arrow: Suppose \( a \) and \( b \) are both even or both odd [asm, for →I]. There are two cases [∨E].
    - Both even: choose \( s \) and \( t \) with \( a = 2s \) and \( b = 2t \) [∃E twice, two fresh names]. Then \( a + b = 2(s + t) \) [∃I, witness \( s + t \)].
    - Both odd: choose \( s \) and \( t \) with \( a = 2s + 1 \) and \( b = 2t + 1 \) [∃E twice]. Then \( a + b = 2(s + t + 1) \) [∃I, witness \( s + t + 1 \)].
    - In either case \( a + b \) is even [∨E, closing; silent at level 3].

  The closing arrow is (iii) ⇒ (i). Its logic is a two-case ∨E, each case with two ∃E boxes under distinct names and one ∃I; no RAA is used. (The names \( s \), \( t \) may be reused in the second case: sibling boxes may share a name, as (N4) of Section 8.6 notes.)

  **Marking scheme.** (10 points)
  - 2: (i) ⇒ (ii), with \( k \) chosen and the witness \( k - b \).
  - 3: (ii) ⇒ (iii): the split on \( b \), with (E1) named (1); the witness \( j + m \) in each case (2).
  - 3: (iii) ⇒ (i): the two cases (1); two distinct names in each case (1); the witnesses (1).
  - 1: the cycle named, with @prp-equivalence-cycle or the sentence that three implications suffice, and the closing arrow identified.
  - 1: the last sentence says what was shown.

  Fatal errors (0 for the step): only two arrows proved; one name for both witnesses, "\( a = 2s \) and \( b = 2s \)" (N4); "\( a - b \) is even, so \( a \) and \( b \) have the same parity" given as its own reason, with neither proof nor citation (N9).

**Sidecars:**
- `exm-rhetoric-cycle.py`: \( n^2 = 2a + 1 \Rightarrow n^2 + 2n = 2(a + n) + 1 \); \( (2k)^2 + 2(2k) = 2(2k^2 + 2k) \); the parity of \( n \), \( n^2 \), \( n^2 + 2n \) for \( |n| \le 200 \).
- `exr-connective-rhetoric-b4.py`: the identities \( a - b = 2(k - b) \), \( a = 2(j + m) \), \( a = 2(j + m) + 1 \), \( a + b = 2(s + t) \), \( a + b = 2(s + t + 1) \); the equivalence of (i), (ii) and (iii) for \( |a|, |b| \le 60 \).
- `exr-connective-rhetoric-a2.py` (R5's), extended by (l)'s count.

**Ledger lines:**
- the purpose paragraph (`latex/fitch-book.sty`'s printed form; F1.1 §05's introduction of the annotation, prose pointer);
- A2 (h), the √5 opening (the faces table, inline);
- the constructive-dilemma row (`exm-constructive-dilemma`, cited; F1.2 §03's derived rule, prose pointer);
- `exm-rhetoric-cycle` (`prp-equivalence-cycle` and `thm-odd-iff-square-odd`, cited; (E1), (E2) and the definitions of even and odd, F1.2 §01; school algebra; sidecar);
- F8.1-e (a fold holding a worked example; nothing cites it outside 8.1) and F8.1-f (moves with its text);
- the cycle check (inline);
- B4 ((E1) and the definitions of even and odd, F1.2 §01; sidecar). B4 no longer uses "\( 3k \), \( 3k + 1 \) or \( 3k + 2 \)" or "nothing between 0 and 1" (§6.2).

### 4.2 Section 8.2: The Quantifier Rules in Prose (`02-quantifier-rhetoric.md`)

**Budget:** main line ≤ 4,200 (now 3,129; R5 ≤ 3,700; expected about 4,200: S1's ~4,180, plus about +40 for the extensionality sentences of item 2 (S2 round 1), less the ~17 words cut from the example's closing paragraph); folds ≤ 260 (R5: none; new F8.2-a ~70, F8.2-b ~110, and room for the fallback). No Looking-ahead box (R5). **Fallback** if S3 measures over 4,200: the two sentences on definitional extension in item 2's lead paragraph (from "A definition adds a word" to "with the definition.", ~50 words) move into a new fold F8.2-c `title="What a definition adds"`, a sibling after that paragraph. The table row "a definition" stays on the main line and carries the rule (S2 round 1: F8.2-a, on monotonicity, was the wrong home).

R5 §4.2 is executed in full. Additions:

1. **Two "stronger" rows** (layout §1.3; gap-matrix row 2.12 [vD]). Two new rows go in the pattern table of `## Induction, lemmas and symmetry` (02:131–135, R5's reordered table), after R5's cut row:

   | it suffices to prove something stronger | "it suffices to prove the stronger …"; "in fact more is true: …" | never the stronger claim; the step from it to the goal may be silent when it is one ∧E, ∨I or chain link |
   | a stronger hypothesis gives a weaker theorem | "in particular, for \( x \in (0, 1) \)"; "since every such \( x \) has \( \abs{x} < 1 \), the result applies" | the narrowing of the hypothesis, never |

   Two sentences go at the end of R5's `### It suffices to show` subsection (~70 words): "Two cases of the move have names of their own. To prove \( \psi \) it suffices to prove a **stronger** \( \varphi \) from which \( \psi \) follows at once: to show \( x^2 < 1 \) for \( 0 < x < 1 \), show \( x^2 < x \), and then \( x^2 < x < 1 \). And a theorem stays true when its hypothesis is narrowed: from 'if \( \abs{x} < 1 \), then \( x^2 < 1 \)' and 'every \( x \in (0, 1) \) has \( \abs{x} < 1 \)', the chain of @prp-implication-transitive gives 'if \( x \in (0, 1) \), then \( x^2 < 1 \)': a stronger hypothesis, a weaker theorem."

   **Fold F8.2-a** `title="Stronger and weaker, in general"` (new, ~70 words, after that subsection): "Both moves are instances of one fact about where a part sits in a formula. Weakening a part in a positive place, such as the conclusion of an implication, weakens the whole; weakening a part in a negative place, such as the hypothesis, strengthens the whole. The second-pass Section 4.9 states and proves this as @thm-monotonicity; nothing on the main line uses it."

2. **`## Definitions, descriptions and sets`** (new subsection, after `## Equality and unique existence`, 02:91–125, and before `## Induction, lemmas and symmetry`, 02:127; about 400 words with the example) [technique: Ha — double inclusion and element chasing, gap-matrix row 7.5; layout G3 and C small 6, the rows "we define" and "the limit" collected from 5.8].

   Lead (one sentence): "Three more phrases do logical work in almost every chapter of analysis: 'we define', 'the', and 'the two sets are equal'."

   Table:

   | Pattern | Phrases | Silent in plain prose? |
   |---|---|---|
   | a definition (a definitional extension, @prp-definitional-extension) | "we define \( f(x) \coloneqq \dots \)"; "call \( n \) *perfect* if …"; "write \( d \) for …" | never the definition; its uses (↔E or =E with it) yes |
   | "the" (a definite description, @def-definite-description) | "let \( L \) be the limit of \( (a_n) \)"; "the least element of \( A \)"; "\( \lim a_n \)" | never the existence and uniqueness behind "the": proved or cited before the name is used |
   | double inclusion | "we show \( A \subseteq B \) and \( B \subseteq A \)"; element chasing: "let \( x \in A \); … so \( x \in B \)"; "so \( A = B \)" | never either inclusion, nor the opening "let \( x \in \dots \)" of each, nor the appeal to extensionality that turns "the same elements" into \( A = B \) |

   Then (~110 words): "A definition adds a word and proves nothing new about the old words (@prp-definitional-extension, Section 5.8). So 'we define' writes an abbreviation, and every later use of it is ↔E or =E with the definition. 'The', as in 'the limit', names an object. It may be used only once there is exactly one such object (Section 5.8): for a limit, existence is the hypothesis that \( (a_n) \) converges, and uniqueness is @exm-rhetoric-equality. Chapter 5 read \( A \subseteq B \) as \( \forall x\, (x \in A \to x \in B) \). Two inclusions give \( \forall x\, (x \in A \leftrightarrow x \in B) \), by ↔I inside ∀I: the two sets have the same elements. Each inclusion is an **element chase**: 'let \( x \in A \)' opens a bounded ∀I box whose last line is \( x \in B \). The last step, from 'the same elements' to \( A = B \), is not logic. Logic gives only the converse, that equal sets have the same elements (@exm-extensionality-logical-half). The step itself is the **axiom of extensionality**, an axiom about sets (Section 5.7), and a proof cites it, as a premise or with the words 'by extensionality'; it is never silent."

   **`exm-rhetoric-double-inclusion`** `[Two inclusions]`. Statement: "Let \( A \coloneqq \{ x \in \nR : x^2 \le 2x \} \) and \( B \coloneqq \{ x \in \nR : 0 \le x \le 2 \} \). Prove that \( A = B \), and tag the steps that carry the logic."

   Solution:
   - \( (\subseteq) \) Let \( x \in A \) [asm, for ∀I]; so \( x^2 \le 2x \), that is, \( x(x - 2) \le 0 \).
     - If \( x < 0 \), then \( x - 2 < 0 \) too, and a product of two negative numbers is positive: \( x(x - 2) > 0 \). This clashes with \( x(x - 2) \le 0 \) [¬E], so \( x < 0 \) is impossible [¬I], and \( x \ge 0 \) by trichotomy.
     - If \( x > 2 \), then both factors are positive and the same clash follows. So \( x \le 2 \).
     - Hence \( 0 \le x \le 2 \) [∧I], and \( x \in B \).
   - \( (\supseteq) \) Let \( x \in B \) [asm, for ∀I]; so \( x \ge 0 \) and \( x - 2 \le 0 \) [∧E]. A product of a non-negative and a non-positive number is at most \( 0 \), so \( x(x - 2) \le 0 \), that is, \( x^2 \le 2x \), and \( x \in A \).
   - So \( A \subseteq B \) and \( B \subseteq A \): every real \( x \) has \( x \in A \leftrightarrow x \in B \) [↔I inside ∀I]. By extensionality, \( A = B \) [∀E, →E with the axiom].

   Then: "The words 'that is' unwind the two sets' definitions (↔E, silent at level 3)." (S2 round 1: the S1 sentence on the ¬I steps is cut, since the solution tags them; it pays for part of the extensionality sentences of the lead.)

   **Quick check (new):** "To prove \( \{ n \in \nZ : n^2 \text{ is even} \} = \{ n \in \nZ : n \text{ is even} \} \) by double inclusion, which inclusion is a theorem of Chapter 2, and which takes one line?" *Solution:* \( \subseteq \) is @thm-square-even-implies-even. \( \supseteq \) is one line: \( n = 2k \) gives \( n^2 = 2(2k^2) \).

3. **Not allowed** (new warning, ~120 words, the last block of the main line, after the warning 02:186–188). `[Not allowed: quantifier steps in prose]`:
   - "Let \( \varepsilon > 0 \) and choose \( N \) with \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \). This \( N \) works for every \( \varepsilon > 0 \)." (N2).
   - "Some \( x \in A \) has \( f(x) > 0 \). Let \( x \in A \); then \( f(x) > 0 \)." The witness of an existential is *chosen* ("choose \( x \in A \) with \( f(x) > 0 \)", ∃E with a fresh name). Written with "let", the second sentence claims \( f(x) > 0 \) for every \( x \in A \): (N3).
   - "Choose \( N \) with \( \abs{a_n - L} < \varepsilon/2 \) for \( n \ge N \), and \( N \) with \( \abs{b_n - M} < \varepsilon/2 \) for \( n \ge N \)." (N4).
   - "Let \( L \) be the limit of \( (a_n) \)", in a proof that has not shown that \( (a_n) \) converges: (N14).
   - "Let \( \varepsilon > 0 \). Then \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \), as required", where no sentence says what \( N \) is. The witness of ∃I, with what it depends on, is never silent (@def-silent-steps). (S2 round 1: this replaces the S1 line on trailing quantifiers, which carried no tag; that reading error stays with "What the sentence does not say".)

4. **Fold F8.2-b** `title="The bookkeeping of the two choices"` (new, a sibling after the solution of `exm-rhetoric-equality`): 02:124 verbatim (~110 words). The solution keeps 02:122. `exm-rhetoric-equality` is not cited outside the chapter (layout §4.3), and the passage is bookkeeping that R5's dependency picture also shows.

5. **R5's four pictures** use the Diagrams templates where one fits:
   - The "it suffices" picture and the WLOG picture: `flowchart`, with `fc step` nodes for the claims and the case boxes (the unwritten case box gets the option `dashed`), and `fc arrow` with `font=\scriptsize` labels.
   - The induction picture: `flowchart`, with an `fc step` for \( P(0) \), an `fc step` holding the two-line box text, and an `fc start` for the conclusion.
   - The dependency picture (nested boxes) has no template. It is drawn with plain `\draw[rounded corners]` rectangles and `\node` labels, with no fill and no colour.

   Every one is a raw LaTeX block with its `tikzpicture` written out (DRAFTING, Diagrams).

**Quick checks:** R5's four (δ at two points, the hidden ∃N, it-suffices, WLOG), plus the double-inclusion check: five in ~4,200 words, about one per 840. (The example's closing paragraph was shortened to pay for the check.)

**Exercises.**
- **A1, B1, B2, C1, C2:** as R5.
- **A2: Drill** (`exr-quantifier-rhetoric-a2`): R5's (a)–(j) in R5's order, then:
  (k) **new** "To prove \( A = B \), a proof shows \( A \subseteq B \) and \( B \subseteq A \). Which rules does that pattern use, and how does each inclusion open?" — ↔I inside ∀I, for \( \forall x\, (x \in A \leftrightarrow x \in B) \); then \( A = B \) by ∀E and →E with the axiom of extensionality, cited. Each inclusion is a bounded ∀I that opens with "let \( x \in A \)" (or "let \( x \in B \)").
  (l) **new** "A proof begins 'Let \( m \) be the least element of \( A \)'. What must already be on the page?" — That such an element exists and that there is only one (∃!, a definite description). Uniqueness is one line, since two least elements are each at most the other; existence is the part that needs a reason.
- **B3** (new, `exr-quantifier-rhetoric-b3`) `[B3: Six, two and three, used later]` [technique: Ha — element chasing]. Statement: "Let \( A \coloneqq \{ n \in \nZ : 6 \mid n \} \) and \( B \coloneqq \{ n \in \nZ : 2 \mid n \text{ and } 3 \mid n \} \). Prove \( A = B \) by double inclusion. Name each 'let', each 'choose' with its fresh name, and each witness."

  *Solution.*
  - \( (\subseteq) \) Let \( n \in A \) [∀I], and choose \( k \) with \( n = 6k \) [∃E, \( k \) fresh]. Then \( n = 2(3k) \) and \( n = 3(2k) \), so \( 2 \mid n \) and \( 3 \mid n \), with the witnesses \( 3k \) and \( 2k \) [∃I twice, ∧I]; so \( n \in B \).
  - \( (\supseteq) \) Let \( n \in B \) [∀I]. Choose \( a \) with \( n = 2a \) and \( b \) with \( n = 3b \) [∃E twice, two fresh names: one name for both would be (N4)]. Then \( b = 3b - 2b = n - 2b = 2a - 2b = 2(a - b) \), so \( n = 3b = 6(a - b) \), and \( 6 \mid n \) with the witness \( a - b \) [∃I]; so \( n \in A \).
  - So \( A = B \).

  The two ∃E boxes of \( (\supseteq) \) close on "\( n \in A \)", which mentions neither \( a \) nor \( b \).

  **Marking scheme.** (10 points)
  - 2: \( (\subseteq) \), with \( k \) chosen and both witnesses written.
  - 4: \( (\supseteq) \): two choices with distinct names (1); the computation \( b = 2(a - b) \), or another valid route to an integer \( c \) with \( n = 6c \) (2); the witness named (1).
  - 2: the double-inclusion frame: both inclusions, each opened by "let \( n \in \dots \)", and the conclusion \( A = B \).
  - 2: the tags: ∀I, ∃E with fresh names, ∃I.

  Fatal errors (0 for the step): one name for both witnesses; "\( 2 \mid n \) and \( 3 \mid n \), so \( 6 \mid n \)" asserted without an argument (N9).

**Sidecars:**
- `exm-rhetoric-double-inclusion.py`: \( x^2 \le 2x \iff 0 \le x \le 2 \), exactly on rationals with denominators up to 50 and on a grid; the sign facts.
- `exr-quantifier-rhetoric-b3.py`: \( 2a = 3b \Rightarrow b = 2(a - b) \) and \( n = 6(a - b) \), for \( |n| \le 600 \); \( A = B \) on that range.
- R5's A2 script, extended by (l), which has no values.

**Ledger lines:**
- the stronger rows (`prp-implication-transitive`, cited; `exm-rhetoric-conjunction`'s \( x^2 < x \), within the chapter);
- F8.2-a (`thm-monotonicity`, F1.3 §09, second pass, prose pointer in a fold; nothing rests on it);
- the definitions row (`prp-definitional-extension`, `def-definite-description`, F1.4 §08, cited);
- subset read as → (F1.4 §01's gloss of subset, prose); the appeal to extensionality (`exm-extensionality-logical-half`, F1.4 §07, cited, with its remark that the converse is an axiom about sets). This agrees with F1.4 §08's B4, which takes the axiom as a cited premise \( E \) and marks "\( a = b \) by extensionality" with no instance of \( E \) written as a fatal error, and with F1.6 §02's "Extensionality: an axiom, not a law of logic". Chapter 8 does not cite 7.2 for it (binding rule 4; the What-you-need line);
- the double-inclusion example (school order facts, trichotomy; extensionality, cited; sidecar);
- B3 (sidecar).

### 4.3 Section 8.3: Four Levels of One Proof (`03-levels-of-abbreviation.md`)

**Budget:** main line ≤ 4,200 (now 4,064; R5 ≤ 4,000; expected about 4,180); folds ≤ 1,600 (R5 ≤ 1,300, plus F8.3-d ~300). Looking-ahead box: R5's, kept. **Fallback** if S3 measures over 4,200: the read-back sentence for column (a) in `exm-suffices-column`'s closing paragraph ("Read from the bottom, (a) is the proof …", ~25 words) is cut; (b)'s read-back makes the point.

R5 §4.3 is executed in full. Changes and additions:

1. **Fold F8.3-d** `title="The two lists against the principle, with an example"` (new, placed after the warning 03:84–86): 03:80 and 03:82 verbatim (~300 words). R5 kept both on the main line. They move to make room for item 2. The principle stays on the main line (R5: "Section 8.1 stated the principle …"), and so do the six-row table and `def-silent-steps`.

2. **Silent steps and truth tables** (new paragraph, ~140 words, in place of 03:80, after R5's sentence on the "eighth and ninth items"; bold lead-in `**Silent steps and truth tables.**`) [Critic C2; layout §1.3 "silent steps tied to TAUT (4.8, 6.3)"]. Text:

   "Section 4.8 named the step that a truth table licenses, TAUT (@def-rule-taut). Section 6.3 let it act on the propositional skeleton of a first-order line, where every atomic and every quantified part counts as a letter (@def-propositional-skeleton, @prp-taut-skeleton). Most items of the first list are TAUT steps: ∧I with both conjuncts displayed, ∧E, R, ∨I, ⊥E once the contradiction is stated, DS, the exchange of the members of a disjunction or conjunction, ↔E with a definition, and →E on a line of the proof. A reader can check each of them by a truth table on the skeleton. The quantifier and equality items, ∀E at the obvious term and =I and =E inside chains, are not TAUT steps: they are silent because the sentence that uses them forces them. TAUT never licenses a first-order law. On the skeleton, \( \forall x\, \forall y\, R(x, y) \) and \( \forall y\, \forall x\, R(x, y) \) are two different letters, so passing from one to the other is a derivation with the quantifier rules, not a TAUT step."

   One more sentence: "From Section 4.8 on, a level-1 line that compresses propositional steps inside one box may cite TAUT with its lines, in place of the names of its rules (NOTATION, TAUT)."

3. **`## It suffices to show, as a column`** (new subsection, ~300 words with its two tables; after `## Uniform continuity, twice`, before `## Expand to check`, 03:280) [technique: En — "it suffices to show" as a column of reductions; plan §3.6 item 6.3].

   Lead: "Section 8.2 read 'it suffices to show \( \varphi \)' as a step that replaces the goal by \( \varphi \) and shows on the spot that \( \varphi \) is enough. A proof that makes several such steps in a row is easiest to plan, and to check, as a **column**. The goal goes at the top. Each row is a claim from which the row above follows, with the reason beside it. At the bottom is a claim that needs no reduction: a hypothesis, a fact or a cited result. Read upwards, the column is the proof."

   **`exm-suffices-column`** `[Two columns]`. Statement: "(a) Prove that \( x^2 - 6x + 10 > 0 \) for every real \( x \). (b) Let \( a_n \coloneqq (2n + 1)/(n + 1) \) for \( n \in \nN \). Prove that \( a_n \to 2 \). Plan each proof as a column of reductions, then write it."

   Solution. (a):

   | It suffices to show | because |
   |---|---|
   | \( x^2 - 6x + 10 > 0 \) | (the goal) |
   | \( (x - 3)^2 + 1 > 0 \) | \( x^2 - 6x + 10 = (x - 3)^2 + 1 \) |
   | \( (x - 3)^2 \ge 0 \) | a number at least \( 0 \), plus \( 1 \), is positive |
   | — | every square is at least \( 0 \) |

   (b) Let \( \varepsilon > 0 \). For \( n \in \nN \) with \( n \ge N \), where \( N \) is still to be chosen:

   | It suffices to show | because |
   |---|---|
   | \( \abs{a_n - 2} < \varepsilon \) | (the goal, for \( n \ge N \)) |
   | \( 1/(n + 1) < \varepsilon \) | \( a_n - 2 = -1/(n + 1) \), so \( \abs{a_n - 2} = 1/(n + 1) \) |
   | \( n + 1 > 1/\varepsilon \) | for positive numbers, taking reciprocals reverses \( < \) |
   | \( N > 1/\varepsilon \) | \( n \ge N \) gives \( n + 1 > N \) |
   | — | choose such an \( N \in \nN \) (the school fact of @exm-rhetoric-existential); it depends on \( \varepsilon \) |

   Then: "Each reason is an implication that points **up**: the row implies the row above it. Read from the bottom, (a) is the proof 'Since \( (x - 3)^2 \ge 0 \), \( x^2 - 6x + 10 = (x - 3)^2 + 1 \ge 1 > 0 \).' Read the same way, (b) is 'Let \( \varepsilon > 0 \), and choose \( N \in \nN \) with \( N > 1/\varepsilon \). For \( n \ge N \), \( \abs{a_n - 2} = 1/(n + 1) < 1/N < \varepsilon \).' In (b) the constant is found at the bottom of the column, last, and written in the proof's first sentence, as step 5 of Section 8.5 will require."

   **Quick check (new):** "In column (b), which row introduces a constant, and which reason needs \( \varepsilon > 0 \)?" *Solution:* The bottom row introduces \( N \), chosen from the school fact at \( 1/\varepsilon \), so it depends on \( \varepsilon \). The reciprocal row needs \( \varepsilon > 0 \): \( 1/\varepsilon \) must exist and be positive for "\( n + 1 > 1/\varepsilon \) gives \( 1/(n + 1) < \varepsilon \)".

**Quick checks:** R5's four, plus the column check: five in ~4,180 words, about one per 840. R5's level-0 check stays in fold F5.3-b.

**Exercises.**
- **A1, B1, B2 (scaffolded, without `\purpose`: D1), C1, C2 (exit check), C3:** as R5.
- **A2: Drill** (`exr-levels-of-abbreviation-a2`): R5's (a)–(h), then:
  (i) **new** "From Section 4.8 on, may the level-1 line \( x_0 > 0 \), citing the line \( x_0 > 0 \wedge y_0 > 0 \), be justified TAUT?" — Yes. On the skeleton it is \( P \wedge Q \vdash P \), true in every row: it is ∧E.
  (j) **new** "May the line \( \forall y\, \forall x\, R(x, y) \), citing \( \forall x\, \forall y\, R(x, y) \), be justified TAUT?" — No. On the skeleton the two lines are different letters, and \( P \vdash Q \) fails in a row. The step needs ∀E twice and ∀I twice.
  (k) **new** "A column for '\( 2^{n+1} > n + 1 \), given \( 2^n > n \) and \( n \ge 1 \)' has the first row 'it suffices to show \( 2^n + 2^n > n + 1 \)'. What is that row's reason, and what row could come next?" — \( 2^{n+1} = 2 \cdot 2^n = 2^n + 2^n \) (=E). Next: "it suffices to show \( 2^n \ge 1 \)", because then \( 2^n + 2^n > n + 2^n \ge n + 1 \) by the hypothesis \( 2^n > n \).
  (l) **new** "In an 'it suffices to show' column, which row is proved outright, with no further reduction?" — The bottom row. It is a hypothesis, a fact or a cited result; every other row is reduced to the one below it.
- **B3** (new, `exr-levels-of-abbreviation-b3`) `[B3: A column of reductions]` [technique: En]. Statement: "(a) Prove that \( \abs{x - 1} + \abs{x + 1} \ge 2 \) for every real \( x \) by an 'it suffices to show' column, each row with its reason. (b) Turn the column into a level-3 proof. (c) Which reasons in your column are =E steps that level 3 may leave silent? (d) A student's column has the row 'it suffices to show \( \abs{x - 1} \ge 1 \) and \( \abs{x + 1} \ge 1 \)'. Is that row's reason correct? Can the student finish?"

  *Solution.* (a):

  | It suffices to show | because |
  |---|---|
  | \( \abs{x - 1} + \abs{x + 1} \ge 2 \) | (the goal) |
  | \( \abs{1 - x} + \abs{x + 1} \ge \abs{(1 - x) + (x + 1)} \) | \( \abs{x - 1} = \abs{1 - x} \), and \( (1 - x) + (x + 1) = 2 \), so the right side is \( \abs{2} = 2 \) |
  | — | the triangle inequality, @exm-triangle-inequality-cases with \( 1 - x \) and \( x + 1 \) in place of its \( x \) and \( y \) |

  (b) "By the triangle inequality, \( \abs{x - 1} + \abs{x + 1} = \abs{1 - x} + \abs{x + 1} \ge \abs{(1 - x) + (x + 1)} = 2 \)."

  (c) \( \abs{x - 1} = \abs{1 - x} \) and \( (1 - x) + (x + 1) = 2 \): both are =E links of a chain, silent at level 3 (@def-silent-steps). The citation of the triangle inequality is never silent.

  (d) The reason is correct: if both hold, the sum is at least \( 2 \), so the row implies the goal. But the student cannot finish. The new row is false at \( x = \tfrac12 \), where \( \abs{x - 1} = \tfrac12 \), although the goal holds there (\( \tfrac12 + \tfrac32 = 2 \)). A reduction is legal whenever its arrow points up; it is useful only when the new row is true.

  **Marking scheme.** (10 points)
  - 3: (a) a column whose every row has an upward-pointing reason, ending in a cited result or a fact (the triangle inequality, or a case split on the sign of \( x - 1 \) and \( x + 1 \)).
  - 3: (b) a forward level-3 text with the citation written.
  - 2: (c) the two =E links named as silent, the citation as spoken.
  - 2: (d) the reason judged correct, and the row shown false at a named \( x \): it fails exactly when \( 0 < \abs{x} < 2 \), for instance at \( x = \tfrac12 \).

  A three-case proof (\( x \le -1 \); \( -1 < x < 1 \); \( x \ge 1 \)) written as a column earns (a) and (b) in full. Fatal errors (0 for the step): a row whose reason points down ("the goal implies the row"); a case split that does not exhaust (N8).

**Sidecars:**
- `exm-suffices-column.py`: the identity; \( \abs{a_n - 2} = 1/(n + 1) \); \( N > 1/\varepsilon \Rightarrow \abs{a_n - 2} < \varepsilon \) for sampled \( \varepsilon \).
- `exr-levels-of-abbreviation-b3.py`: the inequality on a grid; \( x = \tfrac12 \) refuting the student's row; the three-case route.
- R5's A2 script, extended by (k)'s identity.

**Ledger lines:**
- the TAUT paragraph (`def-rule-taut`, F1.3 §08; `def-propositional-skeleton` and `prp-taut-skeleton`, F1.8 §03; cited, earlier chapters; NOTATION's TAUT entry);
- the column subsection (8.2's "it suffices", within the chapter; `exm-rhetoric-existential`'s school fact, cited; school algebra; sidecar);
- B3 (`exm-triangle-inequality-cases`, cited; sidecar).

### 4.4 Section 8.4: Reading a Proof: Self-Explanation (`04-reading-proofs.md`)

**Budget:** main line ≤ 2,200 (now 1,895; R5 ≤ 2,000; expected about 2,190); folds ≤ 550, in the exercises (R5). No Looking-ahead box. **Fallback** if S3 measures over 2,200: the unstated-fact subsection's second sentence ("A proof is read the same way, one line at a time.") is cut.

R5 §4.4 is executed in full. Additions:

1. **The purpose in question 1** (04:63): one sentence appended to item 1 of "How to explain a line": "In a derivation the annotation answers it: 'asm, for →I' beside an assumption names the rule that will close its box (Section 8.1)." (~25 words.)
2. **`## Naming the unstated fact`** (new subsection, ~170 words; after `## How to explain a line`, which ends with the solution 04:87–95, and before `## Strategies of good readers`, 04:97) [technique: Ho, Hu — supplying the suppressed premise; gap-matrix rows 1.9 and 7.8; layout: "argument extraction recalled from 3.3"]. Text:

   "Section 3.3 turned a paragraph of argument into a sequent: its conclusion, its stated premises, and the unstated facts that close its gaps. A proof is read the same way, one line at a time. Often the second question, *where does it come from?*, has an answer the writer did not write: a fact used but not stated. Self-explaining the line means naming that fact, and the fact then turns out to be one of three things. It may be a school fact or a definition: name it. It may be an earlier result: cite it. Or it may be false, and then the line fails. Two lines that look alike:
   - 'Since \( n^2 \) is a multiple of \( 3 \), so is \( n \).' The unstated fact, 'if \( 3 \mid n^2 \), then \( 3 \mid n \)', is true. A careful proof proves it, by cases on the remainder of \( n \) on division by \( 3 \).
   - 'Since \( n^2 \) is a multiple of \( 4 \), so is \( n \).' The unstated fact, 'if \( 4 \mid n^2 \), then \( 4 \mid n \)', is false at \( n = 2 \). Chapter 1 met it as a missing premise (@exr-using-an-implication-b5).

   A reader who only paraphrases reads both lines alike."

   **Quick check (new):** "In 'Since \( x > 1 \), \( x^2 > x \)', name the unstated fact and the hypothesis it needs." *Solution:* Multiplying both sides of \( x > 1 \) by \( x \) keeps the direction of the inequality because \( x > 0 \); and \( x > 0 \) follows from \( x > 1 > 0 \).

**Quick checks:** lines 2–4 (kept), the four questions (R5), the unstated fact (new): three in ~2,190 words, about one per 730.

**Exercises.**
- **A1, B1 (R5's plain solution and fold), B2, C1 (R5's new item), C2 (R5's moved Challenge):** as R5.
- **A2: Drill** (new, `exr-reading-proofs-a2`), 12 parts. Stem: "Answer each part in a phrase." Ramp: justify or paraphrase → which question → what kind of line → name the unstated fact → habits.
  (a) "A line: 'Since \( n \) is even, \( n^2 \) is even.' An explanation: 'With \( n = 2k \), \( n^2 = 2(2k^2) \), and \( 2k^2 \) is an integer.' Does it justify or paraphrase?" — It justifies: it names the definition of even, the witness and the algebra.
  (b) "A line: '\( x^2 - 1 = (x - 1)(x + 1) \).' An explanation: 'We factor it.' Justify or paraphrase?" — Paraphrase. It says what happened, not which identity makes the line true (\( u^2 - v^2 = (u - v)(u + v) \) at \( u = x \), \( v = 1 \)).
  (c) "Which of the four questions asks 'May we divide by \( x - 1 \) here?'" — The fourth: is the step legitimate here (is \( x - 1 \ne 0 \))?
  (d) "Which question does the answer 'this line opens a box' answer?" — The first: what kind of line it is.
  (e) "What kind of line is 'Choose \( \delta > 0 \) such that …', and what does its derivation print beside it?" — An assumption that opens an ∃E box with a fresh name; "asm, for ∃E".
  (f) "What kind of line is 'Since \( \varepsilon \) was arbitrary, …'?" — The closing of a ∀I box.
  (g) "Name the unstated fact: 'Since \( 0 < a < b \), \( a^2 < b^2 \).'" — Multiplying an inequality by a positive number keeps it: \( a \cdot a < a \cdot b \) (multiply \( a < b \) by \( a > 0 \)) and \( a \cdot b < b \cdot b \) (multiply by \( b > 0 \)).
  (h) "Name the unstated fact: '\( \abs{x - 2} < 1 \), so \( x > 1 \).'" — \( \abs{u} < r \) holds exactly when \( -r < u < r \); here \( -1 < x - 2 \).
  (i) "Name the unstated facts: '\( x^2 = 9 \) and \( x > 0 \), so \( x = 3 \).'" — \( x^2 - 9 = (x - 3)(x + 3) \), and a product of real numbers is \( 0 \) only if a factor is, so \( x = 3 \) or \( x = -3 \); then \( x > 0 \) rules out \( -3 \) (DS).
  (j) "After three readings, a proof feels clear. Has the reader self-explained it?" — Not necessarily: familiarity is not a warrant checked line by line (the warning "Self-explanation is not re-reading").
  (k) "'Let \( x < 0 \). Then \( 1/x < 0 \).' Which hypothesis is used, and how?" — \( x < 0 \). It gives \( x \ne 0 \), so \( 1/x \) exists; and \( x \cdot (1/x) = 1 > 0 \), so \( 1/x \) has the sign of \( x \).
  (l) "'Before reading the proof, I tried the claim myself by squaring both sides.' Which strategy is this?" — Try it first.
- **B3** (new, `exr-reading-proofs-b3`) `[B3: Name the unstated facts]` [technique: Ho, Hu]. Statement: "Here is a proof.

  > **Claim.** For every real \( x \ge 0 \), \( x^3 + 2 \ge 3x \).
  >
  > (1) \( x^3 - 3x + 2 = (x - 1)^2 (x + 2) \). (2) \( (x - 1)^2 \ge 0 \). (3) \( x + 2 > 0 \). (4) So \( x^3 - 3x + 2 \ge 0 \), (5) that is, \( x^3 + 2 \ge 3x \).

  (a) Name the unstated fact behind each line. (b) Which line uses the hypothesis \( x \ge 0 \), and how? (c) Find the least \( c \) such that the same proof, with at most two lines reworded, proves the claim for every \( x \ge c \). Show that the claim fails at \( x = -3 \)."

  *Solution.*
  - (a):
    - (1) A polynomial identity, checked by expanding: \( (x^2 - 2x + 1)(x + 2) = x^3 + 2x^2 - 2x^2 - 4x + x + 2 = x^3 - 3x + 2 \).
    - (2) Every square is at least \( 0 \).
    - (3) \( x \ge 0 \) gives \( x + 2 \ge 2 > 0 \).
    - (4) A product of a non-negative and a positive number is non-negative, applied to (2) and (3), then (1) substituted (=E).
    - (5) Adding \( 3x \) to both sides keeps the inequality.
  - (b) Line (3), and only there.
  - (c) \( c = -2 \). For \( x \ge -2 \), line (3) becomes "\( x + 2 \ge 0 \)", and line (4) uses "a product of two non-negative numbers is non-negative"; every other line stands. Below \( -2 \) the claim is false. At \( x = -3 \): \( (-3)^3 + 2 = -25 \), while \( 3x = -9 \), and \( -25 \ge -9 \) fails. (For every \( x < -2 \), \( (x - 1)^2 > 0 \) and \( x + 2 < 0 \), so the product is negative.)

  **Marking scheme.** (10 points)
  - 5: (a), one per line, each naming the fact (not restating the line).
  - 2: (b) line (3), with how \( x \ge 0 \) enters.
  - 2: (c) \( c = -2 \), with the reworded lines (3) and (4).
  - 1: the failure at \( x = -3 \) computed.

  Fatal errors (0 for the step): explanations that restate the lines; in (c), "the hypothesis can be dropped".

**Sidecars:**
- `exr-reading-proofs-b3.py`: the identity; the claim on a grid of \( [-2, 10] \); its failure at \( -3 \) and on \( (-10, -2) \).
- `exr-reading-proofs-a2.py`: (g) and (i) values on samples; (k) the sign rule.

**Ledger lines:**
- the 3.3 recall (F1.7 §03, prose pointer);
- the unstated-fact subsection: \( n = 2 \) (arithmetic; `exr-using-an-implication-b5`, cited); "if \( 3 \mid n^2 \), then \( 3 \mid n \)" (stated; proved in 8.5 C3's solution, prose; nothing rests on it here). Classification, for S2a and for consistency with 8.6 (S2 round 1): each of the two lines asserts its step with "since", so its warrant is a general fact the line itself relies on. The false one is an instance of (N9), a "fact" neither proved nor a true school fact; the true one, left unproved, is the same entry with a true conclusion. Neither is (N14), whose premise is presupposed by a name, never asserted (§4.6, item 2). The 8.4 text does not tag them, since 8.6's catalogue comes later;
- the Quick check (school order facts);
- B3 (sidecar).

### 4.5 Section 8.5: Writing a Proof (`05-writing-proofs.md`)

**Budget:** main line ≤ 2,800 (now 2,413; R5 ≤ 2,600; expected about 2,790); folds ≤ 700 (R5 ≤ 650, plus F8.5-c ~50). No Looking-ahead box. **Fallback** if S3 measures over 2,800: the generalising lead's last sentence ("A line that uses a property of the particular object must be proved again, or the generalisation fails.", ~20 words) is cut; the example's *test* says it.

R5 §4.5 is executed in full. Additions:

1. **Fold F8.5-c** `title="What the example used"` (new; a sibling after `exm-subset-bounded-above`, which R5 moves up): 05:165 verbatim (~50 words). R5 keeps it after the example. It moves to make room for item 2, and nothing on the main line cites it.
2. **`## Generalising a proof`** (new subsection, ~200 words, the last of the main line, after `## Matching sentences and rules`) [technique: LPL — proof generalisation, gap-matrix row 7.7]. Lead (~50 words): "A proof written about one object sometimes proves much more. To **generalise** it, replace the object by a fresh name, the move of ∀I (Section 5.4), and read every line again. A line that uses only what the new name's box assumes stays. A line that uses a property of the particular object must be proved again, or the generalisation fails."

   **`exm-generalise-proof`** `[One of three, generalised]`. Statement: "Here are two proofs that one of \( 17 \), \( 18 \), \( 19 \) is a multiple of \( 3 \). (P1) \( 18 = 3 \cdot 6 \). (P2) \( 17 = 3 \cdot 5 + 2 \), so \( 17 + 1 = 3 \cdot 6 \). Which one generalises to 'for every integer \( n \), one of \( n \), \( n + 1 \), \( n + 2 \) is a multiple of \( 3 \)'? Write the general proof."

   Solution: "(P1) does not generalise: it uses a fact about \( 18 \) alone. (P2) does, once its one particular fact, \( 17 = 3 \cdot 5 + 2 \), is replaced by what every integer has: \( n = 3k \), \( n = 3k + 1 \) or \( n = 3k + 2 \) for an integer \( k \), a school fact. Let \( n \) be an integer [asm, for ∀I], and choose such a \( k \) [∃E]. If \( n = 3k \), \( n \) is a multiple of \( 3 \). If \( n = 3k + 1 \), then \( n + 2 = 3(k + 1) \). If \( n = 3k + 2 \), then \( n + 1 = 3(k + 1) \). In every case one of the three is a multiple of \( 3 \) [∨E]. Since \( n \) was arbitrary, this holds for every integer [∀I]. (P2) was the third case, with \( k = 5 \)." Then (inside the solution): "*The test:* after renaming, can every line still be justified from what the box of \( n \) assumes? A line that computes with the particular number fails the test."

   **Quick check (new):** "A proof that \( 7^2 - 1 \) is divisible by \( 8 \) reads '\( 7^2 - 1 = 48 = 8 \cdot 6 \)'. Does it generalise to every odd \( n \)? What would?" *Solution:* No: it computes with \( 7 \). A general proof writes \( n = 2k + 1 \), so \( n^2 - 1 = 4k(k + 1) \), and shows that \( k(k + 1) \) is even, since one of \( k \), \( k + 1 \) is even. That is the proof of Section 8.3's Exercise B2.

**Quick checks:** R5's three, plus the generalisation check: four in ~2,790 words, about one per 700.

**Exercises.**
- **A1, B1, B2 (ordering), B3 (faded), C1, C2:** as R5.
- **A2: Drill** (new, `exr-writing-proofs-a2`), 12 parts. Stem: "Answer each part in a line." The ramp follows the procedure's steps: symbols → unwinding → skeleton → order on the page → conventions → generalising.
  (a) "Write in symbols, with every quantifier and bound: 'the square of every odd integer is odd' (domain \( \nZ \))." — \( \forall n\, (\exists k\, (n = 2k + 1) \to \exists j\, (n^2 = 2j + 1)) \).
  (b) "Unwind 'the sequence \( (a_n) \) is bounded' (Section 5.6)." — \( \exists M \in \nR\; \forall n \in \nN\; (\abs{a_n} \le M) \).
  (c) "The goal is \( \forall \varepsilon > 0\; \exists \delta > 0\; \forall x\; (\abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon) \). What are the first and the last line of the outer box?" — First: the assumption \( \varepsilon_0 > 0 \), "Let \( \varepsilon > 0 \)" (asm, for ∀I). Last: \( \exists \delta > 0\; \forall x\; (\abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon_0) \), by ∃I with the chosen \( \delta \).
  (d) "A hypothesis says 'some integer \( k \) has \( n = 2k + 1 \)'. When does its box open?" — At once (step 3): an ∃E box with a fresh name \( k \).
  (e) "On the page, which comes first: 'let \( \delta \coloneqq \varepsilon/4 \)' or 'let \( x \) be a real number with \( \abs{x - 1} < \delta \)'?" — The constant (step 5). The box of \( x \) needs \( \delta \); chosen after \( x \), \( \delta \) could depend on \( x \).
  (f) "'\( x \) is positive and \( y \) is negative, and so \( xy < 0 \) and \( x - y > 0 \).' Which convention does this break?" — One claim per sentence: two claims joined by "and" hide which one is used later.
  (g) "A proof uses \( c \) in its fourth sentence, and \( c \) appears nowhere before. Which convention, and which entry of Section 8.6?" — Name every object when it is introduced; (N9), a line that cites nothing.
  (h) "Is 'this holds if \( x < 2 \)' a sentence of the page?" — No. It points backwards, from the goal, and belongs to scratch work or the Idea (step 4).
  (i) "Claim: \( x^2 - 4x + 3 < 0 \) for \( 1 < x < 3 \). A proof ends '… so \( x^2 - 4x + 3 = (x - 1)(x - 3) \).' What is missing?" — The end: \( x - 1 > 0 \) and \( x - 3 < 0 \), so the product is negative. The last sentence must be the claim (end with what was shown).
  (j) "A proof about the number \( 12 \) uses only '\( 12 \) is a multiple of \( 4 \)'. For which integers does the same proof prove the same claim?" — For every multiple of \( 4 \): rename \( 12 \) to a fresh \( n \), with the assumption \( 4 \mid n \).
  (k) "A proof about 'an arbitrary odd \( n \)' uses \( n > 0 \) in one line. What does it prove?" — Only the claim for positive odd \( n \). For all odd \( n \), the box would have to assume no more than oddness, so that line must be proved again without \( n > 0 \).
  (l) "Givens \( \forall x \in A\; (x \in B) \) and \( \forall x \in B\; (x \in C) \); Goal \( \forall x \in A\; (x \in C) \). Write the next row of the Givens/Goal table." — Givens: the same, and \( a_0 \in A \) (∀I, \( a_0 \) fresh). Goal: \( a_0 \in C \).
- **B4** (new, `exr-writing-proofs-b4`) `[B4: Which proof generalises?]` [technique: LPL]. Statement: "Two proofs that \( 6 \) divides \( 7^3 - 7 = 336 \): (P1) '\( 336 = 6 \cdot 56 \).' (P2) '\( 7^3 - 7 = 6 \cdot 7 \cdot 8 \), a product of three consecutive integers; one of them is even and one is a multiple of \( 3 \), so \( 6 \) divides the product.' (a) Which proof generalises to 'for every integer \( n \), \( 6 \mid n^3 - n \)', and why does the other not? (b) Write the general proof at level 3, with its fresh name and every fact it uses. (c) Which fact about \( 6 \) does (P2) leave unstated?"

  *Solution.*
  - (a) (P2) generalises; (P1) computes with \( 7 \) and says nothing about another \( n \).
  - (b) "Let \( n \) be an integer. Then \( n^3 - n = (n - 1)\, n\, (n + 1) \), a product of three consecutive integers. By @exm-generalise-proof, applied to \( n - 1 \), one of \( n - 1 \), \( n \), \( n + 1 \) is a multiple of \( 3 \), so \( 3 \mid n^3 - n \). By (E1), \( n \) is even or odd; if odd, \( n - 1 \) is even. So one factor is even, and \( 2 \mid n^3 - n \). Since \( 2 \) and \( 3 \) divide it, so does \( 6 \) (by @exr-quantifier-rhetoric-b3, the inclusion \( \supseteq \): if \( m = 2a = 3b \), then \( b = 2(a - b) \) and \( m = 6(a - b) \))."
  - (c) "If \( 2 \mid m \) and \( 3 \mid m \), then \( 6 \mid m \)", the fact of @exr-quantifier-rhetoric-b3.

  **Marking scheme.** (10 points)
  - 2: (a) (P2), with the reason (P1) fails.
  - 2: (b) the factorization and the fresh name.
  - 2: (b) a multiple of \( 3 \) among the factors, cited or proved.
  - 2: (b) an even factor, from (E1).
  - 1: (b) the step from \( 2 \) and \( 3 \) to \( 6 \), proved or cited.
  - 1: (c) the fact named.

  Fatal errors (0 for the step): a proof that checks finitely many \( n \) (N1); "\( 2 \mid m \) and \( 3 \mid m \), so \( 6 \mid m \)" with neither proof nor citation (N9).
- **C3** (new, `exr-writing-proofs-c3`) `[C3: From \( \sqrt 2 \) to \( \sqrt 3 \), and not to \( \sqrt 4 \)]` [technique: LPL — generalising a proof; gap-matrix row 7.7]. Statement: "The level-3 proof of @thm-sqrt2-irrational in @exm-sqrt2-four-levels uses (L) and @thm-square-even-implies-even. (a) Rewrite it as a proof that no rational number has square \( 3 \). You may use (L₃): every rational number is \( p/q \) with integers \( p \), \( q \), \( q \ne 0 \), not both multiples of \( 3 \). Prove the lemma your proof needs in place of @thm-square-even-implies-even. (b) Rewrite it once more for \( 4 \), with (L₄): every rational number is \( p/q \) with \( q \ne 0 \) and \( p \), \( q \) not both multiples of \( 4 \), which is true. Which line fails? Why must some line fail? (c) Say in one sentence what a generalisation keeps and what it must prove again."

  *Hint 1:* "The lemma is 'if \( 3 \mid n^2 \), then \( 3 \mid n \)'. Split on the remainder of \( n \) on division by \( 3 \)." *Hint 2:* "For (b), is \( 4 \) the square of a rational number?"

  *Solution.*
  - (a) *Lemma: if \( 3 \mid n^2 \), then \( 3 \mid n \).* Write \( n = 3k \), \( 3k + 1 \) or \( 3k + 2 \). In the first case \( 3 \mid n \). Otherwise \( n^2 = 3(3k^2 + 2k) + 1 \) or \( n^2 = 3(3k^2 + 4k + 1) + 1 \), and a number \( 3j + 1 \) is not a multiple of \( 3 \): from \( 3j + 1 = 3t \) we get \( 3(t - j) = 1 \), and no integer is \( \tfrac13 \). So those cases clash with \( 3 \mid n^2 \), and \( 3 \mid n \) holds in each by ⊥E.

    *The proof.* "Let \( r \) be rational, and suppose \( r^2 = 3 \). By (L₃), write \( r = p/q \) with integers \( p \), \( q \), not both multiples of \( 3 \). Then \( p^2 = 3q^2 \), so \( 3 \mid p^2 \), and by the lemma \( 3 \mid p \). Writing \( p = 3m \) gives \( 9m^2 = 3q^2 \), so \( q^2 = 3m^2 \), and by the lemma \( 3 \mid q \). So \( p \) and \( q \) are both multiples of \( 3 \), a contradiction; hence \( r^2 \ne 3 \)."
  - (b) The line "\( p^2 = 4q^2 \), so \( 4 \mid p^2 \), and by the lemma \( 4 \mid p \)" fails: "if \( 4 \mid n^2 \), then \( 4 \mid n \)" is false at \( n = 2 \). Some line must fail, because the claim is false: \( 4 = (2/1)^2 \), and \( p = 2 \), \( q = 1 \) satisfy (L₄). Lines that are all licensed, from true premises, cannot reach a false conclusion (soundness: @thm-soundness, and Section 7.2's statement for the quantifier steps).
  - (c) A generalisation keeps the skeleton (the boxes, the choices, the clash) and every line that used only properties shared by the new object; it must prove again each line that used a property of the old one, here the lemma.

  **Marking scheme.** (10 points)
  - 3: (a) the lemma, by the three cases, with the clash justified.
  - 2: (a) the rest of the proof, with (L₃) and the lemma used twice.
  - 2: (b) the failing line named, with the counterexample \( n = 2 \).
  - 1: (b) why a line must fail (\( \sqrt 4 = 2 \) is rational).
  - 2: (c) skeleton kept, particular lines re-proved.

  Fatal errors (0 for the step): the lemma asserted without proof (N9); in (b), blaming (L₄).

**Sidecars:**
- `exm-generalise-proof.py`: one of \( n \), \( n + 1 \), \( n + 2 \) divisible by \( 3 \), for \( |n| \le 300 \); \( 17 = 3 \cdot 5 + 2 \); the generalisation check's \( 48 \), and \( 8 \mid n^2 - 1 \) for odd \( |n| \le 301 \).
- `exr-writing-proofs-b4.py`: \( n^3 - n = (n - 1)n(n + 1) \); \( 6 \mid n^3 - n \) for \( |n| \le 500 \); \( 336 = 6 \cdot 56 = 6 \cdot 7 \cdot 8 \).
- `exr-writing-proofs-c3.py`: squares mod 3 are 0 or 1; \( (3k + 1)^2 \), \( (3k + 2)^2 \); the failure at \( n = 2 \) mod 4.
- `exr-writing-proofs-a2.py`: (i)'s signs on \( (1, 3) \).

**Ledger lines:**
- F8.5-c (moves with its text);
- `exm-generalise-proof` (the school fact "3k, 3k + 1, 3k + 2": F2.2 (promised), `thm-division-algorithm`; F1.4 §04's ∀I, prose pointer; sidecar);
- the generalisation check (`exr-levels-of-abbreviation-b2`, within the chapter);
- B4 (`exr-quantifier-rhetoric-b3` and `exm-generalise-proof`, within the chapter; (E1) of F1.2 §01);
- C3 ((L₃) and (L₄) stated as school facts in the item, as (L) is in F1.2 §02 with its proof promised to F2.2; `thm-soundness`, cited).

### 4.6 Section 8.6: Checking Proofs, and What Is Not Allowed (`06-checking-proofs.md`)

**Budget:** main line ≤ 3,000 (now 2,240; R5 ≤ 2,600; expected about 2,990); folds ≤ 360 (R5 ≤ 120, plus F8.6-b ~150 and F8.6-c ~70).

**The estimate (S2 round 1).** The S1 figure did not add up: (N12)–(N14) as S1 wrote them come to about 374 words, not ~210, and with the other additions (~265) 8.6 came to about 3,200. R5's main line is about 2,560. The estimate below is built from the text quoted in this section:
- the flowchart's lead and caption, +40;
- (N12), +95; (N13) with one instance, +85; (N14) with one instance and its line against (N9), +110. The second, true instances of (N13) and (N14) and the barber sentence move into fold F8.6-b (item 2);
- the families row, +30;
- the valid-but-improper paragraph, +75;
- the traditional-names table moves into fold F8.6-c (item 5), 0.

That is about 2,990. **Fallback** if S3 measures over 3,000: the valid-but-improper paragraph (item 4) moves into F8.6-b, and A2 (l)'s answer gains the sentence that makes it self-contained ("a step that no single rule writes, but a chain of rules does, is a matter of level, not an error"). Looking-ahead box: R5's, kept. **The (N11) decision** (recorded for S2 and S9): R5's split of (N11) into parts (a)–(c), with one new instance, is kept. The plan's "(N1)–(N11) untouched" protects the entries' numbers, rules and instances, all of which R5 keeps. R5's S2a item 1 checked fd2's one citation of (N11).

R5 §4.6 is executed in full. Additions:

1. **Figure 8.6-F, "Checking one line"** (new; `flowchart` template; after R5's 2×2 table and its paragraph, before the Quick check 06:16–22; ~40 words of lead-in and caption) [technique: device row "flowcharts"]. Lead: "The two columns, as a procedure for one line:"

   ```latex
   \begin{tikzpicture}[flowchart]
     \node[fc start] (s) {the next line of the proof};
     \node[fc step, below=of s] (q) {first column: is it true wherever\\the hypotheses and the open\\assumptions are true?};
     \node[fc test, below=of q] (t) {second column: which rule, or\\which chain of rules and silent\\steps, from which available lines?};
     \node[fc start, right=of t] (f) {no such chain: the proof fails\\here; name its entry, (N1)--(N14)};
     \node[fc start, below=of t] (n) {the line is licensed at its level;\\go on to the next one};
     \draw[fc arrow] (s) -- (q);
     \draw[fc arrow] (q) -- (t);
     \draw[fc arrow] (t) -- node[above, font=\scriptsize] {none} (f);
     \draw[fc arrow] (t) -- node[right, font=\scriptsize] {found} (n);
   \end{tikzpicture}
   ```

   Caption sentence after it: "A 'no' in the first column marks a line to look at first; only the second column decides. The silent steps are those of @def-silent-steps." (S2 round 1: the test node asked for one rule, which contradicted item 4. A line that a chain of rules writes is licensed at its level, and only a line that no chain of rules writes from the available lines fails.)

2. **(N12), (N13), (N14)**, appended inside the enumerate of `exm-not-allowed-catalogue`, after (N11) (06:44, in R5's lettered form), in the catalogue's format (~290 words; S2 round 1 measured the S1 text at ~374 and moved the second instances of (N13) and (N14) into fold F8.6-b) [technique: LPL, Ha; gap-matrix rows 1.12, 7.4; plan 6.6]:

   "12. **Distinct letters taken for distinct objects.** Two names introduced separately are treated as naming different objects, though no line says they differ. Breaks \( \rulename{\forall I} \): a box opened for two arbitrary names must cover every pair, including the pairs in which both name one object (\( \rulename{\forall E} \) may put the same term for both, @def-rule-universal-elimination). Instance: 'if \( a \) and \( b \) are roots of \( x^2 - 5x + 6 = 0 \), then \( a + b = 5 \): the two roots give \( x^2 - 5x + 6 = (x - a)(x - b) \), and comparing coefficients, \( a + b = 5 \)'. **False:** \( a = b = 2 \) are roots, and \( 2 + 2 = 4 \).

   13. **An 'and so on' with nothing behind it.** A step is repeated 'and so on', and its outcome is used for every stage, but the passage from each stage to the next, or the reason the process ends, is never proved. Breaks @ax-induction (or @thm-strong-induction): \( \rulename{{\to}E} \) on the axiom needs its step as a line, and 'and so on' is not that line. Instance: 'a non-empty set \( A \) of positive rational numbers has a least element: take \( a_1 \in A \); if it is not least, take \( a_2 \in A \) with \( a_2 < a_1 \), and so on, until the least element is reached' (**false:** \( \{1, \tfrac12, \tfrac13, \dots\} \) has no least element, and the process never ends).

   14. **An object named before it is shown to exist.** A step names an object, with 'the …' or 'let … be the …', and so presupposes that such an object exists (for 'the', exactly one), though no line states or proves it. In (N9) the step asserts a fact that is not available; here the missing premise is never asserted at all, because it hides inside a name. Breaks \( \rulename{\exists E} \), which opens its box only by citing a line \( \exists x\, \varphi \) (@def-rules-existential), and the use of 'the' (Section 5.8), which needs existence and uniqueness. Instance: 'let \( N \) be the largest natural number; then \( N + 1 \le N \), so \( 1 \le 0 \)' (**false:** the presupposed premise, that a largest natural number exists, is false)."

   **The line between (N9) and (N14)** (S2 round 1), which every tag in this chapter follows. (N9) is a step whose warrant is **asserted**, by "since", "so" or a citation, but is not available: the goal, a later result, or a general "fact" neither proved nor a true school fact ("\( 2 \mid m \) and \( 3 \mid m \), so \( 6 \mid m \)" with no argument; "the lemma" used unproved). (N14) is a step that **presupposes** a premise it never asserts at all, most often the existence (and uniqueness) behind "the" or "let … be the …". Checked against the chapter: the (N9) tags of 8.1 B4, 8.2 B3, 8.5 B4 and 8.5 C3 are all asserted warrants, and the 8.4 lines "since \( n^2 \) is a multiple of …" are (N9) cases (§4.4 ledger). The (N14) tags of 8.2's Not-allowed block ("let \( L \) be the limit"), 8.6 A2 (k) ("let \( n \) be the positive integer with …") and 8.6 B3 (v) ("let \( x \) be the real solution") are all presupposed by a name, and none of them asserts the existence it needs, so none is also (N9).

   **Fold F8.6-b** `title="True conclusions behind an 'and so on' and a 'the'"` (new, S2 round 1, budget; ~150 words; a sibling after the catalogue block): "Both new kinds of error can reach a true conclusion. The words of (N13)'s instance, said of a non-empty set of natural numbers, reach a true conclusion, but they leave out why the process ends: a strictly decreasing list of natural numbers that starts at \( a_1 \) has at most \( a_1 + 1 \) terms, which needs an induction. 'Let \( m \) be the least positive integer with \( m^2 > 50 \); since \( 7^2 = 49 \) and \( 8^2 = 64 \), \( m = 8 \)' reaches a true conclusion too, but the existence of a least such integer is a premise the proof must state: it is (N14). The barber who shaves exactly the villagers who do not shave themselves is (N14) as well; Section 5.6 shows that no such barber can exist (@thm-barber)." (Edge cases, STYLE §12.3: a true conclusion with an improper step. No exercise needs the fold: A2 (j) gives its own true (N13) instance.)

   (In (N13)'s instance "\( \{1, \tfrac12, \tfrac13, \dots\} \)" is the set \( \{1/n : n \in \nZ_{>0}\} \); the drafter writes whichever form the build renders. The catalogue's head sentence 06:31, "Each entry names the error, the rule it breaks and where that rule lives, and a failing instance whose conclusion is marked true or false", covers the three new entries, each with one instance.)

3. **The families table** (R5's, before the block): (N12) is added to "Naming errors", whose slogan becomes "A new choice gets a new name, and two names may name one thing." A new last row: "Iteration and existence errors | (N13), (N14) | An 'and so on' needs its step; a 'the' needs its object." There are now seven families.

4. **Valid but improper** (new paragraph, ~75 words, after 06:48 as R5 rewords it; S2 round 1: the S1 example, a propositional compression, is one that a single TAUT line writes from Section 4.8 on, as 8.3 says, so a first-order example replaces it): "The catalogue lists steps that can lead from true lines to a false one. A step can also be **valid but improper**. 'For all reals \( a \) and \( b \), \( a^2 + b^2 \ge 2ab \); so for all reals \( b \) and \( a \), \( a^2 + b^2 \ge 2ab \)', taken as one line, never leads from truth to falsehood, but no rule of the book writes it in one line, TAUT included (Section 8.3). That is a matter of level (@def-levels-of-proof), not an error: at level 0 it is ∀E twice and ∀I twice, and in prose it needs no words."

5. **Traditional names**, in **fold F8.6-c** `title="The errors under their traditional names"` (new, ~70 words with the table, a sibling after item 4's paragraph; S2 round 1, budget: an instructor-type comparison, STYLE §12.0, and no exercise needs it) [technique: Hu — informal fallacies under mathematical names; gap-matrix row 1.12]. One sentence: "Older books name some of these errors as fallacies:" then

   | Traditional name | Entry |
   |---|---|
   | hasty generalisation | (N1) |
   | equivocation: one name for two things | (N4) |
   | affirming the consequent; denying the antecedent | (N6) |
   | false dichotomy | (N8) |
   | begging the question | (N9) |
   | a presupposition ("the …") | (N14) |

   and "Affirming a disjunct is a common error of Section 1.6."

**Quick checks:** R5's three (two questions; family; (N2)). No new check: the budget goes to the entries. Three in ~2,990 words, about one per 1,000. The new A2 parts (i)–(l) drill (N12)–(N14) and the improper step. The roadmap bullet of §4.0 item 5 is reworded to match (the traditional names are in a fold).

**Exercises.**
- **A1, B1, B2, C1 (faded), C2, C3 (exit check):** as R5.
- **A2: Drill** (`exr-checking-proofs-a2`): R5's (a)–(h) (stem: "Name the entry of @exm-not-allowed-catalogue that each line commits, and say whether its conclusion is true"), then:
  (i) **new** "Let \( x \) and \( y \) be solutions of \( x^2 = 9 \). Then \( x^2 - y^2 = 0 \), so \( (x - y)(x + y) = 0 \), and since \( x \ne y \), \( x + y = 0 \)." — (N12); false: \( x = y = 3 \) gives \( x + y = 6 \).
  (j) **new** "\( a_1 = 2 \) and \( a_{n+1} = a_n^2 - 2 \). Then \( a_2 = 2 \), \( a_3 = 2 \), and so on, so \( a_n = 2 \) for every \( n \ge 1 \)." — (N13); true. The step "if \( a_n = 2 \), then \( a_{n+1} = 4 - 2 = 2 \)" is one line, and the proof must write it, as the step of an induction.
  (k) **new** "Let \( n \) be the positive integer with \( n^2 = 2 \). Then \( 1 < n^2 < 4 \), so \( 1 < n < 2 \)." — (N14). The presupposed premise, that such an integer exists, is false, and so is the conclusion that an integer lies strictly between \( 1 \) and \( 2 \).
  (l) **new** "From '\( x > 0 \)' and '(\( x > 0 \) implies \( y > 0 \)) and (\( y > 0 \) implies \( z > 0 \))', conclude '\( z > 0 \)' in one line." — No entry. No primitive rule writes the step in one line: at level 0 it is ∧E twice and →E twice. From Section 4.8 on, a single TAUT line citing both premises also writes it (Section 8.3). Either way it is a matter of level, not an error. (S2 round 1: the S1 answer called it improper outright, against 8.3's TAUT paragraph.)
- **B3** (new, `exr-checking-proofs-b3`) `[B3: Correct, or which entry?]` (verdict withheld; D5) [technique: LPL, Hu — critique with the verdict withheld]. Statement: "Each proof below is correct, or commits one of (N12), (N13), (N14); you are not told how many of each. For a correct proof, name its most delicate step. For a wrong one, name the entry, say whether the claim is true, and give a counterexample to the claim or a repair of the proof.
  (i) *Claim:* for all integers \( m \), \( n \), if \( m \) and \( n \) are odd, then \( mn \) is odd. *Proof:* write \( m = 2k + 1 \) and \( n = 2l + 1 \) with integers \( k \), \( l \); then \( mn = 4kl + 2k + 2l + 1 = 2(2kl + k + l) + 1 \).
  (ii) *Claim:* for all real \( a \), \( b \), if \( a^2 = b^2 \), then \( a = b \) or \( a = -b \). *Proof:* \( (a - b)(a + b) = a^2 - b^2 = 0 \), and a product of real numbers is \( 0 \) only if a factor is.
  (iii) *Claim:* for all integers \( m \), \( n \), \( m^2 + n^2 \ge 1 \). *Proof:* two different integers are not both \( 0 \), so one of \( m^2 \), \( n^2 \) is at least \( 1 \).
  (iv) *Claim:* every integer \( n \ge 2 \) is a product of primes. *Proof:* if \( n \) is prime, it is a product of one prime. If not, \( n = ab \) with \( 1 < a, b < n \); split \( a \) and \( b \) in the same way, and so on, until only primes remain.
  (v) *Claim:* \( 1 \) is a solution of \( x^2 + x + 1 = 0 \). *Proof:* let \( x \) be the real solution. Then \( x^3 - 1 = (x - 1)(x^2 + x + 1) = 0 \), so \( x^3 = 1 \), and since \( x \) is real, \( x = 1 \)."

  *Solution.*
  - (i) **Correct.** The delicate step is the second ∃E, which uses a second name \( l \). The case \( m = n \) is covered, since nothing stops \( k = l \): the names are distinct, the objects need not be.
  - (ii) **Correct.** The delicate step is the product fact. It gives "\( a - b = 0 \) or \( a + b = 0 \)" (→E, citing it), which is the claim, and no distinctness is assumed.
  - (iii) **(N12); the claim is false**: \( m = n = 0 \) gives \( 0 \). The proof took \( m \) and \( n \) to be different integers.
  - (iv) **(N13); the claim is true.** The "and so on" hides why the splitting ends: each factor is at least \( 2 \) and smaller than the number split. Repair by strong induction (@thm-strong-induction): if every \( k \) with \( 2 \le k < n \) is a product of primes, so is \( n \), being prime or \( ab \) with \( a \), \( b \) in that range.
  - (v) **(N14); the claim is false**: \( 1 + 1 + 1 = 3 \ne 0 \). The presupposed premise "\( x^2 + x + 1 = 0 \) has a real solution" is false, since \( x^2 + x + 1 = (x + \tfrac12)^2 + \tfrac34 > 0 \).

  Look-alikes: (i) and (iii) both use two letters; only (iii) assumes the letters differ.

  **Marking scheme.** (10 points: 2 per part)
  - 1: the verdict.
  - 1: for a correct proof, the delicate step named; for a wrong one, the entry with a counterexample (iii, v) or a repair (iv).

  Fatal errors (0 for that part): calling (i) an instance of (N12) because \( k \) and \( l \) might be equal; calling (iv) correct.
- **R1** (new, `exr-checking-proofs-r1`) `[R1: A dialogue]` [technique: Hu, Hk — a dialogue as an argument to extract; gap-matrix device row "dialogue extraction"]. It reviews (E1) of Section 2.1, ∀I of Section 5.4 and (N1). Statement: "Two students discuss a claim.

  > **Ana:** For every integer \( n \), \( n^2 + n \) is even.
  > **Ben:** Why?
  > **Ana:** Take \( n = 3 \): \( 9 + 3 = 12 \). Take \( n = 4 \): \( 16 + 4 = 20 \). It always works.
  > **Ben:** That is two numbers.
  > **Ana:** All right. \( n^2 + n = n(n + 1) \). If \( n \) is even, the product has an even factor. If \( n \) is odd, \( n + 1 \) is even, so again it has an even factor. Either way \( n^2 + n \) is even.
  > **Ben:** You only did positive numbers.
  > **Ana:** I never used that \( n \) is positive.

  (a) Which entry of @exm-not-allowed-catalogue does Ana's first argument commit? (b) Write her second argument as a level-3 proof, and name the rule each sentence carries. (c) Is Ben's last objection right? (d) On which fact does the case split rest, and where was it stated?"

  *Solution.*
  - (a) (N1): two instances, then "always".
  - (b) "Let \( n \) be an integer [∀I]. Then \( n^2 + n = n(n + 1) \) [algebra]. By (E1), \( n \) is even or odd [∨E, with the reason the cases exhaust]. If \( n \) is even, say \( n = 2k \) [∃E], then \( n(n + 1) = 2\bigl(k(n + 1)\bigr) \) is even [∃I, witness \( k(n + 1) \)]. If \( n \) is odd, say \( n = 2k + 1 \), then \( n + 1 = 2(k + 1) \), and \( n(n + 1) = 2\bigl(n(k + 1)\bigr) \) is even [∃E, ∃I]. In either case \( n^2 + n \) is even [∨E, closing; silent at level 3]."
  - (c) No. The box of \( n \) assumed only that \( n \) is an integer, and no line used more, so ∀I gives the claim for every integer: \( n \) is in no premise, and the conclusion is about the bound variable. A proof that used \( n > 0 \) would have had to assume it in the box.
  - (d) (E1), "every integer is even or odd", stated in Section 2.1 as a school fact.

**Sidecars:**
- `exm-not-allowed-catalogue.py` (R5's, extended):
  - (N12): the roots 2 and 3 of \( x^2 - 5x + 6 \), and \( 2 + 2 = 4 \);
  - (N13): \( 1/(n + 1) < 1/n \);
  - F8.6-b: a decreasing list from \( a_1 \) in \( \nN \) has at most \( a_1 + 1 \) terms, checked for \( a_1 \le 30 \) by search; \( 7^2 = 49 \le 50 < 64 = 8^2 \), and no smaller positive integer works.
- `exr-checking-proofs-a2.py`: (i) \( x = y = 3 \); (j) \( a_n = 2 \); (k) no integer squares to 2.
- `exr-checking-proofs-b3.py`: (i) and (ii) on a range; (iii) at \( (0, 0) \); (iv) the factorization of every \( n \le 500 \); (v) \( x^2 + x + 1 > 0 \).
- `exr-checking-proofs-r1.py`: \( n^2 + n \) even for \( |n| \le 500 \).

**Ledger lines:**
- (N12): `def-rule-universal-elimination`, cited; arithmetic; sidecar.
- (N13): `ax-induction` and `thm-strong-induction`, cited.
- (N14): `def-rules-existential`, cited; Section 5.8's description, prose pointer. The line against (N9): read off the two entries.
- F8.6-b: "a decreasing list in \( \nN \) from \( a_1 \) has at most \( a_1 + 1 \) terms", stated and not used as a reason; "the least positive integer with \( m^2 > 50 \) exists", a premise named in the fold; both F2.2 (promised), well-ordering; `thm-barber`, cited.
- The improper paragraph: `def-levels-of-proof`, within the section's chapter; Section 8.3's TAUT paragraph, within the chapter.
- F8.6-c, the traditional-names table: a regrouping, read off the entries.
- B3: `thm-strong-induction`, cited; school algebra; sidecar.
- R1: (E1) of F1.2 §01; F1.4 §04's ∀I side condition.

### 4.7 Section 8.7: The Dispute over Excluded Middle (`07-excluded-middle.md`)

**Budget:** main line ≤ 3,950 (now 3,781; R5 ≤ 3,800; layout ≤ 3,900; expected about 3,915: S1's ~3,890, plus item 5's sentence ~40, the longer Glivenko sentence ~5, less ~20 from item 1's shorter lead); folds ≤ 340 (R5 ≤ 200, plus F8.7-c ~140). **Fallback** if S3 measures over 3,950: the paragraph 07:11 (why ⊥E stays primitive, an instructor-type note, STYLE §12.0; nothing on the main line argues from it) moves into a new fold F8.7-d `title="Why ⊥E stays a primitive rule"`, about −100. Looking-ahead box: R5's, kept. Every result stays `.optional` (R5).

R5 §4.7 is executed in full. Changes and additions:

1. **`## Which laws survive without RAA {#laws-without-raa}`** (new subsection, ~210 words with its table). It goes after R5's `## Excluded middle cannot be refuted` (R5 §4.7, item 5) and before `## A short history` [technique: vD — which direction of each law survives; plan §3.6 item 6.7; gap-matrix row 9.1].

   Lead (~50 words; S2 round 1 shortened it from ~70 to pay for item 5): "Chapters 2 and 6 flagged every law they derived with RAA. Here they are side by side, split into directions. The middle column was derived without RAA. For the right column, with letters \( p \), \( q \), **no** derivation without RAA exists. The optional Section 8.8 proves this for the propositional rows; for the quantifier rows it is stated without proof."

   | Law | Derived without RAA | Needs RAA |
   |---|---|---|
   | double negation (@prp-double-negation) | (a) \( P \vdash \neg\neg P \) | (b) \( \neg\neg P \vdash P \) |
   | contraposition (@prp-contrapositive, @prp-contrapositive-converse) | \( P \to Q \vdash \neg Q \to \neg P \) | \( \neg Q \to \neg P \vdash P \to Q \) |
   | De Morgan (@prp-de-morgan) | (a), (b), (c) | (d) \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \) |
   | implication as a disjunction (@prp-implication-as-disjunction) | (a) \( \neg P \vee Q \vdash P \to Q \) | (b) \( P \to Q \vdash \neg P \vee Q \) |
   | excluded middle (@prp-excluded-middle) | \( \vdash \neg\neg(P \vee \neg P) \) (@prp-not-not-excluded-middle) | \( \vdash P \vee \neg P \) |
   | Peirce's law (@prp-peirce) | — | \( \vdash ((P \to Q) \to P) \to P \) |
   | negated implication (@prp-negated-implication) | \( \varphi \wedge \neg\psi \vdash \neg(\varphi \to \psi) \) | \( \neg(\varphi \to \psi) \vdash \varphi \wedge \neg\psi \) |
   | modus tollens, disjunctive syllogism, constructive dilemma (@prp-modus-tollens, @prp-disjunctive-syllogism, @exm-constructive-dilemma) | all | — |
   | quantifier negation (@prp-quantifier-negation) | (b); (c) both ways | (a) \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \) |
   | passage laws (@prp-quantifier-passage) | eight of the ten directions | \( \dashv \) in (d) and in (e) |

   After the table (one sentence; S2 round 1): "For each propositional entry of the right column, the double negation of its conclusion is derivable without RAA from the same premises, by Glivenko's theorem in the remark above (stated without proof) applied to the implication from the premises' conjunction; Exercise B5 (a) and (b) derive two cases." (B5 (c) is not a Glivenko case: it is an instance of excluded middle giving ¬¬E. The step from \( \neg\neg(\gamma \to \varphi) \) and \( \gamma \) to \( \neg\neg\varphi \) is RAA-free, S2a item 13; Γ is a finite list, binding rule 6.)

   **Quick check (new):** "An intuitionist has proved \( \neg Q \to \neg P \). May she conclude \( P \to Q \)?" *Solution:* Not in general: that is @prp-contrapositive-converse, in the right column. She may when \( Q \) is itself a negation, by R5's fold F5.1-c, which reads Section 2.5's fold.

   (The table is derived from the statements of the cited results, each of which says where RAA enters, and from B4's census as recomputed under item 6 below. For the right column's propositional rows, see §4.8, item 7. The rule "every result stays `.optional`" concerns labelled results, and the table is unlabelled prose.)

2. **Pointers to 8.8** (critic small correction 3; prose pointers, no `@ref`, since 8.8 is later). There are **six** (S2 round 1: S1 listed four). Each names a claim that 8.8 proves:
   - The lead of the new table (item 1): "The optional Section 8.8 proves this for the propositional rows".
   - B5 (d)'s parenthesis (below): one instance of Peirce's law does not give the instance of excluded middle that gives it, proved by 8.8's C1 (b).
   - Table cell 07:15: "not derivable (@thm-raa-independent for the propositional rules; …)" → "not derivable (@thm-raa-independent for the propositional rules, and the optional Section 8.8 again, by stages of knowledge; …)".
   - R5's Quick check in "Excluded middle cannot be refuted" ("Does @prp-not-not-excluded-middle show that \( P \vee \neg P \) is derivable without RAA?"): its solution ends "… and Chapter 4's optional @thm-raa-independent shows that no derivation without RAA reaches it, as does the optional Section 8.8."
   - B1's solution 07:304: "(we state this without proof)" → "(the optional Section 8.8 proves it with a two-stage model)".
   - R3's solution 07:558, first sentence: "…; we state this without proof, as Chapter 2 did for similar sequents" → "…; the optional Section 8.8 proves it with a two-stage model".
   - The other "stated without proof" claims stay as they are. These are 07:11 (⊥E; Kripke models do not address it), 07:15's quantifier clause, 07:80 (Glivenko), the remark's quantifier failure, and the right column's quantifier rows.
3. **Fold F8.7-c** `title="Proofs as programs, in Lean"` (new, after `## Proofs as programs`' paragraph 07:210): 07:212 and the Lean block 07:214–221, verbatim (~140 words). The warning 07:223–225 stays on the main line. This is the budget trade for item 1. The Lean passage is an instructor-type comparison (STYLE §12.0), and nothing on the main line cites it.
4. **R1's solution** (07:462): "by part (b) of @prp-bounded-quantifier-negation and then part (a) under the \( \forall \)" → "by part (b) of @prp-bounded-quantifier-negation, and then part (a) used under the \( \forall \), as @prp-replacement of Section 6.2 allows". (Critic C2: a law used on a part under a quantifier is licensed syntactically.)
5. **TAUT is not an intuitionistic rule** (new, S2 round 1; one sentence, ~40 words, appended to 07:9, the definition of an intuitionistic derivation): "TAUT (Section 4.8) is not among these rules: it is licensed by @cor-derivable-iff-valid, that is, by the completeness theorem, whose proof splits on atoms by LEM (@lem-atom-splitting), so a line justified by TAUT, on a formula or on a propositional skeleton (Section 6.3), uses RAA in the sense just defined." Paid by item 1's shorter lead.
6. **B4's census is recomputed** (S2 round 1; supersedes R5 §4.7's "its solution 07:24–28 verbatim" for part (b)). R5 moved the Quick check 07:20–28 into B4 with its solution verbatim. That text predates the deepened Chapters 3–7. Part (a) (Chapter 2) stays verbatim unless ch02-deepen's delivered Chapter 2 adds a labelled result derived with a classical rule; S3 checks. Part (b) is recomputed by the drafter against the delivered Chapters 3–7, by the same rule ("derived with RAA, directly or through ¬¬E, LEM, or a cited result that uses one of them"). It lists at least what 07:28 lists, plus @def-rule-taut's rule TAUT and @prp-taut-skeleton (Section 6.3), both licensed through @thm-completeness, and every new result of 3.x, 4.x, 5.8 and 7.4–7.6 that the delivered text flags as classical. The table of item 1 and S2a item 13 are read off the recomputed census.

   **Recomputed at S2 round 2** against the delivered Chapters 2–7 (every labelled proposition, theorem, lemma and corollary whose block, proof or folds use RAA, ¬¬E, LEM or TAUT, or cite a result that does; checked by grep and by reading each hit). The drafter writes B4's solution from this list:
   - (a) Chapter 2: **unchanged**, 07:24 verbatim. The delivered Chapter 2 has exactly the seven classical results listed there (all in 2.5); `thm-squares-order` cites only `prp-contrapositive`, and `prp-equivalence-cycle`, `lem-not-iff-own-negation` and `prp-provable-equivalence-basics` use none.
   - (b) Chapter 3: @prp-derivable-iff-negation-inconsistent (b), direction \( (\Leftarrow) \), whose box closes by RAA (the delivered text says so). Chapter 4: @lem-atom-splitting, through LEM, and with it @thm-completeness and the direction \( (\Leftarrow) \) of @cor-derivable-iff-valid; the step TAUT of @def-rule-taut, licensed through @cor-derivable-iff-valid; and, in the optional Section 4.10, @lem-lindenbaum (its key step uses RAA, through @prp-derivable-iff-negation-inconsistent), @thm-completeness-infinite and @thm-compactness, as the paragraph after the proof of @thm-completeness-infinite says (10-compactness.md:189). Chapter 5: none (`thm-barber` cites only `lem-not-iff-own-negation`; `prp-definitional-extension`, `prp-unique-existence-use` use no classical rule). Chapter 6: 07:28's six items, unchanged (@prp-quantifier-negation (a); \( \vdash \) of @prp-negated-implication; \( \vdash \) of @prp-bounded-quantifier-negation (a); the two directions \( \dashv \) of @prp-quantifier-passage; @prp-arbitrarily-close-equal), plus @prp-taut-skeleton (Section 6.3), through @cor-derivable-iff-valid; `prp-quantifier-distribution` ("all four are derived without RAA") and `prp-replacement` (rules of Chapters 1 and 2 only) are not classical. Chapter 7: none derived; the classical theorems of 7.6 (`thm-first-order-completeness` and what rests on it) are stated without proof, so the census does not reach them, and the solution says so in one clause.
   - Not listed, since they are statements about valuations and derive nothing: the results of 4.4, 4.5 and 4.9 (for example `prp-standard-equivalences`, `thm-monotonicity`), whose remarks mention RAA only as history. The solution adds one sentence saying this, so that a student who lists them is told why they do not count.
   - Size: the solution grows by about 110 words; it is an exercise solution and does not count against 8.7's main-line budget.

**Quick checks:** R5's four, plus the contraposition check: five in ~3,915 words, about one per 780.

**Exercises.**
- **A1, B1 (pointer, item 2), B2, B3, C1, C2, R1 (item 4), R2, R3 (item 2), R4:** as R5. **B4:** as R5, with its solution (b) recomputed (item 6).
- **A2: Drill** (new, `exr-excluded-middle-a2`), 12 parts. Stem: "Answer each in a line." Ramp: intuitionistic or not → BHK readings → apply the table.
  (a) "A derivation's last line is \( P \), by RAA from a box on \( \neg P \). Is the derivation intuitionistic?" — No.
  (b) "A box opens with \( P \) and ends in \( \bot \), and the next line is \( \neg P \). Which rule? Intuitionistic?" — ¬I; yes.
  (c) "Is \( \neg\neg\neg P \vdash \neg P \) derivable without RAA?" — Yes: @exm-triple-negation derives it without RAA.
  (d) "A classmate derives \( \neg P \vee \neg Q \) from \( \neg(P \wedge Q) \) and says no RAA was used. What do you check first?" — Every line and every cited result. That direction of De Morgan needs RAA (§8.7's table), so some line is RAA, ¬¬E or LEM, or cites a result derived with one.
  (e) "Under BHK, what does a proof of \( (P \wedge Q) \to P \) do?" — It takes any pair, a proof of \( P \) and a proof of \( Q \), and returns the first component.
  (f) "Under BHK, what must a proof of \( \exists n \in \nN\; (n^2 > 50) \) hand over?" — A natural number with a proof of the instance; for example \( 8 \), with \( 8^2 = 64 > 50 \).
  (g) "'\( x \ge 0 \) or \( x < 0 \); we consider the two cases.' What is this in logical form, and does the book flag it?" — LEM in form, an instance of trichotomy. Not flagged: it rests on an axiom for the real numbers ("The book's position").
  (h) "'Suppose \( \sqrt 3 \) is rational. … a contradiction. Hence \( \sqrt 3 \) is irrational.' Intuitionistic?" — Yes: the goal is a negation, and the box closes by ¬I.
  (i) "A proof establishes \( \neg\neg\exists x\, \varphi \). What does it hand over under BHK?" — No object: a method that turns any refutation of \( \exists x\, \varphi \) into a proof of \( \bot \).
  (j) "True or false: every intuitionistic derivation is a derivation of Chapters 1–7." — True. It uses some of the rules, so soundness applies to it.
  (k) "May an intuitionist argue 'not every element of \( A \) is positive, so some element of \( A \) is not positive'?" — Not in general: that is @prp-quantifier-negation (a), derived with RAA. She asks for the element.
  (l) "Which line of the proof of @thm-irrational-power-rational would an intuitionist reject, and would she reject its conclusion?" — The first, the LEM split on "\( s \) is rational". Not the conclusion: @prp-log2-9-irrational proves it with a named witness and no classical rule.
- **B5** (new, `exr-excluded-middle-b5`) `[B5: Behind two negations, and one instance]` [technique: vD — Glivenko instances; plan 6.7]. Statement: "Derive each without RAA, ¬¬E, LEM or TAUT, and without citing a result derived with them: (a) \( \neg(P \wedge Q) \vdash \neg\neg(\neg P \vee \neg Q) \); (b) \( P \to Q \vdash \neg\neg(\neg P \vee Q) \); (c) \( \vdash (P \vee \neg P) \to (\neg\neg P \to P) \). (d) Which row of the table in 'Which laws survive without RAA' does each concern?"

  *Solution.* (a), 13 lines:

  ```latex
  \begin{nd}
    \hypo {1} {\neg (P \wedge Q)}
    \open
    \hypo {2} {\neg (\neg P \vee \neg Q)}
    \open
    \hypo {3} {P}
    \open
    \hypo {4} {Q}
    \have {5} {P \wedge Q} \ai{3,4}
    \have {6} {\bot} \ne{5,1}
    \close
    \have {7} {\neg Q} \ni{4-6}
    \have {8} {\neg P \vee \neg Q} \oi{7}
    \have {9} {\bot} \ne{8,2}
    \close
    \have {10} {\neg P} \ni{3-9}
    \have {11} {\neg P \vee \neg Q} \oi{10}
    \have {12} {\bot} \ne{11,2}
    \close
    \have {13} {\neg\neg (\neg P \vee \neg Q)} \ni{2-12}
  \end{nd}
  ```

  (b), 10 lines:

  ```latex
  \begin{nd}
    \hypo {1} {P \to Q}
    \open
    \hypo {2} {\neg (\neg P \vee Q)}
    \open
    \hypo {3} {P}
    \have {4} {Q} \ie{1,3}
    \have {5} {\neg P \vee Q} \oi{4}
    \have {6} {\bot} \ne{5,2}
    \close
    \have {7} {\neg P} \ni{3-6}
    \have {8} {\neg P \vee Q} \oi{7}
    \have {9} {\bot} \ne{8,2}
    \close
    \have {10} {\neg\neg (\neg P \vee Q)} \ni{2-9}
  \end{nd}
  ```

  (c), 10 lines:

  ```latex
  \begin{nd}
    \open
    \hypo {1} {P \vee \neg P}
    \open
    \hypo {2} {\neg\neg P}
    \open
    \hypo {3} {P}
    \have {4} {P} \r{3}
    \close
    \open
    \hypo {5} {\neg P}
    \have {6} {\bot} \ne{5,2}
    \have {7} {P} \be{6}
    \close
    \have {8} {P} \oe{1,3-4,5-7}
    \close
    \have {9} {\neg\neg P \to P} \ii{2-8}
    \close
    \have {10} {(P \vee \neg P) \to (\neg\neg P \to P)} \ii{1-9}
  \end{nd}
  ```

  Every box closes by ¬I, →I or ∨E. No line uses RAA, ¬¬E or LEM, and no line cites a result. In (c), line 6 is ¬E on \( \neg P \) (line 5) and \( \neg\neg P \) (line 2).

  (d) (a) concerns De Morgan (d): it is Glivenko's double negation of that row's conclusion. (b) concerns implication as a disjunction (b), in the same way. (c) concerns double negation (b): one instance of excluded middle, taken as a hypothesis, gives double-negation elimination at that instance with no further classical step. (The optional Section 8.8's Exercise C1 shows that such a step need not run back: one instance of excluded middle gives Peirce's law for that letter, and that instance of Peirce's law does not give the instance of excluded middle.)

  **Marking scheme.** (10 points)
  - 3: (a).
  - 3: (b).
  - 3: (c).
  - 1: (d).
  - For each derivation: 1 for the skeleton (the outer ¬I or →I box and its last line); 2 for the inside, each clash named.

  Fatal errors (0 for that derivation): a line justified by RAA, ¬¬E or LEM; a line justified by TAUT (each sequent is a tautology, so one TAUT line would "derive" it, but TAUT is licensed by completeness, which splits on atoms by LEM: item 5); citing @prp-de-morgan (d), @prp-implication-as-disjunction (b) or @prp-double-negation (b), each derived with RAA.

**Sidecars:**
- `exr-excluded-middle-b5.py`: truth-table validity of the three sequents (each derivation is checked by `tools/check_fitch.py`).
- `exr-excluded-middle-a2.py`: (f) \( 8^2 = 64 \).
- The table's propositional right-column claims are checked by `kripke.py` (§4.8).

**Ledger lines:**
- The table: each row read off the cited statements (prp-double-negation, prp-contrapositive, prp-contrapositive-converse, prp-de-morgan, prp-implication-as-disjunction, prp-excluded-middle, prp-not-not-excluded-middle, prp-peirce, prp-negated-implication, prp-modus-tollens, prp-disjunctive-syllogism, exm-constructive-dilemma, prp-quantifier-negation, prp-quantifier-passage, all cited). Right column, propositional rows: F1.5 §08 (later section of this chapter; optional), prose pointer, and `thm-raa-independent` for two rows. Quantifier rows: stated without proof and marked so; nothing depends on them.
- The Glivenko sentences: the theorem stated without proof (the remark 07:79–81), extended to finite lists of premises through the conjunction of the premises (inline; RAA-free step, S2a item 13).
- Item 5's sentence: `def-rule-taut`, `cor-derivable-iff-valid` and `lem-atom-splitting`, F1.3 §08, cited; `def-propositional-skeleton`, F1.8 §03, prose pointer.
- B4's recomputed census (item 6): each listed result cited, against the delivered Chapters 3–7.
- F8.7-c: moves with its text.
- R1's clause: `prp-replacement`, F1.8 §02, cited.
- B5: `check_fitch.py`; sidecar.

### 4.8 Section 8.8: Stages of Knowledge: Kripke Models (`08-kripke-models.md`, new, optional)

**Budget:** main line ≤ 3,600 (expected about 3,450); folds ≤ 750 (F8.8-a ~250, F8.8-b ~450). No Looking-ahead box, and no forward pointer of any kind. The section is the volume's last.

**Purpose.** Section 8.7 names several classical laws that have no derivation without RAA. For excluded middle and double-negation elimination, Chapter 4's optional @thm-raa-independent gave a proof; for the rest, 8.7 states the fact without proof. This section proves all of the propositional ones [technique: Si, vD — the Kripke "stages of knowledge" semantics; gap-matrix row 9.2, "OPT-CH (high value)"]. It mirrors the propositional half's meaning chapter in miniature:
- a semantics (stages instead of rows);
- a soundness theorem whose proof is 4.7's proof with the →I and ¬I cases redone (heredity);
- countermodels, the refuting row of logic without RAA.

It is optional, and nothing outside it depends on it. 8.7's pointers to it are prose (item 2 of §4.7).

**Scope.** Propositional formulas only: letters, ⊥, ¬, ∧, ∨, →, ↔ (Chapter 4's formulas, @def-formula). Γ is a finite list (smaller correction 1). Quantifiers are named once, in item 9's remark, and never treated.

**Front matter** (as 7.3 does at its 03:3): `# Stages of Knowledge: Kripke Models`, then the opening paragraph (~120 words):

"This section is optional, and nothing outside it depends on it. Section 8.7 named several classical laws that have no derivation without RAA. For two of them, excluded middle and double-negation elimination, Chapter 4's optional @thm-raa-independent gave a proof by a three-valued reading; for the rest it stated the fact without proof. Truth tables cannot show it: every row makes \( p \vee \neg p \) true. Here is a reading that covers them all. A statement is not true or false once and for all, but *known* or *not yet known* at a stage of an inquiry that grows. The rules without RAA are sound for this reading, and RAA is not; two or three stages then suffice to show which laws need it."

**The main line, in order.**

1. **`## Stages of knowledge`** (~250 words). The story (~90 words): "An inquiry passes through stages. At each stage some atomic statements are known: established, never to be withdrawn. From a stage, the inquiry may go on in several ways, to later stages where more is known. Nobody knows which way it will go." Then the definition.

   **`def-kripke-model`** `[Kripke Model]`: "A **Kripke model** consists of:
   - a finite non-empty set of **stages**;
   - for each stage \( w \), a set of stages **reachable** from \( w \) (written \( w \le w' \)), such that \( w \le w \) for every stage, and \( w \le w' \) and \( w' \le w'' \) give \( w \le w'' \);
   - for each stage \( w \), a set of letters **known at** \( w \), such that a letter known at \( w \) is known at every stage reachable from \( w \)."

   Then (~70 words): "We draw a model as dots for the stages, with an arrow from a stage to each stage that comes directly after it. A stage is reachable from \( w \) when it can be reached by following arrows, none or several; so \( w \) reaches itself, and arrows are never drawn for that. Beside each dot stands the set of letters known there." The template figure of the two-stage model (\( M_1 \)):

   ```latex
   \begin{tikzpicture}[structure]
     \node[elt, label=below:$w_0$, label=right:$\varnothing$] (a) at (0,0) {};
     \node[elt, label=above:$w_1$, label=right:$\{p\}$] (b) at (0,1.6) {};
     \draw[rel] (a) -- (b);
   \end{tikzpicture}
   ```

   Caption sentence: "The model \( M_1 \): at \( w_0 \) nothing is known yet; at the later stage \( w_1 \), \( p \) is known."

2. **`## Forcing`** (~450 words).

   **`def-forcing`** `[Forcing]`: "Let \( w \) be a stage of a Kripke model. **\( w \) forces** a formula \( \varphi \), written \( w \Vdash \varphi \), as follows. The definition is a recursion on \( \varphi \) (@thm-structural-recursion) that defines, for each formula, the set of stages that force it; clauses (K5) and (K6) need the sets of its parts, at other stages. (S2 round 1: the clauses are named (K1)–(K7), since @def-formula's clauses are already (F1)–(F4).)
   - (K1) \( w \Vdash p \), for a letter \( p \), if \( p \) is known at \( w \);
   - (K2) \( w \Vdash \bot \) never;
   - (K3) \( w \Vdash \varphi \wedge \psi \) if \( w \Vdash \varphi \) and \( w \Vdash \psi \);
   - (K4) \( w \Vdash \varphi \vee \psi \) if \( w \Vdash \varphi \) or \( w \Vdash \psi \);
   - (K5) \( w \Vdash \varphi \to \psi \) if every stage \( w' \) reachable from \( w \) with \( w' \Vdash \varphi \) has \( w' \Vdash \psi \);
   - (K6) \( w \Vdash \neg\varphi \) if no stage reachable from \( w \) forces \( \varphi \);
   - (K7) \( w \Vdash \varphi \leftrightarrow \psi \) if \( w \Vdash \varphi \to \psi \) and \( w \Vdash \psi \to \varphi \).

   A stage **refutes** a sequent \( \Gamma \vdash \psi \) if it forces every formula of \( \Gamma \) and does not force \( \psi \)."

   *In words* (~80 words): "A conjunction or a disjunction is decided at the stage itself, and a disjunction is forced only when one of its sides is: the inquiry must already know which. An implication and a negation look ahead. To force \( \varphi \to \psi \) is to know that, however the inquiry goes on, \( \psi \) will be known whenever \( \varphi \) is. To force \( \neg\varphi \) is to know that \( \varphi \) will never be known. Not forcing \( \varphi \) is weaker than forcing \( \neg\varphi \)."

   Then, on rows (~70 words): "A model with **one stage** is a row of a truth table. With one stage, the stages reachable from \( w \) are \( w \) alone, so (K5) says '\( \varphi \) is not forced, or \( \psi \) is', and (K6) says '\( \varphi \) is not forced': forcing becomes Chapter 4's truth (@def-truth-value). Kripke models are rows that can grow."

   The counterexample-set sentence (D4): "A stage that refutes \( \Gamma \vdash \psi \) forces every member of \( \Gamma \) and not \( \psi \), which is weaker than forcing \( \neg\psi \). It is Section 1.1's counterexample set, read at a stage: where truth tables make \( \neg\psi \) true, a stage only fails to know \( \psi \)."

   **Quick check (new):** "In a one-stage model in which \( p \) is not known, does the stage force \( \neg p \)? Does it force \( p \vee \neg p \)?" *Solution:* Yes to both. The only stage reachable is the stage itself, which does not force \( p \), so (K6) gives \( \neg p \), and (K4) gives \( p \vee \neg p \). One stage is one row.

3. **`## A first countermodel`**, with **`exm-two-stage-model`** `[Two stages refute excluded middle]` (~280 words). Statement: "In \( M_1 \), decide whether \( w_0 \) forces \( p \), \( \neg p \), \( p \vee \neg p \), \( \neg\neg p \) and \( \neg\neg p \to p \)."

   Solution:
   - \( p \) is not known at \( w_0 \), so \( w_0 \not\Vdash p \) (K1).
   - \( w_1 \) is reachable from \( w_0 \) and forces \( p \), so \( w_0 \not\Vdash \neg p \) (K6).
   - Hence \( w_0 \not\Vdash p \vee \neg p \) (K4): \( w_0 \) refutes \( \vdash p \vee \neg p \).
   - Next, \( \neg\neg p \). No stage reachable from \( w_0 \) forces \( \neg p \): not \( w_0 \), as just shown, and not \( w_1 \), which forces \( p \). So \( w_0 \Vdash \neg\neg p \).
   - So \( w_0 \) forces \( \neg\neg p \) and not \( p \): it refutes \( \neg\neg p \vdash p \), and by (K5), \( w_0 \not\Vdash \neg\neg p \to p \).

   Then (inside the solution): "At \( w_0 \) the inquiry knows that \( p \) cannot be refuted, since \( p \) becomes known later on every way it can go, but it does not yet know \( p \). Excluded middle asks it to know now which of \( p \) and \( \neg p \) holds."

4. **`## Knowledge persists`** (~150 words on the main line).

   **`lem-heredity`** `[Heredity]`: "In every Kripke model, if \( w \Vdash \varphi \) and \( w \le w' \), then \( w' \Vdash \varphi \)."

   *In words:* "What a stage forces, every later stage forces. Letters stay known by the definition. The lemma says the same of every formula." Then: "The proof is a structural induction on \( \varphi \) (@thm-structural-induction); it is in the fold." **Fold F8.8-a** `title="The proof of heredity"`, ~250 words:
   - Letters: the condition on known letters in @def-kripke-model.
   - \( \bot \): no stage forces it, so there is nothing to show.
   - \( \wedge \) and \( \vee \): the induction hypothesis for the parts, at \( w' \).
   - \( \to \): if \( w \Vdash \varphi \to \psi \) and \( w \le w' \), then every \( w'' \) reachable from \( w' \) is reachable from \( w \) (transitivity), so any such \( w'' \) forcing \( \varphi \) forces \( \psi \): \( w' \Vdash \varphi \to \psi \). No induction hypothesis is used.
   - \( \neg \): the same, with "no \( w'' \) forces \( \varphi \)".
   - \( \leftrightarrow \): from the two implications.

   **Quick check (new):** "A stage \( w \) forces \( \neg\varphi \), and \( w' \) is reachable from \( w \). Why does \( w' \) force \( \neg\varphi \), whatever \( \varphi \) is?" *Solution:* \( w \Vdash \neg\varphi \) says that no stage reachable from \( w \) forces \( \varphi \). The stages reachable from \( w' \) are among those, by transitivity, so none of them forces \( \varphi \) either. Nothing is assumed about \( \varphi \) itself.

5. **`## The rules without RAA are sound for stages`** (~400 words).

   **`thm-kripke-soundness`** `[Soundness without RAA]`: "Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If \( \Gamma \vdash \psi \) by a derivation in which no line uses RAA, nor a derived rule or cited result whose derivation uses RAA, nor TAUT, then every stage of every Kripke model that forces every formula of \( \Gamma \) forces \( \psi \)."

   *In words:* "A derivation without RAA never leads from what a stage knows to what it does not know."

   Then one sentence (S2 round 1): "TAUT (Section 4.8) is not among the rules here: it is licensed by completeness, whose proof uses LEM (Section 8.7), so a derivation with a TAUT line is not a derivation without RAA."

   Then the **rule-by-rule table** (~200 words; a mirror of 4.7's meaning table, layout G7): "The proof is Chapter 4's proof of @thm-soundness, Steps 1–4, with 'every valuation making the context true' replaced by 'every stage forcing the context'. Each rule's case, in one line:"

   | Rule | Why its case holds at a stage \( w \) that forces the context |
   |---|---|
   | ∧I, ∧E, ∨I, R, ↔E | the clause (K3), (K4) or (K7) at \( w \) itself, with (K5) at \( w' = w \) for ↔E |
   | →E, ¬E | (K5) or (K6), applied at \( w' = w \), which is reachable from \( w \) |
   | ⊥E | no stage forces \( \bot \), so there is nothing to show |
   | ∨E | \( w \) forces one side, by (K4); the box of that side ends in its last line, forced at \( w \) |
   | →I, ¬I, ↔I | a later stage \( w' \) forces the context too, **by heredity**, so the box applies at \( w' \) |
   | RAA | **fails**: its box on \( \neg\varphi \) shows only that no stage reachable from \( w \) forces \( \neg\varphi \), that is, \( w \Vdash \neg\neg\varphi \); in \( M_1 \), \( w_0 \) forces \( \neg\neg p \) and not \( p \) |

   The full proof is in **fold F8.8-b** `title="The proof, case by case"` (~450 words), written in 4.7's terms.
   (S2 round 1: renumbered to match 4.7's proof of @thm-soundness, 07-soundness.md:200–270 as delivered (S2 round 2; S1 cited 147–217), where Step 2 is the strong induction, Step 3 the cases and Step 4 the last line.)
   - Step 1: reduce to primitive rules, as 4.7 does, since a derived rule derived without RAA unfolds into primitive rules other than RAA.
   - Step 2: the claim for every line, by strong induction on \( k \) (@thm-strong-induction): every stage forcing the context \( \Gamma_k \) of line \( k \) forces its formula \( \varphi_k \).
   - Step 3: the cases. One-step rules use the clauses at \( w \). For →I: let \( w \) force \( \Gamma_k \), and let \( w' \ge w \) force \( \varphi \). By heredity \( w' \) forces \( \Gamma_k \), so \( w' \) forces the context of the box's last line, \( \Gamma_k \) and \( \varphi \) (@lem-context-inclusion (b)). By the induction hypothesis, \( w' \Vdash \psi \). So \( w \Vdash \varphi \to \psi \) by (K5). ¬I is the same with \( \psi = \bot \): no \( w' \ge w \) can force \( \varphi \), since it would force \( \bot \); so \( w \Vdash \neg\varphi \). ↔I is two →I cases. ∨E: \( w \) forces \( \varphi \) or \( \psi \) at \( w \) itself; apply the induction hypothesis to that side's box at \( w \). ⊥E: vacuous. RAA: the case fails, as the table says.
   - Step 4: the last line. It lies in no box (@def-derivation), so its context \( \Gamma_n \) consists of premises only, each of which belongs to \( \Gamma \) (@def-derivable), as in 4.7's Step 4. A stage forcing every formula of \( \Gamma \) forces every formula of \( \Gamma_n \), so by Steps 2–3 it forces \( \varphi_n = \psi \).

   **`cor-kripke-countermodel`** `[Kripke Countermodel]`: "If some stage of some Kripke model refutes \( \Gamma \vdash \psi \), then \( \Gamma \vdash \psi \) has no derivation without RAA." Proof (main line, two sentences): "Suppose it had one. By @thm-kripke-soundness the stage would force \( \psi \), and it does not; so it has none." (A ¬I proof.)

   **Quick check (new):** "Which case of the proof fails for RAA, and which stage of \( M_1 \) shows that it must?" *Solution:* RAA's: its box assumes \( \neg\varphi \) and the rule writes \( \varphi \). \( w_0 \) forces \( \neg\neg p \) and not \( p \). If RAA were sound for stages, the derivation of \( \neg\neg p \vdash p \) (@prp-double-negation (b)) would make \( w_0 \) force \( p \).

6. **`## Two branches`**, with **`exm-three-stage-model`** `[A fork]` (~300 words with the figure). The model \( M_2 \):

   ```latex
   \begin{tikzpicture}[structure]
     \node[elt, label=below:$w_0$, label=right:$\varnothing$] (a) at (0,0) {};
     \node[elt, label=above:$w_1$, label=left:$\{p\}$] (b) at (-1.2,1.6) {};
     \node[elt, label=above:$w_2$, label=right:$\{q\}$] (c) at (1.2,1.6) {};
     \draw[rel] (a) -- (b);
     \draw[rel] (a) -- (c);
   \end{tikzpicture}
   ```

   Statement: "In \( M_2 \) the inquiry can go two ways: one learns \( p \), the other \( q \). Show that \( w_0 \) refutes \( \vdash (p \to q) \vee (q \to p) \) and \( \neg(p \wedge q) \vdash \neg p \vee \neg q \)."

   Solution:
   - \( w_1 \) is reachable from \( w_0 \), forces \( p \) and does not force \( q \), so \( w_0 \not\Vdash p \to q \) (K5). Likewise \( w_2 \) gives \( w_0 \not\Vdash q \to p \). By (K4), \( w_0 \) does not force the disjunction.
   - No stage forces both \( p \) and \( q \), so \( w_0 \Vdash \neg(p \wedge q) \) (K6).
   - \( w_1 \) forces \( p \), so \( w_0 \not\Vdash \neg p \); \( w_2 \) forces \( q \), so \( w_0 \not\Vdash \neg q \). Hence \( w_0 \not\Vdash \neg p \vee \neg q \).
   - By @cor-kripke-countermodel, neither \( \vdash (p \to q) \vee (q \to p) \) nor \( \neg(p \wedge q) \vdash \neg p \vee \neg q \) has a derivation without RAA.

   Then: "Classically each is derivable (Section 2.5, and @cor-derivable-iff-valid for the first, a tautology). The branch is what defeats them. At \( w_0 \) the inquiry knows that \( p \) and \( q \) will never both be known, but not which one will fail."

7. **`## What two or three stages settle`** (~300 words). The propositional right column of 8.7's table (`#laws-without-raa`), each with its countermodel (\( M_1 \), \( M_2 \), and two more, described in words). Table:

   | Sequent (letters \( p \), \( q \)) | A refuting stage |
   |---|---|
   | \( \vdash p \vee \neg p \); \( \neg\neg p \vdash p \) | \( w_0 \) of \( M_1 \) (the example) |
   | \( \vdash ((p \to q) \to p) \to p \) | \( w_0 \) of \( M_1 \): no stage forces \( p \to q \), so both stages force \( (p \to q) \to p \); \( w_0 \not\Vdash p \) |
   | \( \neg(p \to q) \vdash p \wedge \neg q \) | \( w_0 \) of \( M_1 \): no stage forces \( p \to q \), so \( w_0 \Vdash \neg(p \to q) \); \( w_0 \not\Vdash p \) |
   | \( (p \to q) \to q \vdash p \vee q \) (8.7, R3) | \( w_0 \) of \( M_1 \): as above, both stages force \( (p \to q) \to q \); \( w_0 \) forces neither \( p \) nor \( q \) |
   | \( p \to q \vdash \neg p \vee q \) | \( w_0 \) of \( M_3 \): \( w_0 \to w_1 \), nothing known at \( w_0 \), \( p \) and \( q \) known at \( w_1 \). \( w_0 \Vdash p \to q \); \( w_0 \not\Vdash \neg p \) since \( w_1 \Vdash p \), and \( w_0 \not\Vdash q \) |
   | \( \neg q \to \neg p \vdash p \to q \) | \( w_0 \) of \( M_4 \): \( w_0 \to w_1 \), \( p \) known at both, \( q \) known at \( w_1 \) only. No stage forces \( \neg q \), so \( w_0 \Vdash \neg q \to \neg p \); \( w_0 \) forces \( p \) and not \( q \) |
   | \( \vdash (p \to q) \vee (q \to p) \); \( \neg(p \wedge q) \vdash \neg p \vee \neg q \) | \( w_0 \) of \( M_2 \) (the example) |

   One sentence: "With @cor-kripke-countermodel, each row proves that the sequent has no derivation without RAA. This covers every propositional entry of Section 8.7's right column, and the claims stated without proof in its Exercises B1 and R3."

8. **`## Searching for a countermodel`** (~250 words) [technique: Si — a worked search; the template of 4.6's backwards-from-F search, at stages]. Worked on \( (p \to q) \to q \vdash p \vee q \):
   - "Start with a stage \( w_0 \) that must not force \( p \vee q \). So neither \( p \) nor \( q \) is known there.
   - It must force \( (p \to q) \to q \): every later stage that forces \( p \to q \) must force \( q \). The cheapest way is to make sure no stage forces \( p \to q \).
   - \( w_0 \) itself must then fail \( p \to q \), so some stage reachable from it forces \( p \) and not \( q \). Add \( w_1 \) after \( w_0 \), with \( p \) known.
   - Check every clause at both stages: this is \( M_1 \)."

   Then the general advice, three bullets: "to refute a disjunction at \( w \), refute both sides at \( w \) itself; to refute \( \varphi \to \psi \) or \( \neg\varphi \) at \( w \), add a later stage that forces \( \varphi \) (and, for \( \to \), not \( \psi \)); keep letters known once known." Last sentence: "The search is a guide, not a decision procedure as stated here."

9. **Remark** (~110 words, `::: {.remark}`): "Three facts, stated without proof.
   - The converse of @thm-kripke-soundness holds: a sequent forced at every stage of every Kripke model that forces its premises has a derivation without RAA. This is completeness for this semantics.
   - From it follows the **disjunction property**: if \( \vdash \varphi \vee \psi \) without RAA, then \( \vdash \varphi \) or \( \vdash \psi \) without RAA, the BHK clause for 'or' made a theorem about derivations.
   - Kripke models extend to the quantifiers, with a domain at each stage that may grow. In them \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \) and the two passage directions of Section 8.7's table can be refuted.

   Nothing in this book depends on these facts."

10. **Not allowed** (~110 words, the last block of the main line). `[Not allowed: misreadings of forcing]`:
    - "\( w \not\Vdash p \), so \( w \Vdash \neg p \)." (K6) looks at every stage reachable from \( w \): in \( M_1 \), \( w_0 \) forces neither.
    - "\( w \Vdash \varphi \to \psi \), because \( w \not\Vdash \varphi \)." (K5) looks at every later stage, not only at \( w \).
    - "\( w \Vdash \varphi \vee \psi \), because every later stage forces \( \varphi \) or \( \psi \)." (K4) is decided at \( w \) itself: in \( M_2 \), every stage reachable from \( w_0 \) other than \( w_0 \) forces \( p \) or \( q \), and \( w_0 \) forces neither.
    - "A picture with \( p \) known at \( w_0 \) and not at a later \( w_1 \)." It is not a Kripke model: a known letter stays known (@def-kripke-model).

**Quick checks:** one stage (item 2), heredity (item 4), RAA (item 5): three in ~3,450 words, about one per 1,150. The section is optional and dense with worked computations, and S4 accepts the density. If `check_structure.py` requires about one per 1,000, add after `exm-two-stage-model`: "Does \( w_1 \) of \( M_1 \) force \( p \vee \neg p \)? — Yes: \( w_1 \) forces \( p \). At a stage from which nothing new can be learned, every letter is settled." No drill or exercise part asks this.

**Folds:**
- F8.8-a (item 4): the proof of heredity.
- F8.8-b (item 5): the proof of soundness, case by case.

**Exercises.**
- **A1** (new, `exr-kripke-models-a1`).
  - (a) "In \( M_1 \), does \( w_1 \) force \( \neg\neg p \to p \)?" — Yes. The only stage reachable from \( w_1 \) is \( w_1 \), which forces \( p \), so it forces the implication by (K5).
  - (b) "Why is a one-stage Kripke model a row of a truth table?" — With one stage, (K5) and (K6) look only at that stage, so the clauses become those of @def-truth-value, with "forced" for "true".
  - (c) "True or false: if \( w \) does not force \( \varphi \), then \( w \) forces \( \neg\varphi \)." — False: \( w_0 \) of \( M_1 \), with \( \varphi = p \).
  - (d) "Which rule's case fails in the proof of @thm-kripke-soundness, and how does \( M_1 \) show that it must fail?" — RAA's. \( w_0 \) forces \( \neg\neg p \) and not \( p \), but \( \neg\neg p \vdash p \) is derived with RAA; if RAA's case held, \( w_0 \) would force \( p \).
- **A2: Drill** (new, `exr-kripke-models-a2`), 12 parts.
  - Models: \( M_1 \) and \( M_2 \) as in the text. \( M_5 \) is the chain \( w_0 \to w_1 \to w_2 \), with nothing known at \( w_0 \), \( p \) known at \( w_1 \), and \( p \), \( q \) known at \( w_2 \).
  - Stem: "Decide each in a line, with the clause you use."
  - Ramp: one clause → compound → is it a model? → misreadings → refutation.

  (a) "\( M_1 \): does \( w_1 \) force \( \neg p \)?" — No: \( w_1 \) is reachable from itself and forces \( p \) (K6).
  (b) "\( M_1 \), with \( q \) known nowhere: does \( w_0 \) force \( \neg q \)?" — Yes: no stage reachable from \( w_0 \) forces \( q \) (K6).
  (c) "\( M_2 \): does \( w_0 \) force \( p \vee q \)?" — No: neither letter is known at \( w_0 \) (K4).
  (d) "\( M_2 \): does \( w_1 \) force \( \neg q \)?" — Yes: the only stage reachable from \( w_1 \) is \( w_1 \), where \( q \) is not known.
  (e) "\( M_5 \): does \( w_0 \) force \( p \to q \)?" — No: \( w_1 \) is reachable, forces \( p \), and does not force \( q \) (K5).
  (f) "\( M_5 \): does \( w_1 \) force \( \neg\neg q \)?" — Yes. The stages reachable from \( w_1 \) are \( w_1 \) and \( w_2 \); neither forces \( \neg q \), since \( w_2 \) forces \( q \) and is reachable from both. And \( w_1 \not\Vdash q \).
  (g) "Is this a Kripke model: \( w_0 \to w_1 \), with \( p \) known at \( w_0 \) and not at \( w_1 \)?" — No: a letter known at \( w_0 \) must be known at every stage reachable from it.
  (h) "In \( M_1 \), a student says '\( w_0 \) forces \( \neg p \), because \( p \) is not known at \( w_0 \)'. What is wrong?" — (K6) needs \( p \) to fail at every reachable stage, and \( w_1 \) forces \( p \).
  (i) "\( M_2 \): does \( w_0 \) force \( \neg p \to q \)?" — Yes. Of the stages reachable from \( w_0 \), only \( w_2 \) forces \( \neg p \) (\( w_0 \) and \( w_1 \) reach \( w_1 \), which knows \( p \)), and \( w_2 \) forces \( q \).
  (j) "\( M_5 \): does \( w_0 \) force \( q \vee \neg q \)?" — No: \( q \) is not known at \( w_0 \), and \( w_2 \), reachable from \( w_0 \), forces \( q \), so \( w_0 \not\Vdash \neg q \).
  (k) "\( M_5 \): does \( w_0 \) force \( q \to p \)?" — Yes: the only stage that forces \( q \) is \( w_2 \), which forces \( p \).
  (l) "Can a one-stage model refute \( \neg\neg p \vdash p \)?" — No. At a single stage forcing is truth, and \( \neg\neg p \) is true exactly when \( p \) is. A refutation needs a later stage.
- **B1** (new, `exr-kripke-models-b1`) `[B1: A chain of three stages]`. Statement: "Let \( M_6 \) be the chain \( w_0 \to w_1 \to w_2 \), with nothing known at \( w_0 \), \( q \) known at \( w_1 \), and \( p \) and \( q \) known at \( w_2 \). (a) Decide whether \( w_0 \) forces \( \neg\neg p \), \( p \vee \neg p \), \( q \to p \), \( (q \to p) \vee (p \to q) \) and \( \neg p \to \neg q \). (b) Which sequents among \( \vdash p \vee \neg p \), \( \neg\neg p \vdash p \) and \( \vdash (p \to q) \vee (q \to p) \) does \( w_0 \) refute? (c) Show that no chain refutes \( \vdash (p \to q) \vee (q \to p) \)."

  *Solution.*
  - (a):
    - \( \neg\neg p \): yes. Every stage reachable from \( w_0 \) reaches \( w_2 \), which forces \( p \), so none forces \( \neg p \).
    - \( p \vee \neg p \): no. \( p \) is not known at \( w_0 \), and \( w_0 \not\Vdash \neg p \) because of \( w_2 \).
    - \( q \to p \): no. \( w_1 \) forces \( q \) and not \( p \).
    - \( (q \to p) \vee (p \to q) \): yes. The only stage forcing \( p \) is \( w_2 \), which forces \( q \), so \( w_0 \Vdash p \to q \).
    - \( \neg p \to \neg q \): yes. No stage reachable from \( w_0 \) forces \( \neg p \), so the implication holds with nothing to check.
  - (b) \( \vdash p \vee \neg p \) and \( \neg\neg p \vdash p \). Not \( \vdash (p \to q) \vee (q \to p) \), by (a).
  - (c) In a chain, of any two stages one is reachable from the other. Suppose \( w_0 \) refuted the disjunction. Then some \( u \) reachable from \( w_0 \) forces \( p \) and not \( q \), and some \( v \) forces \( q \) and not \( p \). If \( u \le v \), then \( v \) forces \( p \) (letters stay known), a contradiction. If \( v \le u \), then \( u \) forces \( q \), a contradiction. So no stage of a chain refutes it, and the branch of \( M_2 \) is needed.

  **Marking scheme.** (10 points)
  - 5: (a), one per formula, each with its clause.
  - 2: (b).
  - 3: (c), the two orders of \( u \), \( v \), each with persistence of letters.

  Fatal errors (0 for the step): deciding (K5) or (K6) at \( w_0 \) alone; in (c), checking one chain only.
- **B2** (new, `exr-kripke-models-b2`) `[B2: Derive without RAA, or break with a Kripke model]` (verdict withheld; D5) [technique: LPL, Si, En — derive-or-break with a growing means of breaking]. Statement: "For each claim, either derive it without RAA and without TAUT (and without results derived with RAA), or give a stage of a Kripke model that refutes it. (a) \( \neg\neg(p \wedge q) \vdash \neg\neg p \wedge \neg\neg q \). (b) \( \neg\neg p \wedge \neg\neg q \vdash \neg\neg(p \wedge q) \). (c) \( \neg\neg(p \vee q) \vdash \neg\neg p \vee \neg\neg q \). (d) \( (p \to q) \to p \vdash \neg\neg p \). (e) \( \neg p \to p \vdash p \). (f) \( (p \vee q) \wedge \neg p \vdash q \). (g) \( (p \to q) \wedge (\neg p \to q) \vdash q \)." (S2 round 1: the S1 (g), \( p \to (q \vee r) \vdash (p \to q) \vee (p \to r) \), was a published exercise word for word up to letters; it is replaced by a sequent of fd1's own.)

  *Solution* (verdict first):
  - (a) **Derive** (16 lines). 1 \( \neg\neg(p \wedge q) \). Box 2–7: 2 \( \neg p \); box 3–5: 3 \( p \wedge q \), 4 \( p \) ∧E 3, 5 \( \bot \) ¬E 4, 2; 6 \( \neg(p \wedge q) \) ¬I 3–5; 7 \( \bot \) ¬E 6, 1. Then 8 \( \neg\neg p \) ¬I 2–7. Lines 9–15 are the same for \( q \): 9 \( \neg q \); 10 \( p \wedge q \); 11 \( q \) ∧E 10; 12 \( \bot \) ¬E 11, 9; 13 \( \neg(p \wedge q) \) ¬I 10–12; 14 \( \bot \) ¬E 13, 1; 15 \( \neg\neg q \) ¬I 9–14. Finally 16 \( \neg\neg p \wedge \neg\neg q \) ∧I 8, 15.
  - (b) **Derive** (13 lines). 1 \( \neg\neg p \wedge \neg\neg q \); 2 \( \neg\neg p \) ∧E 1; 3 \( \neg\neg q \) ∧E 1. Box 4–12: 4 \( \neg(p \wedge q) \); box 5–10: 5 \( p \); box 6–8: 6 \( q \), 7 \( p \wedge q \) ∧I 5, 6, 8 \( \bot \) ¬E 7, 4; 9 \( \neg q \) ¬I 6–8; 10 \( \bot \) ¬E 9, 3; 11 \( \neg p \) ¬I 5–10; 12 \( \bot \) ¬E 11, 2. Then 13 \( \neg\neg(p \wedge q) \) ¬I 4–12.
  - (c) **Break**, at \( w_0 \) of \( M_2 \). Every stage reachable from \( w_0 \) is, or reaches, \( w_1 \) or \( w_2 \), each of which forces \( p \vee q \), so none forces \( \neg(p \vee q) \): \( w_0 \Vdash \neg\neg(p \vee q) \). But \( w_2 \Vdash \neg p \) (only \( w_2 \) is reachable from it, and \( p \) is not known there), so \( w_0 \not\Vdash \neg\neg p \). Likewise \( w_1 \Vdash \neg q \), so \( w_0 \not\Vdash \neg\neg q \).
  - (d) **Derive** (9 lines). 1 \( (p \to q) \to p \). Box 2–8: 2 \( \neg p \); box 3–5: 3 \( p \), 4 \( \bot \) ¬E 3, 2, 5 \( q \) ⊥E 4; 6 \( p \to q \) →I 3–5; 7 \( p \) →E 1, 6; 8 \( \bot \) ¬E 7, 2. Then 9 \( \neg\neg p \) ¬I 2–8.
  - (e) **Break**, at \( w_0 \) of \( M_1 \). No stage forces \( \neg p \), so \( w_0 \Vdash \neg p \to p \) with nothing to check, and \( w_0 \not\Vdash p \).
  - (f) **Derive** (9 lines). 1 \( (p \vee q) \wedge \neg p \); 2 \( p \vee q \) ∧E 1; 3 \( \neg p \) ∧E 1. Box 4–6: 4 \( p \), 5 \( \bot \) ¬E 4, 3, 6 \( q \) ⊥E 5. Box 7–8: 7 \( q \), 8 \( q \) R 7. Then 9 \( q \) ∨E 2, 4–6, 7–8.
  - (g) **Break**, at \( w_0 \) of \( M_3 \) (the settle table's model: \( w_0 \to w_1 \), nothing known at \( w_0 \), \( p \) and \( q \) known at \( w_1 \)). The only stage forcing \( p \) is \( w_1 \), which forces \( q \), so \( w_0 \Vdash p \to q \). No stage forces \( \neg p \), since both reach \( w_1 \), which forces \( p \); so \( w_0 \Vdash \neg p \to q \) with nothing to check. Hence \( w_0 \) forces the conjunction (K3), and \( w_0 \not\Vdash q \).

  The look-alikes: (a) and (b) are converses, and both derivable. (c) is (b)'s look-alike with ∨ for ∧, and it breaks. (e) is (d)'s look-alike and breaks: from \( \neg p \to p \) one derives only \( \neg\neg p \) (a box on \( \neg p \), then →E, ¬E and ¬I). (g) is (f)'s look-alike: a proof by cases on \( p \) and \( \neg p \) with no disjunction to split, which needs \( p \vee \neg p \). It is the pattern of @lem-atom-splitting (Section 4.8) with no further premises, which is why completeness, and with it TAUT, rests on LEM.

  **Marking scheme.** (10 points)
  - 6: the four derivations, 1.5 each.
  - 3: the three countermodels, 1 each, every clause checked.
  - 1: one correct remark on a look-alike pair.

  A wrong verdict scores 0 for that item. Fatal errors (0 for that item): a derivation that uses RAA, ¬¬E or LEM, or cites a result derived with one; a TAUT line (every claim is a tautology, so a TAUT line would "derive" each, the breakable (c), (e) and (g) included; TAUT is licensed by completeness, item 5); a "model" with a known letter lost at a later stage.

  S2a checks the look-alike note's derivation of \( \neg p \to p \vdash \neg\neg p \): a box on \( \neg p \); →E with the premise gives \( p \); ¬E gives \( \bot \); ¬I closes the box. It uses no RAA.
- **C1** (new, `exr-kripke-models-c1`) `[C1: Peirce's law and one instance of excluded middle]`. Statement: "(a) Derive \( ((p \to q) \to p) \to p \) from the premise \( p \vee \neg p \) without RAA or TAUT. (b) Derive without RAA or TAUT, or refute with a Kripke model: \( \vdash \bigl( ((p \to q) \to p) \to p \bigr) \to (p \vee \neg p) \). (c) Compare (a), (b) and Exercise 8.7 B5 (c) with @thm-classical-rules-interderivable, in one sentence."

  *Solution.*
  - (a) (12 lines.) 1 \( p \vee \neg p \). Box 2–11: 2 \( (p \to q) \to p \).
    - Box 3–4: 3 \( p \), 4 \( p \) R 3.
    - Box 5–10: 5 \( \neg p \); box 6–8: 6 \( p \), 7 \( \bot \) ¬E 6, 5, 8 \( q \) ⊥E 7; 9 \( p \to q \) →I 6–8; 10 \( p \) →E 2, 9.
    - 11 \( p \) ∨E 1, 3–4, 5–10.

    Then 12 \( ((p \to q) \to p) \to p \) →I 2–11.
  - (b) **Refute**, at \( w_0 \) of the fork \( M_7 \): \( w_0 \to w_1 \), \( w_0 \to w_2 \), with \( p \) known at \( w_1 \) only.
    - At \( w_2 \) no stage reachable forces \( p \), so \( w_2 \Vdash p \to q \), and \( w_2 \not\Vdash p \). So \( w_2 \not\Vdash (p \to q) \to p \), and neither does \( w_0 \), which reaches \( w_2 \). \( w_1 \) forces \( p \), hence \( (p \to q) \to p \). The only stage forcing \( (p \to q) \to p \) is \( w_1 \), and it forces \( p \): so \( w_0 \Vdash ((p \to q) \to p) \to p \) (K5).
    - \( w_0 \not\Vdash p \), and \( w_0 \not\Vdash \neg p \) because of \( w_1 \). So \( w_0 \not\Vdash p \vee \neg p \).
    - (In \( M_1 \) the formula is forced at \( w_0 \): there no stage forces \( p \to q \), so \( w_0 \) forces \( (p \to q) \to p \) and not \( p \), and so does not force Peirce's law; the only stage that does, \( w_1 \), forces \( p \vee \neg p \). So the second branch is needed.)
    - (S2 round 1: the S1 (b), \( (\neg\neg p \to p) \to (p \vee \neg p) \), was an item of a published exercise; it is replaced by this contrast of fd1's own.)
  - (c) @thm-classical-rules-interderivable compares rules, which act on every statement at once. Instance by instance the three differ: one instance of excluded middle gives Peirce's law (a) and double-negation elimination (8.7 B5 (c)) for that letter, while that instance of Peirce's law does not give the instance of excluded middle back (b).

  **Marking scheme.** (10 points)
  - 5: (a). The ∨E on the premise, with both cases inside the box of line 2 (2); the case \( \neg p \) building \( p \to q \) by ⊥E (2); the closing →I (1).
  - 4: (b). A model whose stage forces \( ((p \to q) \to p) \to p \) and not \( p \vee \neg p \), every clause checked.
  - 1: (c).

  Fatal errors (0 for the step): using \( M_1 \) in (b), where the formula is forced; using RAA or TAUT in (a).
- **C2** (new, `exr-kripke-models-c2`) `[C2: Challenge: three negations are one]` (a meta-proof; STYLE §12.8, not on any track's core). Statement: "Prove that in every Kripke model, every stage \( w \) and every formula \( \varphi \): \( w \Vdash \neg\neg\neg\varphi \) if and only if \( w \Vdash \neg\varphi \). Compare with @exm-triple-negation."

  *Solution.*
  - \( (\Leftarrow) \) Let \( w \Vdash \neg\varphi \), and let \( w' \ge w \). By @lem-heredity, \( w' \Vdash \neg\varphi \). Since \( w' \) is reachable from itself, \( w' \not\Vdash \neg\neg\varphi \) (K6). So no stage reachable from \( w \) forces \( \neg\neg\varphi \), and \( w \Vdash \neg\neg\neg\varphi \).
  - \( (\Rightarrow) \) Let \( w \Vdash \neg\neg\neg\varphi \), and suppose some \( w' \ge w \) forces \( \varphi \). Every \( w'' \ge w' \) forces \( \varphi \) by @lem-heredity, so no \( w'' \ge w' \) forces \( \neg\varphi \), and \( w' \Vdash \neg\neg\varphi \). But \( w' \) is reachable from \( w \), and \( w \Vdash \neg\neg\neg\varphi \) says no such stage forces \( \neg\neg\varphi \): a contradiction. So no stage reachable from \( w \) forces \( \varphi \), and \( w \Vdash \neg\varphi \).
  - The comparison: @exm-triple-negation derives \( \neg\neg\neg P \vdash \neg P \) without RAA, and \( \neg P \vdash \neg\neg\neg P \) is @prp-double-negation (a) for \( \neg P \). By @thm-kripke-soundness both directions hold at every stage. The exercise proves the same fact directly, from the clauses.

  **Marking scheme.** (10 points)
  - 4: \( (\Leftarrow) \), with heredity and reflexivity named.
  - 5: \( (\Rightarrow) \), with heredity of \( \varphi \) used to get \( w' \Vdash \neg\neg\varphi \).
  - 1: the comparison.

  Fatal errors (0 for the step): "not forced, so the negation is forced"; heredity used without being cited.

**Sidecars:**
- `kripke.py`: every forced/not-forced claim of items 2–10, A1, A2, B1, B2, C1 and C2's instances. The models are \( M_1 \)–\( M_7 \). Heredity is checked on all formulas over \( p, q, r \) up to depth 4 in each model. One-stage models are checked to agree with truth tables.
- `exr-kripke-models-b2.py`: truth-table validity of every claim of B2, all classically valid. The derivations of (a), (b), (d), (f) and C1 (a) are checked by `check_fitch.py`.

**Ledger lines:**
- `def-forcing` (`thm-structural-recursion`, F1.3 §03, cited);
- the one-stage remark (`def-truth-value`, cited);
- `lem-heredity` (`thm-structural-induction`, cited; fold);
- `thm-kripke-soundness` (`thm-soundness`'s Steps 1–4, `lem-context-inclusion`, `def-derivation` and `def-derivable`, cited; the TAUT sentence, `def-rule-taut`, F1.3 §08, and 8.7's item 5 sentence, within the chapter; `thm-strong-induction`, cited; `prp-double-negation` (b) in the Quick check, cited);
- `cor-kripke-countermodel` (inline ¬I);
- `exm-three-stage-model` (`cor-derivable-iff-valid`, cited);
- the table (`kripke.py`);
- the remark (stated without proof and marked so; nothing depends on it);
- B2's (g) (`lem-atom-splitting`, F1.3 §08, cited in the look-alike note only);
- C1 (`thm-classical-rules-interderivable`, cited);
- C2 (`exm-triple-negation`, `prp-double-negation`, cited).

---

## 5. Budgets and the Time line

| § | Main line now | R5 budget | Final budget | Expected | Folds (budget) |
|---|---|---|---|---|---|
| index | 1,001 | ≤ 1,100 | ≤ 1,300 | ~1,290 | ≤ 300 |
| 8.1 | 4,401 | ≤ 4,750 | ≤ 5,000 | ~4,970 | ≤ 850 |
| 8.2 | 3,129 | ≤ 3,700 | ≤ 4,200 | ~4,200 | ≤ 260 |
| 8.3 | 4,064 | ≤ 4,000 | ≤ 4,200 | ~4,180 | ≤ 1,600 |
| 8.4 | 1,895 | ≤ 2,000 | ≤ 2,200 | ~2,190 | ≤ 550 |
| 8.5 | 2,413 | ≤ 2,600 | ≤ 2,800 | ~2,790 | ≤ 700 |
| 8.6 | 2,240 | ≤ 2,600 | ≤ 3,000 | ~2,990 | ≤ 360 |
| 8.7 | 3,781 | ≤ 3,800 | ≤ 3,950 | ~3,915 | ≤ 340 |
| core sections | 21,923 | ≤ 23,450 | ≤ 25,350 | ~25,235 | ≤ 4,660 |
| 8.8 (optional) | — | — | ≤ 3,600 | ~3,450 | ≤ 750 |

- **Caps.** The core budgets are layout §1.3's (sum 25,200), except 8.1 (≤ 5,000 against the layout's 4,900) and 8.7 (≤ 3,950 against 3,900), raised at S2 round 1 when the S1 estimates were rebuilt from the quoted text (§4.1, §4.6, §4.7); sum 25,350. Every section stays at or under 5,000 main-line words. The whole-file advisory count of `check_structure.py` (exercises included) will exceed 5,000 in 8.1, 8.2, 8.3, 8.6 and 8.7; it is advisory.
- **Where a section runs close**, §4 names the passage that moves to a fold, or is cut, if S3 measures over (S2 round 1: S1 named one for 8.2 only):
  - 8.1: the Not-allowed (N7) line and the purpose paragraph's last sentence (§4.1);
  - 8.2: the definitional-extension sentences into F8.2-c (§4.2);
  - 8.3: the read-back sentence for column (a) in `exm-suffices-column`'s closing paragraph ("Read from the bottom, (a) is the proof …", ~25 words), cut, since (b)'s read-back makes the point (§4.3);
  - 8.4: the second sentence of the unstated-fact subsection ("A proof is read the same way, one line at a time.", ~10 words), cut (§4.4);
  - 8.5: the last sentence of the generalising lead ("A line that uses a property … or the generalisation fails.", ~20 words), cut, since the example's *test* says it (§4.5);
  - 8.6: the valid-but-improper paragraph into F8.6-b (§4.6);
  - 8.7: the paragraph 07:11 into F8.7-d (§4.7).
- The new folds are F8.1-d, F8.1-e, F8.1-f, F8.2-a, F8.2-b, F8.3-d, F8.5-c, F8.6-b, F8.6-c and F8.7-c, plus 8.8's two.

**Exercises after R5 and this file.**
- **A1:** 8 (one new, in 8.8).
- **A2:** 8 drill banks of 12 parts, **96 parts** (84 in the core sections). They count as 21 core exercises, and 24 in all, at one exercise per four parts (STYLE §12.8).
- **B:** 27. R5's 18, plus 8.1 B4, 8.2 B3, 8.3 B3, 8.4 B3, 8.5 B4, 8.6 B3, 8.7 B5, 8.8 B1 and 8.8 B2.
- **C:** 19. R5's 16, plus 8.5 C3, 8.8 C1 and 8.8 C2 (a Challenge).
- **R:** 5. 8.6 R1 and 8.7 R1–R4.
- **Exit checks:** 8.3 C2 and 8.6 C3, as R5.
- **Faded triple:** unchanged (R5).
- **Derive-or-break, verdict withheld:** 8.6 B3, 8.8 B2.
- **Used later:** 8.2 B3.

**Time.** This uses the B1 formula: 15 min per 400 main-line words; A1 25 min; a drill bank one exercise per four parts, at 30 min; one B (30 min) and one non-Challenge C (40 min) per core section; exit checks are a section's C. Index pages are not counted (layout §3). Optional 8.8 is off the core track.
- **Core track:**
  - reading ~25,235 words ≈ 15.8 h;
  - A1, 7 × 25 min ≈ 2.9 h;
  - A2, 21 × 30 min = 10.5 h;
  - one B per section, 7 × 30 min = 3.5 h;
  - one C per section, 7 × 40 min ≈ 4.7 h.
  - Total **≈ 37.4 h**. Rounded to the nearest 5 hours (STYLE §2): **"About 35 hours on the core track."**
  - **Risk (S2 round 1).** 37.4 h is about 0.1 h below the rounding boundary of 37.5 h. About 230 more main-line words, or one more core A1, would make the line "about 40 hours". The drafter of `index.md` rounds the delivered figure honestly, and the S9 packet names the risk (§10).
  - Layout target: about 33 h. The difference is the banks of 12 against the layout's 8, which is this file's choice, not a STYLE floor (D6: +28 parts = 7 exercises ≈ 3.5 h). With banks of 8 the core track would come to about 33.9 h, the layout's figure.
- **Full track:**
  - reading ~25,235 main + ~3,450 (8.8) + ~4,900 folded ≈ 33,585 words ≈ 21.0 h;
  - A1, 8 × 25 min ≈ 3.3 h;
  - A2, 24 × 30 min = 12 h;
  - B, 27 × 30 min = 13.5 h;
  - C, 19 × 40 min ≈ 12.7 h;
  - R, 5 × 40 min ≈ 3.3 h.
  - Total **≈ 65.8 h**: **"about 65 hours for everything"** (layout: about 55 h).
- The drafter of `index.md` recomputes both numbers from the delivered text (`check_structure.py --words`) and the delivered counts, by the same rule, and does not shade them down (STYLE §11.9). The plan's lever (banks capped lower, the surplus in optional batteries) is available: STYLE §12.8's sizes bind rule sections, and Chapter 8 has none. This file does not use it, and keeps banks of 12 to match the author's choice of the heavier workload (2026-10-12); S9 decides (D6).

---

## 6. Pointers and promises

### 6.1 Pointers from Chapter 8 to other chapters (final numbering)

R5's pointers are already in the final numbering (D2's sweep reached the frozen blueprints; spot-checked: "Section 6.1 derived …", "Sections 5.6 and 6.4", "Section 2.5", "Section 7.2"). The pointers this file adds are listed here. All are backward pointers or pointers within the chapter. None is a forward `@ref`.

| Where | Text | Target (atlas) | Status of target |
|---|---|---|---|
| index What you need | "From Chapter 7, only the statement in Section 7.2 under 'From counter-models to non-derivability'" | F1.6 §02, heading `#from-counter-models-to-non-derivability` | in place (D2) |
| index fold F5.0-a | "@thm-structural-induction and the proof of @thm-soundness" (for 8.8) | F1.3 §03, §07 | in place |
| 8.1 purpose paragraph | "Since Section 1.4 every derivation …" | F1.1 §05 | delivered (pilot D) |
| 8.1 disjunction row | @exm-constructive-dilemma; "the derived rule CD of Section 2.3", @exr-derived-rules-b4 | F1.1 §07; F1.2 §03 | delivered (CD is a derived rule in 2.3's B4 (a); S2 round 2) |
| 8.1 cycle | @prp-equivalence-cycle, @thm-odd-iff-square-odd | F1.2 §04 | in place |
| 8.2 rows | @prp-implication-transitive; @prp-definitional-extension, @def-definite-description ("Section 5.8") | F1.1 §05; F1.4 §08 | delivered (5.8) |
| 8.2 double inclusion | @exm-extensionality-logical-half; "an axiom about sets (Section 5.7)" | F1.4 §07 | delivered (5.7: the example, and its paragraph "For sets, the converse is taken as an axiom") |
| 8.2 fold F8.2-a | "the second-pass Section 4.9 … @thm-monotonicity" | F1.3 §09 | delivered (4.9; semantic, positive and negative places, as the fold says) |
| 8.3 TAUT paragraph | @def-rule-taut ("Section 4.8"); @def-propositional-skeleton, @prp-taut-skeleton ("Section 6.3") | F1.3 §08; F1.8 §03 | delivered (4.8; 6.3) |
| 8.4 unstated fact | "Section 3.3 turned a paragraph of argument into a sequent"; @exr-using-an-implication-b5 | F1.7 §03; F1.1 §04 | delivered (3.3's "Extracting an argument", step 3 "Name the unstated facts"); B5 delivered |
| 8.5 generalising | "the move of ∀I (Section 5.4)" | F1.4 §04 | in place |
| 8.6 (N12)–(N14) | @def-rule-universal-elimination; @ax-induction, @thm-strong-induction; @def-rules-existential; "Section 5.8"; @thm-barber ("Section 5.6") | F1.4 §03; F1.3 §02; F1.4 §06, §08; F1.4 §06 | delivered (`thm-barber` in 5.6) |
| 8.6 traditional names | "a common error of Section 1.6" | F1.1 §07 | delivered (affirming a disjunct) |
| 8.7 R1 | @prp-replacement ("Section 6.2") | F1.8 §02 | delivered (6.2; its statement covers a part under a quantifier) |
| 8.7 → 8.8 | "the optional Section 8.8" (six prose pointers, §4.7 item 2: the table cell 07:15, the Quick check of "Excluded middle cannot be refuted", B1's solution, R3's solution, the new table's lead, B5 (d)'s parenthesis) | F1.5 §08 | this file; written in the same pass |
| 8.7 TAUT sentence | @lem-atom-splitting, "TAUT (Section 4.8)", "Section 6.3" | F1.3 §08; F1.8 §03 | delivered |
| 8.8 | @thm-raa-independent, @thm-soundness, @lem-context-inclusion, @thm-strong-induction, @thm-structural-induction, @thm-structural-recursion, @def-truth-value, @def-formula, @def-derivation, @def-derivable, @cor-derivable-iff-valid, @lem-atom-splitting, @def-rule-taut, @thm-classical-rules-interderivable, @exm-triple-negation, @prp-double-negation | F1.3, F1.2, F1.1 | in place |

**Forward pointers to later volumes:** exactly R5's three Looking-ahead boxes (8.3, 8.6, 8.7). After drafting, S4 greps each section's main line and folds for `Analysis on the Real Line`, `Sets, Relations`, `Number Systems`, `later volume` and `this series` (R5 binding rule 3); the only hits allowed are the three boxes, the index's Minimum line (layout G14) and the frozen C1 stem (R5).

### 6.2 STATUS promise rows (by atlas id)

**Paid by F1.5, kept paid** (the paying blocks keep their labels):
- the dictionary and the "silent" column (F1.1 rows "checking a proof line by line" and "the full rule, phrase and Lean dictionary"). R5 adds the rule card, and this file adds the purpose paragraph.
- F1.4 §01, §04, §07 (phrase dictionary; hidden "for every"; (N1)).
- F1.8 §02, §04 ((N11); RAA in `prp-quantifier-negation` (a); levels of proof).
- F1.2 §02, §05 (¬P as P → ⊥; intuitionistic logic; the history).
- F1.2 §05 (costumes).
- F1.3 §07 (who objected to RAA).
- F2.1 (levels; silent steps; entries (N1), (N4), (N5), (N7), with numbers unchanged).
- F1.1 index (Minimum for fd2: "F1.5 core"), and the same Minimum line in the indexes of F1.2, F1.7, F1.3, F1.4 and F1.8, and F1.6's index row ("F1.5 (Chapter 8, core)"; ch07 index:56 "Chapter 8 turns derivations into the prose of mathematics"). Paid by the chapter as a whole; 8.8 is optional, which the Minimum's "core" allows.
- F1.3 §08 (the box at 08-completeness.md:700, "Chapter 8 names the steps a written proof passes over without comment"; STATUS row "F1.3 §08 … F1.5 (paid: 8.3 `def-silent-steps`)"): paid by `def-silent-steps`, verbatim, and by 8.3's TAUT paragraph (§4.3 item 2), which matches the convention of `def-rule-taut` (TAUT only for a step a written proof passes over). S2 round 2: S1 omitted this row.
- F1.4 §08 (the Looking-ahead box at 08-counting-and-descriptions.md:308, "Chapter 8 collects 'we define …' and 'the …' with the other phrases"; STATUS row "F1.4 §08 → F1.5 §02"): paid by 8.2's rows "a definition" and "the" (§4.2 item 2). S2 round 2: S1 recorded it only as a layout seam.
- F1.3 §09 (STATUS: "nothing to pay"): 4.9's note says that nothing in Chapters 5–8 uses the section. F8.2-a's prose pointer to @thm-monotonicity sits in a fold and nothing rests on it, so the note stays true.
- F1.8 §02 (STATUS row 75, "what is at stake when `prp-quantifier-negation` (a) needs RAA"): still paid by 07:109's paragraph "Not every, and some not" and `exr-excluded-middle-b3` (both kept by R5); 8.7's table row and A2 (k) now pay it too. The ch06 02:880 pointer ("Chapter 8 … catalogues the wrong negations of this section") is (N11), unchanged.

**Every prose pointer of Chapters 1–7 into Chapter 8** (S2 round 2; grep of "Chapter 8", "Section 8." and "F1.5" in `fd1/src/ch0[1-7]-*/`; eleven hits, no "Section 8.k" pointer and no citation of an entry (Nk) by number):
| Pointer | Paid by |
|---|---|
| ch02 05:1120 (history of those who declined RAA; a proof by contradiction in costume) | 8.7 "A short history"; the costumes of 8.1 (kept) |
| ch04 index:51 and 07:456 (what reductio asserts, who objected) | 8.7 `#one-extra-rule`, `#what-a-proof-provides`, "A short history" |
| ch04 08:700 (steps passed over without comment) | 8.3 `def-silent-steps`, TAUT paragraph |
| ch05 04:787 (the errors of 5.4 in a catalogue) | `exm-not-allowed-catalogue` (N1), (N3) (kept) |
| ch05 07:417 ("You write" column into a full dictionary) | 8.1–8.2 dictionary tables and the rule card (R5) |
| ch05 08:308 ("we define", "the") | 8.2's two new rows |
| ch06 02:880 (not every/some not; wrong negations) | 8.7 07:109, B3, the table, A2 (k); (N11) |
| ch06 02:1407 (ledger: F1.5 in the Looking-ahead box) | 8.7 table, quantifier row "stated without proof" |
| ch06 04:347 (eleven lines become three sentences, at several levels) | 8.3 `exm-uniform-four-levels` (levels 1 and 3, F5.3-c levels 0 and 2; R5) |
| ch07 index:56 (derivations into prose) | the chapter |

Nothing is missing, so no budget is added.

**Rows changed as R5 §6 lists them.** R5 names them by its row numbers of 2026-10-12; the coordinator matches them by content:
- the AN1.1 facts row (§01 sample sentences; the clause (S2) leaves);
- the AN1.2 Bolzano–Weierstrass row (no volume named);
- the AN1.5 sequential-criterion row (**retired**: the sample sentence is replaced);
- the AN1.6 and AN1.10 rows (reworded pointers);
- the F2.1 row "sets developed properly" (retired), with "cites the entry by number" now §06's Looking-ahead box;
- the AN1.1 and F2.1–F2.3 level rows (source "§03 Looking ahead");
- a new row for §07's Looking-ahead box (AN1 takes trichotomy as an axiom and flags each non-constructive step).

**Rows this file extends or opens:**
- **F1.5 → F2.2** (the arithmetic row) gains:
  - "every integer is 3k, 3k + 1 or 3k + 2" now also in §05 `exm-generalise-proof`, B4 and C3 (`thm-division-algorithm`);
  - "nothing between 0 and 1" now also in §05 C3 (`lem-naturals-arithmetic` (e));
  - (L₃) and (L₄), "every rational number is \( p/q \) with \( q \ne 0 \) and \( p \), \( q \) not both multiples of 3 (resp. 4)", stated as school facts in §05 C3, as (L) is in F1.2 §02 with its proof promised to F2.2 (S2 round 1: S1 left them out of this row);
  - "every non-empty set of natural numbers has a least element", named in the true instances of (N13) and (N14) in §06 (F2.2's well-ordering, by whatever label F2.2 gives it; not used as a reason).
- **F1.5 §07 → F1.5 §08** (new row, paid in the same pass): the claims of §07 that the optional §08 proves. They are the propositional right column of the table `#laws-without-raa` (the claim of its lead); B1's \( \nvdash \neg\neg P \to P \) without RAA; R3's sequent; the second proof of \( \nvdash P \vee \neg P \) (the table cell 07:15 and the Quick check); and B5 (d)'s claim that one instance of Peirce's law does not give back the instance of excluded middle that gives it (8.8 C1 (b)). Six prose pointers carry them (§6.1).
- **Seams this chapter pays** (not STATUS rows; recorded for S8):
  - ch01-deepen §6: "8.1 may cite `exm-constructive-dilemma` as a dictionary row" (paid, §4.1 item 2); "8.1's spoken assumption purposes row reads 1.4's annotation" (paid, §4.1 item 1).
  - layout §8, Wave 3: "5.8 → 8.2" (paid, §4.2 item 2); "4.8/6.3 → 8.3" (paid, §4.3 item 2).
  - Critic, smaller correction 3: "8.7 points to 8.8" (paid, §4.7 item 2).
  - Critic, smaller correction 6: the "we define" row (paid).
- **Backward citations of planned labels**, **confirmed at S2 round 2** against the delivered chapters (S8 re-greps only): `def-rule-taut`, `thm-monotonicity`, `thm-barber`, `exm-extensionality-logical-half`, `def-definite-description`, `prp-definitional-extension`, `prp-replacement`, `def-propositional-skeleton`, `prp-taut-skeleton`; and 3.3's argument extraction (prose). If one of these chapters lands after Chapter 8 is drafted (it should not: Wave 3 follows G3), S3 writes the sentence without the `@ref` and S8 restores it.

---

## 7. What other chapters hold, so that Chapter 8 does not re-teach them

| Chapter | Holds | So Chapter 8 does not |
|---|---|---|
| 1 | purpose annotations introduced (1.4); the constructive dilemma worked (1.6); affirming a disjunct (1.6) | re-introduce the annotation (8.1 reads it); re-derive the dilemma (8.1 gives it a row) |
| 2 | ¬I against RAA (2.5, its single home, ch02-revision); derived rules, with CD and MPT used as derived rules in Exercise B4 of 2.3; TFAE by a cycle (`prp-equivalence-cycle`, 2.4) | teach the ¬I/RAA distinction again (8.1's faces and BHK preview only, R5); re-derive the cycle lemma (8.1 cites it) |
| 3 | the search (3.1); argument extraction and suppressed premises (3.3) | teach extraction (8.4 recalls it in one sentence) |
| 4 | soundness and completeness (4.7, 4.8); TAUT (4.8); monotonicity (4.9, second pass); structural induction and recursion (4.3) | prove soundness again (8.8's fold reuses 4.7's Steps 1–4 and redoes only the box cases); define TAUT (8.3 cites it) |
| 5 | ∃! and "the", definitional extension (5.8); Russell (5.6); the logical half of extensionality, and the converse as an axiom about sets (5.7) | prove that a definition adds nothing (8.2 cites it); prove that no barber exists (8.6 cites it); treat set equality as logic (8.2 cites extensionality as an axiom) |
| 6 | translation (6.1); quantifier laws and `prp-replacement` (6.2); the skeleton and `prp-taut-skeleton` (6.3); uniform continuity rule by rule (6.4) | negate quantifiers anew (8.1, 8.2 point back); prove replacement (8.7 R1 cites it) |
| 7 | counter-models and the statement under `#from-counter-models-to-non-derivability` (7.2); first-order soundness (7.3, optional) | cite 7.3 (binding rule 4); build first-order counter-models (8.8 is propositional) |

---

## 8. What stays exactly as it is

Everything R5 §7 lists, and every passage of the current text that neither R5 §4 nor this file's §4 names. In particular:
- the slogan "the words are the boxes, spoken";
- the six named moves (two are added);
- the costumes;
- 8.1 C1 (frozen);
- every dictionary table, with rows only added (8.1: two; 8.2: five);
- `def-levels-of-proof` and `def-silent-steps`, verbatim;
- the warnings of 8.3 and 8.5;
- the training passage and the five strategies of 8.4;
- the two-column check, Proofs A–D, and (N1)–(N11) as R5 leaves them;
- 8.7's results (all `.optional`), the BHK clauses, the history, "What analysis would lose", the warning in "Proofs as programs", and the R group (R1 gains one clause);
- every exercise not named in §4.

---

## 9. S2a: every new claim, derivation and intended answer to verify

R5 §8's items 1–25 stand, and S2a re-runs only those this file touches (items 1, 13, 15, 18, 19, 25). The new items follow.

**Changed wording of existing blocks:**
1. `exm-not-allowed-catalogue`:
   - (N12)–(N14) appended. Each is an instance of its entry and of no earlier one, its true/false verdict is right, and its rule tag is right.
   - (N12): \( a = b = 2 \) are roots of \( x^2 - 5x + 6 \) and the factorization step fails there.
   - (N13): \( \{1/n\} \) has no least element.
   - (N14): "\( N + 1 \le N \)" from "\( N \) largest". The line between (N9) and (N14) (asserted warrant against presupposed premise), and every (N9)/(N14) tag of the chapter against it (§4.6, item 2).
   - F8.6-b: in \( \nN \) a strictly decreasing list from \( a_1 \) has at most \( a_1 + 1 \) terms; \( m = 8 \) is least with \( m^2 > 50 \); the citation of `thm-barber` (5.6) says what 5.6 delivers.
   - 06:31's head sentence still describes every entry. (N1)–(N11) are unchanged.
   - All 110 outside citations name (N1)–(N11) by number, and their meaning is unchanged.
2. The families table: the (N12) placement, the new family and its slogan; the roadmap's "seven families".
3. 8.7: the six pointers to 8.8 (§4.7, item 2) each name a claim that 8.8's table, examples or exercises prove (B5 (d)'s: 8.8 C1 (b)). Item 5's TAUT sentence: TAUT is licensed through @thm-completeness, whose proof uses LEM in @lem-atom-splitting (as 07:28 says). Item 6: B4's census recomputed against the delivered Chapters 3–7, with at least TAUT and `prp-taut-skeleton` added. R1's clause: `prp-replacement` (6.2) licenses the step "part (a) under the ∀" as R1 uses it, with a bounded quantifier.
4. The moved passages (01:241, 02:124, 03:80, 03:82, 05:165, 07:212 with the Lean block): each moves verbatim. No main-line sentence, A item or B item needs the moved text. In particular 8.3 A2(e) is answerable from `def-silent-steps` with F8.3-d closed.
5. 8.3 B2's scaffold without `\purpose` (D1), the one exception to STYLE §12.13.1 in the chapter.

**New main-line claims and examples:**
6. Index:
   - the motivating question;
   - the What-you-need sentence (layout §1.3; binding rule 4);
   - the Summary, where every claim is a labelled result or a section's content, and "without RAA, excluded middle has no derivation" cites the optional `thm-raa-independent`;
   - every Terms line, against its target.
7. 8.1:
   - The purpose paragraph. Each phrase pairs with the annotation the engine prints (`latex/fitch-book.sty`'s "asm, for …"), including ↔I and the bounded ∀I.
   - The constructive-dilemma row, against `exm-constructive-dilemma` and 2.3's `exr-derived-rules-b4` (a), where CD is used as a derived rule (checked at S2 round 2).
   - The cycle row. `exm-rhetoric-cycle` (in fold F8.1-e): the three arrows; \( n^2 = 2a + 1 \Rightarrow n^2 + 2n = 2(a + n) + 1 \); \( (2k)^2 + 2(2k) = 2(2k^2 + 2k) \); (iii) ⇒ (i) without RAA; "three implications for six". The subsection teaches the move with the fold closed (lead, row, Quick check).
   - The four-condition Quick check.
   - The Not-allowed lines and tags:
     - \( x = \tfrac12 \) refutes \( x^3 \ge x \);
     - the negation of \( \abs{x} < 1 \) is \( \abs{x} \ge 1 \);
     - the unannounced contrapositive breaks the never-silent item "the announcement of a contrapositive", and is not (N5);
     - the single case is (N7).
8. 8.2:
   - The two stronger rows and their sentence: \( x^2 < x < 1 \) for \( 0 < x < 1 \); the chain by `prp-implication-transitive`.
   - F8.2-a's statement of monotonicity, against `thm-monotonicity` as ch04-deepen delivers it.
   - The three new rows. "A definition proves nothing new" against `prp-definitional-extension`; "the" needs ∃! against `def-definite-description`.
   - Two inclusions give \( \forall x\, (x \in A \leftrightarrow x \in B) \) by ↔I inside ∀I, consistent with 5.1's and 8.5's reading of \( \subseteq \); the step to \( A = B \) is extensionality, cited and never silent, consistent with `exm-extensionality-logical-half` (5.7), 5.8 B4 and 7.2's "Extensionality: an axiom, not a law of logic" as delivered.
   - `exm-rhetoric-double-inclusion`: \( x^2 \le 2x \iff 0 \le x \le 2 \), both inclusions, the tags (the last one [∀E, →E with the axiom]), the ¬I steps followed by trichotomy.
   - The Not-allowed lines and tags, the fifth tagged by the never-silent item "the witness of ∃I, with what it depends on".
9. 8.3:
   - The TAUT paragraph. Each named item of the first list of `def-silent-steps` is valid on the propositional skeleton (∧I, ∧E, R, ∨I, ⊥E, DS, the exchange, ↔E with a definition, →E on a line of the proof). ∀E, =I and =E are not TAUT steps. The two \( \forall\forall \) formulas are two letters on the skeleton (NOTATION, TAUT).
   - The level-1 TAUT option, against `check_fitch.py`'s TAUT check (D0 g) and the frozen wording of `def-levels-of-proof`, which it extends and does not change.
   - `exm-suffices-column`. (a) \( x^2 - 6x + 10 = (x - 3)^2 + 1 \). (b) \( a_n - 2 = -1/(n + 1) \), and \( N > 1/\varepsilon \), \( n \ge N \) give \( \abs{a_n - 2} < \varepsilon \). Every reason points up. The two level-3 texts read off the columns.
   - The column Quick check.
10. 8.4:
    - The purpose sentence.
    - The 3.3 recall, worded against 3.3 as delivered.
    - The two lines: "if \( 3 \mid n^2 \) then \( 3 \mid n \)" is true; "if \( 4 \mid n^2 \) then \( 4 \mid n \)" is false at \( n = 2 \); `exr-using-an-implication-b5` (d)(iv) is that fact.
    - The Quick check.
11. 8.5:
    - The generalising lead (∀I, Section 5.4).
    - `exm-generalise-proof`: the three cases; (P2) is the case \( n = 3k + 2 \) with \( k = 5 \).
    - The \( 7^2 - 1 \) check, against 8.3 B2's claim.
12. 8.6:
    - The flowchart's node texts and edges: the first column marks where to look, the second decides; a line written by a chain of rules and silent steps is "found", and only a line no chain writes fails. The flowchart, item 4 and A2 (l) agree.
    - The valid-but-improper paragraph: \( \forall a\, \forall b\, \varphi \) to \( \forall b\, \forall a\, \varphi \) is ∀E twice and ∀I twice at level 0, and no TAUT step (two letters on the skeleton, as 8.3 says).
    - F8.6-c, the traditional-names table, each name matched to its entry.
13. 8.7:
    - The table `#laws-without-raa`. Every middle-column entry is a derivation without RAA in the cited result. Every right-column propositional entry is refuted in 8.8. Every right-column quantifier entry is marked "stated without proof".
    - "Modus tollens, DS, constructive dilemma: all": `prp-modus-tollens` and `prp-disjunctive-syllogism` use no RAA, and `exm-constructive-dilemma` uses Chapter 1's rules.
    - The Glivenko sentence, limited to the propositional rows. Its extension to finite lists of premises: from Glivenko for \( \vdash \gamma \to \varphi \) (\( \gamma \) the premises' conjunction), \( \neg\neg(\gamma \to \varphi) \) without RAA; then \( \neg\neg(\gamma \to \varphi), \gamma \vdash \neg\neg\varphi \) without RAA (a box on \( \neg\varphi \), inside it a box on \( \gamma \to \varphi \) giving \( \varphi \) by →E and \( \bot \) by ¬E, closed by ¬I, then ¬E with the premise and ¬I). "B5 (a) and (b) derive two cases": (c) is not a Glivenko case.
    - The contraposition Quick check and its appeal to R5's fold F5.1-c.
14. 8.8:
    - `def-kripke-model` (reflexive, transitive reachability; persistence of letters) and `def-forcing` (K1)–(K7), by a structural recursion that defines for each formula the set of stages forcing it (as `thm-structural-recursion` as delivered allows a set-valued recursion). The clause names (K1)–(K7) clash with no clause names cited in 8.8.
    - The one-stage remark: forcing = truth.
    - The counterexample-set sentence (D4).
    - `exm-two-stage-model`: \( w_0 \not\Vdash p \), \( \neg p \), \( p \vee \neg p \); \( w_0 \Vdash \neg\neg p \); \( w_0 \not\Vdash \neg\neg p \to p \).
    - `lem-heredity` and its fold proof. For → and ¬ no induction hypothesis is needed.
    - `thm-kripke-soundness`: the statement (TAUT excluded, with its sentence), the rule table row by row (in particular ↔E, ∨E, ⊥E, and RAA's failure), and F8.8-b's Steps 1–4 against 4.7's Steps 1–4 (reduction, induction, cases, last line) and `lem-context-inclusion` as delivered.
    - `cor-kripke-countermodel` and its ¬I proof.
    - `exm-three-stage-model`: both refutations.
    - The settle table, every row. Each model is a Kripke model (letters persist): \( M_3 \) (\( p, q \) at \( w_1 \)); \( M_4 \) (\( p \) at both, \( q \) at \( w_1 \)). The row \( \neg(p \to q) \vdash p \wedge \neg q \) at \( w_0 \) of \( M_1 \). The claim that the table covers the propositional right column of 8.7 and the claims of 8.7 B1 and R3.
    - The worked search.
    - The remark: Kripke completeness, the disjunction property and quantifier models are each stated without proof.
    - The Not-allowed lines.
    - The opening's and the Purpose line's claims: 8.7 names the laws; `thm-raa-independent` (optional, 4.7) proves the non-derivability of LEM and ¬¬E by a three-valued reading; 8.7 states the rest without proof.

**New and changed exercise answers:**
15. 8.1 A2 (h) (the √5 opening: the box is ¬I despite "for a contradiction"), (l); B4 (new at S2 round 1): the five identities, the split on \( b \) by (E1), the two names in each case of (iii) ⇒ (i), the marking scheme, and the fatal-error tags (N4) and (N9) against §4.6 item 2's line.
16. 8.2 A2 (k), (l); B3: \( 2a = 3b \Rightarrow b = 2(a - b) \), \( n = 6(a - b) \); the marking scheme.
17. 8.3 A2 (i)–(l): (k)'s identity and next row; B3: the column, the =E links, the student's row false exactly on \( 0 < \abs{x} < 2 \), the marking scheme.
18. 8.4 A2 (a)–(l); B3: the identity \( (x - 1)^2(x + 2) = x^3 - 3x + 2 \), \( c = -2 \), the failure at \( -3 \) (\( -25 < -9 \)), the marking scheme.
19. 8.5 A2 (a)–(l); B4: \( n^3 - n = (n - 1)n(n + 1) \), the citations of `exm-generalise-proof` and `exr-quantifier-rhetoric-b3` (a later exercise citing an earlier one, STYLE §6); C3: the lemma by cases; (L₃) and (L₄) as stated are true; the failure at \( n = 2 \); \( 4 = (2/1)^2 \) satisfies (L₄); the marking schemes.
20. 8.6 A2 (i)–(l); B3: the five verdicts ((i), (ii) correct; (iii) (N12) false at \( (0, 0) \); (iv) (N13) true, the strong-induction repair; (v) (N14) false, \( x^2 + x + 1 > 0 \)), the look-alike sentence, the marking scheme; R1 (a)–(d).
21. 8.7 A2 (a)–(l): (c) `exm-triple-negation` is RAA-free; (l) the first line is the only classical step, as 07:149 says. B5: the three derivations (13, 10 and 10 lines, each checked by `check_fitch.py`, no RAA, ¬¬E, LEM or TAUT); (d)'s row assignments and its parenthesis (against 8.8 C1 (a) and (b)); the marking scheme with its TAUT line.
22. 8.8 A1 (a)–(d); A2 (a)–(l) on \( M_1 \), \( M_2 \), \( M_5 \); B1 on \( M_6 \): five verdicts, (b), and (c)'s chain argument. B2's seven verdicts:
    - four derivations ((a) 16 lines, (b) 13, (d) 9, (f) 9);
    - three countermodels ((c) \( M_2 \), (e) \( M_1 \), (g) \( M_3 \); (g) is classically valid by cases on \( p \));
    - the look-alike notes, including (e)'s parenthesis \( \neg p \to p \vdash \neg\neg p \) (derivable without RAA) and (g)'s link to `lem-atom-splitting` as delivered;
    - the TAUT clause of the statement and of the fatal errors.
    
    C1:
    - (a) the 12-line derivation from \( p \vee \neg p \);
    - (b) \( \vdash (((p \to q) \to p) \to p) \to (p \vee \neg p) \) is classically valid; \( M_7 \) refutes it at \( w_0 \) (Peirce's law forced there, \( q \) known nowhere), while \( M_1 \) does not (checked by a Kripke script at S2 round 1);
    - (c) the comparison with `thm-classical-rules-interderivable` and 8.7 B5 (c).

    C2: both directions. Every marking scheme.
23. **Derive-or-break audit (binding rule 7).** Every claim of 8.6 B3 and 8.8 B2 has its verdict settled here, by a derivation, a counterexample or a Kripke countermodel checked by `kripke.py`. Every "derive" verdict of 8.8 B2 is classically valid (truth table) and has an RAA-free derivation. Every "break" verdict there has a countermodel. No list contains a claim that is classically invalid or whose RAA-freeness is unsettled. (A truth-table and Kripke check of every claim of 8.7 B5, 8.8 B2 and the settle table was run while writing this blueprint: the derivable ones are valid, and each break has the model stated.)

**Originality (for S2's comparison with the twelve books):** every example, drill and exercise above was written for this book. The items with standard names carry fd1's own wording and numbers: the barber, the "and so on", the two-node and fork models, the Glivenko instances, and the generalisation from √2. The 8.8 models are named \( M_1 \)–\( M_7 \) in fd1's notation; their shapes (a chain, a fork) are the only possible small shapes and are folklore.

Some sequents are **standard and forced**. 8.8 must refute the propositional right column of 8.7's table, which is read off fd1's own Chapters 2 and 6. Those rows, among them the De Morgan direction \( \neg(p \wedge q) \vdash \neg p \vee \neg q \), contraposition's converse, excluded middle, double-negation elimination, Peirce's law and \( (p \to q) \vee (q \to p) \), are the standard examples of every treatment and appear in published exercise lists. They are kept because the table forces them, and S2 should read them as such. The **free choices** follow no book's list: B2's (a)–(g), C1 (b) and the cycle items of 8.1. S2 round 1 replaced three of them that matched published exercises: 8.8's S1 B2 (g) (\( p \to (q \vee r) \vdash (p \to q) \vee (p \to r) \)), 8.8's S1 C1 (b) (\( (\neg\neg p \to p) \to (p \vee \neg p) \)), and 8.1's S1 B4 and `exm-rhetoric-cycle` (the \( n \), \( n^2 \), \( n^3 \) divisibility pattern). Each replacement was grepped against the twelve books' texts: \( (p \to q) \wedge (\neg p \to q) \vdash q \) appears in them only as a classical lemma of a completeness proof, which is fd1's own @lem-atom-splitting. The Kripke contrast of C1 (b), the parity cycle on \( a + b \), \( a - b \) and same parity, and the cycle on \( n \), \( n^2 \), \( n^2 + 2n \) were not found (Critic review, smaller correction 7).

---

**Frozen after S2 (final revision, 2026-10-25).**

## 10. Notes for S3 and S4

- **One pass.** S3 executes R5 §4 and this file's §4 together, section by section, in R5's new order, with this file's insertion points (each names its neighbour in R5's order). There is no intermediate "R5-only" draft.
- **Three drafters:** (i) 8.1, 8.2; (ii) 8.3, 8.4, 8.5; (iii) 8.6, 8.7, 8.8. The index is written last, against the delivered sections (DRAFTING).
- **`08-kripke-models.md`** is a new file in `src/ch08-from-derivations-to-prose/`. The config lists the directory (`fd1/config/config.json` line 108), so no config edit is needed. Its opening sentence marks it optional, as 7.3 does; no class goes on its heading.
- **Derivations.**
  - Every new derivation passes `tools/check_fitch.py`. R5's scaffold of 8.3 B2 carries no `\purpose` (D1), and S4 accepts `--purposes` notes on that block only.
  - The level-1 TAUT option (§4.3, item 2) is used in no derivation of this chapter. It is stated, not exercised, so `check_fitch.py`'s skeleton check needs no new case here.
- **Figures.** Each new figure is a raw LaTeX block with its `tikzpicture` written out, using only `latex/book-diagrams.sty`'s styles (`flowchart`, `fc start`, `fc step`, `fc test`, `fc arrow`; `structure`, `elt`, `rel`), with no colour and no white fill. S4 checks both the HTML (SVG) and the PDF renderings. In 8.8 the two labels on one `elt` node (name and known letters) must not collide. If they do, S4 moves the letters to `label=left:` or `label=right:` as needed.
- **Fallbacks.**
  - 8.8's Quick-check fallback (§4.8, after item 10) is used only if `check_structure.py` flags the density.
  - The heading link of binding rule 4 is used only if the engine resolves heading ids. S4 tests it once and records the result in the S4 note.
- **Seams (S8).** Reconciled at S2 round 2 (S2 replies, round 2): the planned labels of §6.2 are delivered; R5 §6's R4 seam holds (8.2's reprint and bracket table against 06-translation.md:374–399; level 0 of `exm-uniform-four-levels` and F5.3-c against 6.4's derivation). S8 re-greps them after drafting.
- **The S9 packet** for Chapter 8 (layout G4) goes with the whole-volume pass. The packet names the judgment calls of this file:
  - D6, banks of 12 against the layout's 8: this file's choice, not a STYLE floor (Time ≈ 37.4 h, "about 35", against the layout's 33; banks of 8 give ≈ 33.9 h);
  - the Time line's rounding risk: 37.4 h is about 0.1 h under the 37.5 h boundary, so roughly 230 more main-line words turn "about 35" into "about 40" (§5);
  - 8.1 at ≤ 5,000 and 8.7 at ≤ 3,950 against the layout's 4,900 and 3,900, with `exm-rhetoric-cycle` in fold F8.1-e to keep 8.1 under STYLE's cap (§4.1, §4.7);
  - the (N11) decision: R5's split kept;
  - the index at ≤ 1,300 words;
  - D2, galleries not adopted;
  - D11 (b), the non-mathematical extraction item not adopted.

---

## S2 replies

**Round 1** (19 findings; two pairs were duplicates: the (N14)/(N9) overlap and the F8.8-b step numbering, each reported twice, and the contrapositive tag also twice). Every finding is applied; none is disputed.

1. **Extensionality in 8.2** (error). Applied (§4.2, item 2; A2 (k); ledger; S2a item 8). ↔I inside ∀I now yields \( \forall x\, (x \in A \leftrightarrow x \in B) \), and \( A = B \) follows by the cited axiom, tagged [∀E, →E with the axiom]. The row's never-silent column names the appeal. The citation goes to 5.7 (`exm-extensionality-logical-half` and its remark), not to 7.2: Chapter 8's What-you-need line admits from Chapter 7 only the statement under `#from-counter-models-to-non-derivability`. 7.2 and 5.8 B4 are named in the ledger as the passages this agrees with.
2. **The unannounced contrapositive** (error, and its duplicate). Applied (§4.1, item 4; S2a item 7). The line is tagged only with the never-silent item, and "(N5)" is gone.
3. **The flowchart against "valid but improper"** (gap). Applied (§4.6, items 1 and 4; A2 (l)). The test node asks for "a rule, or a chain of rules and silent steps". The failing outcome is "no such chain", and the licensed outcome is "licensed at its level".
4. **"Three cases" and Glivenko with premises** (minor). Applied (§4.7, item 1). The text now says "Exercise B5 (a) and (b) derive two cases" and "applied to the implication from the premises' conjunction". The RAA-free step from \( \neg\neg(\gamma \to \varphi) \) and \( \gamma \) to \( \neg\neg\varphi \) is added to S2a item 13.
5. **F8.8-b's steps** (minor, and its duplicate). Applied (§4.8, item 5). The steps are now Step 1 reduction, Step 2 induction, Step 3 cases (RAA failing) and Step 4 last line, as in 07-soundness.md:147–217.
6. **8.8's opening contradicted itself** (minor). Applied to the opening paragraph and the Purpose line, in the wording the finding proposed.
7. **(N9) against (N14)** (minor gap, and its duplicate). Applied (§4.6, item 2; §4.4 ledger). (N14) is now "an object named before it is shown to exist", with a stated line: (N9) **asserts** a warrant that is not available, and (N14) **presupposes** a premise it never asserts. Every tag was re-checked. The B4/B3/C3 fatal errors are asserted warrants and stay (N9), reworded where needed ("given as its own reason"). The "the" instances stay (N14) and are not (N9). (N14)'s second instance moved to fold F8.6-b, which says it is (N14).
8. **The untagged Not-allowed line in 8.2** (minor). Applied (§4.2, item 3). It is replaced by a tagged line, a missing ∃I witness. No deviation from D3 remains.
9. **B3's triangle-inequality row** (minor). Applied, in the wording the finding proposed.
10. **Name clash (F1)–(F7)** (minor). Applied. The forcing clauses are (K1)–(K7) throughout §4.8 and §9, and the recursion sentence now says that it defines, for each formula, the set of stages forcing it.
11. **The fifth core-to-optional pointer** (minor). Applied (§4.7, item 2; §6.1; §6.2; S2a item 3). Six pointers are listed. B5 (d)'s parenthesis now carries a different claim, because C1 (b) was replaced (item 13 below). The claim is that one instance of Peirce's law does not give back the instance of excluded middle that gives it, and 8.8 C1 (b) proves it.
12. **8.1 B4 and `exm-rhetoric-cycle` too close to a published exercise** (error). Applied (§4.1). B4 is now a parity cycle on two integers: \( a + b \) even, \( a - b \) even, same parity. `exm-rhetoric-cycle` is now \( n \), \( n^2 \), \( n^2 + 2n \) odd. Sidecars, ledger and the F2.2 promise row are updated: B4 no longer uses the division-algorithm fact or "nothing between 0 and 1".
13. **8.8's sequents following published lists** (error). Applied. B2 (g) is now \( (p \to q) \wedge (\neg p \to q) \vdash q \), broken at \( M_3 \). Its look-alike note ties it to `lem-atom-splitting`, and the mislabelled "distributive law" note is gone. C1 (b) is now \( \vdash (((p \to q) \to p) \to p) \to (p \vee \neg p) \), refuted at \( M_7 \) and not at \( M_1 \). It is neither \( \neg p \vee \neg\neg p \) nor any item of the two named exercise lists. Both were checked by a Kripke script and by truth tables, and grepped against the books' texts. The originality paragraph of §9 now says which rows are standard and forced by 8.7's table.
14. **"No single rule" against TAUT** (error). Applied (§4.6, item 4; A2 (l)). The improper example is now first-order (∀∀ exchange), which TAUT does not write. A2 (l) keeps its propositional compression, and its answer says that a TAUT line also writes it from 4.8 on.
15. **TAUT in the RAA-free tasks** (gap). Applied. "Without TAUT" now appears in the statements of B5, B2 and C1 (a) and (b), and the fatal-error lists have a TAUT line. `thm-kripke-soundness` excludes TAUT, with one sentence. 8.7's definition of an intuitionistic derivation gains a sentence (§4.7, item 5). Binding rule 5 records it. B4's census is recomputed against the delivered Chapters 3–7, with at least TAUT and `prp-taut-skeleton` added (§4.7, item 6; superseded item (viii)).
16. **Budgets of 8.1 and 8.6** (error). Applied (§4.1, §4.6, §5).
   - 8.1 was re-estimated from the quoted text. Even with F8.1-f (01:304) folded, the √5 check moved to A2 (h) and the dilemma sentence dropped, it comes to about 5,115 with `exm-rhetoric-cycle` on the main line. The example therefore goes into fold F8.1-e, which leaves about 4,970. The main line keeps the subsection's lead, its row and its Quick check, which teach the move. The budget is raised to ≤ 5,000 (layout 4,900), the most STYLE allows.
   - 8.6 comes to about 2,990 once the second instances of (N13)/(N14) and the barber sentence move to F8.6-b and the traditional names move to F8.6-c.
   - 8.7, re-checked after item 15's sentence, is at ≤ 3,950.
   - Every section that runs close now has a named fallback (§5).
   - The Time line was recomputed: ≈ 37.4 h, "about 35". The rounding risk is in §5 and in the S9 packet.
17. **D6 is a choice, not a STYLE floor** (minor). Applied (D6, §5, §10). STYLE §12.8's sizes bind rule sections, and Chapter 8 has none. Banks of 12 are this file's choice, and banks of 8 would give ≈ 33.9 h.
18. **Bookkeeping** (minor). Applied. §6.1 lists all six 8.7 → 8.8 pointers, and the §07 → §08 row names B5 (d)'s claim. (L₃) and (L₄) are added to the F1.5 → F2.2 row.

## S2 replies (round 2: reconciliation)

2026-10-25: the final S2 revision, against the delivered and approved Chapters 1–7, with no re-review. Every label, section pointer and seam this file cites, and those of R5 that it keeps, was grepped in `fd1/src/ch0[1-7]-*/`.

1. **Planned labels** (§3.2, §6.1, §6.2). All nine are delivered under their planned names and in their planned sections: `def-rule-taut` 4.8, `thm-monotonicity` 4.9, `thm-barber` 5.6, `exm-extensionality-logical-half` 5.7, `def-definite-description` and `prp-definitional-extension` 5.8, `prp-replacement` 6.2, `def-propositional-skeleton` and `prp-taut-skeleton` 6.3. Every other outside label cited by this file or by R5's kept text exists where cited (the (N1)–(N14) rule pointers: 1.4, 1.6, 4.2, 5.3, 5.4, 5.6, 5.8; the table's ten results of Chapters 2 and 6; the 8.8 list). §6.1's status column and §3.2 updated. The statements were checked against what this file says of them: the table's columns against the delivered statements (each says where RAA enters; `prp-quantifier-passage` names exactly \( \dashv \) in (d) and (e)); F8.2-a against `thm-monotonicity` (positive and negative places, semantic); `prp-replacement` covers a part under a quantifier (R1); `thm-structural-recursion` allows any values (8.8's set-valued recursion); `lem-context-inclusion` (b) as F8.8-b uses it. Not changed: R5's `def-supremum`, `thm-naturals-unbounded`, and this file's `thm-division-algorithm`, `lem-naturals-arithmetic` are labels of later volumes, cited as prose (STATUS rows), not `@ref`s.
2. **Constructive dilemma** (§4.1 item 2; §6.1; §7; S2a item 7). The delivered 2.3 has no labelled derived rule CD: CD is used as a derived rule in `exr-derived-rules-b4` (a) (and MPT in its (c)). The row's first cell now reads "the derived rule CD of Section 2.3, @exr-derived-rules-b4"; §7's row 2 likewise.
3. **The 3.3 recall** (§4.4 item 2; §6.1). Reworded to 3.3 as delivered, whose step 3 is "Name the unstated facts": "Section 3.3 turned a paragraph of argument into a sequent: its conclusion, its stated premises, and the unstated facts that close its gaps." Same length.
4. **TAUT's licence** (§4.7 item 5 and its ledger line). The delivered `def-rule-taut` licenses TAUT through @cor-derivable-iff-valid, so item 5's sentence names it before the completeness theorem (+4 words; 8.7 expected ≈ 3,919, under 3,950).
5. **B4's census** (§4.7 item 6; S2a item 3). Recomputed now rather than left to S3: part (a) unchanged; part (b) adds `prp-derivable-iff-negation-inconsistent` (b) (3.2, its box closes by RAA), TAUT and `prp-taut-skeleton`, and the optional 4.10's `lem-lindenbaum`, `thm-completeness-infinite`, `thm-compactness`. Chapters 5 and 7 add none (7.6's theorems are stated without proof). The semantic results of 4.4, 4.5 and 4.9 are excluded with one sentence of reason. The full list is in item 6.
6. **F8.8-b's steps** (§4.8 item 5; round 1 reply 5). 4.7's Steps 1–4 are at 07-soundness.md:200–270 in the delivered text, not 147–217; same order and content (Step 2 strong induction on \( k \), Step 3 the cases, Step 4 the last line), so only the line pointer changes. S2a item 14: `thm-raa-independent` is 4.7, not "4.x".
7. **R5 §6's R4 seam.** Holds, with no change. 8.2's reprint: the delivered 6.1 derivation (06-translation.md:374–399) has 16 lines, the \( \forall\varepsilon \) box 2–15 closing at 16, the \( \exists E \) box 5–14, line 4 \( \forall E \) at \( \varepsilon_0/2 \) with line 3, line 10 the inequality at \( \varepsilon_0/2 \), line 11 by arith from 10, boxes of \( n_0 \) and \( n_0 \ge N_0 \) at 7 and 9, closing at 13 and 12, \( \exists I \) at 14. R5 §4.2 item 2's abbreviations \( A \), \( B \), its bracket table and 02:13–16's line numbers all match; 6.1 names no matrices, so R5's \( A(n, \varepsilon) \), \( B(n, \varepsilon) \) stand. F5.3-c: the level-0 derivation now in 03:217–238 is line for line 6.4's derivation of `exm-uniform-implies-continuous`; R5's level-1 line numbers (7; 8, 9, 10) and A1's numbers stand. R5's "ch04 08" and "ch04 10" mean 6.1 and 6.4.
8. **Pointers into Chapter 8** (§6.2). The eleven prose pointers of Chapters 1–7 into Chapter 8 and every STATUS row targeting F1.5 are paid by R5's kept text or this file's plan; the table is in §6.2. Three STATUS rows that S1 left out of §6.2 are now listed (F1.3 §08; F1.4 §08; the index Minimum lines and F1.6's index), plus the F1.3 §09 "nothing to pay" row, which F8.2-a's fold pointer leaves true. Nothing is missing, so nothing is added. No chapter 1–7 cites an entry (Nk) by number.
9. **Delivered edits inside Chapter 8's current text** (no line shift since `034a2ae`; R5's and this file's line numbers stand). Two seam edits from later chapters change lines that R5 keeps verbatim: ix:11 now names "the cut rule (@lem-weakening-cut)" (it moves into fold F5.0-a verbatim, which keeps it), and 05:14's strategy 3 now reads "(Section 3.1, extended in Section 6.3)". The drafter keeps both as delivered.
10. **§9's S2a items.** Round 1 left none open. The items that waited on delivered chapters are settled here: item 3 (census, TAUT, R1's clause), item 7 (dilemma row), item 8 (monotonicity, extensionality against 5.7, 5.8 B4 and 7.2), item 10 (3.3 recall), item 14 (recursion, 4.7's steps, `lem-context-inclusion`), item 22 (`lem-atom-splitting` is the splitting lemma B2 (g)'s note names). No new derivation was written, so `check_fitch.py` had nothing new to check.
11. **Outside this file, for the coordinator** (not changed here): fd2's `07-gate-0.md:365` cites "*Logic and Proof*, Section 5.6 (@fd1:exm-not-allowed-catalogue)", which is Section 8.6 under the final layout.


*Deviation (S3, 2026-10-25):* `index.md` runs 1,506 main-line words against the budget of at most 1,300 (almost all quoted blueprint text; roadmap 370); left for S9 (ch04's index, 1,576, is a precedent). The Minimum line reads "Minimum before *Sets and Functions*" as in the delivered indexes, not "Minimum for fd2". The two heading targets in the Terms list are plain links to `07-excluded-middle.html#what-a-proof-provides` and `#one-extra-rule` (the engine does not resolve heading ids across files; Section 7.2's heading stays prose in Chapter 8, as §3 C1 allows). Sidecar `kripke.py` is now `def-kripke-model.py` (the checker needs a sidecar named after a label). The 8.1 fold title lost its inline math (it broke the PDF title macro), and 8.7 B5 (a) points to the derivation of the optional proposition by prose, not by reference, since a non-optional block may not cite an optional one. Core Time 37.1 h is 0.4 h under the 37.5 h rounding boundary.
