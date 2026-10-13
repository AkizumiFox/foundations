<!-- hand-written -->
# Deepening blueprint: F1.8 Working with Quantifiers: Translation, Laws and Search (fd1 Chapter 6), D (stage S1)

**Status: S1 draft, 2026-10-13; S2 round 1 findings applied (see "S2 replies" at the end).**

**What this is.** The **full** S1 blueprint for fd1 Chapter 6 (atlas F1.8), the chapter the final layout builds from old Sections 4.8–4.10 and one new section (`layout-final.md` §1.3, §6.2 item 6). It is complete on its own. A drafter executes it with this file, the current `fd1/src/ch06-working-with-quantifiers/` (moved there by D2, commit `034a2ae`), the frozen `ch04-revision.md` (R4) §4.8–§4.10 for every detail this file keeps and does not repeat, `authoring/STYLE.md` (§11, §12, and §12.8 and §12.13 as amended by D1), `DRAFTING.md` (including `\purpose`, `\taut` and the Diagrams templates of `latex/book-diagrams.sty`) and `NOTATION.md`. The model of register and format is the deepened Chapter 1 and its blueprint `ch01-deepen.md`.

Line numbers are those of the current files at `034a2ae`: `01:263` is `01-translation.md` line 263, `02:` is `02-quantifier-laws.md`, `04:` is `04-uniform-continuity-rule-by-rule.md`, and `ix:` is `index.md`. D2 moved the files with `git mv` and did not change their line count, so R4's `08:n`, `09:n` and `10:n` are this file's `01:n`, `02:n` and `04:n` (spot-checked at 01:149, 02:606 and 04:99). The new file `03-first-order-search.md` does not exist yet. Until it does, `04-…` displays as Section 6.3 (STATUS row F1.8). Every number in this file is the final one: 6.1 translation, 6.2 laws, 6.3 search, 6.4 uniform continuity.

**Inputs.**
- The deepening plan (`deepening-plan.md`): §3.0, the volume-wide devices; §3.4, items 4.9, 4.10 and 4.11, which are now 6.1, 6.2 and 6.4; and its binding *Critic review*.
  - **C1:** first-order soundness and `cor-counter-model` sit together in optional 7.3. The core cites only the heading `#from-counter-models-to-non-derivability` in 7.2.
  - **C2:** TAUT applies only to the propositional skeleton, and the replacement rule is proved syntactically.
  - **C3:** isomorphism belongs to Chapter 7. The groups correction is Chapter 7's too.
  - **Small corrections:** finite lists Γ throughout; definitional extension is 5.8's business.
- The final layout (`layout-final.md`): §1.2 (the mirror), §1.3 (Chapter 6's four sections, budgets and content), §1.4 (new labels `prp-replacement`, `def-propositional-skeleton`, `prp-taut-skeleton`, `exr-uniform-continuity-rule-by-rule-r*`), §2 (wording rules G10 and TAUT), §3 (Chapter 6: core ≈ 21 h, full ≈ 36 h, A2 parts "36 + battery"), §4.2 (labels by file), §5 (pointer map) and §9 (Critic checklist).
- `labelmap.json`, the gap matrix (`gap-matrix.md`; **techniques only**: no text, example, exercise, sequent list or figure is taken from any book), the frozen R4 §4.8–§4.10, §5, §6, §8 (items 17–19, 30–31), §9 and its S2 replies, STATUS rows naming F1.8, and the ledger `fd1/authoring/ledger/ch06.yaml` (44 items, 0 stale).

Every example, drill, exercise, figure and answer below is the book's own, in mathematical dress, with school mathematics first. Classic named items (the drinker sentence, Darapti) carry fd1's own wording and numbers (plan, binding rule 3).

**Binding rules for this chapter.**
1. **No label is lost, renamed or moved out.** All 30 labels now in `ch06-working-with-quantifiers/` keep their names, their sections and the content of every cited block (§3.1). Seven are cited downstream (fd2, fd3, an1): `exm-translate-limit`, `prp-bounded-quantifier-rules`, `prp-quantifier-negation`, `prp-negated-implication`, `prp-bounded-quantifier-negation`, `prp-arbitrarily-close-equal` and `exm-uniform-implies-continuous`. Their statements and proofs are verbatim. Two of them change only by the pointer remaps listed in §3.1 and S2a (§9). Labels move **within** the chapter only as R4 already decided (the order of 6.2), and no label moves in from another chapter or out to one (layout §4.2: the 6.1, 6.2 and 6.4 rows list exactly these 30). New labels are listed in §3.2.
2. **Reviewed content stays.** R4 §4.8–§4.10 remains the drafting spec for everything it covers, except the items this file supersedes, which are listed in §2.1. Moving a passage verbatim into a second-reading fold is not a change. The key derivations are copied by line number in Chapter 8 and must stay verbatim: the 16-line limit derivation (01:261–290) and the 11-line derivation of `exm-uniform-implies-continuous` (04:43–65). Chapter 8 cites them at 02:7, 02:13, 02:57, 03:26, 03:214, 03:269 and 03:275, and index:7.
3. **New numbering, and no pre-emption.** Every pointer is written in the final layout's numbering (§6). Chapter 6 comes **before** Chapter 7's structures, so:
   - the chapter never writes ⊨ between first-order formulas and never says "model", "structure" or "satisfies" in their Chapter 7 senses;
   - it never asserts that a first-order claim is **not derivable**, except as a forward claim citing Section 7.2 (G10, layout §2 rule 1);
   - a claim is broken by a **counter-reading** (5.3's name): a reading of the symbols, over numbers or a small set, that makes the premises true and the conclusion false. A counter-reading may be followed by "(Section 7.2)", as R4 §1 item 11 allows.
   
   Propositional semantics (4.4–4.8) may be used freely: truth tables, ⊨ between propositional formulas, `def-valid-argument`, completeness.
4. **TAUT is propositional until 6.3.** `\taut` (`\by{TAUT}`) appears nowhere in 6.1 or 6.2, and from 6.3 on only on propositional skeletons (layout §2 rule 3; NOTATION, TAUT). `prp-replacement` (6.2) is proved **syntactically**, by induction on the formula, without completeness (C2, G6). `prp-taut-skeleton` (6.3) is licensed by propositional completeness (4.8) together with uniform substitution of formulas into a Fitch derivation (G11).
5. **Derive-or-break lists hold only settled claims.** Every "derive" verdict comes with a derivation using the rules available at that point. Every "break" verdict comes with a counter-reading whose truth values are checked by school arithmetic (a sidecar does the checking). No list holds a claim that is neither derived nor broken.
6. **Depends on D0 and D1.** These are in place: `"fitch-purposes": "infer"` is already set in `fd1/config/config.json`; `check_fitch.py` already computes skeletons for `\taut`; the Diagrams templates exist (`square`/`\oppositionsquare`, `flowchart`); and STYLE §12.8 and §12.13 already hold. The drafter writes `\purpose{…}` by hand only on snapshot and scaffold assumptions whose box no justified line closes yet.

---

## 1. The volume-wide devices, as applied to Chapter 6

D1. **Purpose-annotated assumptions** (STYLE §12.13.1). The engine prints "asm, for ∃E", "asm, for ∀I" (on a bounded ∀I box's assumption \( x_0 \in A \)), "asm, for →I", and so on. By hand, `\purpose{\Ee}`, `\purpose{\Ai}`, `\purpose{\ii}`, `\purpose{\ni}` or `\purpose{\raa}` is written only:
- in the two snapshots of `exm-search-with-witnesses` (6.3);
- in the scaffold of 6.3 B2;
- nowhere else. R4's outline displays in 6.1 and 6.4 need none: every box in them has its closing line written and justified (in 6.1 only line 13 is a bare goal, and it closes no box), so the engine infers each purpose.

Chapter 6 adds no rule. Its bounded rules are derived rules, so the purpose annotation is not re-taught; one sentence in 6.1 says that the bounded ∀I box's assumption prints as "asm, for ∀I".

D2. **Rule-instance gallery** (§12.13.2). **Not adopted** in Chapter 6. STYLE gives a gallery to each *rule section*, and Chapter 6 has none: the bounded rules are derived, and TAUT is a licence, not a rule with a schema. In their place, 6.1's traps gallery shows wrong formulas beside right ones, and 6.3's Not-allowed block for TAUT shows look-alikes that are not TAUT steps.

D3. **"Not allowed" blocks** (§12.13.3). There are two. **6.1, after the bounded rules:** four wrong steps, each tagged with the clause of `prp-bounded-quantifier-rules` it breaks. **6.3, after TAUT:** five wrong TAUT steps, each tagged with what it really needs. Each block is a `::: {.warning}` titled `[Not allowed: …]`. Neither cites the catalogue `exm-not-allowed-catalogue` by number: it is in Chapter 8, as `ch01-deepen` D3 records.

D4. **The counterexample set** (§12.13.4). Recalled by name in 6.3's "Four kinds of task, with quantifiers" ("break it: make every member of its counterexample set true, by a counter-reading") and in every "break" verdict of the chapter. Its next return, the counter-model, belongs to 7.2.

D5. **Derive-or-break items** (§12.13.4). The verdict is withheld in 6.2 B4 (six claims) and 6.3 B1 (the battery, twelve claims). A claim is broken by a counter-reading (binding rule 3), and each "break" solution reads "Breaks: under the reading …, every member of the counterexample set is true". STYLE §12.13.4 still says "a counter-model (from the counter-model section)", which is 7.2. Chapter 6 uses its earlier means, the counter-reading.

D6. **Drill banks of 12** (§12.8; layout §3, "36 + battery").
- **Banks:** `exr-translation-a2` (6.1; R4's eight parts plus four new), `exr-quantifier-laws-a2` (6.2; R4's eight plus four new) and `exr-uniform-continuity-rule-by-rule-a2` (6.4, new; this supersedes R4 §1 item 8's "4.10 gets none").
- **6.3's battery:** a battery `exr-first-order-search-b1` of twelve derive-or-break claims **in place of** an A2 bank (layout §1.3, 6.3).
- **Ramps:** 6.1 and 6.2 are not rule sections, so they use the ramp of their skill: recognize, translate or negate, judge, then construct. 6.4's bank uses §12.8's ramp: one-step, missing premise, fill the justification, "is this application correct?", then short derivations.
- **Solutions:** each bank's one folded solution answers every part in one or two lines.

D7. **One fixed key and reading back** (plan §3.0.7). 6.1 B3 is twenty sentences on one ℕ key (Prime, Even, \( < \), \( \mid \)), with two read-back parts. This is the "one ℕ key over 20 items" of layout §1.3.

D8. **Chapter close** (§12.13.5). `index.md` is written new: motivating question, the mirror box, What you need, Time, Minimum for fd2, Roadmap, Named moves, Where this goes, `## Summary`, `## Terms` (§4.0).

D9. **"Used later" marker** (§12.13.6). One item: 6.3 C1 (the drinker), which 7.1 checks semantically (layout §1.3, 7.1: "drinker checked semantically"). The promise is recorded for the ch07 S1 (§6).

D10. **Pictures** (DRAFTING, Diagrams). Each picture is a raw LaTeX block with its `tikzpicture` written out in full, with no colours and no white fills.
- **6.2:** the square of opposition, drawn with the `square` template and `\oppositionsquare`.
- **6.3:** a flowchart, drawn with the `flowchart` template: the next move in a first-order search.
- **6.4:** Figure D of R4 §4.10 item 7 (the δ-windows of \( x^2 \)), kept as R4 specified.

No arrow diagram and no Hasse diagram: those draw structures, which are Chapter 7's.

D11. **Mirror boxes** (layout G13, §1.2). Each twin section names its propositional twin once, in a `::: {.remark}` titled `[Looking back]`, placed after the section's opening paragraph. Each box is one or two sentences, with its words spent on what is new:
- 6.1 names 3.3 (informal to formal);
- 6.2 names 3.2's equivalence task;
- 6.3 names 3.1 and 3.2.

6.4 is the capstone and has no twin.

D12. **Not adopted, with reasons.**
- **The inline "(Why?)" prompt** of plan §3.0.9: STYLE §12.13 does not carry it, as `ch01-deepen` D11 found.
- **The named move "prove it cannot be false" for ∅** (plan §3.4, 4.10): the layout's 6.2 content list does not carry it, and 5.4's subsection `every-element-of-the-empty-set` already does the work.
- **A pictured structure for each trap** of 6.1 (plan §3.4, 4.9): drawn structures are Chapter 7's, and each trap is separated by a reading over numbers or small sets of reals, as STYLE §12.9 asks.
- **"Two-rule combinations"** (plan §3.4, 4.9): these go into 6.3's named moves as one sentence, not into 6.1.

---

## 2. Section map

| § | Title (`#` line) | File | Main line: now → budget | What changes (details in §4) |
|---|---|---|---|---|
| index | Working with Quantifiers: Translation, Laws and Search | `index.md` (placeholder, 16 lines) | — → ≤ 1,000 | written new: motivating question, mirror box, What you need, Time, Minimum for fd2, Roadmap, Named moves, Where this goes, Summary, Terms |
| 6.1 | Translating Mathematics: Nested and Bounded Quantifiers | `01-translation.md` | 3,753 → ≤ 4,200 | R4 §4.8 (moved one-domain paragraph, the outline, folds); **"The search method, extended" moves out to 6.3**; Looking back; a mixed stage; Not allowed: bounded rules; **traps gallery** `exm-translation-traps`; infinitely many against eventually; translation error against derivation error; Looking ahead (second-order); A2 to 12; B3 (one key, twenty sentences), B4 (unfold, fold back), C3 (eventually ⇒ infinitely often) |
| 6.2 | Negating and Moving Quantifiers | `02-quantifier-laws.md` | 4,496 → ≤ 4,600 | R4 §4.9 (reorder, folds, Looking ahead), **`prp-replacement`** at 02:606 (proof folded; R4's F4.9-a and F4.9-c regrouped); **the A/E/I/O square** with figure; twin-law table; the distribution and passage **proofs folded**; **prenex form** and alternation; A2 to 12; B4 (derive or break), B5 (find the error, true conclusion), C3 (∃ as ¬∀¬) |
| 6.3 | Finding First-Order Derivations | `03-first-order-search.md` (**new**) | — → ≤ 4,500 | Looking back; the search method, extended (moved from 01:307–333); three named moves and a flowchart; `exm-search-with-witnesses` (snapshots); **`def-propositional-skeleton`, `prp-taut-skeleton`** (proof folded), TAUT on skeletons, Not allowed: TAUT; **the propositional core** (`exm-propositional-core`); the four tasks with quantifiers (`exm-four-tasks-with-quantifiers`), test the subgoal by a counter-reading; a library of first-order sequents; Looking ahead (7.2); A1, **B1 battery** (twelve claims), B2 (scaffold), B3 (TAUT), C1 (drinker, used later), C2 (Darapti) |
| 6.4 | Uniformly Continuous Implies Continuous, Rule by Rule | `04-uniform-continuity-rule-by-rule.md` | 2,429 → ≤ 3,600 | R4 §4.10 (outline, fold, Figure D, Looking ahead); the Idea's pointer becomes 6.3; **`exm-not-uniform-derived`** (the negation used in a derivation, shortened by TAUT); **witness functions** δ(ε), δ(x, ε), strategies; **`exm-converse-proof-critique`**; A2 (new, 12); B4 (witness functions); **R1–R3** (new, the chapter's R items) |

### 2.1 What this file supersedes in R4, item by item

Everything else in R4 §4.8–§4.10, §5 (rows 4.8–4.10 only as below), §8 (items 17–19, 30–31) and §9 (D2, D3) stands.

| R4 item | Superseded by |
|---|---|
| §4.8 header: "main line ≤ 3,300; folds ≤ 850. No Looking-ahead box." | main line ≤ 4,200, folds ≤ 850; a Looking-ahead box (§4.1 item 14) |
| §4.8 item 8 "`## The search method, extended` (08:307-333): kept" | moved verbatim to 6.3 (§4.3 item 3), with three changes: its first sentence is kept, 01:314's citation stays, and 01:333's last clause is reworded |
| §4.8 "A2: Drill (`exr-translation-a2`)": eight parts | twelve parts, reordered (§4.1, Exercises); R4's (a)–(h) kept word for word |
| §4.8 "Quick checks: three" | four (one new: finitely many) |
| §4.9 header: "main line ≤ 4,150; folds ≤ 400" | main line ≤ 4,600; folds ≤ 1,450 |
| §4.9 item 5, the two main-line sentences replacing 02:606, and fold F4.9-a | the statement of `prp-replacement` with its meaning sentence, its proof (fold F6.2-a) and fold F6.2-b, which holds the condition-survival sentences of 02:606 (§4.2 item 7) |
| §4.9 item 7: the distribution and passage laws, "proof … kept" | the two proofs (02:318–346, 02:374–576) move verbatim into fold F6.2-d; statements, Ideas, 02:312, 02:348 (R4's wording), 02:350, 02:368, 02:578 and the Quick check stay on the main line. F4.9-c becomes F6.2-c, unchanged in text |
| §4.9 "Exercises … A2: eight parts" | twelve parts (§4.2) |
| §4.10 header: "main line ≤ 2,750; folds ≤ 150" | main line ≤ 3,600; folds ≤ 250 |
| §4.10 item 4: "the Idea … Run the search method of Section 6.1" (implicit: kept verbatim) | "Section 6.1" → "Section 6.3" (pointer remap only) |
| §4.10 "Exercises … No drill bank (§1 item 8)" and R4 §9 D7's "none in 4.10" | a drill bank of 12 (layout §3: 36 core A2 parts); R1–R3 are new (C1 R items, layout §1.4) |
| §4.0 item 7, "Where this goes": the pointers cut from 08:305, 09:118, 09:718 and 10:7 | gathered in **Chapter 6's** index (§4.0 item 7); `ch05-deepen` drops them from Chapter 5's note |
| §4.0 item 4, first-reading path: "all of Section 6.1 (… the search method); Section 6.2 up to 'Moving a quantifier across a connective'; Section 6.4" | Chapter 6's index has no separate path: every main-line passage of 6.1–6.4 is core, and the folds are second reading (§4.0). `ch05-deepen` rewrites Chapter 5's path to stop at 5.8 |
| §1 item 4: "Sections … 6.1–7.3 get none [snapshots]" | 6.3, the mirror of 3.1, gets two snapshots for `exm-search-with-witnesses`; 6.1 and 6.4 still get none |
| §1 item 8 and §5's exercise totals for 4.8–4.10 | §5 below |

---

## 3. Labels

### 3.1 Every label now in the chapter (30): all kept, in place

Counts: downstream files citing the label (fd2, fd3, fd4, an1 `src`) / other fd1 files citing it / ch06 files citing it (grep 2026-10-13). "Verbatim" means statement (and proof, where there is one) unchanged in content.

| Label | Where | Downstream / fd1 / ch06 | Plan |
|---|---|---|---|
| `exm-translate-limit` | 01:27 | 2 / 1 / 1 | verbatim, with R4's bound-letter renamings in (d) and (e) (R4 §8 item 3) |
| `prp-bounded-quantifier-rules` | 01:93 | 8 / 6 / 3 | statement and Idea on the main line; proof verbatim → fold F6.1-b (R4) |
| `exr-translation-a1`, `-b1`, `-b2`, `-c2` | 01:339–496 | 0 | kept |
| `exr-translation-c1` | 01:426 | 0 / 0 / 1 | **frozen** (cited by 04:3); its solution's pointers "Section 6.4" and "Section 7.2" stay |
| `prp-quantifier-negation` | 02:13 | 15 / 4 / 1 | verbatim (key proof). The *Try it first* line 02:25 is outside the block, and its pointer "Section 6.1" → "Section 3.1, with the quantifier steps of Sections 5.3–5.6" (the method is no longer in 6.1, and 6.3 comes later) |
| `prp-negated-implication` | 02:134 | 16 / 5 / 1 | verbatim |
| `prp-bounded-quantifier-negation` | 02:199 | 25 / 6 / 1 | verbatim |
| `prp-quantifier-distribution` | 02:297 | 0 / 2 / 0 | statement on the main line; proof verbatim → fold F6.2-d |
| `prp-quantifier-passage` | 02:352 | 0 / 3 / 1 | statement and Idea on the main line; proof verbatim → fold F6.2-d |
| `exm-negating-definitions` | 02:608 | 0 / 2 / 2 | verbatim; moves up with its subsection (R4) |
| `prp-arbitrarily-close-equal` | 02:704 | 2 / 4 / 2 | verbatim |
| `exr-quantifier-laws-a1` … `-c2` | 02:726–952 | 0 | kept (C2 is the exit check) |
| `exm-uniform-implies-continuous` | 04:30 | 1 / 3 / 1 | verbatim (key proof); the Idea's pointer "Section 6.1" (04:37) → "Section 6.3" |
| `exm-converse-fails` | 04:107 | 0 / 3 / 1 | verbatim |
| `exm-square-not-uniform` | 04:160 | 0 / 7 / 1 | verbatim |
| `exr-uniform-continuity-rule-by-rule-a1` … `-c3` | 04:198–453 | 0 | kept (B2 is the ordering item, C1 is faded, C3 is the exit check) |

The chapter has no heading ids today. The subsection title "Negating a definition, mechanically" is kept word for word, because fd2 ch03 07:94 names it. Label prefixes follow the file stem and never change. The new labels use the stems `translation`, `quantifier-laws`, `first-order-search` and `uniform-continuity-rule-by-rule`.

### 3.2 New labels (30, plus 6 heading ids)

`grep -rl` over `fd1`, `fd2/src`, `fd3/src` and `fd4/src` (2026-10-13) finds none of them, except in the blueprints and plans that name them.

| § | Label | Kind | Main line, fold or exercises |
|---|---|---|---|
| 6.1 | `exm-translation-traps` | gallery: five traps, each with a separating reading | main |
| 6.1 | `exr-translation-a2` | drill bank (R4's eight parts plus four new) | exercises |
| 6.1 | `exr-translation-b3`, `-b4` | B items | exercises |
| 6.1 | `exr-translation-c3` | C item | exercises |
| 6.2 | `prp-replacement` | proposition (layout §1.4) | statement main, proof fold F6.2-a |
| 6.2 | `exm-square-of-opposition` | worked example with figure | main |
| 6.2 | `exm-prenex-conversion` | worked example | main |
| 6.2 | `exr-quantifier-laws-a2` | drill bank (R4's eight parts plus four new) | exercises |
| 6.2 | `exr-quantifier-laws-b4`, `-b5` | B items (derive or break; find the error) | exercises |
| 6.2 | `exr-quantifier-laws-c3` | C item | exercises |
| 6.3 | `def-propositional-skeleton` | definition (layout §1.4) | main |
| 6.3 | `prp-taut-skeleton` | proposition (layout §1.4) | statement main, proof fold F6.3-a |
| 6.3 | `exm-search-with-witnesses` | worked search, two snapshots | main |
| 6.3 | `exm-propositional-core` | worked example | main |
| 6.3 | `exm-four-tasks-with-quantifiers` | worked example, four parts | main |
| 6.3 | `exr-first-order-search-a1` | A item | exercises |
| 6.3 | `exr-first-order-search-b1` | battery (twelve claims) | exercises |
| 6.3 | `exr-first-order-search-b2`, `-b3` | B items | exercises |
| 6.3 | `exr-first-order-search-c1` (used later), `-c2` | C items | exercises |
| 6.4 | `exm-not-uniform-derived` | worked derivation with a TAUT line | main |
| 6.4 | `exm-converse-proof-critique` | worked critique | main |
| 6.4 | `exr-uniform-continuity-rule-by-rule-a2` | drill bank (new) | exercises |
| 6.4 | `exr-uniform-continuity-rule-by-rule-b4` | B item | exercises |
| 6.4 | `exr-uniform-continuity-rule-by-rule-r1`, `-r2`, `-r3` | R items (layout §1.4) | exercises |

**Heading ids (new, for the Terms list):**
- 6.2: `{#the-square-of-opposition}` on "## Four forms and their square" and `{#prenex-form}` on "## Prenex form";
- 6.3: `{#the-propositional-core}` on "## The propositional core" and `{#a-library-of-first-order-sequents}`;
- 6.4: `{#witness-functions}` on "## Witness functions", and `{#two-definitions-that-differ-in-one-place}` on the existing heading at 04:5. This id equals the automatic id, so nothing is renamed.

There are no new `thm-`, `lem-` or `cor-` labels. The drafter greps `fd1/src` again before creating each label (DRAFTING, "Labels").

### 3.3 Bookkeeping (coordinator, S4)

**`fd1/authoring/ledger/ch06.yaml`:**
- New entries for the 30 new labels, and for the new Quick checks.
- Items re-reviewed with no verdict carried:
  - the two grown banks: `exr-translation-a2` and `exr-quantifier-laws-a2` are new entries, since R4's banks were never drafted;
  - `prp-quantifier-negation`, if its hash covers the *Try it first* line;
  - `exm-uniform-implies-continuous`, if its hash covers the Idea's pointer;
  - `prp-quantifier-distribution` and `prp-quantifier-passage`, whose proofs move into a fold. A verbatim move keeps the hash if the hash is of the block text; otherwise these are re-reviewed.
- R4's own changes (the folds, the reworded 02:348 and 02:580, 04:156, 04:188) are re-reviewed as R4 §3.3 already says.

**`fd1/verify/ch06/`:**
- **New sidecars:** `exm-translation-traps.py`, `exr-translation-a2.py`, `exr-translation-b3.py`, `exr-translation-b4.py`, `exr-translation-c3.py`, `exm-square-of-opposition.py`, `exr-quantifier-laws-a2.py`, `exr-quantifier-laws-b4.py`, `exr-quantifier-laws-b5.py`, `exm-four-tasks-with-quantifiers.py`, `exm-propositional-core.py`, `exr-first-order-search-b1.py`, `exr-first-order-search-c1.py`, `exr-first-order-search-c2.py`, `exm-converse-proof-critique.py`, `exr-uniform-continuity-rule-by-rule-a2.py` and `exr-uniform-continuity-rule-by-rule-b4.py`. Each checks the values its block quotes (items in §9).
- **Updated:** `exm-square-not-uniform.py` gains R4's Figure D values.
- **Skeleton tables:** every TAUT line is checked by `check_fitch.py`, which builds the skeleton. Each sidecar that quotes a skeleton verdict (the QCs of 6.3, A1, B1, B3, C2, `exm-propositional-core`, `exm-not-uniform-derived`) also checks it by an explicit truth table.

**`authoring/STATUS.md`:** the promise rows of §6, and the F1.8 row's text once 03 exists.

---

## 4. Per-section plans

Budgets count **main-line** prose words, as `tools/check_structure.py --words` counts them: words outside `.second-reading` folds and before `## Exercises`, with a math span counting as one word and derivations not counted. The "now" figures were measured on the current files on 2026-10-13. Folds are budgeted beside the main line. Quick-check density is checked against STYLE §12.7 (one per 800–1,000 words, and never sparser than one per 1,250).

### 4.0 `index.md` (written new; replaces the D2 placeholder ix:1–16)

**Budget:** ≤ 1,000 words. Expected about 960: story ~110, mirror box ~70, What you need ~110, Time ~35, Minimum ~30, Roadmap ~110, Named moves ~140, Where this goes ~120, Summary ~140, Terms ~150. No fold. Written last, against the delivered sections (DRAFTING).

1. **Title:** `# Working with Quantifiers: Translation, Laws and Search` (ix:1, kept).
2. **Story and motivating question** (~110 words, replaces ix:3). A first course in analysis defines a limit in one sentence with three quantifiers and two bounds, then asks the reader to prove that a sequence does **not** converge, which needs that sentence negated. Chapter 5 gave every quantifier rule, one per section, and this chapter puts them to work on three tasks: turning a definition into a formula, negating and rearranging it by laws, and finding the derivation a claim needs. Then the layout's question, in italics: *"You know every quantifier rule. Can you turn a definition from analysis into a formula, negate it without error, and find the derivation it needs?"* Last, one sentence: the chapter ends where Chapter 5 began, with why "uniformly continuous implies continuous" has a short derivation while its converse is false.
3. **Mirror box** (layout §1.2, G13), a `::: {.remark}` titled `[Looking back]`, ~70 words: "Chapter 3 did for the connectives what this chapter does for the quantifiers. Section 3.3 turned arguments in words into derivations; Section 6.1 does the same for definitions with quantifiers. Section 3.2 sorted the tasks, and Section 3.1 gave the search method; Section 6.3 does both again, with flags and witnesses. Section 6.2 collects the equivalences the tasks keep using. Section 6.4 has no twin: it is the chapter's capstone."
4. **What you need** (~110 words): "Chapters 1–5. From Chapter 3: the search method (Section 3.1) and the four kinds of task (Section 3.2). From Chapter 4: truth tables and tautological consequence (@def-valid-argument), completeness (@thm-completeness) and the TAUT step for propositional formulas (@def-rule-taut). From Chapter 5: the four quantifier rules with their side conditions (@def-rules-universal, @def-rules-existential), bounded quantifiers (@def-bounded-quantifier), substitution, free-for and renaming (Section 5.2), equality (Section 5.7), and counter-readings (Section 5.3). School arithmetic and the order of \( \nN \), \( \nZ \), \( \nR \) are used in examples as facts." (`def-rule-taut` is a new label of `ch04-deepen` (layout §1.4, 4.8); S4 checks that it exists before this index is built.)
5. **Time** (STYLE §11.9): recomputed by the drafter from the delivered text and exercise counts (§5). The expected line is "About 20 hours on the core track (all of A, one B and one C per section, the exit checks); about 40 hours for everything." Not shaded down.
6. **Minimum for fd2** (layout G14, one line, the same as every index): "**Minimum for fd2.** Chapters 1–6 and 8, core; Chapter 7 (Sections 7.1–7.2) before *Sets, Relations, and Cardinality*, Chapter 3."
7. **Roadmap** (replaces ix:7–11; four bullets, one sentence each):
   - **Translating mathematics.** Definitions from analysis as formulas, worked from the outside in; the bounded rules; five traps, each with a reading that shows the wrong formula wrong; "infinitely many" against "eventually".
   - **Negating and moving quantifiers.** "Not every" is "some not"; negation pushed inward law by law, through the replacement rule; the four forms A, E, I, O and their square; the laws that move a quantifier across a connective, and prenex form.
   - **Finding first-order derivations.** The search method with flags and witnesses; TAUT on the propositional skeleton; the propositional core; the four kinds of task with quantifiers; a library of sequents and a battery.
   - **Uniformly continuous implies continuous, rule by rule.** The capstone derivation, the lines at which the converse breaks down, \( x^2 \) as the counter-reading, and witness functions δ(ε) against δ(x, ε).
8. **Named moves** (replaces ix:13–16; each with the section where it is named):
   - **Read it back** (6.1): read a translation back into words before using it.
   - **Negate quantifier by quantifier** (6.2): ix:15 kept.
   - **Open the ∃E boxes early, postpone ∀E until the term is known** (6.3; recalls 5.6 and 5.3).
   - **The propositional core** (6.3): instantiate at the names in play, reason propositionally (with TAUT), then close the boxes.
   - **Test the subgoal by a counter-reading** (6.3).
   - **Read the dependency off the boxes** (6.4): ix:16 "read the dependency off the order" kept, with "(Section 5.1; off the boxes, Section 6.4)".
9. **Where this goes** (new, ~120 words, bold lead-in; the cross-volume pointers of 6.1–6.4, gathered here by R4 §1 item 3's rule): "*Analysis on the Real Line*, Chapter 1 proves from the axioms of the real numbers the facts about \( \nN \) inside \( \nR \) and about absolute value that Sections 6.1 and 6.2 use as school facts, and it uses '"not every" gives "some not"' (Section 6.2) in its proof of the Archimedean property. Its Chapters 5 and 6 define continuity and uniform continuity properly, which Section 6.4 uses only as quantifier patterns. Picking a witness for every ε at once, as one function (Section 6.4), is in general an appeal to the axiom of choice, which *Sets, Relations, and Cardinality*, Chapter 3 states." These replace the pointers R4 cut from 01:305, 02:118, 02:718 and 04:7, which R4 §4.0 item 7 had sent to Chapter 5's index. STATUS rows F1.8 §01/§02 → AN1.1 and F1.8 §04 → AN1.5, AN1.6 move their source to "F1.8 index" (§6), and the axiom-of-choice row is new.
10. **`## Summary`** (~140 words, STYLE §12.13.5), four to six sentences:
    - **Proved:** the bounded rules are abbreviations, not new power; "not every" is "some not", with one direction classical; a negated implication is a conjunction; a bound stays with its quantifier; a part may be replaced by a provably equivalent part anywhere, by a syntactic induction; a step that is right for propositional reasons alone is derivable (TAUT on the skeleton).
    - **Done:** the chapter translated, negated and moved quantifiers in the definitions of analysis, and extended the search method and the four tasks to quantifiers.
    - **The capstone:** it derived "uniformly continuous implies continuous" and located the side conditions that stop the converse.
    - **What is open:** every "break" in the chapter was a counter-reading, and whether a counter-reading really rules out every derivation is Chapter 7's question. Per G10, the Summary says this as a question, not as a claim that the converses are not derivable.
11. **`## Terms`** (≤ 160 words; alphabetical, one line each, every entry linked, each defined in at most nine words):
    - **A, E, I and O forms** (#the-square-of-opposition);
    - **alternation** (#prenex-form);
    - **bounded rules** (@prp-bounded-quantifier-rules);
    - **contradictory and contrary** (#the-square-of-opposition);
    - **negated implication** (@prp-negated-implication);
    - **passage laws** (@prp-quantifier-passage);
    - **prenex form** (#prenex-form);
    - **propositional core** (#the-propositional-core);
    - **propositional skeleton** (@def-propositional-skeleton);
    - **quantifier distribution** (@prp-quantifier-distribution);
    - **quantifier negation** (@prp-quantifier-negation);
    - **replacement of provable equivalents** (@prp-replacement);
    - **TAUT step, on the skeleton** (@prp-taut-skeleton);
    - **uniformly continuous** (#two-definitions-that-differ-in-one-place);
    - **witness function** (#witness-functions).

### 4.1 Section 6.1: Translating Mathematics: Nested and Bounded Quantifiers (`01-translation.md`)

**Budget:** main line ≤ 4,200 (now 3,753). Expected about 3,680: R4's ~3,290, minus the 540 words of "The search method, extended", plus about 930 new. Folds ≤ 850: F6.1-a 159 and F6.1-b 591, as in R4. One forward pointer: the Looking-ahead box (item 14).

**Changes, in the file's order.** R4 §4.8 items 1–7 apply, except where an item below says otherwise.

1. **Opening (01:3).** Kept up to "… and every bound costs extra lines in a derivation." The last three sentences ("This section does three things. … extended to quantifiers and equality.") become: "This section does three things. It translates the standard definitions into formulas, by a procedure that works from the outside in. It turns each quantifier rule into a **bounded** rule that handles the bound in the same step. And it collects the traps that make a translation wrong, each with a reading that shows the wrong formula wrong." (The search method now lives in 6.3.)
2. **Looking back** (new, after 01:3; ~55 words): `::: {.remark}` `[Looking back]`: "Section 3.3 turned an argument in words into a derivation, with one key for a whole paragraph. This section does the same for definitions with quantifiers. What is new is the order of the quantifiers and the bounds they carry, which the propositional key never had."
3. **Four pieces in one sentence** (01:5–13): kept.
4. **Translation from the outside in** (01:15–25): R4 item 2, with the paragraph moved from 5.1 (`ch05…/01:178–182`, 156 words) as step 1's body, and the one reworded sentence. Then, after 01:25, **a mixed stage** (new, ~90 words, bold lead-in `**A mixed stage.**`; technique: Sm, En, LB): "Halfway through, a translation is part words and part symbols, and writing that stage down catches most slips." Then a three-row display (an `aligned` block of three lines, words in `\text{…}`), for "for every positive ε, some element of \( A \) lies within ε of \( s \)":
   - stage 1: \( \forall \varepsilon > 0 \; [\text{some element of } A \text{ lies within } \varepsilon \text{ of } s] \);
   - stage 2: \( \forall \varepsilon > 0 \; \exists x \in A \; [x \text{ lies within } \varepsilon \text{ of } s] \);
   - stage 3: \( \forall \varepsilon > 0 \; \exists x \in A \; (\abs{x - s} < \varepsilon) \).
   
   Then one sentence: "Read the last line back, symbol by symbol, into words: if the words are the sentence you began with, the translation is done." (This is the named move *read it back*.)
5. **`exm-translate-limit`, 01:73, Quick check 01:75–81, warning 01:83–85:** R4 item 3 (verbatim, with the bound letters of (d) and (e) renamed to \( m, n \)).
6. **`## Five traps`** (new subsection after the warning 01:85, before "Rules for bounded quantifiers"; ~380 words including the table; technique: LB, Hu, Sm, Ho, a traps gallery with each wrong version refuted). Lead-in, two sentences: "The warning above caught three slips. Here are five more, each with the reading that shows the wrong formula saying something else." Then **`exm-translation-traps`** `[Five traps, each with a separating reading]`, a pipe table with the columns *sentence* | *wrong* | *right* | *a reading that separates them*. Domain \( \nR \) unless the row says \( \nN \); \( A \), \( B \) are sets of reals, and \( x \in A \) is a one-place predicate (Section 5.1).
   - (a) "\( A \) has at least two elements." | \( \exists x\, \exists y\, (x \in A \wedge y \in A) \) | \( \exists x\, \exists y\, (x \in A \wedge y \in A \wedge x \ne y) \) | \( A = \{3\} \): the sentence is false; the wrong formula is true, with \( x \) and \( y \) both \( 3 \). Two letters may name one element, and "two" needs \( x \ne y \). (Section 5.1's \( \forall \)-with-\( \wedge \) slip is not repeated here: 5.1 works it at 05/01:169 and drills it at 05/01:361.)
   - (b) "Every element of \( A \) and of \( B \) is positive." | \( \forall x\, ((x \in A \wedge x \in B) \to x > 0) \) | \( \forall x\, ((x \in A \vee x \in B) \to x > 0) \) | \( A = \{1\} \), \( B = \{-1\} \): the sentence is false (\( -1 \in B \)); the wrong formula speaks only of common elements, and there are none, so it is true. The "and" of the sentence is an "or" in the restriction.
   - (c) "Only even numbers are multiples of \( 4 \)." (over \( \nN \)) | \( \forall n\, (\mathrm{Even}(n) \to 4 \mid n) \) | \( \forall n\, (4 \mid n \to \mathrm{Even}(n)) \) | The right formula is true; the wrong one is false at \( n = 2 \). "Only \( E \) are \( M \)" puts \( E \) after the arrow, as "only if" did in Section 1.1.
   - (d) "If a natural number is divisible by \( 6 \), then it is even." (over \( \nN \)) | \( \exists n\, (6 \mid n) \to \mathrm{Even}(n) \) | \( \forall n\, (6 \mid n \to \mathrm{Even}(n)) \) | The right formula is true. In the wrong one the last \( n \) is free, and read at \( n = 1 \) it says "if some number is divisible by \( 6 \), then \( 1 \) is even": hypothesis true (\( 6 \mid 6 \)), conclusion false. "A … it" hides a "for every".
   - (e) "If any element of \( A \) is negative, then \( 0 \) is not a lower bound of \( A \)." | \( \forall x \in A\, (x < 0) \to \neg\forall x \in A\, (0 \le x) \) | \( \exists x \in A\, (x < 0) \to \neg\forall x \in A\, (0 \le x) \) | \( A = \emptyset \): the right formula is true (its hypothesis is false); in the wrong one the hypothesis "every element of \( \emptyset \) is negative" is true and the conclusion "not every element of \( \emptyset \) is at least \( 0 \)" is false (Section 5.1, the empty set). After "if" or "not", "any" means "some"; elsewhere it means "every".
   
   Aftermath, one sentence: "A reading like these is a counter-reading for the step from one formula to the other; it shows that the two say different things, which is all a translation needs to know." (No derivability claim, G10.)
7. **Infinitely many and eventually** (new paragraph after the traps, bold lead-in `**Infinitely many, and eventually.**`, ~120 words; technique: LPL, Si). "\( a_n > 0 \) for infinitely many \( n \)" says that however far out you start, some later term is positive: \( \forall N \in \nN\; \exists n \in \nN\; (n \ge N \wedge a_n > 0) \). "Eventually \( a_n > 0 \)" (for all large \( n \), warning (3) above) says \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0) \). The quantifiers are swapped, and the bound \( n \ge N \) moves from \( \wedge \) to \( \to \), as @def-bounded-quantifier's two connectives require. For \( a_n = (-1)^n \) the first is true (every even \( n \ge N \)) and the second false (every odd \( n \ge N \)).
   
   **Quick check (new):** "Translate '\( a_n = 0 \) for only finitely many \( n \)'." *Solution:* from some index on, no term is \( 0 \): \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n \ne 0) \). Finitely many exceptions lie below some \( N \).
8. **Translation error or derivation error** (new paragraph, bold lead-in `**Translation error or derivation error?**`, ~160 words; technique: Hk). "When a derivation ends in a statement you believe false, there are two places to look. A **derivation error** is an illegal line, and checking the derivation line by line finds it. A **translation error** is a formula that does not say what its sentence says, and no line check finds it, because every line may be correct." Example: a reader translates "some element of \( A \) exceeds \( 5 \)" as \( \exists x\, (x \in A \to x > 5) \) (warning (1) above), takes \( A = \{1, 2\} \) and derives the formula from the true line \( \neg(7 \in A) \) in two steps: \( 7 \in A \to 7 > 5 \) by @prp-vacuous-implication, then \( \rulename{\exists I} \) at \( 7 \). Both steps are legal. The conclusion is a true formula about \( A \), and the sentence it was meant to translate is false. The fault is the translation. "So check a surprising conclusion in two ways: run the checker on the lines, and read the formulas back."
9. **`## Rules for bounded quantifiers`:** R4 item 4: the statement verbatim, 01:145 and 01:147 kept, fold F6.1-a (01:149), the Idea on the main line, the proof in fold F6.1-b with R4's lead sentence, then 01:237 and the Quick check 01:239–245. Two insertions:
   - (i) After 01:147, one sentence: "When the engine prints a derivation, the assumption \( x_0 \in A \) of a bounded \( \rulename{\forall I} \) box reads 'asm, for ∀I', since the box closes by \( \rulename{\forall I} \)." (D1.)
   - (ii) After the Idea, before F6.1-b's lead sentence, a **`::: {.warning}` titled `[Not allowed: the bounded rules]`** (new, ~90 words), with four one-line wrong steps, each tagged with the clause it breaks:
     - from \( \forall \varepsilon > 0\; \varphi \) alone, write \( \varphi[1/\varepsilon] \): *the bounded \( \rulename{\forall E} \) cites two lines, and the line \( 1 > 0 \) is missing*;
     - from \( \abs{a_7 - L} < 1 \) alone, write \( \exists N \in \nN\; (\abs{a_N - L} < 1) \): *the bounded \( \rulename{\exists I} \) needs the line \( 7 \in \nN \)*;
     - close a bounded \( \rulename{\forall I} \) box on \( \varepsilon_0 \) while the assumption \( \delta_0 < \varepsilon_0 \) of an enclosing box is still open: *the flag appears in an open assumption*;
     - close a bounded \( \rulename{\exists E} \) box on \( N_0 \) with the last line \( N_0 + 1 \in \nN \): *the conclusion mentions the witness*.
10. **`## A limit derivation with bounds`:** R4 items 5–7. That is: 01:249–259 kept; the outline display with \( G \) and \( G_2 \), its two sentences and the Quick check on \( \varepsilon_0/2 \); then the full derivation 01:261–290 verbatim; then 01:292–303, and 01:305 with R4's reworded last sentence. In the outline the engine infers every purpose, since lines 14, 15 and 16 are written and justified (D1). One change to the text around it: 01:299's last sentence "Section 6.4 makes this reading of dependence precise." stays, as an in-chapter pointer.
11. **`## The search method, extended`** (01:307–333): **moved out** to 6.3 (§4.3 item 3). Nothing replaces it in 6.1.
12. **Quick checks:** a maximum (kept), the bounded \( \rulename{\exists E} \) box (kept), \( \varepsilon_0/2 \) (R4), finitely many (new). That is four in about 3,680 words, one per about 920.
13. **Warnings:** three mistranslations (kept); Not allowed: the bounded rules (new).
14. **Looking ahead** (new; the last block before `## Exercises`): `::: {.remark}` `[Looking ahead]`: "Induction ('a set of natural numbers that contains \( 0 \) and contains \( n + 1 \) whenever it contains \( n \) contains every natural number') and the least-upper-bound property of the real numbers say 'for every **set** of numbers', and the variables of this chapter range over numbers only. Chapter 7's optional last section says what that costs." (STATUS row F1.8 §01 → F1.6 §06; layout §2: a core section may point into 7.6 only as "(optional)".)

**Folds.** F6.1-a `title="Why a proposition, not a definition"`: 01:149. F6.1-b `title="The proof: each bounded rule as a block of unbounded steps"`: 01:155–235. Both are as in R4.

**Cut outright:** 01:21 (replaced by the moved paragraph), 01:305's pointer (R4), and the three sentences of 01:3 named in item 1.

**Exercises.**

- **A1:** unchanged.
- **A2: Drill** (`exr-translation-a2`), twelve parts. R4's eight keep their wording; their letters in R4 are in brackets.
  - (a) [a] Over \( \nR \), translate "\( f \) is bounded above on \( A \)". — \( \exists M\; \forall x \in A\; (f(x) \le M) \).
  - (b) [b] Translate "every element of \( A \) is less than some element of \( B \)". — \( \forall x \in A\; \exists y \in B\; (x < y) \).
  - (c) [c] Translate "some element of \( A \) is less than every element of \( B \)". — \( \exists x \in A\; \forall y \in B\; (x < y) \).
  - (d) [d] Unfold the bounds of (c). — \( \exists x\, (x \in A \wedge \forall y\, (y \in B \to x < y)) \).
  - (e) **new** Write the mixed stage, then the formula, for "every element of \( A \) has a larger element in \( A \)". — "\( \forall x \in A\; [\text{some element of } A \text{ is larger than } x] \)"; \( \forall x \in A\; \exists y \in A\; (x < y) \).
  - (f) [e] Translate "\( a_n > 0 \) for all large \( n \)". — \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0) \).
  - (g) **new** Translate "\( a_n \le 0 \) for infinitely many \( n \)". — \( \forall N \in \nN\; \exists n \in \nN\; (n \ge N \wedge a_n \le 0) \).
  - (h) **new** Translate "not every element of \( A \) is positive" and "no element of \( A \) is positive", and decide both for \( A = \{-1, 1\} \). — \( \neg\forall x \in A\; (x > 0) \), true (\( -1 \)); \( \neg\exists x \in A\; (x > 0) \), or \( \forall x \in A\; \neg(x > 0) \), false (\( 1 \)). (A minimal pair: one word apart, opposite truth values.)
  - (i) **new** Translate "if \( x \cdot x < 0 \) for any real \( x \), then \( 0 = 1 \)". — \( \exists x\, (x \cdot x < 0) \to 0 = 1 \): "any" after "if" is "some". (True, since no real square is negative.)
  - (j) [f] Lines 1 \( \forall \varepsilon > 0\; \varphi \) and 2 \( 1 > 0 \). What does the bounded \( \rulename{\forall E} \) 1, 2 give? — \( \varphi[1/\varepsilon] \).
  - (k) [g] Lines 1 \( 3 \in \nN \) and 2 \( 3 + 3 = 6 \). What does the bounded \( \rulename{\exists I} \) 1, 2 give, with \( \varphi \) the formula \( n + n = 6 \)? — \( \exists n \in \nN\; (n + n = 6) \).
  - (l) [h] How many lines does a bounded \( \rulename{\exists E} \) save over the unbounded rule? — One: two assumptions in place of one assumption and two \( \rulename{\wedge E} \) lines.
  
  None of the new parts repeats a main-line answer: (e) and (g) use sentences of their own, (h)'s pair is not among the traps, and (i)'s "any" differs from trap (e).
- **B1, B2:** kept.
- **B3** (new) `[B3: One key, twenty sentences]` (technique: LB, Sm; one key across a graded set, with reading back). Stem: "The domain is \( \nN = \{0, 1, 2, \dots\} \). Use only \( \mathrm{Prime}(x) \) ('\( x \) is prime'), \( \mathrm{Even}(x) \), \( x < y \), \( x \mid y \) ('\( x \) divides \( y \)', that is, \( y = x \cdot k \) for some \( k \)), \( = \) and the constants \( 1 \), \( 2 \), \( 9 \), with variables \( x \), \( y \), \( z \). Translate sentences 1–18 into formulas. Then translate 19 and 20 into English and decide whether each is true." (Variables avoid \( p, q \): R4 §1 item 10.) Answers:
  1. \( 2 \) is an even prime. — \( \mathrm{Even}(2) \wedge \mathrm{Prime}(2) \)
  2. Some prime divides \( 9 \). — \( \exists x\, (\mathrm{Prime}(x) \wedge x \mid 9) \)
  3. Every prime greater than \( 2 \) is odd. — \( \forall x\, ((\mathrm{Prime}(x) \wedge 2 < x) \to \neg\mathrm{Even}(x)) \)
  4. No prime is less than \( 2 \). — \( \neg\exists x\, (\mathrm{Prime}(x) \wedge x < 2) \), or \( \forall x\, (\mathrm{Prime}(x) \to \neg(x < 2)) \)
  5. Every even number is divisible by \( 2 \). — \( \forall x\, (\mathrm{Even}(x) \to 2 \mid x) \)
  6. Only odd numbers divide \( 9 \). — \( \forall x\, (x \mid 9 \to \neg\mathrm{Even}(x)) \)
  7. \( 1 \) divides every number. — \( \forall x\, (1 \mid x) \)
  8. Some number divides every number. — \( \exists x\, \forall y\, (x \mid y) \)
  9. Every number is divisible by some number. — \( \forall y\, \exists x\, (x \mid y) \)
  10. There is no largest prime. — \( \forall x\, (\mathrm{Prime}(x) \to \exists y\, (\mathrm{Prime}(y) \wedge x < y)) \)
  11. There are infinitely many primes. — \( \forall x\, \exists y\, (x < y \wedge \mathrm{Prime}(y)) \)
  12. Every number greater than \( 1 \) has a prime divisor. — \( \forall x\, (1 < x \to \exists y\, (\mathrm{Prime}(y) \wedge y \mid x)) \)
  13. The only divisors of a prime are \( 1 \) and the prime itself. — \( \forall x\, (\mathrm{Prime}(x) \to \forall y\, (y \mid x \to (y = 1 \vee y = x))) \)
  14. If a number divides \( 2 \), it is \( 1 \) or \( 2 \). — \( \forall x\, (x \mid 2 \to (x = 1 \vee x = 2)) \)
  15. Not every odd number is prime. — \( \neg\forall x\, (\neg\mathrm{Even}(x) \to \mathrm{Prime}(x)) \)
  16. Between any two numbers, one less than the other, there is a third. — \( \forall x\, \forall y\, (x < y \to \exists z\, (x < z \wedge z < y)) \)
  17. Some prime divides every even number. — \( \exists x\, (\mathrm{Prime}(x) \wedge \forall y\, (\mathrm{Even}(y) \to x \mid y)) \)
  18. Every divisor of \( 1 \) is \( 1 \). — \( \forall x\, (x \mid 1 \to x = 1) \)
  19. (read back) \( \forall x\, \forall y\, ((x \mid y \wedge y \mid x) \to x = y) \). — "Two numbers that divide each other are equal." True in \( \nN \): if \( y = xk \) and \( x = yl \), then \( x = xkl \), so \( x = 0 = y \) or \( kl = 1 \), and in \( \nN \) that means \( k = l = 1 \).
  20. (read back) \( \forall x\, (\mathrm{Even}(x) \to \exists y\, (\mathrm{Prime}(y) \wedge y \mid x \wedge \neg(y = 2))) \). — "Every even number has a prime divisor other than \( 2 \)." False: at \( x = 2 \) (and at every power of \( 2 \)) the only prime divisor is \( 2 \).
  
  The solution closes with two sentences: 10 restricts \( x \) to primes and 11 does not; both are true, and in \( \nN \) each follows from the other; 16 is a translation of a false sentence (take \( x = 0 \), \( y = 1 \)), and a correct translation of a false sentence is still correct. Counted for Time as five exercises (the drill rule: twenty one-line tasks).
- **B4** (new) `[B4: Unfold, then fold back]` (technique: Ha; defined notation unfolded to primitives and back). Stem: "Over \( \nR \), for fixed sets \( A \), \( B \), \( C \) of reals, write \( A \subseteq B \) for 'every element of \( A \) is an element of \( B \)', \( A \cup B \) for the set of reals in \( A \) or in \( B \), and \( A \cap B \) for the set of those in both. Use only the predicates \( \in A \), \( \in B \), \( \in C \)."
  - (a) Unfold \( A \subseteq B \cap C \). — \( \forall x\, (x \in A \to (x \in B \wedge x \in C)) \).
  - (b) Unfold \( A \cup B \subseteq C \). — \( \forall x\, ((x \in A \vee x \in B) \to x \in C) \).
  - (c) Unfold "\( A \cap B \) has no element". — \( \neg\exists x\, (x \in A \wedge x \in B) \).
  - (d) Fold back \( \forall x\, (x \in A \to x \in B) \wedge \forall x\, (x \in B \to x \in C) \). — "\( A \subseteq B \) and \( B \subseteq C \)".
  - (e) Fold back \( \forall x\, ((x \in A \wedge x \in B) \to x \in C) \). — \( A \cap B \subseteq C \).
  - (f) A reader unfolds (b) as the formula in (e). Give sets that separate the two. — \( A = \{1\} \), \( B = \{2\} \), \( C = \emptyset \): \( A \cup B \subseteq C \) is false, and (e) is true because \( A \cap B \) has no element. (Trap (b) of the section.)
  
  **Marking scheme** (10 points): 2 for (a)–(c) together (all three bounds attached with \( \to \)); 2 for (d) and (e); 3 for (f): the two sets, plus one sentence on each truth value; 3 for the reason in words that "and" in the restriction of (b) is an "or". Fatal error, scoring 0 for (f): a pair of sets on which the two formulas agree.
- **C1:** frozen, unchanged. **C2:** kept.
- **C3** (new) `[C3: Eventually, therefore infinitely often]` (technique: LPL, Si). Stem: "(a) With the bounded rules, derive \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to P(n)) \vdash \forall M \in \nN\; \exists n \in \nN\; (n \ge M \wedge P(n)) \). Lines of arithmetic may be justified 'arith'. (b) For the converse, give a reading of \( P \) over \( \nN \) under which the premise is true and the conclusion false." Answer (a), in 13 lines:
  1. \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to P(n)) \) — premise
  2. \( M_0 \in \nN \) — asm (box of \( M_0 \), for ∀I)
  3. \( N_0 \in \nN \) — asm (box of \( N_0 \), for ∃E)
  4. \( \forall n \in \nN\; (n \ge N_0 \to P(n)) \) — asm (same box)
  5. \( N_0 + M_0 \in \nN \) — arith 2, 3
  6. \( N_0 + M_0 \ge N_0 \to P(N_0 + M_0) \) — ∀E 4, 5
  7. \( N_0 + M_0 \ge N_0 \) — arith 2 (\( M_0 \ge 0 \))
  8. \( P(N_0 + M_0) \) — →E 6, 7
  9. \( N_0 + M_0 \ge M_0 \) — arith 3 (\( N_0 \ge 0 \))
  10. \( N_0 + M_0 \ge M_0 \wedge P(N_0 + M_0) \) — ∧I 9, 8
  11. \( \exists n \in \nN\; (n \ge M_0 \wedge P(n)) \) — ∃I 5, 10
  12. the same — ∃E 1, 3–11
  13. \( \forall M \in \nN\; \exists n \in \nN\; (n \ge M \wedge P(n)) \) — ∀I 2–12
  
  Side conditions:
  - At 12, \( N_0 \) is not in line 12, line 1, the premise or the open assumption on line 2.
  - At 13, \( M_0 \) is not in the premise or in line 13, and no assumption is open.
  - At 6 and 11, the term \( N_0 + M_0 \) is free for \( n \).
  
  The witness \( N_0 + M_0 \) is built from the two names in play, the move "fix, obtain, choose". (b) \( P(n) \): "\( n \) is even". The premise of the converse holds (beyond any \( M \) there is an even number), and its conclusion fails (beyond any \( N \) there is an odd number). This is a counter-reading (Section 7.2).
  
  **Marking scheme** (10 points): 2 for opening the box of \( M_0 \) first and the \( \rulename{\exists E} \) box on the premise early; 3 for a witness depending on both names, with both bounds checked by arith lines; 2 for checking the side conditions at lines 12 and 13; 3 for (b): a reading, with both truth values justified. Fatal errors, scoring 0 for the step: a witness chosen before \( M_0 \) is given; the witness \( N_0 \) itself (it need not be \( \ge M_0 \)).

**Sidecars:**
- `exm-translation-traps.py`: each of (a)–(e) checked on its reading. Over finite \( A \), \( B \) and a grid of reals for (a), (b), (e); over \( \nN \) up to 200 for (c), (d).
- `exr-translation-a2.py`: (h) on \( \{-1, 1\} \); (i)'s hypothesis false on a grid (for the statement, \( x^2 \ge 0 \)).
- `exr-translation-b3.py`: every one of the twenty formulas evaluated against its English sentence for numbers up to 60 (bounded quantifiers cut at 60, the sentence's own truth asserted only for 19 and 20); 19 true and 20 false at \( 2, 4, 8, 16, 32 \); 16 false at \( (0, 1) \).
- `exr-translation-b4.py`: (f).
- `exr-translation-c3.py`: \( N_0 + M_0 \ge N_0, M_0 \) for \( N_0, M_0 \le 50 \); the parity reading.

**Ledger lines** (new):
- the mixed stage (no fact);
- the traps (school facts: \( \{3\} \) has one element, \( 4 \mid n \Rightarrow \) even, \( 6 \mid 6 \), \( 1 \) odd; the empty set of 5.1);
- \( (-1)^n \) (parity);
- the translation-error example (\( \neg(7 \in \{1, 2\}) \), \( 7 > 5 \));
- the Not-allowed entries (rule clauses of `prp-bounded-quantifier-rules`, cited).

### 4.2 Section 6.2: Negating and Moving Quantifiers (`02-quantifier-laws.md`)

**Budget:** main line ≤ 4,600 (now 4,496). Expected about 4,560: R4's ~4,120, plus `prp-replacement`'s statement and meaning (+85 net), the square (~300), prenex (~260), the twin table (~120) and the mirror box (~50), minus the two proofs folded (−382). Folds ≤ 1,450 (F6.2-a ~550, F6.2-b ~300, F6.2-c ~110, F6.2-d 382). One forward pointer: R4's Looking-ahead box (Chapter 8).

**Fallback, if the delivered main line is over 4,600:** the twin-law table (item 11) moves whole into a fold `title="Twin laws"` (about −120). It is not the section's only anything.

**Order of material.** This is R4 §4.9's order, with the new items placed: opening; Looking back; Not every, and some not; the negation of an implication; bounded quantifiers keep their bounds; negating a definition, mechanically (with `prp-replacement`); four forms and their square (new); how the laws look in a mathematical proof; moving a quantifier across a connective (proofs folded; twin table); prenex form (new); Looking ahead.

1. **Opening (02:3):** R4 item 1, with its new last sentence extended: "… and ends with the laws that move a quantifier across a connective, and with prenex form, where every quantifier stands at the front."
2. **Looking back** (new, after 02:3, ~50 words): `::: {.remark}` `[Looking back]`: "Section 3.2 proved two statements equivalent by two derivations, one each way. Every law of this section is such a pair. What is new is that a law may now be used on a part of a formula buried under quantifiers, and the subsection on negating a definition says why that is safe."
3. **`## Not every, and some not`** (02:5–128): R4 item 2, with one more change. The *Try it first* line 02:25 is reworded: "*Try it first (ten minutes): run the search method of Section 3.1, with the quantifier steps of Sections 5.3–5.6, on (a). Which rule should give the last line, and what would that rule need from the premise?*" The method extended to quantifiers is in 6.3, which comes later, so no pointer to it may serve here.
4. **`## The negation of an implication`** (02:130–191): kept (R4 item 3).
5. **`## Bounded quantifiers keep their bounds`** (02:193–291): R4 item 4, which cuts the parenthesis of 02:290.
6. **`## Negating a definition, mechanically`** (02:588–696, moved up; heading kept word for word): the algorithm 02:590–604 kept. Then 02:606 is **replaced on the main line** (this supersedes R4 item 5's two sentences) by:
   - a lead sentence: "Why may a step act on a part buried inside the formula? Because a part may be replaced by a part provably equivalent to it, even under quantifiers that bind its variables, as long as the equivalence is derivable for every choice of those variables, that is, its closure is derivable.";
   - then **`prp-replacement`**:

     ```
     ::: {#prp-replacement}
     [Replacement of Provable Equivalents]

     Let \( \varphi \) and \( \psi \) be formulas, and let \( z_1, \dots, z_k \) be the variables free in
     \( \varphi \) or in \( \psi \). Suppose that
     \( \vdash \forall z_1 \cdots \forall z_k\, (\varphi \leftrightarrow \psi) \).
     If \( \chi' \) is obtained from a formula \( \chi \) by replacing one occurrence of \( \varphi \)
     in \( \chi \) by \( \psi \), then
     \( \vdash \forall w_1 \cdots \forall w_m\, (\chi \leftrightarrow \chi') \), where
     \( w_1, \dots, w_m \) are the variables free in \( \chi \) or in \( \chi' \).
     In particular, \( \chi \dashv\vdash \chi' \).
     :::
     ```

   - then the meaning, as one italic line: *In words: swap a part for a provably equivalent part anywhere in a formula, provided the equivalence is derivable for every choice of its free variables, that is, its closure is derivable; every law of this section is.*
   - Then two main-line sentences: "The proof is an induction on the formula \( \chi \); its connective steps are short derivations with the rules of Chapters 1 and 2, its quantifier steps use a flagged box or an \( \rulename{\exists E} \) box with a fresh name, and it does not use truth tables or completeness. It is in the fold below, followed by a second fold that checks the hypothesis for the laws of this section."
   - Then **fold F6.2-a** `title="The proof of the replacement rule"` (new, ~550 words), which holds the `.proof` of `prp-replacement`. The route is fixed here and checked at S2a (§9, item 12).
     - **Order of the variables.** The order of \( z_1, \dots, z_k \) does not matter, because adjacent \( \forall \)'s may be exchanged (@exm-universal-introduction-derivations (c)), so "the closure" means any one order.
     - **Strong induction** (@thm-strong-induction) on the number of connectives and quantifier symbols of \( \chi \). Write \( \overline{\forall}\theta \) in the proof only, defined there as the closure of \( \theta \) over its free variables.
     - *Case 0: the occurrence is \( \chi \) itself.* Then \( \chi \) is \( \varphi \), \( \chi' \) is \( \psi \), and the claim is the hypothesis.
     - *Case 1: \( \chi = \neg\chi_0 \), with the occurrence in \( \chi_0 \).* The induction hypothesis gives \( \vdash \overline{\forall}(\chi_0 \leftrightarrow \chi_0') \). Derivation:
       - one flagged box per variable of the closure, with fresh flags, nested in the closure's order;
       - inside, \( \rulename{\forall E} \) of the hypothesis at the flags gives the instance of \( \chi_0 \leftrightarrow \chi_0' \);
       - a short derivation with the rules of Section 2.4 (\( \rulename{\leftrightarrow E} \), \( \rulename{\neg I} \) twice, \( \rulename{\leftrightarrow I} \)) gives the instance of \( \neg\chi_0 \leftrightarrow \neg\chi_0' \);
       - the flagged boxes close by \( \rulename{\forall I} \). The side conditions hold because the flags are fresh and no premise or assumption is open at the closing lines.
     - *Case 2: \( \chi = \chi_1 \circ \chi_2 \)*, where \( \circ \) is \( \wedge \), \( \vee \), \( \to \) or \( \leftrightarrow \), and the occurrence is in \( \chi_1 \) (or in \( \chi_2 \), the same with the parts exchanged). As in case 1, with the propositional step \( \alpha \leftrightarrow \beta \vdash (\alpha \circ \gamma) \leftrightarrow (\beta \circ \gamma) \), a derivation with the rules of Chapters 1 and 2 for each \( \circ \). A variable free in \( \chi \) but not in \( \chi_1 \) is flagged and never instantiated, which is harmless: the instance of the hypothesis is taken at the flags of its own variables only.
     - *Case 3: \( \chi = \forall x\, \chi_0 \) or \( \exists x\, \chi_0 \), with the occurrence in \( \chi_0 \).* The induction hypothesis gives \( \vdash \overline{\forall}(\chi_0 \leftrightarrow \chi_0') \), whose closure may include \( x \).
       - Flag the variables free in \( \chi \) or \( \chi' \) with fresh names \( \bar w_0 \); \( x \) is not among them.
       - For \( \forall \), left to right: assume \( \forall x\, \chi_0[\bar w_0/\bar w] \) and open a flagged box with a fresh \( x_1 \). Use \( \rulename{\forall E} \) at \( x_1 \). Use \( \rulename{\forall E} \) of the induction hypothesis at \( \bar w_0 \) and \( x_1 \), each variable at its own flag in the closure's order. Then \( \rulename{\leftrightarrow E} \), and \( \rulename{\forall I} \) gives \( \forall x\, \chi_0'[\bar w_0/\bar w] \). The flag \( x_1 \) appears in no premise, in no open assumption and not in the conclusion.
       - Right to left is the same, and \( \rulename{\leftrightarrow I} \) joins the two directions.
       - For \( \exists \): an \( \rulename{\exists E} \) box with a fresh witness, \( \rulename{\leftrightarrow E} \) inside, closed after \( \rulename{\exists I} \).
       - Substitution passes \( \forall x \) and \( \exists x \) because \( x \) is not among \( \bar w \), and all the flags are fresh, so the simultaneous and the step-by-step substitutions agree.
     - *The "in particular":* \( \rulename{\forall E} \) at each \( w_i \) itself (a variable is free for itself), then \( \rulename{\leftrightarrow E} \) each way.
   - Then **fold F6.2-b** `title="Why the laws of this section meet the hypothesis"`. It holds the sentences of 02:606 that check that a law's condition survives at fresh names. This supersedes R4's F4.9-a, whose congruence argument `prp-replacement` now carries. The text:
     - first, a new opening sentence: "A law of this section is proved for every formula that meets its condition, so it holds for the instances at fresh names \( z_{1,0}, \dots, z_{k,0} \), and \( k \) flagged boxes give its closure, as `prp-replacement` asks."
     - then 02:606's sentences from "The derivation of \( \alpha[x_0/x] \vdash \beta[x_0/x] \) is available because each law used holds for **every** formula that meets its condition, in particular for the instances at \( x_0 \)." through "… for the same reason." (verbatim);
     - then R4's bridging sentence ("… the passage laws at the end of this section have one kind, checked in the fold after them, and the bounded negation laws the other.");
     - then 02:606's sentences on `prp-bounded-quantifier-negation` ("A law of @prp-bounded-quantifier-negation with a bound such as \( z > a \) …" through "… so \( z \) does not occur in it."), verbatim;
     - then "So the instance is again an instance of the same law, with its condition met."
     
     The sentences of 02:606 that the new proposition makes redundant ("If \( \alpha \dashv\vdash \beta \), then \( \neg\alpha \dashv\vdash \neg\beta \) …" through "… and \( \exists x\, \alpha \vdash \exists x\, \beta \) by an \( \rulename{\exists E} \) box ending in \( \rulename{\exists I} \).") and "A part sitting under several symbols is reached one symbol at a time." are cut. Their content is cases 1–3 of F6.2-a.
   - Then, on the main line, **one sentence on renaming** (new): "Renaming a bound variable is a replacement of this kind: Section 5.4 derived \( \forall y\, \varphi \dashv\vdash \forall z\, \varphi[z/y] \) for every formula \( \varphi \) in which \( z \) does not appear (@exm-universal-introduction-derivations (b)), and Section 5.6 did the same for \( \exists \), so the convention of Section 5.2, that a renaming may be made anywhere inside a formula, is now a provable equivalence." The 5.6 result is the heading `#existential-renaming`. This sentence is the payoff 6.3 uses in `prp-taut-skeleton`.
   - Then `exm-negating-definitions` (02:608–667) verbatim; 02:669–680 with R4's letters \( m, n \); the Quick check 02:682–692; R4's new Quick check ("\( f \) is bounded on \( A \)"); and the warning 02:694–696 without its last sentence (R4).
   - 02:676's "both steps act on a part, as the paragraph before @exm-negating-definitions allows" → "both steps act on a part, by @prp-replacement".
7. **`## Four forms and their square {#the-square-of-opposition}`** (new subsection, ~300 words with the figure; technique: LB, Hu, Le — A/E/I/O and the square with its diagonals; contrary against contradictory).
   - **Lead-in:** "Four sentence shapes come up so often that they have names. Fix two one-place predicates \( S \) and \( P \)."
   - **The forms, as a bulleted list:**
     - A, "every \( S \) is \( P \)": \( \forall x\, (S(x) \to P(x)) \);
     - E, "no \( S \) is \( P \)": \( \forall x\, (S(x) \to \neg P(x)) \);
     - I, "some \( S \) is \( P \)": \( \exists x\, (S(x) \wedge P(x)) \);
     - O, "some \( S \) is not \( P \)": \( \exists x\, (S(x) \wedge \neg P(x)) \).
   - **The figure** (DRAFTING, the `square` template), a raw LaTeX block:
     `\begin{tikzpicture}[square] \oppositionsquare{$\forall x\,(S(x) \to P(x))$}{$\forall x\,(S(x) \to \neg P(x))$}{$\exists x\,(S(x) \wedge P(x))$}{$\exists x\,(S(x) \wedge \neg P(x))$} \end{tikzpicture}`.
     Caption sentence, in the text after the figure: "The diagonals always hold: A and O are each the negation of the other, and so are E and I. The other three labels hold only when something is an \( S \)."
   - **The diagonals, by the laws** (two sentences): \( \neg\forall x\, (S(x) \to P(x)) \dashv\vdash \exists x\, (S(x) \wedge \neg P(x)) \) follows by the two steps of the proof of @prp-bounded-quantifier-negation (a), QN and then NIm under \( \exists \). The bound \( S(x) \) is not one the proposition names, and 02:680 makes the same remark for \( \mathrm{Prime}(q) \). \( \neg\forall x\, (S(x) \to \neg P(x)) \dashv\vdash \exists x\, (S(x) \wedge P(x)) \) is the same, followed by @prp-double-negation under \( \exists x \) (by @prp-replacement).
   - **Contrary against contradictory** (two sentences): A and E are **contrary**: they are never both true when something is an \( S \), but they may both be false. The negation of "every element of \( A \) is positive" is "some element of \( A \) is not positive", the O form, and not the E form "every element of \( A \) is non-positive".
   - **`exm-square-of-opposition`** `[The square for multiples of 4 and squares]`: over \( \nN \), \( S \) is "a multiple of \( 4 \)" and \( P \) is "a perfect square".
     - The values: A, "every multiple of \( 4 \) is a perfect square", is false (\( 8 \)); E, "no multiple of \( 4 \) is a perfect square", is false (\( 4 = 2^2 \)); I is true (\( 4 \)); O is true (\( 8 \)). Each diagonal joins a true corner to a false one.
     - Then \( S \) is "an odd multiple of \( 4 \)", and nothing is one. Now A and E are both true and I and O both false. Contraries both true, subcontraries both false: this is why the outer labels need something to be an \( S \) (existential import, Section 5.1).
   - **Quick check (new):** "Which corner is the negation of 'no multiple of \( 4 \) is a perfect square', and is that corner true?" *Solution:* I: "some multiple of \( 4 \) is a perfect square", true, since \( 16 = 4 \cdot 4 = 4^2 \). The negation of E is I, by the diagonal.
8. **`## How the laws look in a mathematical proof`** (02:698–720): R4 item 6.
9. **`## Moving a quantifier across a connective`** (02:293–586, moved to the end): R4 item 7, with this file's changes.
   - **The proofs.** The `.proof` of `prp-quantifier-distribution` (02:318–346) and the `.proof` of `prp-quantifier-passage` (02:374–576) move **verbatim** into **fold F6.2-d** `title="The derivations of the distribution and passage laws"`, placed after 02:368's paragraph and the Idea 02:370–372. Each proof is a sibling `.proof` inside the fold, with the distribution proof first.
   - **The Idea 02:314–316** (distribution) stays on the main line, after the statement.
   - **The lead sentence on the main line** (replacing R4's "reference material" sentence): "The laws of this subsection are proved by the method's short runs; the derivations are in a fold, and Section 7.2 returns to two of the one-way laws."
   - **Kept on the main line:** 02:312; 02:348 (as R4 rewords it); 02:350; 02:368; "Why the condition on \( \psi \)" 02:578; and the Quick check 02:580–586. The Quick check's parenthesis becomes "(a law may be used on a part under a quantifier: @prp-replacement, with the fold after this subsection)".
   - 02:578's "The derivation of (b) shows where the condition was used" still points to the derivation, now in F6.2-d. A link opens the fold.
   - **Fold F6.2-c** `title="Passage laws on a part"`: R4's F4.9-c, unchanged in text, placed after "Why the condition on \( \psi \)".
10. **Statements of the two propositions:** verbatim and on the main line, including 02:309 ("All four are derived without RAA") and 02:365 (the count of classical directions). Both are meta-claims about the derivations, which are in the fold. That is allowed: the fold is read as main line by `check_forward_deps.py` (STYLE §12.0).
11. **Twin laws** (new, bold lead-in `**Twin laws.**`, after F6.2-c; ~120 words with the table; technique: Le, LB). Lead sentence: "Over a domain with two elements \( a \), \( b \), a \( \forall \) is an 'and' and an \( \exists \) is an 'or' (Section 5.5 read \( \exists \) over a finite domain as a long 'or'), and each law of this section becomes a propositional law." A pipe table with the columns *law* | *over \( \{a, b\} \)* | *the propositional twin*:
    - QN (a), (b): \( \neg(\varphi_a \wedge \varphi_b) \dashv\vdash \neg\varphi_a \vee \neg\varphi_b \) | @prp-de-morgan (d), (c);
    - QN (c): \( \neg(\varphi_a \vee \varphi_b) \dashv\vdash \neg\varphi_a \wedge \neg\varphi_b \) | @prp-de-morgan (a), (b);
    - distribution (c), one way: \( (\varphi_a \wedge \varphi_b) \vee (\psi_a \wedge \psi_b) \vdash (\varphi_a \vee \psi_a) \wedge (\varphi_b \vee \psi_b) \) | a direct derivation: \( \rulename{\vee E} \) on the premise; in each case \( \rulename{\wedge E} \) twice, \( \rulename{\vee I} \) twice and \( \rulename{\wedge I} \) (the distribution of \( \vee \) over \( \wedge \), one way; @prp-distributivity is \( \wedge \) over \( \vee \) and is not cited);
    - passage (b): \( (\varphi_a \to \psi) \wedge (\varphi_b \to \psi) \dashv\vdash (\varphi_a \vee \varphi_b) \to \psi \) | @exm-cases-on-hypothesis, @exm-or-hypothesis-split.
    
    (\( \varphi_a \) abbreviates \( \varphi[a/x] \), explained in one clause.) Then two sentences: "In each pair the direction that needs \( \rulename{RAA} \) is the same: QN (a) and De Morgan (d). A twin is a reading, not a proof: a domain may be infinite, and the laws were derived for every domain."
12. **`## Prenex form {#prenex-form}`** (new subsection, the last before Looking ahead; ~260 words; technique: LPL, vD, En — one worked conversion, and alternation as a measure).
    - **Definition, in prose:** "A formula is in **prenex form** when all its quantifiers stand at the front, as a **prefix**, before a part with no quantifier, the **matrix**." @exr-quantifier-laws-c1 already uses the term. Its stem's own definition stays, and the main line now says it first.
    - **`exm-prenex-conversion`** `[Bringing a formula into prenex form]`: "Bring \( \exists x\, P(x) \to \exists y\, Q(y) \) into prenex form." Solution:

      \( \exists x\, P(x) \to \exists y\, Q(y) \;\dashv\vdash\; \forall x\, \bigl( P(x) \to \exists y\, Q(y) \bigr) \;\dashv\vdash\; \forall x\, \exists y\, \bigl( P(x) \to Q(y) \bigr) \)

      (an `aligned` display).
      - The first step is passage law (b), with \( \psi \) the formula \( \exists y\, Q(y) \), in which \( x \) is not free.
      - The second is law (e), under \( \forall x \) by @prp-replacement, with \( \psi \) the formula \( P(x) \) and \( y \) not free in it. Its hypothesis is checked in fold F6.2-c.
      - One more sentence: going right, the second step uses the classical direction of (e).
    - **Alternation** (~90 words): count the changes between \( \forall \) and \( \exists \) along the prefix. The example has one, \( \forall \exists \). "\( a_n \to L \)" has two, \( \forall \exists \forall \). Each change is one more round of the game of Section 5.1: a challenger move answered by a defender move. "A prefix with more alternations takes more rounds to win, and checking it by examples gets harder: no finite table of values settles a \( \forall \exists \forall \) sentence over \( \nN \)."
    - **Quick check (new):** "How many alternations have the prefixes of 'uniformly continuous on \( A \)' and 'continuous at every point of \( A \)' (Section 6.1, @exr-translation-c1)?" *Solution:* two each: \( \forall \varepsilon\, \exists \delta\, \forall x\, \forall y \) and \( \forall x\, \forall \varepsilon\, \exists \delta\, \forall y \). The count is the same, and the order differs. Section 6.4 is about that difference.
13. **Looking ahead:** R4's box text ("Chapter 8 says what is at stake when 'not every' becomes 'some not' by RAA, and catalogues the wrong negations of this section among the steps a proof may not take."). It is the last block before `## Exercises`.
14. **Quick checks:** \( \neg\forall x\, P(x) \) and \( \neg P(c) \) (kept), the supremum statement negated (kept), "\( f \) bounded on \( A \)" negated (R4), the square corner (new), the passage law with \( y \) (kept), alternations (new). Six in about 4,560 words, one per about 760.
15. **Warnings:** negate the quantifier, not the bound (kept); the negation of an implication is not an implication (kept).

**Folds.** F6.2-a (new): the proof of `prp-replacement`. F6.2-b (new): condition survival, as described in item 6. F6.2-c (R4's F4.9-c). F6.2-d (new): the proofs 02:318–346 and 02:374–576, verbatim.

**Cut outright:** the pointers R4 cuts (02:118, 02:290, 02:695, 02:718); the congruence sentences of 02:606 (item 6).

**Exercises.**

- **A1** (key proof), **B1**, **B2**, **B3**, **C1** and **C2** (exit check): kept. B2's and C1's solutions cite "the paragraph after the negation procedure" (02:833, 02:877). They become "@prp-replacement", a pointer remap only, and S2a item 14 checks it.
- **A2: Drill** (`exr-quantifier-laws-a2`), twelve parts. R4's (a)–(h) keep their wording and letters. Parts (a)–(h) are negated into positive form; (i)–(l) are new.
  - (a) \( \forall x\, P(x) \). — \( \exists x\, \neg P(x) \).
  - (b) \( \exists x\, (P(x) \wedge Q(x)) \). — \( \forall x\, (\neg P(x) \vee \neg Q(x)) \), equivalently \( \forall x\, (P(x) \to \neg Q(x)) \).
  - (c) \( \forall x > 0\; (x^2 > 0) \), over \( \nR \). — \( \exists x > 0\; (x^2 \le 0) \).
  - (d) "If \( n \) is even, then \( n^2 \) is even", for one integer \( n \). — "\( n \) is even and \( n^2 \) is not even".
  - (e) \( \forall \varepsilon > 0\; \exists \delta > 0\; (\delta < \varepsilon) \). — \( \exists \varepsilon > 0\; \forall \delta > 0\; (\delta \ge \varepsilon) \).
  - (f) \( \forall x \in A\; (x \le s) \). — \( \exists x \in A\; (x > s) \).
  - (g) Which is the negation of \( \forall x \in A\; \exists y \in B\; (x < y) \): (i) \( \exists x \in A\; \forall y \in B\; (x \ge y) \); (ii) \( \exists x \notin A\; \forall y \notin B\; (x \ge y) \); (iii) \( \forall x \in A\; \exists y \in B\; (x \ge y) \)? — (i).
  - (h) "\( (a_n) \) is bounded below", \( \exists m\; \forall n \in \nN\; (m \le a_n) \). — \( \forall m\; \exists n \in \nN\; (a_n < m) \).
  - (i) **new** Over \( \nN \), with \( S \) "is a multiple of \( 3 \)" and \( P \) "is odd", which corner of the square is the negation of "some multiple of \( 3 \) is not odd", and is it true? — A, "every multiple of \( 3 \) is odd"; false (\( 6 \)).
  - (j) **new** Over \( \{a, b\} \), write \( \exists x\, (P(x) \wedge Q(x)) \) and \( \exists x\, P(x) \wedge \exists x\, Q(x) \) without quantifiers, and give truth values that make the second true and the first false. — \( (P(a) \wedge Q(a)) \vee (P(b) \wedge Q(b)) \) and \( (P(a) \vee P(b)) \wedge (Q(a) \vee Q(b)) \); \( P(a) \) and \( Q(b) \) true, \( P(b) \) and \( Q(a) \) false.
  - (k) **new** Name the passage law, and give a prenex form of \( \exists x\, P(x) \to R \), where \( x \) is not free in \( R \). — Law (b): \( \forall x\, (P(x) \to R) \).
  - (l) **new** Is this step correct: from \( \forall x\, (P(x) \to Q(x)) \) to \( \forall x\, (\neg P(x) \to \neg Q(x)) \), "contrapositive under \( \forall \)"? — No. The contrapositive is \( \forall x\, (\neg Q(x) \to \neg P(x)) \). Over \( \nZ \), with \( P \) "multiple of \( 4 \)" and \( Q \) "even", the premise is true and the line false at \( 2 \).
  
  None of the new parts repeats a main-line answer: (i) is not the main line's corner, (j) is distribution (d), which the twin table omits, and (k) is not the worked conversion.
- **B4** (new) `[B4: Derive or break]` (§12.13.4; verdict withheld). Stem: "Derive each claim with the rules and laws so far, or break it by a reading over \( \nZ \) that makes every member of its counterexample set true. (a) \( \forall x\, (P(x) \leftrightarrow Q(x)) \vdash \forall x\, P(x) \leftrightarrow \forall x\, Q(x) \). (b) \( \forall x\, P(x) \leftrightarrow \forall x\, Q(x) \vdash \forall x\, (P(x) \leftrightarrow Q(x)) \). (c) \( \neg\exists x\, (P(x) \wedge \neg Q(x)) \vdash \forall x\, (P(x) \to Q(x)) \). (d) \( \exists x\, P(x) \to \exists x\, Q(x) \vdash \forall x\, (P(x) \to Q(x)) \). (e) \( \exists x\, \forall y\, R(x, y) \vdash \exists x\, R(x, x) \). (f) \( \exists x\, R(x, x) \vdash \exists x\, \forall y\, R(x, y) \)." Answers, each verdict first:
  - (a) **Derive.** \( \rulename{\leftrightarrow I} \) closing two boxes (@def-rules-biconditional). Left to right: assume \( \forall x\, P(x) \); open a flagged box \( x_0 \); \( \rulename{\forall E} \) at \( x_0 \) of the premise and of the assumption; \( \rulename{\leftrightarrow E} \) gives \( Q(x_0) \); \( \rulename{\forall I} \). Right to left is the same with \( P \) and \( Q \) exchanged. Each \( \rulename{\forall I} \): the flag is in neither the premise, the open assumption nor the conclusion. 12 lines (the premise, two boxes of five lines, the \( \rulename{\leftrightarrow I} \) line).
  - (b) **Breaks.** \( P \): "even", \( Q \): "odd". Both \( \forall \)'s are false, so the premise is true; at \( 0 \), "even ↔ odd" is false, so the conclusion is false.
  - (c) **Derive.** 10 lines:
    1. premise;
    2. \( \forall x\, \neg(P(x) \wedge \neg Q(x)) \) — QN (c) 1;
    3. flagged box \( x_0 \): \( \neg(P(x_0) \wedge \neg Q(x_0)) \) — ∀E 2;
    4. \( P(x_0) \) — asm (for →I);
    5. \( \neg Q(x_0) \) — asm (for RAA);
    6. \( P(x_0) \wedge \neg Q(x_0) \) — ∧I 4, 5;
    7. \( \bot \) — ¬E 6, 3;
    8. \( Q(x_0) \) — RAA 5–7;
    9. \( P(x_0) \to Q(x_0) \) — →I 4–8;
    10. \( \forall x\, (P(x) \to Q(x)) \) — ∀I 3–9.
  - (d) **Breaks.** \( P \): "even", \( Q \): "positive". \( \exists \) even and \( \exists \) positive are both true, so the premise is true; "every even integer is positive" fails at \( 0 \).
  - (e) **Derive.** Open the \( \rulename{\exists E} \) box early with a witness \( x_0 \) and \( \forall y\, R(x_0, y) \); \( \rulename{\forall E} \) at \( x_0 \) gives \( R(x_0, x_0) \); \( \rulename{\exists I} \); \( \rulename{\exists E} \). Five lines; \( x_0 \) is not in the conclusion.
  - (f) **Breaks.** \( R(x, y) \): "\( x \le y \)". \( \exists x\, (x \le x) \) is true, and \( \exists x\, \forall y\, (x \le y) \), "some integer is at most every integer", is false.
  
  Closing sentence: (a)/(b) and (e)/(f) are converse pairs; (d) asks for more than its premise gives. The breaks are counter-readings (Section 7.2).
  
  **Marking scheme** (10 points): 1 per correct verdict (6); 2 for the derivations of (a), (c), (e) with every side condition at a closing line checked; 2 for the three readings, each with the truth values of every premise and of the conclusion justified. Fatal errors, scoring 0 for the item's part: a "break" whose reading leaves a premise false; a derivation that closes an \( \rulename{\exists E} \) box on a line mentioning its witness.
- **B5** (new) `[B5: Find the error]` (STYLE §11.3, find the error with a true conclusion; technique: LPL, Hk). Stem: "Here is a 'derivation' of \( \exists x\, (P(x) \wedge Q(x)), \ \forall x\, (Q(x) \to R(x)) \vdash \exists x\, R(x) \).
  1. \( \exists x\, (P(x) \wedge Q(x)) \) — premise
  2. \( \forall x\, (Q(x) \to R(x)) \) — premise
  3. \( P(c) \wedge Q(c) \) — ∃E 1
  4. \( Q(c) \) — ∧E 3
  5. \( Q(c) \to R(c) \) — ∀E 2
  6. \( R(c) \) — →E 5, 4
  7. \( \exists x\, R(x) \) — ∃I 6
  
  Is the conclusion derivable? Does this derivation prove it? Find the line that fails, break the step that line takes, and repair the derivation."
  
  *Answer:*
  - The conclusion is derivable, and the derivation does not prove it. Line 3 fails: \( \rulename{\exists E} \) is not a one-line step. It opens a box with a fresh witness, and a constant already in use is not fresh.
  - The step "from \( \exists x\, (P(x) \wedge Q(x)) \) to \( P(c) \wedge Q(c) \)" breaks over \( \nZ \): \( P \) "even", \( Q \) "positive", \( c \) read as \( 0 \). The premise is true (\( 2 \)), and the line is false.
  - Repair (8 lines): open a box with the witness \( x_0 \) and the assumption \( P(x_0) \wedge Q(x_0) \) (asm, for ∃E); then \( Q(x_0) \) (∧E), \( Q(x_0) \to R(x_0) \) (∀E 2), \( R(x_0) \) (→E) and \( \exists x\, R(x) \) (∃I); close with \( \rulename{\exists E} \) 1, 3–7. \( x_0 \) is not in line 8, in line 1 or in a premise.
  
  **Marking scheme** (10 points): 2 for "derivable, not proved by this derivation"; 3 for line 3 and the rule broken; 2 for a reading breaking the step, with both truth values; 3 for a repaired derivation with the side condition checked. Fatal error, scoring 0 for the step: naming line 7 (\( \rulename{\exists I} \) is legal there).
- **C3** (new) `[C3: "There exists" from "for every"]` (technique: vD, Le; ∃ defined as ¬∀¬, with its rules derived). Stem: "Suppose \( \exists \) were not a symbol of the language, and \( \exists x\, \varphi \) abbreviated \( \neg\forall x\, \neg\varphi \). (a) Show that \( \rulename{\exists I} \) is then a derived step: from \( \varphi[t/x] \), with \( t \) free for \( x \) in \( \varphi \), derive \( \neg\forall x\, \neg\varphi \). (b) Show that \( \rulename{\exists E} \) is: if \( \Gamma, \varphi[x_0/x] \vdash \chi \), where \( x_0 \) is a variable other than \( x \) that appears neither in \( \Gamma \), nor in \( \chi \), nor in \( \varphi \), then \( \Gamma, \neg\forall x\, \neg\varphi \vdash \chi \). (c) Which of (a) and (b) uses \( \rulename{RAA} \)?"
  
  *Answer:*
  - (a) 1 \( \varphi[t/x] \); 2 \( \forall x\, \neg\varphi \) (asm, for ¬I); 3 \( \neg\varphi[t/x] \) (∀E 2, with \( t \) free for \( x \) in \( \neg\varphi \) because it is free in \( \varphi \)); 4 \( \bot \) (¬E 1, 3); 5 \( \neg\forall x\, \neg\varphi \) (¬I 2–4).
  - (b) From the premises \( \Gamma \) and \( \neg\forall x\, \neg\varphi \):
    - assume \( \neg\chi \) (for RAA);
    - open a flagged box \( x_0 \), and in it assume \( \varphi[x_0/x] \) (for ¬I);
    - paste the given derivation of \( \chi \), whose premises \( \Gamma \) are available. Its own flags are first renamed to names that appear nowhere else, as "The laws as one line" (02:128) requires, so that the open assumption \( \neg\chi \) cannot spoil its side conditions;
    - \( \bot \) (¬E with \( \neg\chi \)); \( \neg\varphi[x_0/x] \) (¬I); close the box with \( \forall x\, \neg\varphi \) (∀I). Here \( x_0 \) is in no premise, not in the open assumption \( \neg\chi \) and not in \( \forall x\, \neg\varphi \);
    - \( \bot \) (¬E with the premise \( \neg\forall x\, \neg\varphi \)); \( \chi \) (RAA).
  - (c) (b) uses \( \rulename{RAA} \), at its last line. (a) does not. (Whether (b) could avoid it is not asked.)
  
  **Marking scheme** (10 points): 3 for (a); 2 for setting up (b)'s RAA box and flagged box in the right nesting; 3 for checking the side condition of the \( \rulename{\forall I} \) line, including the renaming of the pasted flags; 2 for (c). Fatal errors, scoring 0 for the step: \( \rulename{\forall I} \) on \( x_0 \) while \( \varphi[x_0/x] \) is still open; instantiating \( \neg\forall x\, \neg\varphi \) by \( \rulename{\forall E} \).

**Sidecars:**
- `exm-square-of-opposition.py`: the four values over \( \nN \) up to 100, and the empty-\( S \) case.
- `exr-quantifier-laws-a2.py`: (i), (j) by truth table, (l) at \( 2 \).
- `exr-quantifier-laws-b4.py`: the readings of (b), (d), (f) over \( \nZ \) cut to \( [-50, 50] \), with the \( \exists \)-witnesses \( 2 \), \( 1 \) quoted.
- `exr-quantifier-laws-b5.py`: \( c = 0 \).

**Ledger lines** (new):
- `prp-replacement` (proof): @exm-universal-introduction-derivations (c) (exchange), @thm-strong-induction, Section 2.4's rules (@def-rules-biconditional), and the side conditions of @def-rules-universal and @def-rules-existential; all argued inline.
- The renaming sentence: @exm-universal-introduction-derivations (b) and `#existential-renaming` (cited).
- The square: parity facts and \( 2 \), \( 3 \) prime.
- The twin table: the cited propositional labels; the reading of 5.5.
- Prenex: the passage laws (cited); "no finite table settles a \( \forall\exists\forall \) sentence" (illustrative, nothing rests on it).

### 4.3 Section 6.3: Finding First-Order Derivations (`03-first-order-search.md`, new)

**Budget:** main line ≤ 4,500. Expected about 4,250: opening and mirror box ~210, the moved search method 540, three moves and the flowchart ~340, `exm-search-with-witnesses` ~410, TAUT on the skeleton ~880, the propositional core ~320, the four tasks with "test the subgoal" ~970, the library ~300, Looking ahead ~40, plus about 240 of connecting sentences. Folds ≤ 450: F6.3-a, the proof of `prp-taut-skeleton`, ~380. One forward pointer: the Looking-ahead box (item 11). Counter-readings carry at most "(Section 7.2)" after them (R4 §1 item 11). STYLE §12.4 requires snapshots only in rule sections, and R4 §1 item 4 gave Sections 6.1–7.3 none. 6.3 gives two to its one worked search, `exm-search-with-witnesses`, as the mirror of 3.1's partial derivations (`def-partial-derivation`), and none to its other examples, each of which shows a move already found.

**Content, in the order of the new file.** The file opens with `# Finding First-Order Derivations`.

1. **Opening** (~150 words). "Chapter 5 added one step to the search method in each rule section, and Section 6.2 added laws. This section puts the steps into one method, names the three moves that do most of the work with quantifiers, admits the propositional step TAUT into derivations with quantifiers, and runs the four kinds of task of Section 3.2 again. The new difficulty is names: which term to instantiate at, when to open a box for a witness, and which names a line may mention when a box closes."
2. **Looking back** (~60 words): `::: {.remark}` `[Looking back]`: "Section 3.1 assembled the search method for the connectives, and Section 3.2 sorted the tasks it serves. Here both return with flags and witnesses. Backward from the goal and forward from the premises is unchanged; what is new is that a box may carry a name, and a closing line must not mention it."
3. **`## The search method, extended`**: 01:307–333 moved **verbatim** (the algorithm and its two paragraphs), with one change: 01:333's last clause "as \( N_0 \) was in the limit derivation above" → "as \( N_0 \) was in the limit derivation of Section 6.1". The opening sentence "Section 3.1 put the moves for the connectives in order. Each of Sections 5.3–5.7 added a step. Here is the method with all of them." stays. 01:314's "as in @exm-translate-limit" stays (a backward citation).
4. **`## Three moves for quantifiers`** (new, ~300 words; technique: Le, LB, named strategy moves). Three bold-led paragraphs:
   - **Open the \( \exists E \) boxes early.** An \( \exists \) line among the resources: open its box at once, with a fresh witness, and make the box's last line the current goal (Section 5.6's "name the witness early"). The witness is often the very term that a \( \forall \) line or the goal is waiting for.
   - **Postpone \( \forall E \) until the term is known.** A \( \forall \) line can be instantiated at any term, so instantiating it before the goal or a witness names the term is a blind choice (Section 5.3's "instantiate at the term you need"). Wait.
   - **The propositional core**, named in its own subsection below.
   
   Then one sentence on two rules in a row (technique: Hu): "Two pairs of steps recur: \( \rulename{\forall E} \) followed by \( \rulename{{\to}E} \), which applies a general law at one point, and \( \rulename{\exists E} \) followed, inside its box, by \( \rulename{\exists I} \) with a term built from the names in hand." Then the figure.

   **Figure 6.3-F** (the `flowchart` template; caption sentence before it: "The next move, read off the goal and the lines in hand"):
   - nodes:
     - (s) `fc start`: "the current goal and the available lines";
     - (t1) `fc test`, below s: "goal begins with \( \forall \),\\ \( \wedge \), \( \to \), \( \neg \) or \( \leftrightarrow \)?";
     - (a) `fc step`, right of t1: "set up its introduction rule\\(for \( \forall \): a fresh flag)";
     - (t2) `fc test`, below t1: "an \( \exists \) line available,\\box not yet opened?";
     - (b) `fc step`, right of t2: "open its \( \exists E \) box now;\\fresh witness, same goal";
     - (t3) `fc test`, below t2: "a \( \forall \) line, and a term\\the goal or a witness names?";
     - (c) `fc step`, right of t3: "\( \forall E \) at that term";
     - (t4) `fc test`, below t3: "goal \( \exists x\, \psi \), and a line\\showing \( \psi[t/x] \)?";
     - (d) `fc step`, right of t4: "\( \exists I \) at \( t \)";
     - (e) `fc start`, below t4: "stuck: test the subgoal\\by a counter-reading;\\then RAA or LEM";
   - arrows:
     - s→t1;
     - t1 –yes→ a; t1 –no→ t2;
     - t2 –yes→ b; t2 –no→ t3;
     - t3 –yes→ c; t3 –no→ t4;
     - t4 –yes→ d; t4 –no→ e;
     - from a, b, c, d one arrow each back to s, drawn as `(a.east) -- ++(0.5,0) |- (s.east)` and the like, all on the right.
   
   The edge from t4 reads "no", never "impossible": the chart is a guide, with no claim of completeness (as 1.6's chart; `ch01-deepen` §9 item 36).
5. **`exm-search-with-witnesses`** `[A search that waits for its witnesses]` (new, ~410 words with snapshots; technique: LB, Le, worked search). "Show that \( \forall x\, (P(x) \to \exists y\, R(x, y)), \ \forall x\, \forall y\, (R(x, y) \to Q(y)), \ \exists x\, P(x) \vdash \exists y\, Q(y) \)."
   - *Idea:* the goal is an \( \exists \): postpone it. Premise 3 is an \( \exists \): open its box now, with witness \( x_0 \). Premise 1 is a \( \forall \), and \( x_0 \) is now the term it needs: \( \rulename{\forall E} \) then \( \rulename{{\to}E} \) gives an \( \exists y \) line. Open that box at once, with witness \( y_0 \). Premise 2 needs two terms, and both are in hand: \( x_0 \), then \( y_0 \). The postponed goal gets its witness, \( y_0 \).
   - **Snapshots.**
     - S1: lines 1–3; the box of \( x_0 \) opened with line 4 \( P(x_0) \) (`\purpose{\Ee}`), a gap, line 12 \( \exists y\, Q(y) \) unjustified as the box's last line, and line 13 \( \exists y\, Q(y) \) unjustified.
     - S2: lines 1–6 written (5 \( P(x_0) \to \exists y\, R(x_0, y) \), ∀E 1; 6 \( \exists y\, R(x_0, y) \), →E 5, 4); the box of \( y_0 \) opened with line 7 \( R(x_0, y_0) \) (`\purpose{\Ee}`), a gap, line 11 \( \exists y\, Q(y) \) unjustified; lines 12 and 13 unjustified.
   - **The derivation:**
     1. \( \forall x\, (P(x) \to \exists y\, R(x, y)) \) — premise
     2. \( \forall x\, \forall y\, (R(x, y) \to Q(y)) \) — premise
     3. \( \exists x\, P(x) \) — premise
     4. \( P(x_0) \) — asm (box of \( x_0 \))
     5. \( P(x_0) \to \exists y\, R(x_0, y) \) — ∀E 1
     6. \( \exists y\, R(x_0, y) \) — →E 5, 4
     7. \( R(x_0, y_0) \) — asm (box of \( y_0 \))
     8. \( \forall y\, (R(x_0, y) \to Q(y)) \) — ∀E 2
     9. \( R(x_0, y_0) \to Q(y_0) \) — ∀E 8
     10. \( Q(y_0) \) — →E 9, 7
     11. \( \exists y\, Q(y) \) — ∃I 10
     12. \( \exists y\, Q(y) \) — ∃E 6, 7–11
     13. \( \exists y\, Q(y) \) — ∃E 3, 4–12
   - Side conditions: at 12, \( y_0 \) is not in line 12, line 6, the premises or the open assumption on line 4. At 13, \( x_0 \) is not in line 13, line 3 or the premises.
   - Reading (one sentence, school level, over \( \nZ \)): \( P(x) \): "\( x > 0 \)", \( R(x, y) \): "\( y = 2x + 1 \)", \( Q(y) \): "\( y \) is odd". Every positive integer has a \( 2x + 1 \); every number of the form \( 2x + 1 \) is odd; some integer is positive; so some integer is odd.
   
   **Quick check (new):** "Why is line 8 an instance at \( x_0 \) and not at some other term?" *Solution:* line 7, the only line that asserts \( R \) of particular terms, mentions \( x_0 \) and \( y_0 \). Premise 2 is useful only at the terms that line names. This is the move "postpone \( \rulename{\forall E} \) until the term is known".
6. **`## Steps that are right for propositional reasons`** (new, ~880 words; technique: LPL, a tautological-consequence rule restricted to the propositional skeleton; C2, G11).
   - **Lead** (~80 words): "Inside the boxes of a first-order derivation, many steps are propositional: \( \rulename{\wedge E} \), \( \rulename{{\to}E} \), a contrapositive, a case split. Section 4.8 let a propositional derivation take such steps in one line, as TAUT. With quantifiers the step must not look inside a quantifier, and the next definition says exactly what it may look at."
   - **`def-propositional-skeleton`:**

     ```
     ::: {#def-propositional-skeleton}
     [Propositional Skeleton]

     Call a first-order formula **prime** if it is atomic and not \( \bot \), or begins with a
     quantifier, bounded or not. Assign to each prime formula a propositional atom, the **same** atom to two prime
     formulas exactly when they differ at most by renaming bound variables (Section 5.2). The
     **propositional skeleton** \( \mathrm{sk}(\varphi) \) of a formula \( \varphi \) is defined by
     recursion: \( \mathrm{sk}(\bot) = \bot \); \( \mathrm{sk}(\pi) \) is the atom of \( \pi \) for a
     prime formula \( \pi \); \( \mathrm{sk}(\neg\varphi) = \neg\,\mathrm{sk}(\varphi) \); and
     \( \mathrm{sk}(\varphi \circ \psi) = \mathrm{sk}(\varphi) \circ \mathrm{sk}(\psi) \) for each of
     \( \wedge \), \( \vee \), \( \to \), \( \leftrightarrow \). The formulas of one list take their
     skeletons from one assignment.
     :::
     ```

     One sentence after it: "The skeleton keeps the connectives outside every quantifier and hides everything else; this is not the skeleton of a derivation that Section 3.1 reads off the goal, and the book always says 'propositional skeleton' for this one." Example, one display: the skeleton of \( \forall x\, P(x) \to (\exists y\, R(y, c) \vee \neg\forall z\, P(z)) \) is \( p \to (q \vee \neg p) \). \( \forall x\, P(x) \) and \( \forall z\, P(z) \) differ only by renaming, so they share \( p \).
   - **`prp-taut-skeleton`:**

     ```
     ::: {#prp-taut-skeleton}
     [Tautological Steps on the Skeleton]

     Let \( \Gamma \) be a list of first-order formulas and \( \psi \) a formula, with skeletons taken
     from one assignment. If \( \mathrm{sk}(\psi) \) is a tautological consequence of the skeletons of
     \( \Gamma \) (@def-valid-argument), then \( \Gamma \vdash \psi \). If no two different prime
     formulas of \( \Gamma \) and \( \psi \) share an atom, the derivation uses only the rules of
     Chapters 1 and 2.
     :::
     ```

     Meaning, one italic line: *In words: a step that is right for propositional reasons alone is derivable, with the quantified parts carried along untouched.*
     Then one main-line sentence: "The proof takes the propositional derivation that completeness provides and puts the prime formulas back in place of their atoms; it is in the fold below."
   - **Fold F6.3-a** `title="The proof: completeness on the skeleton, then substitution"` (~380 words), holding the `.proof`.
     - **Step 1, no two different prime formulas share an atom.**
       - By @cor-derivable-iff-valid (completeness, Section 4.8) there is a derivation \( D \) of \( \mathrm{sk}(\Gamma) \vdash \mathrm{sk}(\psi) \) with the rules of Chapters 1 and 2. Its lines are propositional formulas.
       - Replace, in every line of \( D \), each atom by the prime formula it stands for, and any other atom by \( \bot \). This is the substitution of formulas for atoms that @def-derived-rule makes for letters, and that @lem-substitution makes for meaning.
       - Every rule of Chapters 1 and 2 is a schema in formulas, and the replacement commutes with each connective and leaves \( \bot \) alone. So each line keeps its rule and its citations, and each box keeps its extent and its assumption.
       - \( D \) has no flagged box, so no side condition about names arises.
       - Each premise \( \mathrm{sk}(\gamma) \) becomes \( \gamma \), and the last line becomes \( \psi \). So the result is a first-order derivation of \( \Gamma \vdash \psi \) (@def-derivation, as Section 5.4 extended it).
     - **Step 2, the general case.**
       - Choose one prime formula for each atom, and let \( \gamma^* \) be \( \gamma \) with every prime formula replaced by the chosen one of its atom.
       - Prime formulas with one atom differ only by renaming. A renaming is a provable equivalence whose closure is derivable (the renaming sentence after @prp-replacement), so @prp-replacement gives \( \gamma \dashv\vdash \gamma^* \) for each formula of the list, and \( \psi \dashv\vdash \psi^* \).
       - Step 1 gives \( \Gamma^* \vdash \psi^* \).
       - @lem-weakening-cut (Section 2.3) chains \( \Gamma \vdash \gamma^* \) for each \( \gamma \), then \( \Gamma^* \vdash \psi^* \), then \( \psi^* \vdash \psi \). Each pasted block's flags are first renamed to names new to the whole derivation, as "The laws as one line" (Section 6.2) argues, so @lem-weakening-cut (c) holds for these first-order derivations by the same pasting: no flag of a pasted block then occurs in a premise or an open assumption of the derivation it is pasted into.
   - **The TAUT step** (~120 words, bold lead-in `**TAUT on the skeleton.**`): "From now on, a line of a derivation may be justified \( \rulename{TAUT} \) (`\taut{…}`), citing available lines, when its skeleton is a tautological consequence of their skeletons, all from one assignment; with no cited lines, when its skeleton is a tautology. This is @def-rule-taut of Section 4.8, applied to skeletons. By @prp-taut-skeleton the line abbreviates a block of primitive steps, pasted in with any flags renamed to names new to the whole derivation, as 'The laws as one line' (Section 6.2) allows. As in Section 4.8, use TAUT only for a step a written proof would leave unsaid." (Layout §2 rule 3: `check_fitch.py` builds the skeleton.)
   - **Examples** (~150 words; a short list). These are TAUT steps:
     - from \( \neg(\exists x\, P(x) \wedge Q(c)) \) and \( Q(c) \) to \( \neg\exists x\, P(x) \): \( \neg(p \wedge q), q \models \neg p \);
     - from \( \forall x\, (P(x) \to Q(x)) \to R \) and \( \neg R \) to \( \neg\forall x\, (P(x) \to Q(x)) \): modus tollens on the skeleton, \( p \to r, \neg r \models \neg p \).
     
     These are not:
     - from \( \forall x\, \forall y\, R(x, y) \) to \( \forall y\, \forall x\, R(x, y) \): the two prime formulas do not differ by renaming, so the skeletons are \( p \) and \( q \), and \( p \not\models q \). The step is derivable, by @exm-universal-introduction-derivations (c), and the derivation looks inside the quantifiers;
     - from \( \forall x\, P(x) \) to \( P(c) \): the skeletons are \( p \) and \( q \); this is \( \rulename{\forall E} \);
     - \( x = x \): the skeleton is one atom, not a tautology; this is \( \rulename{{=}I} \).
   - **Quick check (new):** "Which are TAUT steps? (a) From \( \exists x\, P(x) \wedge \forall y\, Q(y) \) to \( \forall y\, Q(y) \wedge \exists x\, P(x) \). (b) From \( \forall x\, (P(x) \wedge Q(x)) \) to \( \forall x\, P(x) \). (c) From \( \neg\forall x\, P(x) \) to \( \exists x\, \neg P(x) \)." *Solution:* (a) yes: \( p \wedge q \models q \wedge p \). (b) no: the skeletons are two different atoms; the step is @prp-quantifier-distribution (a), which looks inside \( \forall x \). (c) no: \( \neg p \) and \( q \); it is QN (a) of Section 6.2, which needs quantifier rules and \( \rulename{RAA} \).
   - **`::: {.warning}` titled `[Not allowed: TAUT]`** (~120 words; D3), five one-line wrong steps, each tagged with what it really needs:
     - from \( \forall x\, (P(x) \wedge Q(x)) \) to \( \forall x\, Q(x) \): *looks inside a quantifier; needs a flagged box*;
     - from \( \forall x\, P(x) \) to \( P(f(c)) \): *an instance, not a tautological consequence; needs \( \rulename{\forall E} \)*;
     - from \( P(c) \) to \( \exists x\, P(x) \): *needs \( \rulename{\exists I} \)*;
     - from \( s = t \) and \( P(s) \) to \( P(t) \): *the skeleton is \( p, q \models r \), false; needs \( \rulename{{=}E} \)*;
     - citing a line inside a box that has closed: *not available, whatever the table says (@def-derivation)*.
7. **`## The propositional core {#the-propositional-core}`** (new, ~320 words; technique: Le). Lead: "Many first-order derivations have the same shape. Open the boxes the goal asks for, instantiate every \( \forall \) line at the names in play, then finish with a step that is propositional. The quantifiers frame the derivation, and its core is a truth-table fact."
   - **`exm-propositional-core`** `[A propositional core inside a flagged box]`: "Show that \( \forall x\, (P(x) \to (Q(x) \vee R(x))), \ \forall x\, \neg Q(x) \vdash \forall x\, (P(x) \to R(x)) \)." Derivation:
     1. \( \forall x\, (P(x) \to (Q(x) \vee R(x))) \) — premise
     2. \( \forall x\, \neg Q(x) \) — premise
     3. \( P(x_0) \to (Q(x_0) \vee R(x_0)) \) — ∀E 1 (box of \( x_0 \) opens here, with no assumption)
     4. \( \neg Q(x_0) \) — ∀E 2
     5. \( P(x_0) \to R(x_0) \) — TAUT 3, 4
     6. \( \forall x\, (P(x) \to R(x)) \) — ∀I 3–5
     
     The skeleton of line 5's step is \( p \to (q \vee r), \neg q \models p \to r \). At line 6, \( x_0 \) is not in a premise or in line 6, and no assumption is open. Reading over \( \nZ \): \( P(n) \): "\( n > 1 \)", \( Q(n) \): "\( n^2 = 2 \)", \( R(n) \): "\( n > 0 \)". The premises are "if \( n > 1 \), then \( n^2 = 2 \) or \( n > 0 \)" (true, since \( n > 1 \) gives \( n > 0 \)) and "no integer squares to \( 2 \)", each checked without the conclusion. The conclusion is "every integer greater than \( 1 \) is positive". Its quantifier part is two instantiations and one generalization, and its core is propositional.
   - **Quick check (new):** "Write out what line 5 abbreviates, with the rules of Chapters 1 and 2." *Solution:*
     - assume \( P(x_0) \) (for →I);
     - \( Q(x_0) \vee R(x_0) \) (→E 3);
     - split by \( \rulename{\vee E} \): in the case \( Q(x_0) \), a clash with line 4 gives \( \bot \) and \( \rulename{\bot E} \) gives \( R(x_0) \); in the case \( R(x_0) \), repeat it;
     - \( R(x_0) \) by \( \rulename{\vee E} \), then \( \rulename{{\to}I} \).
     
     That is nine lines in place of one. A written proof would say "so \( R(x_0) \), since \( \neg Q(x_0) \)".
8. **`## Four kinds of task, with quantifiers`** (new, ~970 words; the mirror of 3.2; technique: LB, LPL, task types and derive-or-break). Lead (~100 words): "Section 3.2 sorted propositional problems into four kinds, and the kind decides how the search begins. The same four come back. A **theorem** \( \vdash \varphi \) has no premises; an **equivalence** \( \varphi \dashv\vdash \psi \) needs two derivations; **inconsistency** of a list is a derivation of \( \bot \) from it (Section 3.2's definition reads the same for first-order formulas, now with all the rules); and **derive or break** withholds the verdict. A claim is broken by a counter-reading, which makes every member of its counterexample set true (Section 7.2)."
   - **`exm-four-tasks-with-quantifiers`** `[One pair of predicates, four tasks]`, in four parts:
     - (a) *Theorem.* \( \vdash \forall x\, P(x) \to \exists x\, (P(x) \vee Q(x)) \).
       1. \( \forall x\, P(x) \) — asm (for →I)
       2. \( P(x) \) — ∀E 1, at the variable \( x \)
       3. \( P(x) \vee Q(x) \) — ∨I 2
       4. \( \exists x\, (P(x) \vee Q(x)) \) — ∃I 3, at \( x \) itself, as in @prp-forall-implies-exists
       5. \( \forall x\, P(x) \to \exists x\, (P(x) \vee Q(x)) \) — →I 1–4
       
       With no premises the search starts from the goal alone.
     - (b) *Equivalence.* \( \forall x\, (P(x) \to Q(x)) \dashv\vdash \forall x\, (\neg Q(x) \to \neg P(x)) \). Each direction: open a flagged box \( x_0 \); \( \rulename{\forall E} \) at \( x_0 \); TAUT (\( p \to q \models \neg q \to \neg p \), and back); \( \rulename{\forall I} \). Four lines each.
     - (c) *Inconsistency.* The list \( \forall x\, (P(x) \to Q(x)), \ \exists x\, (P(x) \wedge \neg Q(x)) \) is inconsistent (an A form and its O form, Section 6.2):
       1. \( \forall x\, (P(x) \to Q(x)) \) — premise
       2. \( \exists x\, (P(x) \wedge \neg Q(x)) \) — premise
       3. \( P(x_0) \wedge \neg Q(x_0) \) — asm (box of \( x_0 \))
       4. \( P(x_0) \to Q(x_0) \) — ∀E 1
       5. \( \bot \) — TAUT 3, 4
       6. \( \bot \) — ∃E 2, 3–5
     - (d) *Derive or break.* The pair \( \forall x\, (P(x) \to Q(x)) \vdash \forall x\, P(x) \to \forall x\, Q(x) \) and its converse.
       - The first derives:
         1. premise;
         2. \( \forall x\, P(x) \) — asm (for →I);
         3. flagged box \( x_0 \): \( P(x_0) \) — ∀E 2;
         4. \( P(x_0) \to Q(x_0) \) — ∀E 1;
         5. \( Q(x_0) \) — →E 4, 3;
         6. \( \forall x\, Q(x) \) — ∀I 3–5;
         7. →I 2–6.
         
         At 6, \( x_0 \) is not in the premise or in the open assumption on line 2.
       - The converse breaks. Over \( \nZ \), with \( P \): "even" and \( Q \): "positive", "every integer is even" is false, so the premise is true; "every even integer is positive" is false at \( 0 \).
   - **Test the subgoal** (bold lead-in `**Test the subgoal by a counter-reading.**`, ~150 words; the first-order form of G9's move, which 4.7 names; technique: LPL). "When a search produces a subgoal, look for a reading that makes the available lines true and the subgoal false before you chase it. If you find one, the subgoal is the wrong one: Section 7.2 states that such a reading rules out every derivation of it from those lines. Return to the step that produced it." The text cites 4.7 for the propositional move, and says that the first-order statement is 7.2's. No rule-by-rule reason is given: read line by line it is false (∀I goes from a true \( P(x_0) \) to a possibly false \( \forall x\, P(x) \), and →I and ∃E close boxes), and the true reason is first-order soundness, which C1 keeps out of the core. The sentence is a forward claim citing 7.2, which G10 allows.
   - **Quick check (new):** "A search for the limit derivation of Section 6.1 instantiates the premise at \( \varepsilon_0 \) instead of \( \varepsilon_0/2 \), and reaches the subgoal \( \abs{2 a_{n_0} - 2L} < \varepsilon_0 \) with \( \abs{a_{n_0} - L} < \varepsilon_0 \) available. Find a sequence and numbers that make every available line true and the subgoal false." *Solution:* \( \varepsilon_0 = 1 \); \( a_n = L \) for every \( n \) except \( a_{n_0} = L + 0.75 \); \( N_0 = n_0 \). The premise holds, since the sequence is eventually constant at \( L \). Every term is within \( 0.75 < 1 \) of \( L \), so the instance of the premise at \( \varepsilon_0 \) and the box line \( \forall n \in \nN\, (n \ge N_0 \to \abs{a_n - L} < \varepsilon_0) \) hold; \( n_0 \ge N_0 \) holds; and \( \abs{a_{n_0} - L} = 0.75 < 1 \). But \( \abs{2 a_{n_0} - 2L} = 1.5 \ge 1 \). The subgoal is the wrong one; go back to the choice of term.
   - **Quick check (new):** "Which task is \( \exists x\, (P(x) \wedge \neg P(x)) \vdash \bot \), and how long is its derivation with TAUT?" *Solution:* inconsistency. Three lines below the premise: the box \( P(x_0) \wedge \neg P(x_0) \) (asm, for ∃E), \( \bot \) by TAUT, and \( \bot \) by \( \rulename{\exists E} \).
9. **`## A library of first-order sequents {#a-library-of-first-order-sequents}`** (new, ~300 words, a reference table; layout §1.3, 6.3; fd1's own grouping, by the move that does the main work; C small 7).
   - **Lead sentence:** "Here is what the book has proved about quantifiers, grouped by use; a search that needs one of these can copy its derivation, with formulas in place of letters, rather than rediscover it."
   - **Table columns:** *use* | *sequent* | *where*.
   - **Rows:**
     - exchange two like quantifiers: \( \forall x\, \forall y\, \varphi \dashv\vdash \forall y\, \forall x\, \varphi \) | @exm-universal-introduction-derivations (c);
     - rename a bound variable: \( \forall y\, \varphi \dashv\vdash \forall z\, \varphi[z/y] \), and the same for \( \exists \) | @exm-universal-introduction-derivations (b), Section 5.6 (`#existential-renaming`);
     - every gives some: \( \forall x\, \varphi \vdash \exists x\, \varphi \) | @prp-forall-implies-exists;
     - some-all gives all-some: \( \exists x\, \forall y\, R(x, y) \vdash \forall y\, \exists x\, R(x, y) \) | @prp-exists-forall-swap;
     - distribute: \( \forall \) over \( \wedge \) and \( \exists \) over \( \vee \) both ways, \( \forall \) over \( \vee \) and \( \exists \) over \( \wedge \) one way | @prp-quantifier-distribution;
     - negate: "not every" and "some not", "none" and "every not", a negated implication, bounded forms | @prp-quantifier-negation, @prp-negated-implication, @prp-bounded-quantifier-negation;
     - move across a connective | @prp-quantifier-passage;
     - replace a part | @prp-replacement;
     - equality: symmetric and transitive | @prp-equality-symmetric-transitive;
     - bounds in one step | @prp-bounded-quantifier-rules;
     - propositional steps | @prp-taut-skeleton.
   - **The licence:** no new licence. The laws of Section 6.2 may already be used as one line, by "The laws as one line" (02:128), and the others are patterns to copy. The table counts toward the main line, and layout §3's lever (a) applies to 3.3's library, not to this one.
10. **Quick checks:** line 8's term, TAUT steps, what line 5 abbreviates, the wrong subgoal, the inconsistency task. Five in about 4,250 words, one per about 850.
11. **Looking ahead** (the last block before `## Exercises`): `::: {.remark}` `[Looking ahead]`: "Every claim this section broke, it broke by a counter-reading. Chapter 7 gives counter-readings an exact form, the counter-model, and states that a counter-model rules out every derivation." (STATUS row F1.8 §03 → F1.6 §02, new.)

**Warnings:** Not allowed: TAUT (item 6). It is the section's warning.

**Folds:** F6.3-a, as above.

**Exercises.**

- **A1** (new) `[A1]`, five parts. Answers:
  - (a) The skeleton of \( \neg\exists x\, P(x) \vee (Q(c) \wedge \exists y\, P(y)) \)? Is it a tautology? — \( \neg p \vee (q \wedge p) \): \( \exists x\, P(x) \) and \( \exists y\, P(y) \) share \( p \). Not a tautology: \( p \) true and \( q \) false make it false.
  - (b) The skeleton of \( \exists x\, (P(x) \wedge Q(x)) \wedge \neg\exists x\, (Q(x) \wedge P(x)) \)? Can a TAUT step derive \( \bot \) from it? — \( p \wedge \neg q \). The two prime formulas are not renamings of each other (\( P(x) \wedge Q(x) \) against \( Q(x) \wedge P(x) \)), so they get different atoms, and \( p \wedge \neg q \) is not contradictory: no. \( \bot \) is derivable all the same, by an \( \rulename{\exists E} \) box on the first conjunct, TAUT inside it, \( \rulename{\exists I} \) and a clash with the second conjunct.
  - (c) Which are TAUT steps? (i) From \( \forall x\, P(x) \) and \( \forall x\, P(x) \to \exists y\, Q(y) \) to \( \exists y\, Q(y) \). (ii) From \( \forall x\, (P(x) \to Q(x)) \) and \( P(c) \) to \( Q(c) \). (iii) From \( \neg\neg\exists x\, P(x) \) to \( \exists x\, P(x) \). — (i) yes (\( p, p \to q \models q \)); (ii) no (\( p, q \not\models r \)): it is \( \rulename{\forall E} \) at \( c \), then \( \rulename{{\to}E} \); (iii) yes (\( \neg\neg p \models p \)).
  - (d) In @exm-search-with-witnesses, why is the box on premise 3 opened before premise 1 is used? — Premise 1 is a \( \forall \) whose useful term is not yet known, and the box supplies it, \( x_0 \). These are the moves "open the \( \exists E \) boxes early" and "postpone \( \forall E \)".
  - (e) A counter-reading makes the premises of a claim true and its conclusion false. What may you say now, and what will Section 7.2 add? — Now: the claim breaks, and a search for it is abandoned. Section 7.2 states that such a claim has no derivation. (Answered within G10.)
- **B1** (new) `[B1: Derive or break, twelve claims]`: the battery, **in place of** an A2 bank. It is fd1's own selection and order, grouped by the move that does the main work (C small 7; no book's sequent list). Stem: "Derive each claim, with TAUT allowed, or break it by a reading over \( \nZ \) that makes every member of its counterexample set true. The groups say which move to try first; they do not say which claims hold." Twelve claims in four groups, with answers, verdict first.
  - *Open the \( \exists E \) box early:*
    1. \( \exists x\, (P(x) \wedge Q(x)), \ \forall x\, (Q(x) \to R(x)) \vdash \exists x\, (P(x) \wedge R(x)) \). — **Derive.** 3 box \( x_0 \): \( P(x_0) \wedge Q(x_0) \) (asm, for ∃E); 4 \( Q(x_0) \to R(x_0) \) (∀E 2); 5 \( P(x_0) \wedge R(x_0) \) (TAUT 3, 4); 6 \( \exists x\, (P(x) \wedge R(x)) \) (∃I 5); 7 the same (∃E 1, 3–6).
    2. \( \exists x\, R(x, x) \vdash \forall x\, \exists y\, R(x, y) \). — **Breaks.** \( R(x, y) \): "\( x \cdot y = 1 \)". The premise is true (\( 1 \cdot 1 = 1 \)); the conclusion fails at \( x = 0 \).
    3. \( \exists x\, \exists y\, R(x, y) \vdash \exists y\, \exists x\, R(x, y) \). — **Derive.** 2 box \( x_0 \): \( \exists y\, R(x_0, y) \) (asm); 3 box \( y_0 \): \( R(x_0, y_0) \) (asm); 4 \( \exists x\, R(x, y_0) \) (∃I 3); 5 \( \exists y\, \exists x\, R(x, y) \) (∃I 4); 6 the same (∃E 2, 3–5); 7 the same (∃E 1, 2–6).
  - *Postpone \( \forall E \) until the term is known:*
    4. \( \forall x\, \forall y\, (R(x, y) \to R(y, x)), \ \forall x\, R(x, f(x)) \vdash \forall x\, R(f(x), x) \). — **Derive.** 3 box \( x_0 \): \( R(x_0, f(x_0)) \) (∀E 2); 4 \( \forall y\, (R(x_0, y) \to R(y, x_0)) \) (∀E 1); 5 \( R(x_0, f(x_0)) \to R(f(x_0), x_0) \) (∀E 4, at \( f(x_0) \), free for \( y \)); 6 \( R(f(x_0), x_0) \) (→E 5, 3); 7 \( \forall x\, R(f(x), x) \) (∀I 3–6).
    5. \( \forall x\, R(x, f(x)) \vdash \forall x\, R(f(x), x) \). — **Breaks.** \( f(x) = x + 1 \), \( R \) is \( < \): every \( x < x + 1 \), and no \( x + 1 < x \).
  - *The propositional core:*
    6. \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to R(x)) \vdash \forall x\, (\neg R(x) \to \neg P(x)) \). — **Derive.** 3 box \( x_0 \): \( P(x_0) \to Q(x_0) \) (∀E 1); 4 \( Q(x_0) \to R(x_0) \) (∀E 2); 5 \( \neg R(x_0) \to \neg P(x_0) \) (TAUT 3, 4); 6 ∀I 3–5.
    7. \( \forall x\, (P(x) \vee Q(x)), \ \forall x\, \neg P(x) \vdash \forall x\, Q(x) \). — **Derive.** 3 box \( x_0 \): \( P(x_0) \vee Q(x_0) \) (∀E 1); 4 \( \neg P(x_0) \) (∀E 2); 5 \( Q(x_0) \) (TAUT 3, 4); 6 ∀I 3–5.
    8. \( \forall x\, (P(x) \vee Q(x)), \ \neg\forall x\, P(x) \vdash \forall x\, Q(x) \). — **Breaks.** \( P \): "even", \( Q \): "odd". Every integer is even or odd; not every integer is even; and \( 0 \) is not odd.
  - *Move a quantifier, or derive \( \bot \):*
    9. \( \forall x\, (P(x) \to Q(x)) \vdash \exists x\, P(x) \to \exists x\, Q(x) \). — **Derive.** 2 \( \exists x\, P(x) \) (asm, for →I); 3 box \( x_0 \): \( P(x_0) \) (asm, for ∃E); 4 \( P(x_0) \to Q(x_0) \) (∀E 1); 5 \( Q(x_0) \) (→E 4, 3); 6 \( \exists x\, Q(x) \) (∃I 5); 7 the same (∃E 2, 3–6); 8 →I 2–7.
    10. \( \forall x\, (P(x) \to Q(x)) \vdash \exists x\, P(x) \to \forall x\, Q(x) \). — **Breaks.** \( P(x) \): "\( x = 0 \)", \( Q(x) \): "\( x \cdot x = x \)". The premise holds (\( 0 \cdot 0 = 0 \)); \( \exists x\, (x = 0) \) is true and \( \forall x\, (x \cdot x = x) \) is false (\( 2 \cdot 2 = 4 \)).
    11. \( \forall x\, (P(x) \leftrightarrow \neg P(f(x))), \ \forall x\, P(x) \vdash \bot \). — **Derive.** 3 \( P(y) \leftrightarrow \neg P(f(y)) \) (∀E 1, at \( y \)); 4 \( P(y) \) (∀E 2); 5 \( P(f(y)) \) (∀E 2, at \( f(y) \)); 6 \( \bot \) (TAUT 3, 4, 5: \( p \leftrightarrow \neg q, p, q \models \bot \)).
    12. \( \forall x\, \exists y\, R(x, y), \ \forall x\, \forall y\, (R(x, y) \to \neg R(y, x)) \vdash \bot \). — **Breaks.** \( R \) is \( < \): every integer has a larger one, and \( < \) is asymmetric. Both premises are true, and \( \neg\bot \) is true, so the whole counterexample set is true: the list is not shown inconsistent.
  
  Seven derive and five break. Four breaks sit beside a derivable look-alike in the battery (5 beside 4, 8 beside 7, 10 beside 9, 12 beside 11). Claim 2 weakens the premise of the derivable \( \forall x\, R(x, x) \vdash \forall x\, \exists y\, R(x, y) \) of @exm-existential-introduction-derivations (c). The closing sentence of the solution says so, and adds that every break is a counter-reading (Section 7.2). Counted for Time as three exercises (twelve short claims, by the drill rule).
  
  **Marking scheme** (10 points): 4 for the twelve verdicts (⅓ point for each correct one, rounded down); 3 for the seven derivations, each with every closing side condition checked and every TAUT line's skeleton named; 3 for the five readings, each with every premise and the conclusion evaluated. Fatal errors, scoring 0 for the claim: a TAUT line that looks inside a quantifier; a "break" with a premise false.
- **B2** (new) `[B2: Two witnesses in a row]` (scaffolded, STYLE §12.8). Stem: "Premises 1 \( \forall x\, (P(x) \to \exists y\, R(x, y)) \), 2 \( \forall x\, \forall y\, (R(x, y) \to P(y)) \), 3 \( P(c) \); goal \( \exists y\, \exists z\, (R(c, y) \wedge R(y, z)) \)." A partial derivation: lines 1–3; a gap; line 6 \( R(c, y_0) \), the assumption of a box (`\purpose{\Ee}`); a gap; line 16 \( \exists y\, \exists z\, (R(c, y) \wedge R(y, z)) \) as that box's last line; line 17, the same, outside it. "*Name the move, then complete it.*"
  
  *Answer:* the move is "name the witness early", twice, with each \( \forall \) line instantiated only at the terms the witnesses supply. The derivation:
  1–3. premises
  4. \( P(c) \to \exists y\, R(c, y) \) — ∀E 1
  5. \( \exists y\, R(c, y) \) — →E 4, 3
  6. \( R(c, y_0) \) — asm (box of \( y_0 \))
  7. \( \forall y\, (R(c, y) \to P(y)) \) — ∀E 2, at \( c \)
  8. \( R(c, y_0) \to P(y_0) \) — ∀E 7, at \( y_0 \)
  9. \( P(y_0) \) — →E 8, 6
  10. \( P(y_0) \to \exists y\, R(y_0, y) \) — ∀E 1, at \( y_0 \)
  11. \( \exists y\, R(y_0, y) \) — →E 10, 9
  12. \( R(y_0, z_0) \) — asm (box of \( z_0 \))
  13. \( R(c, y_0) \wedge R(y_0, z_0) \) — ∧I 6, 12
  14. \( \exists z\, (R(c, y_0) \wedge R(y_0, z)) \) — ∃I 13
  15. \( \exists y\, \exists z\, (R(c, y) \wedge R(y, z)) \) — ∃I 14, at \( y_0 \), free for \( y \)
  16. the same — ∃E 11, 12–15
  17. the same — ∃E 5, 6–16
  
  At 16, \( z_0 \) is not in line 16, line 11, the premises or the open assumption on line 6. At 17, \( y_0 \) is not in line 17, line 5 or the premises.
  
  **Marking scheme** (10 points): 2 for naming the move; 3 for the two boxes opened as soon as their \( \exists \) lines exist; 3 for the \( \forall E \) lines at \( c \), \( y_0 \) and \( y_0 \), the terms read off the lines in hand; 2 for the two side conditions. Fatal error, scoring 0 for the step: \( \rulename{\exists I} \) on line 15 before line 14, so that the witness \( z_0 \) appears in the box's last line.
- **B3** (new) `[B3: How much TAUT saves]` (technique: LPL). Stem: "(a) Derive \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to \neg P(x)) \vdash \forall x\, \neg P(x) \) twice: once without TAUT, once with exactly one TAUT line. Count the lines. (b) Is the step from \( \forall x\, (P(x) \to Q(x)) \) to \( \forall x\, (\neg Q(x) \to \neg P(x)) \) a TAUT step?"
  
  *Answer:*
  - (a) With TAUT, 6 lines: box \( x_0 \): 3 \( P(x_0) \to Q(x_0) \) (∀E 1); 4 \( Q(x_0) \to \neg P(x_0) \) (∀E 2); 5 \( \neg P(x_0) \) (TAUT 3, 4: \( p \to q, q \to \neg p \models \neg p \)); 6 ∀I 3–5.
  - Without, 10 lines: 3 and 4 as before; 5 \( P(x_0) \) (asm, for ¬I); 6 \( Q(x_0) \) (→E 3, 5); 7 \( \neg P(x_0) \) (→E 4, 6); 8 \( \bot \) (¬E 5, 7); 9 \( \neg P(x_0) \) (¬I 5–8); 10 ∀I 3–9.
  - (b) No: the skeletons are two different atoms. The step is derivable by instantiating, one TAUT line and generalizing, which is @exm-four-tasks-with-quantifiers (b).
  
  **Marking scheme** (10 points): 3 for the TAUT derivation with the skeleton named; 4 for the derivation without TAUT; 1 for the count; 2 for (b) with the reason. Fatal error, scoring 0 for the step: a TAUT line citing \( \forall \) lines directly to reach \( \neg P(x_0) \).
- **C1** (new) `[C1: Some index decides, used later]` (the drinker sentence in index dress; technique: vD, En; 7.1 comes back to it, D9). Stem: "Let \( D(n) \) say '\( a_n > 0 \)' for a sequence \( (a_n) \), over a domain of indices. (a) Derive \( \vdash \exists n\, (D(n) \to \forall m\, D(m)) \), with \( \rulename{LEM} \) on \( \forall m\, D(m) \). (b) Derive it again in two lines, from one TAUT line and one law of Section 6.2. (c) Say in two sentences which index the sentence promises, and why the derivations of (a) and (b) name none."
  
  *Answer (a):*
  1. \( \forall m\, D(m) \vee \neg\forall m\, D(m) \) — LEM
  2. \( \forall m\, D(m) \) — asm (for ∨E)
  3. \( D(n) \) — asm (for →I)
  4. \( \forall m\, D(m) \) — R 2
  5. \( D(n) \to \forall m\, D(m) \) — →I 3–4
  6. \( \exists n\, (D(n) \to \forall m\, D(m)) \) — ∃I 5, at \( n \) itself (as 02:528 does; domains are non-empty)
  7. \( \neg\forall m\, D(m) \) — asm (for ∨E)
  8. \( \exists m\, \neg D(m) \) — QN (a) 7
  9. \( \neg D(m_0) \) — asm (box of \( m_0 \))
  10. \( D(m_0) \to \forall m\, D(m) \) — VI 9
  11. \( \exists n\, (D(n) \to \forall m\, D(m)) \) — ∃I 10, at \( m_0 \)
  12. the same — ∃E 8, 9–11
  13. the same — ∨E 1, 2–6, 7–12
  
  At 12, \( m_0 \) is not in line 12, in line 8, or in the open assumption on line 7.
  
  *(b):*
  1. \( \forall n\, D(n) \to \forall m\, D(m) \) — TAUT (no cited lines). The two prime formulas differ only by renaming, so the skeleton is \( p \to p \).
  2. \( \exists n\, (D(n) \to \forall m\, D(m)) \) — passage law (d), the direction \( \dashv \), used as one line (02:128), with \( \varphi \) the formula \( D(n) \) and \( \psi \) the formula \( \forall m\, D(m) \), in which \( n \) is not free.
  
  *(c):* If every term is positive, any index will do; if not, an index with \( a_n \le 0 \) does, since then the implication is vacuously true. The derivation splits on which case holds without deciding it (LEM in (a), the classical direction of (d) in (b)), so it never names the index.
  
  **Marking scheme** (10 points): 4 for (a): the LEM split, both cases closed, and the side condition at line 12; 3 for (b): the TAUT line justified by renaming, and law (d) with its condition checked; 3 for (c). Fatal errors, scoring 0 for the step: giving \( \forall n\, D(n) \) and \( \forall m\, D(m) \) different atoms and then claiming the TAUT line anyway; \( \rulename{\exists I} \) at \( m_0 \) after its box has closed.
- **C2** (new) `[C2: Every M is P, every M is S, so some S is P?]` (Darapti in integer dress; technique: Co). Stem: "(a) Break \( \forall x\, (M(x) \to P(x)), \ \forall x\, (M(x) \to S(x)) \vdash \exists x\, (S(x) \wedge P(x)) \) by a reading over \( \nN \). (b) Add the premise \( \exists x\, M(x) \) and derive the conclusion. (c) Which line of (b) needs the new premise, and what does Section 5.1's existential import have to do with it?"
  
  *Answer:*
  - (a) **Breaks.** \( M(n) \): "\( n \) is an even prime greater than \( 2 \)" (true of no \( n \)), \( P(n) \): "\( n \) is odd", \( S(n) \): "\( n \) is even". Both premises are vacuously true, and "some even number is odd" is false.
  - (b) 3 \( \exists x\, M(x) \); 4 box \( x_0 \): \( M(x_0) \) (asm, for ∃E); 5 \( M(x_0) \to P(x_0) \) (∀E 1); 6 \( M(x_0) \to S(x_0) \) (∀E 2); 7 \( S(x_0) \wedge P(x_0) \) (TAUT 4, 5, 6); 8 \( \exists x\, (S(x) \wedge P(x)) \) (∃I 7); 9 the same (∃E 3, 4–8).
  - (c) Line 8's witness \( x_0 \) exists only inside the box that premise 3 opens. A "for every" claims no instance, so the old reading of "every \( M \) is \( P \)" as also saying that there are \( M \)s is not the book's reading. With it, the inference was valid; without it, the premise must be added.
  
  **Marking scheme** (10 points): 3 for (a) with all three truth values justified; 4 for (b); 3 for (c). Fatal error, scoring 0 for the step: a "break" whose \( M \) is non-empty.

**Sidecars:**
- `exm-four-tasks-with-quantifiers.py`: (d)'s reading.
- `exm-propositional-core.py`: the reading of the three premises for \( \abs{n} \le 100 \); the skeleton table.
- `exr-first-order-search-b1.py`: the five readings (2 at \( x = 0 \); 5 with \( f(x) = x + 1 \); 8 at \( 0 \); 10 at \( 2 \); 12 asymmetry of \( < \) on \( [-50, 50] \)); the skeleton tables of every TAUT line of 1, 6, 7, 11.
- `exr-first-order-search-c1.py`: the skeleton \( p \to p \); the case split on random finite sequences.
- `exr-first-order-search-c2.py`: \( M \) empty on \( 0..200 \).
- The QCs' and A1's skeleton verdicts go in `exm-propositional-core.py` or a section-level `def-propositional-skeleton.py`.

**Ledger lines** (new):
- `prp-taut-skeleton` (proof): @cor-derivable-iff-valid, @def-derived-rule, @lem-substitution, @def-derivation, @prp-replacement, @lem-weakening-cut (all cited); the claim that substitution preserves each rule instance, argued inline; the use of @lem-weakening-cut (c) for first-order derivations, justified inline by renaming each pasted block's flags to names new to the whole derivation (as "The laws as one line", 6.2).
- The search method: as 01's ledger line 509, moved with it.
- The reading of `exm-search-with-witnesses`: \( 2x + 1 \) odd.
- `exm-propositional-core`: \( n > 1 \Rightarrow n > 0 \), and no integer squares to \( 2 \) (school facts).
- The battery readings (school arithmetic).
- The drinker's ∃I at \( n \) itself: non-empty domains, by the reading of 02:528 (Section 7.1 explains; nothing rests on it).

### 4.4 Section 6.4: Uniformly Continuous Implies Continuous, Rule by Rule (`04-uniform-continuity-rule-by-rule.md`)

**Budget:** main line ≤ 3,600 (now 2,429). Expected about 3,500: R4's ~2,720, plus `exm-not-uniform-derived` (~230), witness functions (~280), `exm-converse-proof-critique` (~210) and one Quick check (~50). Folds ≤ 250: F6.4-a, 204, as in R4. One forward pointer: R4's Looking-ahead box (Chapter 8). The counter-reading sentences of 04:156 and 04:188 (R4) carry "Section 7.2", by the convention of R4 §1 item 11.

**Changes, in the file's order.** R4 §4.10 items 1–8 apply, except where this file says otherwise.

1. **04:3** kept (R4 item 1). "Chapter 5 opened with a question" stays true: Chapter 5's index keeps the frozen keys-and-locks and continuity question (layout §1.3, Chapter 5).
2. **`## Two definitions that differ in one place`**: R4 item 2, with the heading id `{#two-definitions-that-differ-in-one-place}` added (§3.2).
3. **`## The skeleton first`**: R4 item 3, as frozen: the six-line derivation, the paragraph with the line map, and the Quick check on closing the box of \( \delta_0 \). Its heading and its word "skeleton" mean the outline of a derivation, as in Section 3.1. One change: in the six-line display, the assumption of line 2 is printed by the engine ("asm, for ∃E"), since line 5 closes the box; no hand-written purpose is needed. (Section 6.3 always says "propositional skeleton" for its own notion, §4.3 item 6, so the two words do not collide.)
4. **`## The derivation`**: R4 item 4. One change inside the labelled block: the Idea's first sentence (04:37) "Run the search method of Section 6.1." → "Run the search method of Section 6.3." This is a pointer remap only; the method moved (§2.1).
5. **`## Reading dependence off the boxes`**: R4 item 5 (fold F6.4-a).
6. **`## The converse breaks at a side condition`**: R4 item 6 (`exm-converse-fails` verbatim; 04:156 reworded).
7. **`## A function that is continuous and not uniformly continuous`**: R4 item 7: Figure D, `exm-square-not-uniform` verbatim, 04:188 reworded, and the warning 04:190–192 kept. Then the following, new.
8. **`exm-not-uniform-derived`** `[The negation at work, in one derivation]` (new, ~230 words; after the warning 04:192). Lead: "The proof that UC fails for \( x^2 \) established, with numbers, the positive form of the negation from Section 6.2. That form refutes UC by logic alone, and a derivation shows how; one TAUT line (Section 6.3) carries its propositional core." Statement: "Let \( E \) be \( \exists \varepsilon > 0\; \forall \delta > 0\; \exists x \in A\; \exists y \in A\; (\abs{x - y} < \delta \wedge \neg(\abs{f(x) - f(y)} < \varepsilon)) \), the form of @exm-negating-definitions (c) before its last order fact. Derive \( E \vdash \neg\mathrm{UC} \)." Derivation (an `nd` block, with the bounded rules of Section 6.1):
   1. \( E \) — premise
   2. UC — asm (for ¬I)
   3. \( \varepsilon_1 > 0 \) — asm (box of \( \varepsilon_1 \), for ∃E)
   4. \( \forall \delta > 0\; \exists x \in A\; \exists y \in A\; (\abs{x - y} < \delta \wedge \neg(\abs{f(x) - f(y)} < \varepsilon_1)) \) — asm (same box)
   5. \( \exists \delta > 0\; \forall x \in A\; \forall y \in A\; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_1) \) — ∀E 2, 3
   6. \( \delta_1 > 0 \) — asm (box of \( \delta_1 \), for ∃E)
   7. \( \forall x \in A\; \forall y \in A\; (\abs{x - y} < \delta_1 \to \abs{f(x) - f(y)} < \varepsilon_1) \) — asm (same box)
   8. \( \exists x \in A\; \exists y \in A\; (\abs{x - y} < \delta_1 \wedge \neg(\abs{f(x) - f(y)} < \varepsilon_1)) \) — ∀E 4, 6
   9. \( x_1 \in A \) — asm (box of \( x_1 \), for ∃E)
   10. \( \exists y \in A\; (\abs{x_1 - y} < \delta_1 \wedge \neg(\abs{f(x_1) - f(y)} < \varepsilon_1)) \) — asm (same box)
   11. \( y_1 \in A \) — asm (box of \( y_1 \), for ∃E)
   12. \( \abs{x_1 - y_1} < \delta_1 \wedge \neg(\abs{f(x_1) - f(y_1)} < \varepsilon_1) \) — asm (same box)
   13. \( \forall y \in A\; (\abs{x_1 - y} < \delta_1 \to \abs{f(x_1) - f(y)} < \varepsilon_1) \) — ∀E 7, 9
   14. \( \abs{x_1 - y_1} < \delta_1 \to \abs{f(x_1) - f(y_1)} < \varepsilon_1 \) — ∀E 13, 11
   15. \( \bot \) — TAUT 12, 14
   16. \( \bot \) — ∃E 10, 11–15
   17. \( \bot \) — ∃E 8, 9–16
   18. \( \bot \) — ∃E 5, 6–17
   19. \( \bot \) — ∃E 1, 3–18
   20. \( \neg\mathrm{UC} \) — ¬I 2–19
   
   Then three sentences. Line 15's propositional skeleton is \( p \wedge \neg q, \ p \to q \models \bot \), so the line replaces \( \rulename{\wedge E} \) twice, \( \rulename{{\to}E} \) and \( \rulename{\neg E} \), four lines. The witness lines 5, 8 and 10 are opened as soon as they exist, the move of Section 6.3. Every closing line's witness (\( y_1 \), \( x_1 \), \( \delta_1 \), \( \varepsilon_1 \)) is absent from \( \bot \), from the \( \exists \) line it cites, from the premise, and from the assumptions still open. The display stays one block, wide, scrolled by the renderer (R4 §1 item 4's rule for long derivations).
9. **`## Witness functions {#witness-functions}`** (new, ~280 words; technique: vD, En, LPL, Skolem functions and strategies). Text points, in order:
   - "UC says that for every \( \varepsilon > 0 \) some \( \delta > 0 \) works for all points. A rule that picks such a \( \delta \) for each \( \varepsilon \) is a function, \( \delta(\varepsilon) \): a **witness function** for UC." Example: for \( f(x) = x/2 \) on \( \nR \), \( \delta(\varepsilon) = 2\varepsilon \) works, since \( \abs{x/2 - y/2} = \abs{x - y}/2 < \varepsilon \) when \( \abs{x - y} < 2\varepsilon \).
   - "For C the witness may depend on the point too: \( \delta(x, \varepsilon) \). For \( x^2 \), @exm-square-not-uniform gave \( \delta(x, \varepsilon) = \min(1, \varepsilon/(2\abs{x} + 1)) \)."
   - Read off a derivation: "a witness obtained inside the boxes of \( \varepsilon_0 \) and \( x_0 \) may be a function of both, and one obtained inside the box of \( \varepsilon_0 \) alone is a function of \( \varepsilon_0 \) alone. 'May depend' and 'does depend' are exactly the two readings of 'Reading dependence off the boxes'." So: UC holds when some witness function for C ignores its point argument; the derivation of @exm-uniform-implies-continuous turns \( \delta(\varepsilon) \) into \( \delta(x, \varepsilon) \coloneqq \delta(\varepsilon) \).
   - The game, one sentence: "In the game of Section 5.1, a witness function is a strategy for the defender: a rule that answers every challenge, and the defender wins by following it."
   - One sentence, careful: "A formula of this book cannot say 'there is a function': its variables range over numbers. A function symbol can stand for one chosen function, and that is how Sections 5.1 and 6.1 wrote sequences."
   
   **Quick check (new)**, after `exm-converse-proof-critique`: "For which sets \( A \) does the step 'let \( \delta \) be the smallest of the \( \delta_x \)' make sense, and give a positive \( \delta \)?" *Solution:* for finite non-empty \( A \). Finitely many positive numbers have a smallest, and it is positive. For empty \( A \), UC holds outright, since its \( \forall x \in A \) is vacuous.
10. **`exm-converse-proof-critique`** `[A "proof" that continuity gives uniform continuity]` (new, ~210 words; technique: LPL, critique of a purported proof; layout §1.3, 6.4). The "proof", displayed as a quotation: "*Let \( \varepsilon > 0 \). For each \( x \in A \), continuity at \( x \) gives \( \delta_x > 0 \) with \( \abs{f(x) - f(y)} < \varepsilon \) whenever \( y \in A \) and \( \abs{x - y} < \delta_x \). Let \( \delta \) be the smallest of the numbers \( \delta_x \). Then \( \delta > 0 \), and it works at every point, so \( f \) is uniformly continuous.*" Solution:
    - The conclusion is false for \( x^2 \) on \( \nR \) (@exm-square-not-uniform), so some step fails, and it is the third sentence.
    - Infinitely many positive numbers need not have a smallest, and they may come arbitrarily close to \( 0 \). With \( \varepsilon = 1 \), the largest \( \delta \) that works for \( x^2 \) at \( x \ge 0 \) is \( \sqrt{x^2 + 1} - x \) (Figure D), which is \( 1/(\sqrt{x^2 + 1} + x) < 1/(2x) \) and so smaller than any positive number once \( x \) is large.
    - In the rules: each \( \delta_x \) is the witness of an \( \rulename{\exists E} \) box inside the box of \( x_0 \), and "the smallest of them" would be a line about all the witnesses at once. That is the line whose two routes @exm-converse-fails found blocked by side conditions.
    - For finite \( A = \{a_1, \dots, a_k\} \) the proof is right: \( k \) uses of \( \rulename{\exists E} \) give \( \delta_1, \dots, \delta_k \) (Section 5.6, "Two witnesses", repeated), and \( \min(\delta_1, \dots, \delta_k) > 0 \) works.
    
    One closing sentence: "The search stalls at the same side condition that stopped @exm-converse-fails; that \( x^2 \) is a counter-reading for the converse is the evidence that no other route exists (Section 7.2)."
11. **Looking ahead:** R4's box ("Chapter 8 shows how the eleven lines of this derivation become the three sentences of a written proof, at several levels of detail."). It is the last block before `## Exercises`.
12. **Quick checks:** the swapped \( \exists \delta\, \forall \varepsilon \) (kept), closing the box of \( \delta_0 \) (R4), the boxes around \( \delta_0 \) (kept), and finite \( A \) (new). Four in about 3,500 words, one per about 875.
13. **Warnings:** "Depending on ε" is a claim (kept).

**Folds:** F6.4-a, R4's ("Choosing \( \delta \) before the point"). No new fold.

**Exercises.**

- **A1** (key proof), **B1**, **B2** (proof ordering), **B3**, **C1** (faded, scaffolded), **C2**, **C3** (exit check): kept.
- **A2: Drill** (`exr-uniform-continuity-rule-by-rule-a2`), twelve parts, in §12.8's ramp. Answers:
  - (a) Line 1 is UC and line 2 is \( 1 > 0 \). Write the line that the bounded \( \rulename{\forall E} \) 1, 2 gives. — \( \exists \delta > 0\; \forall x \in A\; \forall y \in A\; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < 1) \).
  - (b) Lines \( \delta_1 > 0 \) and \( \forall y \in A\; (\abs{x_0 - y} < \delta_1 \to \abs{f(x_0) - f(y)} < \varepsilon_0) \). Write the line that the bounded \( \rulename{\exists I} \) with witness \( \delta_1 \) gives. — \( \exists \delta > 0\; \forall y \in A\; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0) \).
  - (c) In @exm-not-uniform-derived, line 13 is the bounded \( \rulename{\forall E} \) from line 7 at \( x_1 \). Which second line must be available? — Line 9, \( x_1 \in A \).
  - (d) In the six-line derivation of "The skeleton first", give the rule and the cited lines of lines 3 and 4. — Line 3: ∀E 2, at \( x_0 \). Line 4: ∃I 3, with witness \( \delta_0 \).
  - (e) In @exm-converse-fails, give the rule and the cited lines of line 10. — The bounded ∀I, 3–9.
  - (f) Is this correct? Inside the boxes of \( \varepsilon_0 \) and \( x_0 \), a witness \( \delta_0 \) obtained from C at \( x_0 \) is used in \( \rulename{\exists I} \) to write \( \exists \delta > 0\; \forall x \in A\; \forall y \in A\; (\dots) \). — No. That \( \rulename{\exists I} \) needs the line \( \forall x \in A\; \forall y \in A\; (\abs{x - y} < \delta_0 \to \dots) \), and that line needs \( \rulename{\forall I} \) over \( x_0 \) while an open assumption about \( \delta_0 \) mentions \( x_0 \): the side condition of \( \rulename{\forall I} \).
  - (g) A witness function for UC of \( f(x) = 5x \) on \( \nR \)? — \( \delta(\varepsilon) = \varepsilon/5 \): \( \abs{5x - 5y} = 5\abs{x - y} < \varepsilon \).
  - (h) For \( x^2 \), the witness function \( \min(1, \varepsilon/(2\abs{x} + 1)) \) at \( x = 3 \), \( \varepsilon = 1 \)? — \( \min(1, 1/7) = 1/7 \).
  - (i) For \( x^2 \) and \( \varepsilon = 1 \), the largest \( \delta \) that works at \( x = 4 \), by Figure D's formula? — \( \sqrt{17} - 4 \approx 0.123 \).
  - (j) Negate C, "continuous at every point of \( A \)", into positive form. — \( \exists x \in A\; \exists \varepsilon > 0\; \forall \delta > 0\; \exists y \in A\; (\abs{x - y} < \delta \wedge \abs{f(x) - f(y)} \ge \varepsilon) \).
  - (k) Which quantifier of C must move, and past which, to turn C into UC? — \( \forall x \in A \) moves to the right, past \( \exists \delta > 0 \). Passing \( \forall \varepsilon > 0 \) is harmless (two \( \forall \)'s exchange); passing \( \exists \delta \) is the swap that fails.
  - (l) Derive \( \forall \varepsilon > 0\; \exists \delta > 0\; (\delta \le \varepsilon) \) with the bounded rules, given the arith line "\( \varepsilon_0 \le \varepsilon_0 \)". — 1 \( \varepsilon_0 > 0 \) (asm, box of \( \varepsilon_0 \)); 2 \( \varepsilon_0 \le \varepsilon_0 \) (arith); 3 \( \exists \delta > 0\; (\delta \le \varepsilon_0) \) (∃I 1, 2, witness \( \varepsilon_0 \)); 4 \( \forall \varepsilon > 0\; \exists \delta > 0\; (\delta \le \varepsilon) \) (∀I 1–3). The witness function is \( \delta(\varepsilon) = \varepsilon \).
  
  None of the parts repeats a main-line answer: (h) and (i) use values the text does not compute, and (c) cites the new example, not A1's line 7.
- **B4** (new) `[B4: Witness functions]` (technique: vD, En). Stem: "For each function, give a witness function for uniform continuity on the set named, say what it depends on, and prove that it works. (a) \( f(x) = \abs{x} \) on \( \nR \). (b) \( f(x) = x^2 \) on \( [0, 3] \). (c) Say in one sentence why the formula of (b) gives no witness function on all of \( \nR \)."
  
  *Answer:*
  - (a) \( \delta(\varepsilon) = \varepsilon \). By the triangle inequality (@exm-triangle-inequality-cases), \( \abs{x} \le \abs{x - y} + \abs{y} \) and \( \abs{y} \le \abs{y - x} + \abs{x} \), so \( \abs{\abs{x} - \abs{y}} \le \abs{x - y} < \varepsilon \).
  - (b) \( \delta(\varepsilon) = \varepsilon/6 \). For \( x, y \in [0, 3] \), \( \abs{x + y} \le 6 \), so \( \abs{x^2 - y^2} = \abs{x - y}\,\abs{x + y} \le 6\abs{x - y} < \varepsilon \). It depends on \( \varepsilon \) and on the bound \( 3 \) of the set, and on no point.
  - (c) On \( \nR \), \( \abs{x + y} \) has no bound, so no constant can replace the \( 6 \), and @exm-square-not-uniform shows that no witness function at all exists there.
  
  **Marking scheme** (10 points): 3 for (a), with the two triangle inequalities; 4 for (b): 1 for the bound \( \abs{x + y} \le 6 \), 2 for the chain, 1 for the dependence; 3 for (c). Fatal error, scoring 0 for the step: a "witness" that mentions \( x \) or \( y \).
- **R items** (new; `### R. Review` after C, the chapter's last section; STYLE §11.5). The problem texts name no source chapter, and the solutions do.
  - **R1** `[R1]` (method from Chapter 5): "Derive \( \forall x\, (f(x) = x) \vdash \forall x\, (f(f(x)) = x) \)." *Answer:* box \( x_0 \): 2 \( f(x_0) = x_0 \) (∀E 1, at \( x_0 \)); 3 \( f(f(x_0)) = f(x_0) \) (∀E 1, at the compound term \( f(x_0) \)); 4 \( f(f(x_0)) = x_0 \) (@prp-equality-symmetric-transitive, transitivity, 3, 2); 5 \( \forall x\, (f(f(x)) = x) \) (∀I 2–4). The solution names Section 5.3 (instantiate at the term you need, here a compound one) and Section 5.7. About 10 minutes.
  - **R2** `[R2]` (method from Chapters 2–3; a propositional inconsistency task): "Show that the list \( P \leftrightarrow \neg Q, \ Q \leftrightarrow \neg R, \ R \leftrightarrow \neg P \) is inconsistent." *Answer:* derive \( \bot \), without \( \rulename{RAA} \), in 19 lines:
    1–3. the premises
    4. \( P \) — asm (for ¬I)
    5. \( \neg Q \) — ↔E 1, 4
    6. \( R \) — asm (for ¬I)
    7. \( \neg P \) — ↔E 3, 6
    8. \( \bot \) — ¬E 4, 7
    9. \( \neg R \) — ¬I 6–8
    10. \( Q \) — ↔E 2, 9
    11. \( \bot \) — ¬E 10, 5
    12. \( \neg P \) — ¬I 4–11
    13. \( R \) — ↔E 3, 12
    14. \( Q \) — asm (for ¬I)
    15. \( \neg R \) — ↔E 2, 14
    16. \( \bot \) — ¬E 13, 15
    17. \( \neg Q \) — ¬I 14–16
    18. \( P \) — ↔E 1, 17
    19. \( \bot \) — ¬E 18, 12
    
    The solution names Section 3.2 (inconsistency: derive \( \bot \)) and Section 2.4 (↔E). It adds that a TAUT line (Section 4.8) would do it in one step, since the skeleton list has no satisfying row: an odd cycle of "is the negation of" is impossible. About 20 minutes.
  - **R3** `[R3]` (spiral from Part I: a propositional law and its quantifier version): "You have derived \( P \wedge (Q \vee R) \vdash (P \wedge Q) \vee (P \wedge R) \). Derive \( \exists x\, (P(x) \wedge (Q(x) \vee R(x))) \vdash \exists x\, (P(x) \wedge Q(x)) \vee \exists x\, (P(x) \wedge R(x)) \), and say which line is the propositional law." *Answer:*
    1. premise
    2. \( P(x_0) \wedge (Q(x_0) \vee R(x_0)) \) — asm (box of \( x_0 \), for ∃E)
    3. \( (P(x_0) \wedge Q(x_0)) \vee (P(x_0) \wedge R(x_0)) \) — @prp-distributivity used as a derived rule (@def-derived-rule), or TAUT 2
    4. \( P(x_0) \wedge Q(x_0) \) — asm (for ∨E)
    5. \( \exists x\, (P(x) \wedge Q(x)) \) — ∃I 4
    6. the goal — ∨I 5
    7. \( P(x_0) \wedge R(x_0) \) — asm (for ∨E)
    8. \( \exists x\, (P(x) \wedge R(x)) \) — ∃I 7
    9. the goal — ∨I 8
    10. the goal — ∨E 3, 4–6, 7–9
    11. the goal — ∃E 1, 2–10
    
    At 11, \( x_0 \) is not in the goal, in line 1, or in the premise. Line 3 is the propositional law, and the quantifier steps frame it (the propositional core, Section 6.3). The solution names Section 1.6 (@prp-distributivity). About 15 minutes.
  
  R4 (optional) is not set. Three items meet STYLE §11.5's minimum, and the chapter's other review is its battery.

**Sidecars:**
- `exm-converse-proof-critique.py`: \( \sqrt{x^2 + 1} - x = 1/(\sqrt{x^2 + 1} + x) < 1/(2x) \) for \( x \) in \( (0, 1000] \) on a grid, and the minimum of finitely many positive values.
- `exr-uniform-continuity-rule-by-rule-a2.py`: (g), (h) \( = 1/7 \), (i) \( = \sqrt{17} - 4 = 0.1231 \).
- `exr-uniform-continuity-rule-by-rule-b4.py`: (a) on a grid; (b) \( \abs{x^2 - y^2} \le 6\abs{x - y} \) on \( [0, 3]^2 \).
- `exm-square-not-uniform.py` gains R4's Figure D values.
- `exm-not-uniform-derived` quotes no numbers; its TAUT line is checked by `check_fitch.py`.

**Ledger lines** (new):
- `exm-not-uniform-derived`: the bounded rules (cited); TAUT on the skeleton (@prp-taut-skeleton, cited).
- Witness functions: \( \abs{x/2 - y/2} = \abs{x - y}/2 \) (school algebra); "a formula cannot say there is a function" (a remark; nothing rests on it).
- The critique: Figure D's formula (R4's sidecar) and the identity \( \sqrt{x^2 + 1} - x = 1/(\sqrt{x^2 + 1} + x) \) (school algebra).
- R1: @prp-equality-symmetric-transitive. R3: @prp-distributivity.

---

## 5. Budgets and the Time line

| § | Main line now (before Exercises) | Main-line budget | Expected | Folds now | Fold budget |
|---|---|---|---|---|---|
| index | 187 (placeholder) | ≤ 1,000 | ~960 | — | — |
| 6.1 | 3,753 | ≤ 4,200 | ~3,680 | 0 | ≤ 850 (~750) |
| 6.2 | 4,496 | ≤ 4,600 | ~4,560 | 0 | ≤ 1,450 (~1,340) |
| 6.3 | — (new) | ≤ 4,500 | ~4,250 | — | ≤ 450 (~380) |
| 6.4 | 2,429 | ≤ 3,600 | ~3,500 | 0 | ≤ 250 (~204) |
| sections | 10,678 | ≤ 16,900 | ~15,990 | 0 | ≤ 3,000 (~2,670) |

Every section stays at or under STYLE's 5,000 main-line cap and under the layout's budgets (§1.3). The whole-file advisory count of `check_structure.py`, exercises included, will be over 5,000 in 6.2, 6.3 and 6.4; it is advisory.

**Exercises after the deepening:**
- **4 A1 items** (6.1, 6.2 and 6.4 kept; 6.3 new);
- **3 A2 banks of 12, 36 parts**: in 6.1 and 6.2, R4's eight parts each plus four new; in 6.4, twelve new. That is 16 parts from R4 (never drafted) and 20 written here, counted for Time as 9 exercises;
- **6.3's battery B1**, twelve claims, counted as 3 exercises;
- **16 B items**: 8 kept (6.1 B1, B2; 6.2 B1–B3; 6.4 B1–B3) and 8 new (6.1 B3, B4; 6.2 B4, B5; 6.3 B1, B2, B3; 6.4 B4). 6.1 B3 (twenty sentences) counts as 5 exercises and the battery as 3, so B counts as 22 exercise-equivalents;
- **11 C items**: 7 kept (6.1 C1, C2; 6.2 C1, C2; 6.4 C1–C3) and 4 new (6.1 C3; 6.2 C3; 6.3 C1, C2). The exit checks are 6.2 C2 and 6.4 C3;
- **3 R items** (6.4 R1–R3, new).

**Time** (B1 formula: 15 minutes per 400 main-line words; A1 25 minutes; a drill bank as one exercise per four parts at 30 minutes; one B 30 minutes and one non-Challenge C 40 minutes per section; index pages not counted, as in layout §3).
- **Core track:**
  - reading ~15,990 words ≈ 10.0 h;
  - 6.1, 6.2 and 6.4: A1 25 + A2 3 × 30 + B 30 + C 40 = 185 minutes each, 555 minutes in all (in 6.2 and 6.4 the C is the exit check);
  - 6.3: A1 25 + B 30 + C 40 = 95 minutes, with no bank (layout §3: about 1.6 h for a battery section);
  - exercises 650 minutes ≈ 10.8 h.
  
  Total **≈ 20.8 h** (layout: about 21 h). Rounded to the nearest 5 hours (STYLE §2), this is **"About 20 hours on the core track."**
- **Full track:**
  - reading ~15,990 + ~2,670 folded ≈ 18,660 words ≈ 11.7 h;
  - A1: 4 × 25 = 100 minutes;
  - A2: 9 × 30 = 270 minutes;
  - battery: 3 × 30 = 90 minutes;
  - the other 15 B items, with 6.1 B3 at 5: 19 exercise-equivalents × 30 = 570 minutes;
  - C: 11 × 40 = 440 minutes;
  - R: 3 × 40 = 120 minutes;
  - exercises 1,590 minutes ≈ 26.5 h.
  
  Total **≈ 38.2 h** (layout: about 36 h). This is **"about 40 hours for everything."** The full track is above the layout's 36 h because R4's banks grew from 8 to 12 parts, 6.4 gained a bank, and B and C items were added. Core stays on target.
- The drafter of `index.md` recomputes both lines from the delivered text (`check_structure.py --words`) and the delivered counts, by the same rule, and does not shade either down (STYLE §11.9).

---

## 6. Pointers, promises, and edits outside the chapter (new numbering)

### 6.1 Forward pointers from Chapter 6

Each section has at most one forward pointer, in its Looking-ahead box (STYLE §12.1). Counter-readings carry "(Section 7.2)" by R4 §1 item 11's convention, and plain pointers inside solutions are kept where R4 kept them.

| Where | Text (new numbering) | Paid by | STATUS |
|---|---|---|---|
| 6.1 Looking ahead (new) | "… Chapter 7's optional last section says what that costs." | 7.6 (the induction schema against the second-order axiom; layout §1.3) | **new row**: F1.8 §01 → F1.6 §06 |
| 6.2 Looking ahead (R4) | "Chapter 8 says what is at stake … and catalogues the wrong negations …" | 8.7's paragraph "Not every, and some not", `exr-excluded-middle-b3`; 8.6's `exm-not-allowed-catalogue` (N11) | row F1.8 §02, §04 → F1.5 (already paid; the text moves into the box) |
| 6.3 Looking ahead (new) | "Chapter 7 gives counter-readings an exact form, the counter-model, and states that a counter-model rules out every derivation." | 7.2: `#from-counter-models-to-non-derivability` and its statement (C1) | **new row**: F1.8 §03 → F1.6 §02 |
| 6.4 Looking ahead (R4) | "Chapter 8 shows how the eleven lines … become the three sentences of a written proof, at several levels of detail." | 8.3 `def-levels-of-proof`, `exm-uniform-four-levels` | row F1.8 §02, §04 → F1.5 (already paid) |
| counter-readings "(Section 7.2)" in 6.1 C3, 6.2 02:348, B4, 6.3 (main line, B1, C2), 6.4 04:156, 04:188, `exm-converse-proof-critique` | — | 7.2's statement, and 7.2's retroactive paragraph (G5), which certifies the counter-readings of 5.3–6.4 one by one | row F1.8 §01, §02, §04 → F1.6 is **extended to §03** |
| 02:528 "(Section 7.1)" (non-empty domains; now inside fold F6.2-d), and C1(a) line 6 of 6.3 (the same step) | — | 7.1 `#why-domains-are-non-empty` | the same row (non-empty domains, §02), extended to §03 |
| index "Where this goes" | AN1.1 (school facts; QN (a) in the Archimedean proof); AN1.5, AN1.6 (continuity, uniform continuity); *Sets, Relations, and Cardinality*, Chapter 3 (axiom of choice) | AN1.1 `thm-naturals-unbounded`, `cor-archimedean-epsilon`, `prp-absolute-value-rules`; AN1.5, AN1.6; fd2 `ax-choice` (F2.3 §03) | rows F1.8 §01, §02 → AN1.1 and F1.8 §04 → AN1.5, AN1.6: the **source becomes "F1.8 index"**; **new row**: F1.8 index → F2.3 (`ax-choice`) |
| 6.3 C1 title ", used later" | — | **7.1 checks the drinker sentence semantically** (layout §1.3, 7.1) and cites `exr-first-order-search-c1` by label; no proof rests on it | **new row**: F1.8 §03 → F1.6 §01 (for the ch07 S1) |
| 6.1 01:299; `exr-translation-c1`'s solution; 02:666; 02:669 | in-chapter pointers (to 6.4, to 6.1) | in-chapter | — |

### 6.2 Promises this chapter pays

| STATUS row (atlas ids) | What | Paid by |
|---|---|---|
| F1.4 §01–§08, index → F1.8 (row 83) | translation, the search method extended, quantifier laws, dependence | already paid by `prp-bounded-quantifier-rules`, `exm-translate-limit`, `prp-quantifier-negation`, `prp-bounded-quantifier-negation`, `prp-quantifier-distribution`, `prp-quantifier-passage`, `exm-uniform-implies-continuous`. **Update:** "the search method extended" is now paid in F1.8 §03 (the moved algorithm), not §01 |
| F1.2 §05 → F1.8 (row 87) | ε = x/2, "the hypothesis applies to it" | `prp-arbitrarily-close-equal` (unchanged) |
| F2.1 → F1.8 (rows 105, 106) | bounded rules; quantifier negation, unbounded and bounded; negated implication | `prp-bounded-quantifier-rules`, `prp-quantifier-negation`, `prp-bounded-quantifier-negation`, `prp-negated-implication` (unchanged, verbatim) |
| F1.4 §02 (5.2, 02:396): renaming inside a formula is "a convention of this book" | — (not a STATUS row today) | 6.2's renaming sentence after `prp-replacement` makes it a provable equivalence. `ch05-deepen` may add one clause to 02:396 pointing to Section 6.2 (seam, not a promise) |
| F1.3 §08 (4.8) → F1.8 (expected from `ch04-deepen`) | `def-rule-taut` extended to quantified formulas | `def-propositional-skeleton`, `prp-taut-skeleton` (6.3). Recorded for the ch04 S1; 4.8's box may name Chapter 6 |
| F1.4 §03–§07 (5.3–5.7) → F1.8: "Section 6.1 collects the steps" | ch05 05:262, 06:588, 07:256 | 6.3's "The search method, extended". The pointers must read "Section 6.3" (§6.3 below) |

### 6.3 Edits needed outside Chapter 6 (for the coordinator, `ch05-deepen` and `ch08-deepen`)

| File:line | Now | Becomes | Why |
|---|---|---|---|
| `ch05…/05-existential-introduction.md:262` | "… and Section 6.1 collects them." | "… and Section 6.3 collects them." | the method moved |
| `ch05…/06-existential-elimination.md:588` | "… Section 6.1 collects them with the steps of Section 3.1." | "Section 6.3" | same |
| `ch05…/07-equality-and-uniqueness.md:256` | "Section 6.1 collects all the steps into one method." | "Section 6.3" | same |
| `ch08…/05-writing-proofs.md:14` | "(Section 3.1, extended in Section 6.1)" | "(Section 3.1, extended in Section 6.3)" | same |
| `ch05…/index.md` (R4 §4.0 items 4 and 7) | the first-reading path and "Where this goes" name 6.1–6.4 | `ch05-deepen` drops the 6.x items; Chapter 6's index carries them (§2.1) | one index per chapter |
| `ch05…/05-existential-introduction.md:244` | "Section 6.1 folds lines 3 and 4 into a single bounded step." | unchanged (still true) | — |
| `ch08…/02-quantifier-rhetoric.md:7, 13, 57, 68, 88`; `03-levels-of-abbreviation.md:26, 269, 275, 462`; `index.md:7` | cite 6.1's 16-line and 6.4's 11-line derivations and 6.2's RAA box | unchanged: those derivations stay verbatim with their line numbers | binding rule 2 |
| fd2 ch03 07:94 | names "Negating a definition, mechanically" | unchanged: heading kept | — |

The D2 sweep is done, so these four one-word pointer edits go to the ch05/ch08 drafters, or to the S8 seam pass if those chapters are drafted first.

### 6.4 Seams recorded for later S1 units (not promises)

- **7.2** cites `def-propositional-skeleton` for "instance of a tautology (skeleton sense)" in its hierarchy (C small 4).
- **7.2's retroactive paragraph** names Chapter 6's counter-readings: 6.1 C3(b), 02:348's two, 6.2 B4 (b), (d), (f), 6.3's (d) of `exm-four-tasks-with-quantifiers` and B1's five breaks, C2(a), and 6.4's \( x^2 \) (04:188).
- **7.4** may cite 6.3's first-order inconsistency (a list is inconsistent when ⊥ is derivable) before `def-inconsistent-theory`.
- **8.3** cites `prp-taut-skeleton` for silent steps (layout §1.3, 8.3).
- **8.2**'s "the limit" row may cite 6.1's mixed stage.
- **3.3**'s library is the propositional twin of 6.3's.

---

## 7. What later chapters hold, so that Chapter 6 does not pre-empt them

| Chapter (new number) | Holds | So Chapter 6 does not |
|---|---|---|
| 7 Models and Theories | structures, assignments, satisfaction, first-order ⊨ (7.1); counter-models, the statement that a counter-model rules out every derivation, the side-condition table, the retroactive paragraph, the hierarchy (7.2); first-order soundness and `cor-counter-model` (7.3, optional); theories and `def-inconsistent-theory` (7.4); definability, isomorphism (7.5); completeness, compactness, Löwenheim–Skolem (7.6, optional) | write ⊨ between first-order formulas, say "model", "structure" or "satisfies" in their technical senses, or draw a structure as an arrow diagram; assert non-derivability except as a forward claim citing 7.2 (G10); prove or cite first-order soundness; define a theory; state compactness or completeness for first-order logic (the 6.1 box says only "what that costs") |
| 8 From Derivations to Mathematical Prose | the dictionaries (8.1, 8.2), levels of proof (8.3), the catalogue (N1)–(N14) (8.6), excluded middle and constructive readings (8.7), Kripke models (8.8) | cite the catalogue by number (D3); discuss constructive meaning beyond 02:118's sentence and C1(c) of 6.3; write the "we define" or "the limit" rows (5.8, 8.2) |
| *Sets, Relations, and Cardinality*; *Number Systems*; *Analysis on the Real Line* | sets as objects, the axiom of choice (F2.3); ℕ and ℝ built in set theory; continuity and uniform continuity (AN1.5, AN1.6) | quantify over sets or functions (the witness-function subsection says so); prove the Archimedean property |

---

## 8. What stays exactly as it is

Everything R4 §7 lists for 4.8–4.10:
- the three ways to break the limit definition (01:9–11);
- the prose versions of the long derivations with line references (01:303, 04:81);
- the negation procedure (02:592–604);
- `exm-negating-definitions`;
- the "Why the condition on ψ" paragraph;
- the uniform-continuity derivation and its side-condition list;
- the converse's search and its two blocked lines;
- the \( x^2 \) proof;
- the warning "Depending on ε is a claim".

Also: every kept exercise and its solution (6.1 A1, B1, B2, C1 (frozen), C2; 6.2 A1, B1–B3, C1, C2; 6.4 A1, B1–B3, C1–C3), except the pointer remaps of B2's and C1's solutions in 6.2 (§4.2, Exercises); the dependency-ledger comments of the three files, which move with their text, plus new lines; and every Try-it-first (02:25 with its pointer reworded; 04:113).

---

## 9. S2a: every new claim, derivation and answer that needs blueprint verification

**Changed wording of existing blocks (check that every later citation still holds):**
1. 02:25 (*Try it first* of `prp-quantifier-negation`): the method of 3.1 with the quantifier steps of 5.3–5.6 suffices to start the search on (a); no pointer to 6.3 serves as a reason.
2. 04:37 (Idea of `exm-uniform-implies-continuous`): "Section 6.3" names the method the Idea runs; ch08 copies the derivation, not the Idea.
3. 01:3 rewritten (item 1 of §4.1): the three promised items are each delivered in 6.1.
4. 01:307–333 moved to 6.3, with 01:333's reworded clause: the algorithm and its two paragraphs make no claim that depends on their position (they cite 3.1, 5.3–5.7 and `exm-translate-limit`, all earlier).
5. 02:606 split: F6.2-b keeps exactly the condition-survival sentences, and the cut sentences are covered by `prp-replacement`'s cases 1–3. 02:676's and the Quick check 02:580–586's new pointers (to `prp-replacement`), and B2's and C1's solution remaps: each application they describe meets `prp-replacement`'s hypothesis, by F6.2-b or F6.2-c.
6. The distribution and passage proofs folded verbatim (F6.2-d): no main-line proof or Idea cites a line of them except "Why the condition on ψ" (02:578) and 02:528's internal remark, both of which point into the fold; the statements' meta-claims (02:309, 02:365) stay true of the folded derivations.
7. R4's outlines in 6.1 and 6.4: every box has its closing line written and justified, so the engine infers each purpose and no hand-written one is needed (D1).

**New main-line claims and examples:**
8. 6.1 mixed stage: the three stages say the same thing; the formula is the translation of the sentence.
9. 6.1 `exm-translation-traps`, each row:
   - (a) \( A = \{3\} \): the sentence and the right formula false, the wrong formula true at \( x = y = 3 \); the trap is not in 5.1 (05/01:169 and 05/01:361 are the \( \forall \)-with-\( \wedge \) slip, which this file no longer repeats);
   - (b) \( A = \{1\} \), \( B = \{-1\} \): the sentence false and the wrong formula true;
   - (c) wrong false at \( 2 \), right true;
   - (d) the wrong formula's last \( n \) is free, and at \( n = 1 \) it is false while the sentence is true;
   - (e) at \( A = \emptyset \) the right formula is true and the wrong one false.
   
   Also: "after 'if' or 'not', 'any' means 'some'" is offered as a reading rule, with no claim beyond the examples; and the traps do not duplicate 5.1's translations as delivered (checked against 05/01:167–175 and 05/01:361 in S2 round 1; recheck once `ch05-deepen` is drafted).
10. 6.1 infinitely many and eventually: both formulas; \( (-1)^n \) values; the Quick check's formula for "only finitely many \( n \)".
11. 6.1 translation error: \( \neg(7 \in \{1, 2\}) \vdash \exists x\, (x \in A \to x > 5) \) for \( A = \{1, 2\} \) by VI and ∃I at \( 7 \) (both legal); "some element of \( \{1, 2\} \) exceeds 5" is false. 6.1 Not allowed: each entry breaks the clause named, and no entry is in fact legal.
12. `prp-replacement`: the statement (with the closure hypothesis) and the proof route of F6.2-a, in particular:
    - case 3 when \( x \) is free in \( \varphi \) and bound in \( \chi \);
    - the order of instantiation of the closure;
    - the claim that substitution of fresh flags passes \( \forall x \);
    - that the connective steps of cases 1–2 are derivable with the rules of Chapters 1–2 for every connective (↔ included);
    - that the "in particular" follows by ∀E at the variables themselves;
    - and that no truth table or completeness is used (C2, G6).
13. F6.2-b's new opening sentence: "a law proved for every formula meeting its condition holds for the instances at fresh names, and \( k \) flagged boxes give its closure", for every law of 6.2 including the bounded ones with \( z > a \).
14. The renaming sentence: front renamings (5.4 (b), 5.6 `#existential-renaming`) plus `prp-replacement` give renaming anywhere as a provable equivalence; the closure hypothesis holds for the front renamings.
15. 6.2 square:
    - the diagonals derived as stated (A/O by `prp-bounded-quantifier-negation` with bound \( S(x) \), as 02:680 argues; E/I with `prp-double-negation` under ∃ by `prp-replacement`);
    - contraries and subcontraries need some \( S \);
    - `exm-square-of-opposition`'s eight truth values (multiples of \( 4 \) and perfect squares; the empty \( S \), odd multiples of \( 4 \));
    - the caption's sentence;
    - `\oppositionsquare` labels all four relations, and the caption says which need import;
    - the Quick check (E's negation is I, true at \( 16 \));
    - originality: no sentence of the square example, its Quick check, 6.2 A2 (i) or 6.1 B3 is an Aristotelian form over Prime/Even or Square/Even (LPL 9.13, 9.25 avoided).
16. 6.2 twin table: each propositional twin is the reading over \( \{a, b\} \) of its law; each is valid (truth-table check done while writing: the distribution (c) twin valid, its converse invalid at \( \varphi_a, \psi_b \) true, others false; passage (a) and (b) twins valid both ways); the cited labels prove the twins stated, and the distribution (c) row's direct derivation (∨E, then ∧E, ∨I, ∧I in each case) is correct; the RAA-direction sentence (QN (a) and De Morgan (d) are the classical directions; `prp-de-morgan` (d) is the part Section 2.5 derives with RAA).
17. 6.2 prenex: `exm-prenex-conversion`'s two steps (law (b) with \( x \) not free in \( \exists y\, Q(y) \); law (e) under \( \forall x \), \( y \) not free in \( P(x) \)), and the second step's left-to-right direction is (e)'s classical one; alternation counts (\( \forall\exists \); \( \forall\exists\forall \); the Quick check: two each for UC and C); the remark about finite tables is illustrative only.
18. 6.3: the moved algorithm unchanged; the three moves; the flowchart (every branch uses only rules and moves of the book; no claim of completeness).
19. `exm-search-with-witnesses`: the 13-line derivation, the snapshots, the side conditions at 12 and 13, the reading over \( \nZ \) (all three premises true), and the Quick check.
20. `def-propositional-skeleton`:
    - well defined by recursion on first-order formulas (5.2's formation rules; bounded quantifiers are abbreviations beginning with a quantifier); \( \bot \), atomic under (Fm1) (05/02:91), is excluded from the prime formulas, so the clauses \( \mathrm{sk}(\bot) = \bot \) and \( \mathrm{sk}(\pi) \) never apply to one formula;
    - "alike up to renaming" is an equivalence on prime formulas, so the assignment exists;
    - the example skeleton \( p \to (q \vee \neg p) \);
    - the distinction from 3.1's "skeleton".
21. `prp-taut-skeleton` and F6.3-a:
    - step 1: substitution into a propositional derivation preserves every rule instance of Chapters 1–2, including RAA, LEM and ⊥E, and their citations and boxes;
    - extra atoms go to ⊥;
    - \( D \) has no flagged boxes;
    - the result is a first-order derivation by @def-derivation as extended in 5.4;
    - step 2: alike primes provably equivalent with closure (item 14), and `lem-weakening-cut` chains the three sequents, after each pasted block's flags are renamed to names new to the whole derivation (the renaming derivations always contain flagged boxes), so that no ∀I or ∃E side condition of a pasted block is broken; the extension of `lem-weakening-cut` (c) to first-order derivations is argued inline by this renaming, not cited;
    - the second sentence of the statement (no shared atoms ⇒ only Chapters 1–2 rules) is exactly step 1;
    - the licence covers a TAUT line inside open boxes, with pasted flags renamed;
    - `check_fitch.py`'s skeleton agrees with the definition, including alike-up-to-renaming, and keeps \( \bot \) as \( \bot \) (not an atom), so the TAUT lines that conclude \( \bot \) (`exm-four-tasks-with-quantifiers` (c) line 5, the inconsistency Quick check, B1 claim 11, `exm-not-uniform-derived` line 15) check.
22. 6.3 TAUT examples and non-examples: \( \neg(p \wedge q), q \models \neg p \); \( p \to r, \neg r \models \neg p \); \( \forall x\forall y R \) against \( \forall y \forall x R \) gives two atoms (not renamings of each other); \( \forall x P(x) \) against \( P(c) \); \( x = x \) one atom. The Quick check's three verdicts; Not allowed: TAUT's five entries.
23. `exm-propositional-core`:
    - the 6-line derivation;
    - the skeleton \( p \to (q \vee r), \neg q \models p \to r \);
    - the reading over \( \nZ \) (premise 1 true since \( n > 1 \) gives \( n > 0 \); no integer squares to 2; neither premise is checked by the conclusion, so the reading is not circular);
    - the Quick check's nine-line expansion.
24. `exm-four-tasks-with-quantifiers`:
    - (a) the 5 lines, with ∃I at \( x \) itself, sound as `prp-forall-implies-exists` is;
    - (b) both TAUT skeletons;
    - (c) the 6 lines and the skeleton \( p \wedge \neg q, p \to q \models \bot \);
    - (d) the 7-line derivation and the reading (P even, Q positive, 0);
    - "Section 3.2's definition reads the same for first-order formulas" (`def-inconsistent-set`'s wording as drafted by `ch03-finding-derivations` must allow this; S2 checks once 3.2's blueprint exists).
25. Test the subgoal: the sentence is a forward claim citing 7.2 and 4.7 (G9, G10), with no rule-by-rule soundness reason on the main line (C1); the Quick check's reading makes every available line true (premise, line 2 \( \varepsilon_0 > 0 \), the instance at \( \varepsilon_0 \), the \( N_0 \) and \( n_0 \) box lines, \( n_0 \ge N_0 \), \( 0.75 < 1 \)) and the subgoal false (\( 1.5 \ge 1 \)); the inconsistency Quick check (three lines).
26. 6.3 library: every row's sequent is the one its label proves (with \( \varphi \) where the label has letters, as 02:319 argues for distribution); no new licence is claimed.
27. `exm-not-uniform-derived`:
    - the 20-line derivation: every bounded rule's citations, every closing side condition;
    - line 15's skeleton;
    - "four lines replaced";
    - \( E \) is the form of `exm-negating-definitions` (c) before the order fact.
28. Witness functions: \( \delta(\varepsilon) = 2\varepsilon \) for \( x/2 \); the \( x^2 \) formula quoted from `exm-square-not-uniform`; the reading of "may"/"does"; the strategy sentence; the sentence on functions in formulas.
29. `exm-converse-proof-critique`:
    - the third sentence fails;
    - \( \sqrt{x^2 + 1} - x = 1/(\sqrt{x^2 + 1} + x) < 1/(2x) \) for \( x > 0 \);
    - the finite case by \( k \) uses of ∃E and the minimum;
    - the claim about the search;
    - the Quick check (finite non-empty \( A \); empty \( A \) trivial).
30. Index: the Summary's claims (each a labelled result or worked example of the chapter); "What you need" labels exist (`def-rule-taut` from `ch04-deepen`); "Where this goes" against STATUS rows 79 and 80 and fd2 `ax-choice`; the mirror box's claims against layout §1.2.

**New and changed exercise answers:**
31. `exr-translation-a2`: all twelve parts, the four new ((e), (g), (h), (i)) in particular; (h)'s values on \( \{-1, 1\} \).
32. `exr-translation-b3`: the twenty formulas (each against its sentence); 19 true in \( \nN \) (the argument from \( x = xkl \)); 20 false at \( 2 \) and every power of \( 2 \); 16 false at \( (0, 1) \); 10 and 11 both true. No sentence repeats the traps (6 is about \( 9 \), not trap (c)).
33. `exr-translation-b4`: (a)–(e); (f)'s sets \( \{1\}, \{2\}, \emptyset \).
34. `exr-translation-c3`: the 13-line derivation (arith lines 5, 7, 9 true for \( M_0, N_0 \in \nN \); side conditions at 12 and 13); (b)'s parity reading.
35. `exr-quantifier-laws-a2`: R4's (a)–(h) (R4 S2a item 31 stands); (i) A false at \( 1 \); (j) the two expansions and the truth values; (k) law (b); (l) at \( 2 \).
36. `exr-quantifier-laws-b4`: six verdicts; the derivations of (a) (12 lines with ↔I closing two boxes), (c) (10 lines, RAA at 8), (e); the readings of (b), (d), (f) over \( \nZ \).
37. `exr-quantifier-laws-b5`: line 3 is the only illegal line; the break at \( c = 0 \); the repaired 8-line derivation and its side condition; the conclusion is derivable.
38. `exr-quantifier-laws-c3`: (a)'s 5 lines; (b)'s nesting and the side condition of its ∀I, with the pasted flags renamed; (c).
39. `exr-first-order-search-a1`: five answers; (b)'s claim that the two prime formulas are not renamings of each other and that \( \bot \) is still derivable.
40. **Binding rule 5 audit:**
    - `exr-first-order-search-b1`: seven derivations (1, 3, 4, 6, 7, 9, 11) and five readings (2, 5, 8, 10, 12), each truth value checked;
    - every TAUT skeleton verified by truth table while writing this blueprint: claims 1, 6, 7, 11, the propositional core, B3, the inconsistency example, C2(b), and R2's cycle (no satisfying row);
    - no claim duplicates a sequent stated in Chapter 5 or 6 (checked against the grep list of ch05's \( \vdash \)-statements of 2026-10-13; claim 2 deliberately weakens `exm-existential-introduction-derivations` (c));
    - claim 1 against 6.2 B5's sequent: different conclusions;
    - no claim matches a sequent list of any of the twelve books (C small 7).
41. `exr-first-order-search-b2`: the 17-line derivation, the instantiation terms, and the side conditions at 16 and 17.
42. `exr-first-order-search-b3`: 6 and 10 lines; (b).
43. `exr-first-order-search-c1`: the 13-line derivation (LEM, QN (a) as one line, VI, ∃I at \( n \) and at \( m_0 \)); (b)'s TAUT line (\( \forall n\, D(n) \) and \( \forall m\, D(m) \) are renamings, so \( p \to p \)) and passage (d)'s condition; (c)'s two cases.
44. `exr-first-order-search-c2`: (a)'s reading with \( M \) empty; (b)'s 9 lines; (c).
45. `exr-uniform-continuity-rule-by-rule-a2`: twelve answers, especially (f), (h) \( = 1/7 \), (i) \( = \sqrt{17} - 4 \), (j), (l).
46. `exr-uniform-continuity-rule-by-rule-b4`: (a) by two triangle inequalities; (b) \( \abs{x + y} \le 6 \) on \( [0, 3] \); (c).
47. R1: the 5-line derivation (∀E at the compound term \( f(x_0) \) is free for \( x \)). R2: the 19-line derivation without RAA (each ↔E in the direction stated). R3: the 11-line derivation. Each takes at most 20 minutes (STYLE §11.5). The problem texts name no source.
48. Marking schemes of every new B and C item: points sum to 10; each fatal error is a real error.

**Originality (for S2's comparison with the twelve books):** every example, drill, exercise and figure above is written for this book. The drinker sentence and Darapti carry fd1's own dress: an index of a sequence; even primes greater than \( 2 \). The battery of 6.3 B1 and the library of 6.3 are fd1's own selection and order, grouped by fd1's named moves.

---

## 10. Notes for S3 and S4

- **Drafters:** three, as in R4: (i) 6.1 (with the move of its search subsection to (ii)); (ii) the new 6.3, which takes 01:307–333 verbatim from (i)'s file; (iii) 6.2 and 6.4. The index is written last, against the delivered sections (DRAFTING). (i) and (ii) coordinate the move in one commit, so the method is never in both files or in neither.
- **Order:** 6.3 cites `prp-replacement` (6.2) in F6.3-a, and 6.4 cites `prp-taut-skeleton` (6.3). Each drafter greps the delivered earlier file before citing.
- **Depends on `ch04-deepen`:** `def-rule-taut` (4.8) must exist before 6.3 is built. If 4.8 is drafted later, 6.3's TAUT paragraph keeps its citation, and S4 runs after both.
- **Checking derivations:** every new derivation passes `tools/check_fitch.py`, including its TAUT lines, which the tool checks on skeletons. Every snapshot carries `% schema (partial derivations: …)` and `\purpose{…}` on each assumption whose box no justified line closes yet. 6.2 B5's flawed derivation, as printed in the stem, carries the expect-invalid marker.
- **Figures:** each is a raw LaTeX block with its `tikzpicture` written out in full: the square in 6.2, the flowchart in 6.3, Figure D in 6.4. They use only `latex/book-diagrams.sty`'s styles, plus plain TikZ for Figure D's graph, with no colour and no white fill. S4 checks both the HTML (SVG) and the PDF renderings.
- **STATUS:** the F1.8 row's text ("§03 is not yet written, so §04 displays as 6.3 … 'The search method, extended' stays in §01 until §03 exists") is rewritten once 03 exists. That is the coordinator's job at S4.
- **STYLE:** §12.13.4's means of breaking still reads "a counter-model (from the counter-model section of the models chapter)". Chapter 6 breaks by counter-readings (D5), which is consistent, since 7.2 is that section. No STYLE change is needed.

## S2 replies

**Round 1.** Every finding was applied; findings raised by both reviewers are answered together.

1. *`def-propositional-skeleton`: \( \bot \) is atomic under (Fm1), so "prime" clashed with \( \mathrm{sk}(\bot) = \bot \).* Applied: a prime formula is now "atomic and not \( \bot \), or begins with a quantifier, bounded or not". S2a item 20 records the exclusion, and item 21 now checks that `check_fitch.py` keeps \( \bot \) as \( \bot \), naming the four TAUT lines that conclude \( \bot \).
2. *Test the subgoal: "no rule leads from true lines to a false one" is false line by line, and it is soundness.* Applied: the rule-by-rule reason is gone. The sentence now reads "Section 7.2 states that such a reading rules out every derivation of it from those lines", a forward claim (G10, C1). S2a item 25 updated.
3. *`exm-converse-proof-critique`, third bullet, claimed that no legal step can write the line.* Applied: "That is the line whose two routes @exm-converse-fails found blocked by side conditions." The claim about all derivations is left to the closing sentence, which cites 7.2.
4. *F6.3-a step 2 pastes first-order derivations with @lem-weakening-cut, which was proved for flag-free derivations.* Applied: step 2 now renames each pasted block's flags to names new to the whole derivation, as "The laws as one line" (6.2) argues, so @lem-weakening-cut (c) holds by the same pasting. The renaming is added to S2a item 21 and to the ledger line of `prp-taut-skeleton`, as an inline argument rather than a citation.
5. *C1 (c) stem claimed something about every derivation.* Applied: "…and why the derivations of (a) and (b) name none." The answer already argues only about those two.
6. *B1 marking scheme did not add up to 10 (two findings).* Applied: "4 for the twelve verdicts (⅓ point for each correct one, rounded down)"; 4 + 3 + 3 = 10.
7. *6.1 B3 closing sentence on 10 and 11 (two findings).* Applied: "10 restricts \( x \) to primes and 11 does not; both are true, and in \( \nN \) each follows from the other."
8. *Quick check after `exm-search-with-witnesses`: lines 1, 2 and 6 also mention \( R \).* Applied: "line 7, the only line that asserts \( R \) of particular terms, mentions \( x_0 \) and \( y_0 \)."
9. *`exm-propositional-core`'s reading was circular (two findings).* Applied, with neither suggested key as given: both make premise 2, \( \forall x\, \neg Q(x) \), false (\( n = 0 \) and odd integers exist). The reading keeps \( Q(n) \): "\( n^2 = 2 \)" and takes \( P(n) \): "\( n > 1 \)", \( R(n) \): "\( n > 0 \)". Both premises are checked without the conclusion, which is "every integer greater than \( 1 \) is positive". The citation of `thm-square-even-implies-even` is dropped from the text, the ledger line and S2a item 23.
10. *Twin table, distribution (c) row cited @prp-distributivity, which is \( \wedge \) over \( \vee \) (two findings).* Applied: the cell now names a direct derivation (∨E on the premise; ∧E, ∨I and ∧I in each case), and says that @prp-distributivity is not cited. S2a item 16 checks that derivation.
11. *`prp-replacement`'s lead sentence and meaning line stated a syntactic hypothesis in semantic words.* Applied: "provided the equivalence is derivable for every choice of its free variables, that is, its closure is derivable; every law of this section is", and the lead sentence likewise.
12. *Figure 6.3-F node (a): ∧I opens no box, ↔I opens two.* Applied: "set up its introduction rule\\(for \( \forall \): a fresh flag)".
13. *§6.1 pointer row listed 6.3 B2 among the counter-readings.* Applied: "6.3 (main line, B1, C2)".
14. *Trap (a) repeated 5.1 (05/01:169, 05/01:361).* Applied by replacement, so "five more" stays true: trap (a) is now "\( A \) has at least two elements", wrongly \( \exists x\, \exists y\, (x \in A \wedge y \in A) \), separated by \( A = \{3\} \) (two letters may name one element). Neither 5.1 nor 5.8 shows this slip (grep: 5.8 writes \( x \ne y \) but never warns about omitting it). The other tempting replacement, "not every" against "every … not", is 6.1 A2 (h) and the contrary paragraph of 6.2, so it was not used. S2a item 9 now records the check against the delivered 5.1.
15. *Originality risk against LPL 9.13 and 9.25 (square example, its Quick check, B3 item 2, 6.2 A2 (i)).* Applied: the square example is now over multiples of \( 4 \) and perfect squares (A false at \( 8 \), E false at \( 4 \), I true at \( 4 \), O true at \( 8 \); the empty \( S \) is "an odd multiple of \( 4 \)"), and its Quick check negates "no multiple of \( 4 \) is a perfect square" (I, true at \( 16 \)). B3 item 2 is now "Some prime divides \( 9 \)", \( \exists x\, (\mathrm{Prime}(x) \wedge x \mid 9) \). 6.2 A2 (i) now uses "multiple of \( 3 \)" and "odd" and negates the O form (A, false at \( 6 \)); it is still not the main line's corner. S2a item 15 gains an originality check.
16. *Quick check on the wrong subgoal made only one available line true.* Applied: the solution now gives a whole reading, \( a_n = L \) except \( a_{n_0} = L + 0.75 \), \( N_0 = n_0 \), \( \varepsilon_0 = 1 \), and checks the premise, the instance at \( \varepsilon_0 \), the box lines and \( n_0 \ge N_0 \) before the subgoal. The question asks for "a sequence and numbers that make every available line true". S2a item 25 updated.
17. *§6.2 promise row named F1.3 §07 for Section 4.8.* Applied: F1.3 §08, matching `ch04-deepen`.

