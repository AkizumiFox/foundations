<!-- hand-written -->
# Revision blueprint: F1.1 Connectives and Derivations (fd1 Chapter 1), pilot R2

**What this is.** A **delta** blueprint (stage S1) for revising the released Chapter 1 of *Logic and Proof* so that a first-year reader gets in more easily. It is complete on its own: a drafter executes it with this file, the current `fd1/src/ch01-connectives-and-derivations/`, the original blueprint `fd1/authoring/blueprints/ch01.md` (for anything this file does not change), `authoring/STYLE.md`, `DRAFTING.md` and `NOTATION.md`. All line numbers below are of the **current** files (commit `83a2b9f`), written `01:164` for `01-statements-and-connectives.md` line 164, and so on.

**Inputs.** The novice-reader report on Chapter 1, the corpus and classic-texts comparisons, and the fd1 revision plan (chapter list, conventions, Chapter 1 changes). Reference books were used for teaching technique only (counterexample-first, goal analysis, Givens/Goal tables, drill volume, the promise reading of →). **Every example, drill and exercise below is the book's own**; none is taken from any book. The S2 review rule of `ch01.md` (no Huth & Ryan sequent lists come back) still binds.

**Binding rules for this revision.**
1. **No label is lost.** Every label now in the chapter survives, in this chapter, except uncited `exr-` labels, which this file renames or retires explicitly (§3). Every label that is cited anywhere (fd1 Ch2–5, fd2, fd3, an1) keeps its name.
2. **Reviewed content of cited results does not change**, except where this file says so and lists the item for S2a (§8). Moving a passage into a Second-reading fold verbatim is not a change.
3. **Forward references** to unseen theorems by `@ref` are removed from the whole chapter (list in §1.12). Plain-text pointers ("Chapter 4 gives 'for every' its rules") are allowed only where this file keeps them; no forward pointer is ever used as a *reason*.
4. **Depends on R0 and R1.** The relaxed ∧I citation order (§1.10) lands only with the `tools/check_fitch.py` change of step R0. The fold, drill-bank, Challenge and Looking-ahead markup (§1.1–§1.8) follows STYLE as amended by step R1; if R1 chose a different markup for any of them, use R1's markup and keep the content given here.

---

## 1. The volume-wide conventions, as applied to Chapter 1

1. **Second-reading fold.** `::: {.second-reading title="…"}` … `:::`, folded on the web, printed with a marker in the PDF. It is **not** `.optional`: a label inside a fold may be cited later. It holds edge cases, minimal-change nonexamples, long justifications and meta-proofs whose statement stays on the main line. Every fold this chapter gets is listed by current file:line in its section's plan; nothing else goes into a fold.
2. **Looking ahead.** At most one per section, as the last thing before `## Exercises`: `::: {.remark}` whose first words are `**Looking ahead.**`, one or two sentences, no `@ref`. The soundness promise is made **once**, in 1.2.
3. **Effort in proportion to difficulty.** ∧I, ∧E and ∨I get **three bullets** each in place of the clause-by-clause reading. →E keeps a short reading (four bullets). →I and ∨E keep the full clause-by-clause reading and are introduced by the sentence *"This rule has conditions that matter; read each one."*
4. **Snapshots.** Every worked derivation of **four or more lines** in the main text shows two or three partial derivations in its Idea (goal at the bottom, the gap as a `\have[\ ][0] {} {\vdots}` row, given lines at the top, every line carrying the number it has at the end), in the existing style of 03:173-190. Snapshot blocks carry the `% schema (partial derivations: …)` marker, as 03:174 does. Two- and three-line derivations get none.
5. **Givens/Goal table.** A two-column Markdown table, `| Givens | Goal |`, introduced in 1.2's "Two directions of reasoning". The Givens column lists what is in hand (premises, derived lines, open assumptions); the Goal column what is still needed. A goal-directed step replaces a goal by subgoals; a premise-directed step adds to the Givens; →I moves the hypothesis into the Givens and makes the conclusion the goal; each ∨E case adds its assumption to the Givens. A search is finished when every goal is among the Givens. Used in 1.2, 1.4 and 1.6 at the places named below.
6. **Rule card.** Each section's "What the rules sound like" table becomes a **cumulative rule card**: every rule so far, one row each, columns `Rule | Shape | You write | Lean`. *Shape* is one line, e.g. "\( \varphi \), \( \psi \) ⟹ \( \varphi \wedge \psi \)" or "box \( \varphi \) … \( \psi \) ⟹ \( \varphi \to \psi \)". The Lean column and its one-line explanations stay (ch04 03:239, 04:420 and 07:419 rely on them). 1.6 ends with the whole chapter's card as a one-page reference.
7. **Quick-check density.** About one Quick check per 800–1,000 main-line words, mostly cheap ("is this line legal? which rule? which lines?"). The new checks are given per section.
8. **Drill bank.** Each section gets a second A exercise, `exr-<slug>-a2`, titled `[A2: Drills]`: lettered short items (justify a line, find the illegal line, 2–6-line derivations, try to break a form) in order of difficulty, with **one folded solution** answering every item in one or two lines. A1 stays the comprehension exercise of STYLE §6. All drill items are written out with answers below.
9. **Scaffolded B items and Challenges.** A scaffolded B item gives the premises and the last line, with the gap marked and the lines numbered as at the end, and asks *"Name the move, then complete it."* A C item that is a meta-proof or hard mathematics is titled `[Cn: Challenge: …]` and is never the section's core C.
10. **∧I in either order.** The two cited lines of ∧I may be listed in either order; the written line decides which conjunct is which. →E keeps its fixed order (implication first). Remove 03:78-84, the error paragraph 03:365 and old B3(d). Coordinated with R0 (`check_fitch.py`) and NOTATION.md.
11. **Letters.** One sentence with the analogy, once, in 1.2 (text in §4.2). Greek letters are introduced once, there (delete the second introduction at 03:17). Γ is pronounced "capital gamma" and called a list.
12. **Forward `@ref`s removed** (each replaced as the section plan says): 01:127 `def-formula`, `thm-unique-readability`; 01:255 `thm-soundness`; 01:259 `cor-derivable-iff-valid`; 01:261 `cor-refuting-row`; 02:352 `thm-soundness`; 02:438 `ax-induction`; 02:468 `thm-soundness`; 03:88 `thm-soundness`; 03:303 `thm-completeness`; 03:533 `thm-strong-induction`, `thm-soundness`; 04:76 `thm-soundness`; 04:82 `cor-refuting-row`; 05:67, 05:205 `thm-soundness`; 06:69, 06:100, 06:204 `thm-soundness`; 07:625 `thm-soundness`; index.md:5 `thm-soundness`, `thm-completeness`.
13. **Parentheses.** Chapter 1 always writes the parentheses in nested →. The right-grouping convention survives as a one-line remark in 1.1 (ch03 04:125 relies on "Chapter 1 fixed a convention (→ groups to the right)").
14. **≤ and ≥** are written out as disjunctions in derivations: stated once, in a box, in 1.5 (§4.5).

---

## 2. Section map

| New | Title (the `#` line) | File | From | Kind |
|---|---|---|---|---|
| index | Connectives and Derivations | `index.md` | index.md | rewritten |
| 1.1 | Statements, Arguments and How to Break One | `01-statements-and-connectives.md` | 01 | rewritten |
| 1.2 | Derivations, Starting with And | `02-derivations.md` | 02 + 03 merged | rewritten |
| 1.3 | Using an Implication: Modus Ponens | `04-using-an-implication.md` | 04 | edited |
| 1.4 | Proving an Implication: the Rule of the Box | `05-proving-an-implication.md` | 05 | rewritten |
| 1.5 | Or, Introduced | `06-disjunction-introduction.md` | 06 | edited |
| 1.6 | Using Or: Proof by Cases | `07-disjunction-and-cases.md` | 07 | edited |

`03-conjunction.md` is **deleted**; its content goes into `02-derivations.md`. File names 04–07 are kept (the numbering gap is harmless: the engine orders by file name, and keeping the names keeps every ledger `file:` key and every review's file:line evidence readable). The atlas entry F1.1 and the chapter title do not change.

---

## 3. Labels

### 3.1 Every label now in the chapter

Citation counts are `@label` / `@fd1:label` hits in fd1 Ch2–5, fd2, fd3 and an1 (grep of 2026-10-12, excluding Chapter 1 itself). An `exr-` label was renamed or retired only after that grep found no citation of it anywhere, and an internal ch01 citation (07:813 cites C1) froze `exr-disjunction-and-cases-c1`.

| Label | Now | New | Status | Cited outside ch01 |
|---|---|---|---|---|
| `def-statement` | 01:27 | 1.1 | kept | — |
| `exm-statements` | 01:35 | 1.1 | kept | 3 |
| `def-main-connective` | 01:131 | 1.1 | kept | 5 |
| `def-sequent` | 01:198 | 1.2 | kept; **moves** to 1.2, right after `def-derivable` (wording in §4.2, S2a) | 1 |
| `exr-statements-and-connectives-a1` | 01:282 | 1.1 | kept; parts (e), (f) reworded | — |
| `exr-statements-and-connectives-b1` | 01:311 | 1.1 | kept | — |
| `exr-statements-and-connectives-b2` | 01:334 | 1.1 | kept; part (d) dropped; parse trees in the solution | — |
| `exr-statements-and-connectives-c1` | 01:363 | 1.1 | **frozen** (cited ch02 04:7, ch03 07:673): label, tier, content unchanged | 2 |
| `exr-statements-and-connectives-c2` | 01:392 | 1.1 | **renamed → `exr-statements-and-connectives-b3`** (moved to B; content unchanged) | — |
| `def-rule-schema` | 02:36 | 1.2 | kept; "given lines and boxes" → "given lines"; "possibly none" kept (S2a) | 10 |
| `def-box-free-derivation` | 02:92 | 1.2 | kept, unchanged | — |
| `exm-chaining-derivation` | 02:115 | 1.2 | kept; old part (b) dropped, old (c) becomes (b) | — |
| `def-derivable` | 02:191 | 1.2 | kept; block unchanged; remarks trimmed, "Section 1.5" → "Section 1.4" | 14 |
| `exm-derivations` | 02:220 | 1.2 (fold) | kept; parts (a)–(c) unchanged except "Section 1.5" → "Section 1.4" (part (a) is cited by ch02 03:128, 04:225) | 2 |
| `exm-not-a-derivation` | 02:266 | 1.2 (fold) | kept, unchanged | — |
| `exr-derivations-a1` | 02:316 | 1.2 | kept; content merged (§4.2) | — |
| `exr-derivations-b1` | 02:357 | 1.2 | old item (Sh, then chain) **dropped**; the label now carries old `exr-conjunction-b1` | — |
| `exr-derivations-b2` | 02:380 | 1.2 | old item (Tr/Sh instances) **dropped** (Tr parts → A2 drills); the label now carries old `exr-conjunction-b2` | — |
| `exr-derivations-b3` | 02:413 | 1.2 | old item (steps of a chain) **dropped** ((a) → drill A2(d)); the label now carries a new scaffolded item | — |
| `exr-derivations-c1` | 02:443 | 1.2 | kept; `@thm-soundness` removed from the solution | — |
| `exr-derivations-c2` | 02:471 | 1.2 | kept; part (c) marked Challenge | — |
| `def-rules-conjunction` | 03:21 | 1.2 | kept; one sentence added (∧I either order) (S2a) | 3 |
| `exm-conjunction-warm-ups` | 03:106 | 1.2 | kept; old (b) \( P \vdash P \wedge P \) → edge-case fold; old (c) becomes (b) | — |
| `prp-and-commutes` | 03:164 | 1.2 | kept; statement and proof unchanged | 5 |
| `prp-and-associative` | 03:216 | 1.2 | kept; statement and proof unchanged | 1 |
| `exm-product-in-unit-interval` | 03:309 | 1.2 | kept, unchanged | — |
| `exr-conjunction-a1` | 03:382 | — | **retired**: parts (a), (b), (d), (e) → `exr-derivations-a1`; (c) → drill A2(f) | — |
| `exr-conjunction-b1` | 03:420 | 1.2 | **renamed → `exr-derivations-b1`** (content unchanged) | — |
| `exr-conjunction-b2` | 03:446 | 1.2 | **renamed → `exr-derivations-b2`** (content unchanged) | — |
| `exr-conjunction-b3` | 03:464 | — | **retired**: (a), (b), (c), (e) → drill A2(g); (d) dropped | — |
| `exr-conjunction-c1` | 03:504 | 1.2 | **renamed → `exr-derivations-c4`**, Challenge; Ch3 `@ref`s removed | — |
| `exr-conjunction-c2` | 03:546 | 1.2 | **renamed → `exr-derivations-c3`**; part (d) marked Challenge | — |
| `exm-wason-selection` | 04:9 | 1.3 | kept; solution reworded (§4.3) | 1 |
| `def-rule-implication-elimination` | 04:39 | 1.3 | kept; block unchanged; the "Why this rule" example is replaced | 2 |
| `exm-implication-chains` | 04:118 | 1.3 | kept | — |
| `exr-using-an-implication-a1` … `-c2` | 04:319–482 | 1.3 | all six kept | — |
| `def-rules-implication` | 05:29 | 1.4 | kept, unchanged | 12 |
| `prp-implication-transitive` | 05:75 | 1.4 | kept; statement and proof unchanged | 3 |
| `def-derivation` | 05:157 | 1.4 | kept, block unchanged (now "the official version") | 69 |
| `exm-illegal-citation` | 05:254 | 1.4 | kept | — |
| `exm-first-boxes` | 05:317 | 1.4 | kept; (b)'s Idea shortened | — |
| `prp-curry` | 05:394 | 1.4 | kept; statement and proofs unchanged | 7 |
| `exr-proving-an-implication-a1` | 05:502 | 1.4 | kept; part (c) changed (no "context") | — |
| `exr-proving-an-implication-b1` | 05:548 | 1.4 | old item → drill A2(e); the label now carries a new scaffolded item | — |
| `exr-proving-an-implication-b2` | 05:576 | 1.4 | **frozen** (cited ch03 03:28, 06:125): unchanged | 2 |
| `exr-proving-an-implication-b3`, `-b4`, `-c1`, `-c2`, `-c3` | 05:628–853 | 1.4 | kept | — |
| `def-rule-disjunction-introduction` | 06:25 | 1.5 | kept, block unchanged | 3 |
| `exm-disjunction-introduction-derivations` | 06:110 | 1.5 | kept | — |
| `exm-or-hypothesis-split` | 06:214 | 1.5 | kept | 2 |
| `exm-product-zero` | 06:293 | 1.5 | kept | — |
| `exr-disjunction-introduction-a1` … `-c2` | 06:352–521 | 1.5 | all six kept | — |
| `def-rules-disjunction` | 07:25 | 1.6 | kept, unchanged | 13 |
| `exm-disjunction-first-derivations` | 07:85 | 1.6 | kept | 13 |
| `exm-cases-on-hypothesis` | 07:166 | 1.6 | kept | 3 |
| `prp-distributivity` | 07:207 | 1.6 | kept; statement and proofs unchanged | 11 |
| `exm-disjunction-regroup` | 07:279 | 1.6 | kept; outline figure added before it | 3 |
| `exm-abs-at-least-x` | 07:349 | 1.6 | kept, unchanged | 3 |
| `exm-abs-product-cases` | 07:394 | 1.6 | kept, unchanged | 2 |
| `exm-triangle-inequality-cases` | 07:420 | 1.6 | kept, unchanged (an1 01:196, 01:261 need its two splits as they are) | 10 |
| `exr-disjunction-and-cases-a1` | 07:589 | 1.6 | kept; (d) solution reworded | — |
| `exr-disjunction-and-cases-b1`, `-b2`, `-b3` | 07:634–692 | 1.6 | kept | — |
| `exr-disjunction-and-cases-c1` | 07:729 | 1.6 | **frozen** (cited by C2 at 07:813): unchanged; title becomes `[C1: Challenge: The reverse triangle inequality]` | (internal) |
| `exr-disjunction-and-cases-c2`, `-c3`, `-c4`, `-r1`, `-r2`, `-r3` | 07:785–989 | 1.6 | kept | — |

### 3.2 New labels

`exr-statements-and-connectives-a2`, `-b4`; `exr-derivations-a2` (and the reused `-b3`); `exr-using-an-implication-a2`, `-b4`; `exr-proving-an-implication-a2` (and the reused `-b1`); `exr-disjunction-introduction-a2`; `exr-disjunction-and-cases-a2`, `-b4`. No new `def-`, `prp-` or `exm-` label. Grep `fd1/src` before creating each (DRAFTING rule).

### 3.3 Bookkeeping the renames force (coordinator, S4)

- `fd1/authoring/ledger/ch01.yaml`: re-key `exr-conjunction-b1/-b2/-c1/-c2` to their new labels; retire the entries of `exr-conjunction-a1`, `exr-conjunction-b3`, `exr-statements-and-connectives-c2` (re-keyed to `-b3`), and the old contents of `exr-derivations-b1/-b2/-b3` and `exr-proving-an-implication-b1` (their label strings now carry different items: new entries, not carried verdicts). Every `file:` of a merged 03 item becomes `02-derivations.md`. Retire nothing else.
- `fd1/verify/ch01/`: delete `exr-derivations-b1.py` (Sh); rewrite `exr-derivations-b2.py`, `-b3.py` for the drills they became (or fold them into a new `exr-derivations-a2.py`); update `exm-chaining-derivation.py` (two parts), `def-rule-implication-elimination.py` (the 42 example replaces √2), `def-sequent.py` (its n = 2 witness now sits in 1.1 after `def-main-connective`: rename the script after the block the drafter ledgers it under). New sidecars are listed per section.
- `NOTATION.md`: the ∧I order rule (R0/R1); the \( \Gamma_k \) row (146) points at F1.3 §05 for "context", which leaves Chapter 1 (§4.4).

---

## 4. Per-section plans

Budgets: **main line** = prose words by `tools/check_structure.py`'s `prose_words`, counted over the section file **outside `.second-reading` folds and before `## Exercises`**. Exercises are budgeted separately (drill answers one or two lines each). Totals in §5.

### 4.0 `index.md` (rewritten)

- Story paragraph: keep 1 (index.md:3), with "the answer arrives in Section 1.5" → "Section 1.4". Paragraph 2 (index.md:5): cut to two sentences, no `@ref`: "This chapter builds the calculus that answers it: a proof is a chain in which every line is a premise, an assumption, or one application of a rule. It gives the rules for 'and', 'implies' and 'or', one at a time; Chapter 2 adds 'not', 'iff' and proof by contradiction."
- **What you need:** keep index.md:7 as it is (four lines).
- **Time:** recomputed from the delivered text (§5). Target: "About 30 hours on the core track …; about 45 hours for everything."
- **Roadmap:** six bullets, one sentence each: 1.1 statements, connectives, the promise reading of "if … then", and how to break a bad argument form; 1.2 the format of a derivation and the first two rules, ∧I and ∧E; 1.3 →E; 1.4 →I, the box and the scope rule, and Argument B diagnosed; 1.5 ∨I and postponing a disjunctive goal; 1.6 ∨E, the laws of "or", case proofs about absolute values, and the chapter's rule card.
- **Named moves:** the heading stays (`check_structure.py` requires it), with one sentence: "The chapter's six moves are collected at the end of Section 1.6, beside the rules that make them." The list itself (index.md:21-28) moves to 1.6.

### 4.0a Preface (`fd1/src/index.md`), one paragraph added

The 1.1 drafter adds, after "How to read it", a paragraph **Why rules before truth tables**, adapted from 01:259 with no `@ref`: many logic books begin with truth tables, where the row "a false hypothesis makes \( P \to Q \) true" must be accepted as a convention; this book starts from the rules, Chapter 2 shows that row coming out of how proofs work, and Chapter 3 brings the tables and proves that rules and tables agree. Add one sentence to "How to read it" on Second-reading folds: they hold edge cases and longer justifications, can be left closed on a first reading, and are not optional (later proofs may use them).

### 4.1 Section 1.1: Statements, Arguments and How to Break One (`01-statements-and-connectives.md`)

**Budget:** main line ≤ 4,000 words (now 4,147 before the exercises); folds ≤ 250. Forward pointers kept: the convention box (Chapter 4) and the promise table's caption (Chapter 3). No Looking-ahead box.

**New order of material.**
1. Opening frame (01:3), cut to two sentences.
2. `## Two arguments about squares`: 01:5-19 kept. In 01:7 replace "(The word 'some' has rules of its own, which come in Chapter 4; here we use it as school algebra does.) Here is a fact about integers that Chapter 2 proves properly, once the rules for 'not' are in place." by "Here is a fact about integers." (The pointer to Chapter 2 now sits in 1.4's Looking ahead.)
3. `## Statements`: def-statement, exm-statements, 01:64 kept (its last sentence becomes "… are the **quantifiers**."). 01:66 is **replaced by the convention box** below. Remark 01:68-70 → fold F1.1-b.
4. `## The connectives`: 01:74 kept. 01:76: "We write \( P, Q, R, S \) for statements…" kept; the sentence "In the last column … \( P \) is '\( x > 0 \)', and \( Q \) is '\( x < 1 \)'" becomes "In the last column, \( x \) is a real number, and every example is true whatever \( x \) is." New table (Example column):
   - \( P \wedge Q \): "\( x^2 \ge 0 \) and \( x^2 + 1 > 0 \)"
   - \( P \vee Q \): "\( x \ge 0 \) or \( x < 0 \)"
   - \( P \to Q \): "if \( x > 1 \), then \( x^2 > 1 \)"
   - \( P \leftrightarrow Q \): "\( x^2 = 0 \) if and only if \( x = 0 \)"
   - \( \neg P \): "not \( x^2 < 0 \), that is, \( x^2 \ge 0 \)"
   
   01:86 (⊥) kept, last clause → "its rules come with those of 'not'". 01:88: keep the first sentence (hypothesis/conclusion, antecedent/consequent) and the "iff" sentence; the list of English forms moves to the new subsection 6. 01:90, 01:92, 01:94 kept. Both warnings 01:96-102 kept; in 01:101 delete "Section 2.4 explains this convention of language."
5. `## When is an implication broken?` **(new, ~280 words; the promise reading).** Read \( P \to Q \) as a **promise**: whenever \( P \) holds, \( Q \) holds too. A promise is broken only when its condition is met and the promised thing fails. Slogan (italic): *An implication is broken only when its hypothesis holds and its conclusion fails.* Then the four-row table for "if \( x > 1 \), then \( x^2 > 1 \)", caption **"Informal: Chapter 3 shows that the rules of proof agree with this table."**

   | \( P \): \( x > 1 \) | \( Q \): \( x^2 > 1 \) | the promise | a value of \( x \) |
   |---|---|---|---|
   | true | true | kept | \( x = 3 \) |
   | true | false | **broken** | none: this is why the promise holds for every \( x \) |
   | false | true | not broken: it says nothing | \( x = -3 \) |
   | false | false | not broken: it says nothing | \( x = 0 \) |

   Then two sentences: this answers "what if \( P \) is false?" (the implication is not broken, so it counts as true); and to show \( P \to Q \) false, exhibit one case with \( P \) true and \( Q \) false. **Quick check (new):** "Which of \( x = 3 \), \( x = -3 \), \( x = 1 \) breaks 'if \( x^2 > 4 \), then \( x > 2 \)'?" Solution: only \( -3 \) (\( 9 > 4 \) holds, \( -3 > 2 \) fails); at \( 3 \) both parts hold; at \( 1 \) the hypothesis fails, so nothing is promised.
6. `## "Only if", "necessary" and "sufficient"` **(new, ~330 words).** List the six English forms of \( P \to Q \) (from 01:88). Work them with \( P \): "\( n \) is divisible by \( 4 \)", \( Q \): "\( n \) is even", asking of each sentence *when is it broken?*
   - "\( n \) is divisible by \( 4 \) only if \( n \) is even": it says divisibility by \( 4 \) never happens without evenness, so it is broken exactly when \( n \) is divisible by \( 4 \) and odd, which is when \( P \to Q \) is broken. So "\( P \) only if \( Q \)" is \( P \to Q \). True: \( 4k = 2(2k) \).
   - The reverse, "\( n \) is even only if \( n \) is divisible by \( 4 \)", is \( Q \to P \), broken by \( n = 2 \).
   - "Being even is **necessary** for being divisible by \( 4 \)": no divisibility by \( 4 \) without evenness, again \( P \to Q \). "Being divisible by \( 4 \) is **sufficient** for being even": it is enough to guarantee it, \( P \to Q \).
   
   A three-column table (English | broken when | symbols) for "\( P \) only if \( Q \)", "\( Q \) if \( P \)", "\( Q \) is necessary for \( P \)", "\( P \) is sufficient for \( Q \)". One closing sentence: "if" and "only if" put the same two statements in opposite directions, and confusing them is Argument B's mistake.
7. `## Translating a sentence`: 01:104-112 kept.
8. `## Reading a statement: precedence and the main connective`: 01:114-118 kept. The list keeps **two** conventions, (1) ¬ binds most tightly, (2) ∧ and ∨ bind more tightly than → and ↔, followed by the sentence "In a mixture of ∧ and ∨, or of → and ↔, the parentheses are always written." Then the one-line remark (`::: {.remark}`): "When parentheses in a chain of arrows are dropped, they group to the right: \( P \to Q \to R \) means \( P \to (Q \to R) \). Chapters 1 and 2 always write them." 01:127 is cut to its last sentence, "In this chapter we parse by eye." 01:129-156 kept (def-main-connective, the tree, the one-symbol change). The second worked parse 01:158-162 is **cut** (it becomes drill A2(b)). 01:164 kept, "Section 1.3 gives this habit a name … Section 2.6 turns it into a method" → "Section 1.2 gives this habit a name, and each later section adds to it." Quick check 01:166-182 kept.
9. `## The form of an argument`: 01:186-196 kept, with 01:196's last sentence ("The notation for a claim about forms is the following.") replaced by "An argument form is written with its premises above a line and its conclusion below it," followed by the display of the form of 01:188-190:
   \[ \begin{array}{l} P \to Q \\ P \\ \hline Q \end{array} \]
   (an `array` with `\hline` is a display, not a derivation). def-sequent and 01:208-214 **leave 1.1** (def-sequent goes to 1.2). Inline, a form is written "from \( P \to Q \) and \( P \), conclude \( Q \)".
10. `## Try to break it` **(new, ~350 words; the named move).** Definition in prose, bold terms: a form is **bad** if some argument of that form has **true premises and a false conclusion**; such an argument is a **counterexample** to the form. Slogan (italic): *To test a form, try to break it: put statements in for the letters that make every premise true and the conclusion false.* One counterexample settles that the form is bad; failing to find one settles nothing yet. Then the Quick check 01:216-231 as the move's first use, rewritten without ⊢: (i) has the form "from \( P \to Q \) and \( Q \), conclude \( P \)", and \( n = 2 \) breaks it (first premise true for every integer, second true, conclusion false); (ii) has the good form of 01:188. Then **Argument B, tried** (~120 words): B's last step, read as a form, is "from 'if \( n \) is even, then \( n^2 \) is even' and '\( n^2 \) is even', conclude '\( n \) is even'". With B's own content no integer breaks it, because the conclusion is a true theorem; but the *form* breaks with other content, as \( n = 2 \) just showed. A true conclusion reached by a bad form is still not proved.
11. `## Good form, false sentences` **(new, ~200 words; the converse pair).** Side by side: Argument B (every sentence true, form bad) and the argument "If \( 6 \) is even, then \( 6 \) is prime. \( 6 \) is even. So \( 6 \) is prime." (form "from \( P \to Q \) and \( P \), conclude \( Q \)", good; the first premise is false, since \( 6 \) is even and not prime; the conclusion is false). A 2×2 table, rows "form good / form bad", columns "every sentence true / some sentence false", with Argument B, the 6-argument, and the two-squares Argument A placed in it (Argument A: good form, all true; the fourth cell: e.g. the n = 2 instance of the Quick check has true premises and false conclusion, bad form). Moral: a good form guarantees only that true premises give a true conclusion.
12. **Convention box** (placed at the end of `## Statements`, item 3, replacing 01:66; `::: {.remark}`, first words `**Convention: a fixed but arbitrary number.**`; ~120 words): "When an example says 'let \( x \) be a real number' and then talks about \( x \), the letter names **one** number, fixed for the whole example, that we are not told. Every sentence about \( x \) is then a statement, true or false according to which number \( x \) is: with \( x = 3 \), '\( x > 2 \)' is true; with \( x = 0 \), it is false; and the example does not know which \( x \) it has. So an argument about \( x \) may use only what holds whatever \( x \) is, and an argument that never peeks at \( x \) works for \( x = 3 \), for \( x = 0 \), and for every other number at once. Chapter 4 gives 'for every' its rules and explains why such an argument proves a statement about every \( x \)." (ch04 04:13 and ch03 02:64 rely on this convention and promise.) **Quick check (new):** "Let \( x \) be a real number. Is '\( x > 2 \) or \( x \le 2 \)' a statement? Is it true?" Solution: yes, about the one fixed \( x \); and true whatever \( x \) is, since one of the two sides holds for every number.
13. `## Each connective, two rules`: 01:235-253 kept, with 01:240 "as Section 1.3 shows" → "as Section 1.2 shows", 01:242 "Section 1.3" → "Section 1.2", 01:249's list → "those for \( \wedge \) in Section 1.2, those for \( \to \) in Sections 1.3 and 1.4, and those for \( \vee \) in Sections 1.5 and 1.6". **Cut** 01:255 (soundness: the promise now lives in 1.2). 01:257 kept up to "it is the question to ask of Argument B."; its last sentence is cut. 01:259 → preface (§4.0a). 01:261 → one sentence: "Section 1.4 names exactly what B did wrong; the move above already shows that B's tempting repair, 'from \( P \to Q \) and \( Q \), conclude \( P \)', is a bad form."
14. `## What comes next`: three lines replacing 01:263-276: "Section 1.2 shows what a derivation is, with the rules for 'and'. Each later section adds one rule. Two questions guide every search: what does the goal's main connective ask for, and what does an available line's main connective let me do?"

**Folds.** F1.1-a `title="Valid, or only convincing?"` (new, ~150 words): a list of true cases is evidence, not a proof of form: \( n^2 + n + 41 \) is prime for \( n = 0, 1, \dots, 39 \), yet at \( n = 40 \) it is \( 1681 = 41^2 \); an argument from many cases can be strong without being of a good form, and logic studies only form. F1.1-b `title="Statements or propositions?"`: the remark 01:68-70 verbatim.

**Quick checks:** main connective (kept), form (kept, as the first try-to-break), promise (new), convention (new): four, about one per 1,000 words.

**Exercises.**
- **A1** (kept label): parts (a)–(d) unchanged. (e) → "Let \( x \) and \( y \) be real numbers. Write the form of 'x > 0 and y > 0; so y > 0 and x > 0' with premises above a line, saying what each letter stands for." Answer: premise \( P \wedge Q \), conclusion \( Q \wedge P \), with \( P \): "\( x > 0 \)", \( Q \): "\( y > 0 \)"; Section 1.2 derives it. (f) kept, "Section 1.3" → "Section 1.2", and the solution's last sentence → "… the first question of 'What comes next' …" (heading kept). (a)'s solution "as in this chapter's convention" → "by the convention of the box in 'Statements'".
- **A2: Drills** (new), with answers:
  (a) Main connective of \( \neg P \wedge Q \to R \)? — \( \to \); it is \( ((\neg P) \wedge Q) \to R \).
  (b) Main connective of \( P \vee Q \to R \wedge S \), and its full parenthesization? — \( \to \); \( (P \vee Q) \to (R \wedge S) \).
  (c) Main connective of \( \neg (P \to Q) \wedge R \)? — \( \wedge \).
  (d) With \( P \): "\( x > 0 \)", \( Q \): "\( x^2 > x \)", translate "\( x \) is positive but \( x^2 \) is not greater than \( x \)". — \( P \wedge \neg Q \).
  (e) With \( O \): "\( n \) is odd", \( S \): "\( n^2 \) is odd", \( C \): "\( n^3 \) is odd", translate "if \( n \) is odd, then \( n^2 \) and \( n^3 \) are odd". — \( O \to (S \wedge C) \).
  (f) Is "if \( x > 1 \), then \( x^2 > 1 \)" broken at \( x = -2 \)? — No: the hypothesis \( -2 > 1 \) is false, so nothing is promised.
  (g) Is "if \( x^2 > 1 \), then \( x > 1 \)" broken at \( x = -2 \)? — Yes: \( 4 > 1 \) holds and \( -2 > 1 \) fails.
  (h) Write "\( n \) is prime only if \( n \) is odd" as an implication and break it. — "\( n \) prime → \( n \) odd"; \( n = 2 \).
  (i) Try to break "from \( P \vee Q \) and \( P \), conclude \( \neg Q \)". — With \( P \): "\( x \ge 0 \)", \( Q \): "\( x \le 0 \)", at \( x = 0 \): both premises true (the "or" is inclusive), \( \neg Q \) false. Bad form.
  (j) The argument "If \( 7 \) is even, then \( 7^2 \) is even. \( 7 \) is even. So \( 7^2 \) is even." has a false conclusion. Is its form bad? — No: its form is "from \( P \to Q \) and \( P \), conclude \( Q \)"; the premise "\( 7 \) is even" is false, and a form is bad only when some instance has **all** premises true and the conclusion false.
- **B1** kept. **B2** kept without (d) (dropped: convention 3 is now a remark); the solution adds a parse tree (TikZ, as 01:143-154) for each of (a), (b), (c).
- **B3** = old C2 renamed `exr-statements-and-connectives-b3`, `[B3: Necessary and sufficient]`, content unchanged (the worked passage of item 6 is its worked example).
- **B4** (new), `[B4: Break it or explain why not]`: "For each form, either find statements about a real number \( x \) that make every premise true and the conclusion false, or explain with the promise table why no choice of statements can: (a) from \( P \to Q \) and \( \neg P \), conclude \( \neg Q \); (b) from \( P \to Q \) and \( Q \to R \), conclude \( P \to R \); (c) from \( P \vee Q \), conclude \( P \); (d) from \( P \wedge Q \), conclude \( P \vee Q \)." Answers: (a) bad: \( P \): "\( x > 2 \)", \( Q \): "\( x^2 > 4 \)", \( x = -3 \) (\( P \to Q \) holds for every \( x \); \( \neg P \) true; \( Q \) true, so \( \neg Q \) false). (b) cannot be broken: breaking the conclusion needs \( P \) true and \( R \) false; then if \( Q \) is true, \( Q \to R \) is broken, and if \( Q \) is false, \( P \to Q \) is broken, so some premise is false. (c) bad: \( P \): "\( x > 0 \)", \( Q \): "\( x \le 0 \)", \( x = -1 \). (d) cannot be broken: if \( P \wedge Q \) is true then \( P \) is true, so \( P \vee Q \) is true. The solution says once that "cannot be broken" is shown here by reasoning about every case, not by failing to find one.
- **C1** frozen, unchanged.

**Sidecars:** promise table values (\( x = 3, -3, 0 \)) and the Quick check (\( x = 3, -3, 1 \)); \( 1681 = 41^2 \) and primality of \( n^2 + n + 41 \) for \( 0 \le n \le 39 \); the connective-table examples (each true on a grid of \( x \)); B4 witnesses. Ledger: the 6-argument (6 even, not prime), Argument A's facts as before.

### 4.2 Section 1.2: Derivations, Starting with And (`02-derivations.md`, merged)

**Budget:** main line ≤ 4,500 words (02 + 03 now 6,599); folds ≤ 1,800. The one Looking-ahead box carries the soundness promise.

**New order of material.**
1. Opening frame (new, ~80 words; replaces 02:3 and 03:3): this section says what a derivation is and gives the first two rules of logic, for "and".
2. `## Why check by matching` (new, ~220 words, then 02:7-17 shortened to ~150): three reasons before the fraction chain. A proof in a research paper may run to hundreds of steps, too long for anyone to hold in mind at once; two careful readers can disagree about whether a step is "obvious", and matching settles it; and computer programs that check proofs work exactly this way, by comparing each step with a pattern. Then the chain \( 0 < \tfrac13 < \tfrac12 < 1 \) and the clerk (02:7-17), ending with "a proof is correct when every step matches its pattern, and matching is mechanical."
3. `## A rule is a pattern`: one sentence introducing **Tr** only (02:25, and the first sentence of 02:28 "a fact about numbers used as a rule, for practice"); **Sh is cut** (02:26, 02:66-78). def-rule-schema with "**given** lines at the top, possibly none" (was "lines and boxes"), "cites the given lines" (was "lines and boxes"); everything else verbatim (S2a). Then **three bullets** replacing 02:55-60: the given lines may stand anywhere above, in any order on the page; the citation's order says which line plays which part; letters are replaced consistently, symbol for symbol. One instance (02:62) and one noninstance (02:64), kept. 02:80: keep its first two sentences; delete "Every rule of logic … no given lines at all." (The definition's "possibly none" stays: ch04 07:18 says the schema was worded so that a Chapter 4 rule could have no given lines.) Warning 02:84-86 kept.
   **The letter sentence (new, replaces 02:82 and 03:17):** "From now on the letters in a schema are Greek: \( \varphi \), \( \psi \), \( \chi \) (phi, psi, chi). A Greek letter is a hole in a rule's pattern; a capital \( P \) is a statement we are reasoning about. A pattern works like the formula \( (a + b)^2 = a^2 + 2ab + b^2 \), whose \( a \) and \( b \) are holes to be filled with any expression, the same one wherever the hole appears." Then 02:82's instance example (\( P \to Q \), \( R \), \( (P \to Q) \wedge R \)) kept.
4. `## Derivations without boxes`: def-box-free-derivation verbatim. 02:105 kept with "Section 1.5" → "Section 1.4". 02:107 kept, "From Section 1.5 on" → "From Section 1.4 on". 02:109 → fold F1.2-a.
5. `## First derivations`: exm-chaining-derivation with parts (a) and (b) (old (c)); old (b) and 02:158 are dropped. 02:174 kept. 02:177 → "Part (b) was found backwards, from the goal; part (a) forwards. The rest of this section names the two directions." Quick check 02:179-185 kept.
6. `## Reading a derivation`: 02:244-262 (three questions, table, slogan) kept; 02:260 "Section 1.5 extends this table" → "Section 1.4". 02:264 and exm-not-a-derivation (02:266-300) → fold F1.2-b.
7. `## What a derivation proves` (⊢ arrives here): 02:189 → "A derivation shows that its conclusion follows from its premises. The symbol \( \vdash \) says that such a derivation exists." def-derivable verbatim. Then (prose) "Here \( \Gamma \) (capital gamma) is just a name for a list of statements." Then **def-sequent** (moved), reworded to sit after def-derivable without redefining ⊢ (S2a): "[Sequent] Let \( P_1, \dots, P_n \) and \( Q \) be statements, where \( n \ge 0 \). The expression \( P_1, \dots, P_n \vdash Q \), read '\( P_1 \) to \( P_n \) prove \( Q \)', is a **sequent**. It is the **claim** that \( Q \) is derivable from \( P_1, \dots, P_n \) in the sense of @def-derivable. The statements \( P_1, \dots, P_n \) are its **premises** and \( Q \) is its **conclusion**; when \( n = 0 \) we write \( \vdash Q \)." Then 02:208's first half (a sequent is not true because its conclusion is; it is proved by exhibiting a derivation) in one sentence. The four remarks 02:201-206: drop 1 (now def-sequent), keep 2 ("Until Section 1.4 …"), 3, 4. 02:208 example and 02:210 kept, with "Chapter 3 makes this precise" cut (ch03 01:390 relies on 02:210's phrase "the letters stand for arbitrary statements" being in this section). Quick check 02:212-218 → "What sequent with Tr does part (b) of @exm-chaining-derivation show?" (same answer). exm-derivations (02:220-238) → fold F1.2-a. Warning 02:240-242 kept, trimmed to two sentences (premises are given; Tr takes the false \( 1 < 0 \), \( 0 < -1 \) to the false \( 1 < -1 \); a derivation guarantees only "if the premises are true, so is the conclusion").
8. `## The rules for and`: 03:5-13 cut to ~140 words (uses take a half, proofs prove both; "here these become rules, checked by matching, as Tr was"). def-rules-conjunction: schemas and block text verbatim, plus one sentence inside the block after the first sentence: "Its two given lines may be cited in either order: the new line shows which statement is its left conjunct." (S2a; needs R0.) Then **three bullets** (replacing 03:48-64 and 03:86-88):
   - **∧I.** Two lines in hand, anywhere above and in either order; write their conjunction.
   - **∧E.** One line whose **main connective** is \( \wedge \); write either side. One layer at a time: from \( (P \wedge Q) \wedge R \) it writes \( P \wedge Q \) or \( R \), never \( P \).
   - **Why truth is safe.** If \( \varphi \) and \( \psi \) are true, so is \( \varphi \wedge \psi \); if \( \varphi \wedge \psi \) is true, so is each side.
   
   Warning 03:66-68 kept. Quick check 03:70-76 kept. Quick check 03:78-84 **deleted**. **Quick check (new):** "Line 2 is \( P \) and line 5 is \( Q \). Is '\( Q \wedge P \) — ∧I 2, 5' legal?" Solution: yes; ∧I's lines may be cited in either order, and the line shows \( Q \) on the left.
9. `## Two directions of reasoning`: 03:90-98 kept; 03:100 → "The derivation is finished when the two ends meet. Part (b) of @exm-chaining-derivation already worked backwards, with Tr in the part that introduction rules play from now on." (cut "Section 2.6 collects …"). Then the **Givens/Goal table** introduced (convention §1.5) in ~120 words, with the commutes search as its first run:

   | Givens | Goal |
   |---|---|
   | \( P \wedge Q \) | \( Q \wedge P \) |
   | \( P \wedge Q \) | \( Q \), \( P \) (∧I splits the goal) |
   | \( P \wedge Q \), \( P \), \( Q \) (∧E) | \( Q \) ✓, \( P \) ✓ |

10. `## First derivations with and`: exm-conjunction-warm-ups with parts (a) \( P, Q \vdash Q \wedge P \) and (b) \( P \wedge Q \vdash Q \) (old (c)); 03:131 → "The citation '2, 1' lists \( Q \)'s line first; '1, 2' would do as well, since the line shows the order." 03:144 goes with old (b) to the fold. 03:160 kept (box-free derivations, ⊢). prp-and-commutes: statement, Idea (with its two snapshots 03:173-190 and a pointer to the Givens/Goal table above), proof verbatim (03:207's "in that order" is still true). 03:210-212 kept. prp-and-associative: statement and proof verbatim; its Idea gains **two snapshots** (a: premise, gap, goal \( P \wedge (Q \wedge R) \) as line 7; b: lines 2–5 written from the premise, line 6 \( Q \wedge R \) and line 7 from the goal, nothing missing). 03:248 and remark 03:250-252 kept. `### A line is not used up` (03:254-276) kept. `### Take everything apart, rebuild` (03:278-303) → fold F1.2-c.
11. `## How this looks in a mathematical proof`: exm-product-in-unit-interval verbatim except 03:340 "as Tr was used in Section 1.2" → "as Tr was used above". 03:343 kept. 02:302-310 (the \( 1/n \) chain) → fold F1.2-d.
12. `## Common errors`: 03:347 → one lead sentence; warning 03:349-351 and the expect-invalid derivation 03:353-361 and 03:363 kept. 03:365 **deleted**.
13. **Rule card** (replaces 03:367-376): rows ∧I, ∧E (Shape, You write as 03:373-374, Lean as 03:373-374), with 03:369's Lean sentence.
14. **Looking ahead** (`::: {.remark}`): "**Looking ahead.** Chapter 3 checks, for every rule of the book at once, that no rule leads from true lines to a false one. Until then each rule comes with the one-sentence reason it is safe, as the third bullet above gave for 'and'." (ch03 05:7 needs a matching edit, §6.)

**Folds.** F1.2-a `title="Edge cases"`: 02:109; exm-derivations 02:220-238 (with "Section 1.5" → "Section 1.4" at 02:235); 03:54 (∧I with \( i = j \)); old warm-up (b) 03:133-144 as one paragraph. F1.2-b `title="Two ways to break a derivation"`: exm-not-a-derivation 02:264-300 verbatim ("Exercise C2 below" stays true). F1.2-c `title="Any rearrangement of a conjunction"`: 03:278-303 without the `@thm-completeness` parenthetical. F1.2-d `title="A chain in an analysis proof"`: 02:302-310.

**Cut outright:** Sh (02:26, 02:66-78), the long clause readings 02:55-60 and 03:48-64 (replaced by bullets), 03:86-88, 03:78-84, 03:365, exm-chaining-derivation old (b) with 02:158.

**Quick checks:** Tr citation (kept), sequent of (b) (kept), one layer (kept), either order (new): four in ~4,500 words, plus the Givens/Goal table as a worked check.

**Exercises.**
- **A1** (`exr-derivations-a1`, merged): (a) State the definition of a box-free derivation and of \( \Gamma \vdash \psi \), and write the three schemas of @def-rules-conjunction from memory (02 A1(a) + 03 A1(a)). (b) Which statements does one application of ∧E give from \( P \wedge (Q \wedge R) \)? (03 A1(b)). (c) In the proof of @prp-and-associative, why must line 2 come before line 4? (03 A1(d): comprehension part on the first multi-step derivation). (d) Fill in (i)–(iv) of the derivation at 03:392-402 (03 A1(e); answer (iv) "∧I 4, 2", and "∧I 2, 4" is equally right). (e) True or false: if \( \Gamma \vdash \psi \) with Tr and every statement of \( \Gamma \) is true, then \( \psi \) is true (02 A1(e)); the solution's last sentence becomes "This is the property the Looking-ahead box of this section promises for the rules of logic." (f) What sequent does drill A2(h) below show? Answer \( P \wedge Q, \ R \vdash R \wedge P \).
- **A2: Drills** (new):
  (a) Lines 1 \( 2 < y \), 2 \( y < z \). What does "Tr 1, 2" justify? — \( 2 < z \) (\( a, b, c \) := \( 2, y, z \)).
  (b) Lines 1 \( u < 3 \), 2 \( 4 < v \). Is "\( u < v \) — Tr 1, 2" justified? — No: the middles \( 3 \) and \( 4 \) differ, so it is no instance, although \( u < v \) does follow.
  (c) Premises 1 \( 0 < x \), 2 \( x < 3 \), 3 \( 3 < y \). Is "4. \( 0 < y \) — Tr 1, 3" justified? — No: line 1 makes \( b \) the expression \( x \), line 3 makes it \( 3 \).
  (d) Write \( 0 < \tfrac14 < \tfrac13 < \tfrac12 \) as a derivation of \( 0 < \tfrac12 \) from its three links with Tr. — 4 \( 0 < \tfrac13 \) Tr 1, 2; 5 \( 0 < \tfrac12 \) Tr 4, 3.
  (e) In the list "1 \( 0 < 1 \) premise; 2 \( 1 < 2 \) premise; 3 \( 0 < 2 \) — Tr 2, 1", which of the three questions fails? — The second: citing 2 first makes \( b \) be \( 2 \) (from line 2) and \( 0 \) (from line 1).
  (f) May ∧E be applied to the line \( P \wedge Q \to R \)? — No: its main connective is \( \to \).
  (g) Lines 1 \( P \wedge (Q \wedge R) \), 2 \( S \), 3 \( Q \wedge R \) (∧E 1). Which can be line 4? (i) \( (Q \wedge R) \wedge S \), ∧I 3, 2; (ii) \( S \wedge (Q \wedge R) \), ∧I 3, 2; (iii) \( R \), ∧E 1; (iv) \( R \), ∧E 3. — (i) yes; (ii) yes (either order); (iii) no, \( R \) is a layer deeper; (iv) yes.
  (h) Derive \( P \wedge Q, \ R \vdash R \wedge P \). — 3 \( P \) ∧E 1; 4 \( R \wedge P \) ∧I 2, 3.
  (i) Derive \( (P \wedge Q) \wedge R \vdash Q \). — 2 \( P \wedge Q \) ∧E 1; 3 \( Q \) ∧E 2.
  (j) Derive \( P \wedge Q, \ R \wedge S \vdash S \wedge P \). — 3 \( P \) ∧E 1; 4 \( S \) ∧E 2; 5 \( S \wedge P \) ∧I 4, 3.
  (k) Fill in the Givens/Goal table for \( P \wedge (Q \wedge R) \vdash R \): one row per step. — Givens \( P \wedge (Q \wedge R) \), goal \( R \); after ∧E: \( P \), \( Q \wedge R \); after ∧E again: \( Q \), \( R \) ✓.
  (l) Line 1 is \( (P \wedge Q) \wedge (R \wedge S) \). List every statement ∧E can write from line 1 in one step. — \( P \wedge Q \) and \( R \wedge S \) only.
- **B1** = old `exr-conjunction-b1` (the other grouping), unchanged. **B2** = old `exr-conjunction-b2` (annotating \( 1 < x < 2 \), \( 3 < y < 4 \)), unchanged, its last sentence's `@exm-product-in-unit-interval` kept.
- **B3** (new, scaffolded), `[B3: Two layers, then rebuild]`: "A search for \( P \wedge (Q \wedge R), \ S \vdash (R \wedge P) \wedge S \) has reached the stage below. *Name the move, then complete it.*" Shown: lines 1–2 premises, a gap, line 7 \( (R \wedge P) \wedge S \) with justification "?". Answer: the move is *read the skeleton off the goal* (∧I on subgoals \( R \wedge P \) and \( S \); \( S \) is line 2; \( R \wedge P \) splits again) and *take the premise apart one layer at a time*: 3 \( P \) ∧E 1; 4 \( Q \wedge R \) ∧E 1; 5 \( R \) ∧E 4; 6 \( R \wedge P \) ∧I 5, 3; 7 ∧I 6, 2.
- **C1** (`exr-derivations-c1`, Flip) kept; in (c) replace "Chapter 3 proves … (@thm-soundness)" by "The rules of logic are chosen to have it; this section's Looking-ahead box says where that is checked."
- **C2** kept; title `[C2: Find the error]`, with part (c) prefixed "*(Challenge.)*". It stays one of the chapter's find-the-error items with a **true** conclusion.
- **C3** = old `exr-conjunction-c2`, `[C3: A shortcut through two layers]`, (a)–(c) unchanged, (d) prefixed "*(Challenge.)*"; its "Section 2.3 calls such a rule a derived rule" stays (plain pointer inside a challenge solution).
- **C4** = old `exr-conjunction-c1`, `[C4: Challenge: What conjunction cannot do]`, content unchanged except 03:533's last paragraph → "The argument, 'look at the first bad line; it cannot be a premise, and no rule can create it from good lines', is an induction on the lines of a derivation; Chapter 3 makes such arguments exact." (no `@ref`). Its marking scheme gets the S6 finding of `ch01-S6.md` row 3 (credit the line-by-line route).

**Sidecars:** drills (a)–(e) values; the merged A1(e) argument as before.

### 4.3 Section 1.3: Using an Implication: Modus Ponens (`04-using-an-implication.md`)

**Budget:** main line ≤ 2,800 words (now 2,970); folds ≤ 300. Forward pointers: the green card (Chapter 2, plain) and the Looking-ahead box.

**Changes, in the file's order.**
1. 04:3: "Section 1.3 gave the two rules for 'and'" → "Section 1.2 …"; "Section 1.5" → "Section 1.4".
2. Four cards (04:9-31): the solution's first paragraph is reworded to use the move: "For each card, try to break the claim: can its hidden side make a card that is even and not red? (By the promise reading of Section 1.1, that is the only way to break it.)" The four card paragraphs are kept. 04:33: "Section 2.3 returns to this card with the rule behind it, called modus tollens" → "the rules for 'not', in Chapter 2, say exactly what follows from that".
3. The rule: def-rule-implication-elimination verbatim. The reading 04:56-66 becomes **four bullets** (two given lines; read \( \varphi \) and \( \psi \) off the main connective; the hypothesis must match exactly, with the \( Q \wedge P \) example; the new line is the whole conclusion), plus 04:66 rewritten: "The citation lists the implication first and its hypothesis second, always." Degenerate case 04:68 → fold F1.3-a.
4. **"Why this rule" (04:70-74) replaced** (~150 words): "It is what 'by Theorem so-and-so' means. A theorem of school arithmetic says: if an integer is divisible by \( 2 \) and by \( 3 \), then it is divisible by \( 6 \). For \( n = 42 \) it says
   \[ \bigl( (2 \mid 42) \wedge (3 \mid 42) \bigr) \to (6 \mid 42) . \]
   We know \( 2 \mid 42 \) (\( 42 = 2 \cdot 21 \)) and \( 3 \mid 42 \) (\( 42 = 3 \cdot 14 \)). ∧I builds the hypothesis, and →E fires: \( 6 \mid 42 \), which is right, as \( 42 = 6 \cdot 7 \)." Then a 5-line derivation (1 the implication; 2 \( 2 \mid 42 \); 3 \( 3 \mid 42 \); 4 ∧I 2, 3; 5 \( 6 \mid 42 \) →E 1, 4), then 04:74's last sentence ("Every application of a theorem has this shape: check the theorem's hypotheses, assemble them into exactly the theorem's hypothesis, and fire.") kept. **No** quantifier parenthetical. If `\mid` is not yet in NOTATION, write "\( 42 \) is divisible by \( 2 \)" in words in the derivation (the drafter checks NOTATION; S2a item). **Quick check (new):** "To get '\( 36 \) divides \( 72 \)' from the theorem 'if \( 4 \) and \( 9 \) divide \( n \), then \( 36 \) divides \( n \)' at \( n = 72 \), which line must stand on the page before →E fires?" Solution: the conjunction \( (4 \mid 72) \wedge (9 \mid 72) \), exactly, built by ∧I (\( 72 = 4 \cdot 18 = 9 \cdot 8 \)).
5. "Why it is safe" (04:76) → one sentence, no Chapter 3: "If \( \varphi \to \psi \) and \( \varphi \) are true, then \( \psi \) is true: that is what the promise says."
6. "Why nothing more" (04:78-82) kept to "… and it is the red card of the puzzle. It is not an instance of →E …"; then "It is a bad form: Section 1.1 broke it at \( n = 2 \). It is also the step that would repair Argument B." The `@cor-refuting-row` sentence moves to the Looking-ahead box. Warning 04:84-86 kept. Quick check 04:88-94 kept. Remark 04:96-98 kept, "Section 1.5" → "Section 1.4" (ch04 03:229 relies on it).
7. Chains (04:100-116) kept; 04:104 "as in Section 1.3" → "1.2"; 04:106 "In Section 1.3" → "In Section 1.2"; 04:108's "and Chapter 5 collects it …" cut.
8. exm-implication-chains kept. (a)'s 04:145 → "This is the form of the two arguments of Section 1.1, now shown as a sequent: a derivation with these premises and this last line exists." (d)'s 04:218 "(Section 1.5 shows …)" → "(Section 1.4 …)". (e) gains **two snapshots** (premises taken apart: lines 1–6 and the goal at 9 with a gap; then the meeting lines 7–8). (b)'s snapshots kept.
9. Checking table 04:243-260 kept; 04:245 "the questions of Section 1.2" stays (now true of the merged 1.2).
10. How this looks (04:262-291) kept.
11. Common errors: the warning 04:297-299 **replaced**: "→E needs the **whole** hypothesis. From \( (P \wedge Q) \to R \) and \( P \) alone, it gives nothing. Take the true theorem 'if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)' and the line \( x > 0 \): at \( x = 1 \), \( y = -1 \) the theorem and \( x > 0 \) are true, and \( xy > 0 \) is false." The extreme-value example (04:298 from "This is the commonest slip in analysis") → fold F1.3-b. 04:301 kept.
12. Rule card (replaces 04:303-313): rows ∧I, ∧E, →E; 04:313's Lean sentence kept.
13. **Looking ahead:** "Chapter 3 proves more than 'affirming the consequent is a bad form': no derivation at all, however long, leads from \( P \to Q \) and \( Q \) to \( P \)." (ch03 05:284 relies on this promise, §6.)

**Folds.** F1.3-a `title="A legal, useless line"`: 04:68. F1.3-b `title="The same slip in analysis"`: the extreme-value example of 04:298.

**Quick checks:** 42/72 (new), \( P \to (Q \to R) \) (kept), backward search (kept): three.

**Exercises.** A1, B1–B3, C1, C2 kept (C1's solution (b) prefaced "Try to break the step:"). New:
- **A2: Drills**:
  (a) Lines 1 \( (P \vee Q) \to R \), 2 \( P \vee Q \). What does "→E 1, 2" give? — \( R \).
  (b) Lines 1 \( P \to (Q \to R) \), 2 \( Q \). Is "→E 1, 2" legal? — No: line 1's hypothesis is \( P \).
  (c) Lines 1 \( (P \wedge Q) \to R \), 2 \( Q \wedge P \). Is "\( R \) — →E 1, 2" legal? — No: the hypothesis must be \( P \wedge Q \) exactly.
  (d) Lines 1 \( P \to Q \wedge R \), 2 \( P \). What does "→E 1, 2" give? — \( Q \wedge R \) (∧ binds tighter, so line 1 is \( P \to (Q \wedge R) \)); \( Q \) needs one more ∧E.
  (e) Lines 1 \( P \to Q \), 2 \( P \). Is "3. \( Q \) — →E 2, 1" correct as written? — No: →E cites the implication first; "→E 1, 2" is correct.
  (f) Justify each line: 1 \( P \), 2 \( P \to Q \), 3 \( Q \to (R \wedge S) \), 4 \( Q \), 5 \( R \wedge S \), 6 \( S \). — premises 1–3; 4 →E 2, 1; 5 →E 3, 4; 6 ∧E 5.
  (g) Derive \( P \wedge (P \to Q) \vdash Q \). — 2 \( P \) ∧E 1; 3 \( P \to Q \) ∧E 1; 4 \( Q \) →E 3, 2.
  (h) Derive \( P \to (Q \to R), \ P, \ Q \vdash R \). — 4 \( Q \to R \) →E 1, 2; 5 \( R \) →E 4, 3.
  (i) Derive \( P \to (Q \wedge R), \ (Q \wedge R) \to S, \ P \vdash S \wedge Q \). — 4 \( Q \wedge R \) →E 1, 3; 5 \( S \) →E 2, 4; 6 \( Q \) ∧E 4; 7 \( S \wedge Q \) ∧I 5, 6.
  (j) Break the form of "if \( n \) is divisible by \( 6 \), then by \( 3 \); \( n \) is divisible by \( 3 \); so \( n \) is divisible by \( 6 \)". — \( n = 3 \): both premises true, conclusion false.
  (k) Premises \( P \to Q \), \( R \to Q \), \( R \); goal \( Q \). Searching backwards, which implication leads to a derivation? — \( R \to Q \) (its hypothesis is a premise); \( P \to Q \) is a dead end.
- **B4** (new, scaffolded), `[B4: Assemble the hypothesis]`: "A search for \( P \to (Q \wedge R), \ (R \wedge P) \to S, \ P \vdash S \) has reached the stage below. *Name the move, then complete it.*" Shown: lines 1–3, a gap, line 7 \( S \) with "?". Answer: the move is *backwards from the goal*: \( S \) is the conclusion of line 2, so it suffices to reach its hypothesis \( R \wedge P \) exactly, and build it: 4 \( Q \wedge R \) →E 1, 3; 5 \( R \) ∧E 4; 6 \( R \wedge P \) ∧I 5, 3; 7 \( S \) →E 2, 6.

**Sidecars:** `def-rule-implication-elimination.py` rewritten: \( 42 = 2 \cdot 21 = 3 \cdot 14 = 6 \cdot 7 \); \( 72 = 4 \cdot 18 = 9 \cdot 8 = 36 \cdot 2 \); \( x = 1, y = -1 \); \( x = -3 \) kept. Drill (j) \( n = 3 \).

### 4.4 Section 1.4: Proving an Implication: the Rule of the Box (`05-proving-an-implication.md`)

**Budget:** main line ≤ 4,500 words (now 4,359, with ~850 words of new material); folds ≤ 600. Looking ahead: "Chapter 2 proves the claim Argument B wanted, with the rules for 'not'."

**New order of material.**
1. Opening (05:3), "Sections 1.3 and 1.4 gave three rules" → "Sections 1.2 and 1.3 …".
2. `## Supposing something we do not know`: 05:5-23 kept (the temporary world, \( x^2 > 4 \) for every \( x \), the box). 05:17 may be trimmed to two sentences.
3. `## The introduction rule for implication`: first a sentence widening the schema notion (S2a): "From now on the given part of a schema may also be a **box**, cited as a range of lines from its first line to its last; nothing else in @def-rule-schema changes." Then 05:27 and def-rules-implication verbatim. Then *"This rule has conditions that matter; read each one."* and clauses 1–5 (05:55-61) kept. 05:63 → "The subsection 'Which lines a line may cite' below turns clause 5 into an exact rule." Degenerate case 05:65 → fold F1.4-a. "Why the rule is right" 05:67: its first two sentences only. "Why the box closes" 05:69 kept.
4. `## A first box: implication is transitive`: prp-implication-transitive, statement and proof verbatim. The Idea gains a **Givens/Goal table** (row 1: Givens \( P \to Q \), \( Q \to R \) | Goal \( P \to R \); row 2, after opening the box: Givens + \( P \) | Goal \( R \); row 3: + \( Q \) (→E) | \( R \); row 4: + \( R \) ✓) and **two snapshots** (box opened with \( P \) on line 3 and \( R \) on line 5, gap between, line 6 \( P \to R \); then the full box). 05:106-121 kept. Remark 05:123-141 kept on the main line (it carries the book.yaml must-prove \( (P \to Q) \wedge (Q \to R) \vdash P \to R \); see `ch01.md`, Deviation (2)).
5. `## Argument B, diagnosed` **(new, ~450 words; replaces 05:143-149).** With \( E \): "\( n \) is even" and \( S \): "\( n^2 \) is even", B's prose is the derivation
   ```
   1 | E            assumption      ("Suppose n is even, say n = 2k")
   2 | S            algebra 1       ("n² = 4k² = 2(2k²)")
   3 E → S          →I 1–2
   ```
   (an `nd` block with `\by{algebra}{1}`, as in exm-product-in-unit-interval). Set beside it, as a two-column figure (two `nd` blocks side by side, left headed "what B's box earns", right headed "what B claimed"), the claim \( S \to E \). Prose: B's box opens with \( E \) and closes on \( S \), so →I lets it write \( E \to S \), the converse; B's last sentence wrote \( S \to E \). The rule asks the box to open with the **hypothesis** of the implication being proved, here \( S \), and B never opened that box. **The repair fails:** keeping \( E \to S \) and adding the true fact \( S \) to reach \( E \) is "from \( E \to S \) and \( S \), conclude \( E \)", affirming the consequent; try to break the form: with "if \( x > 2 \), then \( x^2 > 4 \)" and "\( x^2 > 4 \)", at \( x = -3 \) both premises are true and "\( x > 2 \)" is false. So B cannot be saved by moving its lines around: a proof of \( S \to E \) must start from \( S \), and that needs the rules for "not" (the Looking-ahead box). Close with the warning 05:145-147 reworded as the section's verdict, one sentence: *B used →I with the box opened at the wrong end.* **Quick check (new):** "A proof of 'if \( x^3 > 8 \), then \( x > 2 \)' begins 'Suppose \( x > 2 \).' and ends 'Hence \( x^3 > 8 \).' What does its box earn, and is the claim it was meant to prove true?" Solution: it earns \( (x > 2) \to (x^3 > 8) \), the converse; the claim is true (a cube is increasing), but this box does not prove it, exactly as with Argument B.
6. `## A box must end on a line of its own` **(new, ~250 words; replaces 05:207's first two sentences in the main line).** The attempted derivation of \( \vdash P \to (Q \to P) \), as an expect-invalid `nd` block:
   ```
   1 | P              assumption
   2 | | Q            assumption
   3 | Q → P          →I 2–2          ← rejected
   4 P → (Q → P)      →I 1–3
   ```
   (`% expect-invalid: line 3 cites a box whose last line is Q, so →I may write only Q → Q`). The checker reads the box \( \lines{2}{2} \): assumption \( Q \), last line \( Q \); →I may write only \( Q \to Q \). The statement \( P \) stands on line 1, outside the inner box, and clause 3 asks for \( \psi \) as a line **of the box itself**. The fix is bookkeeping: copy \( P \) into the box. Copying an available line is the rule **R** (repetition), made official as (D3) of the definition below. One sentence: "Some books let a box end on any line available inside it; this book copies the line in, so that every →I line can be checked by looking only at the box it cites." The corrected derivation is @exm-first-boxes (b) below.
7. `## Which lines a line may cite` **(rewritten; picture first).**
   - The picture rule (bold, then the italic slogan 05:197 after it): "**Going up the page from the line that cites, you may step out of a box across its top, but never into a box across its bottom.** A box whose bottom is above you has closed, and everything inside it is out of reach." For a **whole box** (cited by →I, and later by ∨E): "the citing line must stand in exactly the boxes that the cited box stands in, other than the cited box itself" (05:199 in words).
   - The three bullets 05:193-195 kept.
   - **Scope figure (new TikZ).** A schematic derivation of 11 numbered lines with no formulas (dots), drawn as Fitch bars: line 1 a premise (no box); box A = lines 2–4; line 5 outside every box; box B = lines 6–10, containing box C = lines 7–8; line 11 outside every box. Arrows from the citing line to the cited line, each marked ✓ (solid) or ✗ (dashed), colour optional and never the only carrier: ✓ 4 → 2 (same box); ✓ 8 → 6 (out of C across its top, into B's line); ✓ 8 → 1 (a premise, from two boxes deep); ✗ 6 → 3 (into the closed box A across its bottom); ✗ 9 → 7 (into the closed box C); ✗ 11 → 9 (into the closed box B). Two brackets for whole-box citations: ✓ line 5 cites box 2–4, ✓ line 11 cites box 6–10. Caption: "Up the page: out of a box across its top, never into one across its bottom." **Quick check (new):** "In the figure, which of lines 1–9 may line 10 cite?" Solution: 1, 5, 6 and 9; not 2–4 (box A closed), not 7–8 (box C closed). It may also cite the whole box 7–8.
   - Then **"Here is the official version, the one a checker uses."** and def-derivation **verbatim** (scope rule, (D1)–(D4), the R schema). 05:189 (D-clause paraphrase) cut to one sentence: "(D1)–(D4) say: given, assumed, copied, or one step of one rule, always from what is still available." 05:191 kept ("The scope rule is the definition's real content …"). "Nothing earlier changes" (05:203) kept with "Sections 1.2–1.4" → "Sections 1.2 and 1.3". "Well defined" (05:201) → fold F1.4-b. **05:205 (length and context) removed from Chapter 1** (it moves to Chapter 3; §6 lists the two edits that needs). 05:207-224 (R discussion and the typical-use schema) → fold F1.4-c. Warning 05:226-228 kept.
8. `## How to check a derivation`: 05:230-248 kept, "Section 1.2" stays; the table **loses its Context column**; 05:238's "The last column lists the context of each line." deleted; 05:248 → "Every line passes, and the last line lies in no box. The bar shows the temporary world: it starts at line 3 and stops after line 5."
9. `## An assumption used outside its box`: exm-illegal-citation, warning 05:285-287, Quick check 05:289-311, all kept.
10. `## More boxes`: exm-first-boxes kept. (a): 05:343's sentence "Section 1.2 observed that nothing could be: every rule of Sections 1.3 and 1.4 (…) cites at least one line …" → "No earlier derivation had no premises: every earlier rule cites at least one line, so a derivation using only them starts with a premise. A box is what escapes …". (b): Idea shortened to "This is the derivation the checker accepted after the fix in 'A box must end on a line of its own'", the derivation and 05:363 kept. (c) kept.
11. `## Two hypotheses, or one at a time`: prp-curry (key proof), statements and proofs verbatim; Try-it-first and the Idea kept; the Idea gains **one snapshot** (both boxes opened, line 5 \( R \) as the inner goal, a gap after line 3). 05:452-454 and Quick check 05:456-483 kept.
12. Rule card (replaces 05:485-496): rows ∧I, ∧E, →E, →I, R; 05:494's first four sentences kept ("… It is also the line Argument B got wrong."); "Chapter 5 turns sentences like these into a dictionary" and 05:496 cut.
13. Looking ahead (as above).

**Folds.** F1.4-a `title="A box of one line"`: 05:65 (the degenerate case; @exm-first-boxes (a) shows it on the main line). F1.4-b `title="Why checking stays mechanical"`: 05:201. F1.4-c `title="More on repetition"`: 05:207 from "Most rules may cite an available line directly" through 05:224, with the typical-use schema.

**Quick checks:** Argument B converse (new), scope figure (new), lines that may cite line 2 (kept), one box or two (kept): four, plus the figure.

**Exercises.**
- **A1** kept, except (c): "Which of lines 1–5 are available at line 6, and which boxes?" Answer: lines 1 and 2; the box \( \lines{3}{5} \). (No "context".) (e), (f) stay the comprehension parts on the key proof prp-curry.
- **A2: Drills** (new; items (a)–(c) refer to the scope figure):
  (a) In the figure, may line 8 cite line 5? — Yes: line 5 is in no box.
  (b) May line 9 cite the whole box 2–4? — No: box 2–4 stands in no box, line 9 stands in box B.
  (c) May line 11 cite line 6? — No: line 6 is inside the closed box B.
  (d) Fill in the justifications: 1 \( P \); 2 | \( Q \); 3 | \( P \wedge Q \); 4 \( Q \to (P \wedge Q) \). — premise; assumption; ∧I 1, 2; →I 2–3.
  (e) (old B1) Show \( \vdash (P \wedge Q) \to (Q \wedge P) \) and write it as prose, one sentence per line. — The 5-line derivation and the prose of 05:557-573, unchanged.
  (f) Derive \( P \to Q \vdash (P \wedge R) \to Q \). — 2 | \( P \wedge R \) assumption; 3 | \( P \) ∧E 2; 4 | \( Q \) →E 1, 3; 5 →I 2–4.
  (g) Derive \( Q \vdash (P \wedge R) \to (Q \wedge R) \). — 2 | \( P \wedge R \); 3 | \( R \) ∧E 2; 4 | \( Q \wedge R \) ∧I 1, 3; 5 →I 2–4.
  (h) Find the illegal line: 1 \( P \to Q \) premise; 2 | \( P \) assumption; 3 | \( Q \) →E 1, 2; 4 \( P \to Q \) →I 2–3; 5 \( Q \) →E 4, 2. — Line 5: line 2 is inside the closed box 2–3.
  (i) Derive \( \vdash (P \wedge Q) \to (R \to P) \); which box opens first? — The box of \( P \wedge Q \): 1 | \( P \wedge Q \); 2 | | \( R \); 3 | | \( P \) ∧E 1; 4 | \( R \to P \) →I 2–3; 5 →I 1–4.
  (j) Is "Suppose \( x > 3 \). Then \( x^2 > 9 \)." with nothing after it a proof that \( x^2 > 9 \)? — No: the box never closes; at \( x = 0 \) the sentence \( x^2 > 9 \) is false.
- **B1** (label reused; new scaffolded item), `[B1: Two boxes, one inside the other]`: "A search for \( (P \wedge Q) \to R, \ S \to Q \vdash S \to (P \to R) \) has reached the stage below. *Name the move, then complete it.*" Shown: 1, 2 premises; 3 | \( S \) assumption; 4 | | \( P \) assumption; a gap; 9 \( S \to (P \to R) \) "?". Answer: an implication goal opens a box with its hypothesis, twice (outer \( S \), inner \( P \)); inside, assemble the premise's hypothesis: 5 \( Q \) →E 2, 3; 6 \( P \wedge Q \) ∧I 4, 5; 7 \( R \) →E 1, 6; 8 \( P \to R \) →I 4–7; 9 →I 3–8.
- **B2** frozen; **B3**, **B4** (proof ordering) kept; **C1** (exit check), **C2**, **C3** (exit check) kept.

**Sidecars:** none new beyond the \( x = -3 \) and \( x^3 \) facts (ledger: a cube is increasing on ℝ, school algebra).

### 4.5 Section 1.5: Or, Introduced (`06-disjunction-introduction.md`)

**Budget:** main line ≤ 2,900 words (now 3,436); folds ≤ 350. No Looking-ahead box (the section ends on the stalled goal, which 1.6 pays).

**Changes, in the file's order.**
1. 06:3: "Sections 1.3 to 1.5" → "Sections 1.2 to 1.4".
2. 06:5-17 kept (trimmed). Right after 06:7-13, the **≤/≥ convention box** (`::: {.remark}`, first words `**Convention: inequalities written out.**`): "In derivations, \( a \le b \) is always written out as \( (a < b) \vee (a = b) \), and \( a \ge b \) as \( (a > b) \vee (a = b) \). Prose keeps the short forms. A checker compares symbols, so a derivation that needs '\( x \ge 0 \)' writes the disjunction." (Reused by 2.1.)
3. def-rule-disjunction-introduction verbatim. **Three bullets** replace 06:46-51 and 06:67-71: one given line, available (an earlier line not inside a closed box), cited alone; the new line is a disjunction with that statement as one **whole** side, left or right; the other side may be **any** statement, true or false, related or not, and the rule is safe because "or" is inclusive: one true side makes the disjunction true. Slogan 06:71 kept. 06:53-57 (the instance with \( x > 0 \)) kept. 06:59 (degenerate) and 06:61-65 (three nonexamples) → fold F1.5-a. "Why this rule" 06:67: its first three sentences kept; the rest cut. "Why it is safe" 06:69 cut (the third bullet). Warning 06:73-75 kept; warning 06:77-79 → fold F1.5-a. Quick check 06:81-94 kept, (iv)'s solution pointing at the convention box.
4. `## A disjunction as a goal`: 06:98 → "Section 1.2 asked two questions …" (number fixed). 06:100 **rewritten**: the choice is new, and a wrong choice can make a reachable goal unreachable. "Suppose the premise is \( x > 1 \) and the goal is \( (x > 3) \vee (x > 0) \). Choose the left side, and the new goal \( x > 3 \) is out of reach: at \( x = 2 \) the premise holds and \( x > 3 \) fails, so no correct chain of steps leads from one to the other (every rule carries truth to truth). Choose the right side, and \( x > 0 \) follows from \( x > 1 \)." Slogan 06:104 and 06:106 kept. **Quick check (new):** "Premise \( 0 < x < 1 \), goal \( (x < 0) \vee (x < 2) \): which side, and why not the other?" Solution: \( x < 2 \) (from \( x < 1 \)); \( x < 0 \) fails at \( x = \tfrac12 \), where the premise holds.
5. exm-disjunction-introduction-derivations kept; (c) and (d) gain **one snapshot** each (the box opened, the goal \( Q \vee R \) (resp. \( R \vee S \)) at its bottom, a gap). 06:204-208: keep the warning 06:206-208 (the \( x = 2.5 \) instance), delete 06:204's soundness sentence and fold its first two sentences into the warning's lead.
6. `## Manufacturing a hypothesis`: 06:210-257 kept.
7. `## A goal we cannot reach yet`: 06:259-287 kept (trimmed); it is 1.6's hook.
8. `## How this looks`: exm-product-zero and 06:336 kept.
9. Rule card (replaces 06:338-346): rows ∧I, ∧E, →E, →I, R, ∨I; 06:346's first two sentences kept, "Chapters 2 and 4 add rows … Chapter 5 …" cut.

**Folds.** F1.5-a `title="Edge cases and near misses"`: 06:59, 06:61-65, 06:77-79.

**Quick checks:** \( x = 2 \) (kept), side choice (new), skipping line 3 (kept): three.

**Exercises.** A1, B1–B3 (B2 is the faded middle of the chapter's faded triple), C1, C2 kept; C1's solution "(Section 1.1)" stays. New:
- **A2: Drills**:
  (a) Line 1 is \( x = 5 \). Which are "∨I 1"? (i) \( (x = 5) \vee (x = 6) \); (ii) \( (x > 4) \vee (x = 5) \); (iii) \( x \ge 5 \) as written; (iv) \( (x = 5) \wedge (x \ge 0) \). — (i) yes, first schema; (ii) yes, second schema; (iii) only once written out as \( (x > 5) \vee (x = 5) \); (iv) no, not a disjunction.
  (b) Line 1 is \( P \wedge Q \). Is "\( P \vee Q \) — ∨I 1" legal? — No: \( P \wedge Q \) is not a side of \( P \vee Q \). (\( (P \wedge Q) \vee R \) would be.)
  (c) Line 1 is \( Q \vee P \). Is "\( P \vee Q \) — ∨I 1" legal? — No: \( Q \vee P \) is not a whole side of \( P \vee Q \).
  (d) Derive \( P \vdash (P \vee Q) \wedge (R \vee P) \). — 2 \( P \vee Q \) ∨I 1; 3 \( R \vee P \) ∨I 1; 4 ∧I 2, 3.
  (e) Derive \( P \wedge Q \vdash Q \vee R \). — 2 \( Q \) ∧E 1; 3 \( Q \vee R \) ∨I 2.
  (f) Derive \( P \to Q \vdash P \to (R \vee Q) \). — 2 | \( P \); 3 | \( Q \) →E 1, 2; 4 | \( R \vee Q \) ∨I 3; 5 →I 2–4.
  (g) Derive \( (P \vee Q) \to R, \ Q \vdash R \). — 3 \( P \vee Q \) ∨I 2; 4 \( R \) →E 1, 3.
  (h) Premise \( x > 1 \), goal \( (x > 5) \vee (x > 0) \): which side? — \( x > 0 \); \( x > 5 \) fails at \( x = 2 \).
  (i) "We have \( n = 4 \). So \( n \) is even or \( n > 10 \)." Which steps? — Algebra (\( 4 = 2 \cdot 2 \), so \( n \) is even), then ∨I; ∨I alone gives only "\( n = 4 \) or …".
  (j) Is "\( x > 0 \), so \( x \ge 0 \)" one step of ∨I? — Yes, once \( x \ge 0 \) is written out as \( (x > 0) \vee (x = 0) \): the first schema.

**Sidecars:** quick check (\( x = \tfrac12 \), \( x = 2 \)); drill (h).

### 4.6 Section 1.6: Using Or: Proof by Cases (`07-disjunction-and-cases.md`)

**Budget:** main line ≤ 4,300 words (now 4,245, plus the outline figure, the named moves and the card's prose); folds ≤ 500. Looking ahead: 07:583 kept as the box ("The rules for 'not', … are the subject of Chapter 2.").

**Changes, in the file's order.**
1. 07:3 kept (it says "the previous section"); 07:17 "at the end of Section 1.6" → "Section 1.5"; 07:23 "recalled from Section 1.6" → "1.5".
2. def-rules-disjunction verbatim. *"This rule has conditions that matter; read each one."* before the five clauses 07:63-67 (kept). Degenerate case 07:69 → fold F1.6-a. Warning 07:71-73 kept.
3. `## Cases end in the current goal`: 07:77 "Section 1.3 set up …" → "Section 1.2 …"; "Section 1.6 answered" → "Section 1.5 answered"; 07:83 "Section 1.6" → "1.5". Add the Givens/Goal reading in one sentence and a 3-row table: after the split on \( P \vee Q \), each case adds its assumption to the Givens and keeps the same Goal.
4. exm-disjunction-first-derivations kept (\( P \vee P \vdash P \) stays on the main line); the first derivation's Idea gains **one snapshot** (line 1, both boxes opened with \( P \) and \( Q \), each ending in the goal \( Q \vee P \) with a gap, line 6). 07:111 "Section 1.6" → "1.5". The invalid variant 07:133-152 → fold F1.6-b. Quick check 07:154-160 kept. "Why is the rule built like this?" 07:162 → fold F1.6-c.
5. exm-cases-on-hypothesis and 07:201 ("Section 1.6" → "1.5") kept.
6. `## Laws of "or"`: prp-distributivity (key proof), Try-it-first, Idea, proofs verbatim; 07:271-275 kept. **Outline figure (new)** before exm-disjunction-regroup: an `nd` skeleton with `% schema (outline: …)` marker, statements as goals and gaps only: line 1 \( P \vee (Q \vee R) \); box 2–4 opened by \( P \), ⋮, line 4 the goal \( (P \vee Q) \vee R \); box 5–11 opened by \( Q \vee R \), containing box 6–8 (opened by \( Q \), ⋮, line 8 the goal) and box 9–10 (opened by \( R \), ⋮, line 10 the goal), then line 11 the goal by ∨E; line 12 the goal by ∨E. Lead sentence: "Before the lines, the shape: each split ends with its own ∨E line, line 11 for the inner split and line 12 for the outer." 07:317's last two sentences → "Line 11 is the inner split's own ∨E line, so the box 5–11 ends on a line of its own, as @def-rules-disjunction requires." **Quick check (new):** "In the outline, which line closes the inner split, and which boxes does it cite?" Solution: line 11, citing line 5 and the boxes 6–8 and 9–10.
7. `## From a skeleton to a proof about numbers`: 07:320-345 kept (ch02 06:244 quotes "skeleton").
8. exm-abs-at-least-x, exm-abs-product-cases, exm-triangle-inequality-cases, 07:392, 07:416-418, 07:438 kept **verbatim**. Warnings 07:440-448: keep 07:440-442 and 07:446-448; cut 07:444. 07:450 and the Quick check 07:452-464 kept.
9. `## The rules of this chapter` (replaces 07:466-583), the one-page reference:
   - the **rule card** (all seven rows: ∧I, ∧E, →E, →I, R, ∨I, ∨E; columns Rule | Shape | You write | Lean; the "You write" and Lean entries are those of 07:575-581), with 07:474's sentence on the dropped disjunction kept below it;
   - the schemas display 07:478-561, kept;
   - the goal/premise table 07:563-569, kept;
   - `### Named moves` (moved from index.md:21-28): the six moves verbatim, each followed by the section where it was first used (1.2, 1.2, 1.4, 1.2, 1.5, 1.6).
   07:571 is replaced by the card itself; 07:583 is the Looking-ahead box.

**Folds.** F1.6-a `title="A box of one line"`: 07:69. F1.6-b `title="One line short"`: 07:133-152. F1.6-c `title="Why one common last line loses nothing"`: 07:162.

**Quick checks:** missing box (kept), outline (new), exhaustive splits (kept): three, plus the Givens/Goal table.

**Exercises.**
- **A1** kept; (d)'s solution: replace "(informally: a derivation never leads … @thm-soundness)" by "Try to break the sequent's form:" followed by the existing instance (\( x = -1 \)).
- **A2: Drills** (new):
  (a) "If \( x \ge 0 \), then \( \abs{x}^2 = x^2 \); if \( x < 0 \), then \( \abs{x}^2 = (-x)^2 = x^2 \). So \( \abs{x}^2 = x^2 \)." Name the disjunction and the common last line. — \( (x \ge 0) \vee (x < 0) \); \( \abs{x}^2 = x^2 \).
  (b) Is the split "\( n > 0 \) or \( n < 0 \)" exhaustive for integers? — No: \( n = 0 \) is in neither case.
  (c) Find the illegal line: 1 \( P \vee Q \); 2 \( P \to R \); 3 \( Q \to R \); 4 | \( P \); 5 | \( R \) →E 2, 4; 6 | \( Q \); 7 | \( R \) →E 3, 4; 8 \( R \) ∨E 1, 4–5, 6–7. — Line 7 cites line 4, inside the closed first box; it should cite 3, 6.
  (d) Derive \( P \vee Q \vdash Q \vee (P \vee R) \). — 2 | \( P \); 3 | \( P \vee R \) ∨I 2; 4 | \( Q \vee (P \vee R) \) ∨I 3; 5 | \( Q \); 6 | \( Q \vee (P \vee R) \) ∨I 5; 7 ∨E 1, 2–4, 5–6.
  (e) Derive \( (P \wedge Q) \vee (P \wedge R) \vdash P \). — 2 | \( P \wedge Q \); 3 | \( P \) ∧E 2; 4 | \( P \wedge R \); 5 | \( P \) ∧E 4; 6 \( P \) ∨E 1, 2–3, 4–5.
  (f) Derive \( P \vee Q, \ Q \to P \vdash P \). — 3 | \( P \); 4 | \( Q \); 5 | \( P \) →E 2, 4; 6 \( P \) ∨E 1, 3–3, 4–5.
  (g) Two case boxes end in \( R \wedge S \) and \( S \wedge R \). May ∨E close the split? — No: both must end in the same statement; add ∧E and ∧I lines so both end in the current goal.
  (h) How many case boxes does the proof of @exm-abs-product-cases open? — Six: two for the sign of \( x \), and two inside each for the sign of \( y \).
  (i) "Case \( x \ge 1 \): \( x^2 \ge 1 \). Case \( x \le -1 \): \( x^2 \ge 1 \). So \( x^2 \ge 1 \) for every real \( x \)." What fails? — The disjunction cited is not available: it is false at \( x = 0 \), where the conclusion fails too.
  (j) Inside a box whose current goal is \( S \), the available line is \( Q \vee R \). What do the two case boxes end in? — \( S \).
- **B1–B3** kept.
- **B4** (new), `[B4: The smaller of two numbers]`: "With \( \max(a, b) \) as in B2, let \( \min(a, b) \coloneqq b \) if \( a \ge b \), and \( \min(a, b) \coloneqq a \) if \( a < b \). Prove by cases that \( \max(a, b) + \min(a, b) = a + b \) and \( \max(a, b) - \min(a, b) = \abs{a - b} \). Hence deduce \( \max(a, b) = \frac12 (a + b + \abs{a - b}) \)." Answer: split on \( a \ge b \) or \( a < b \), the current goal the conjunction of the two equations; case \( a \ge b \): \( \max = a \), \( \min = b \), sum \( a + b \), difference \( a - b = \abs{a - b} \) since \( a - b \ge 0 \); case \( a < b \): \( \max = b \), \( \min = a \), sum \( a + b \), difference \( b - a = \abs{a - b} \) since \( a - b < 0 \); ∧I in each case, ∨E. Adding the two equations: \( 2 \max(a, b) = a + b + \abs{a - b} \). Check \( a = 3 \), \( b = -5 \): \( \frac12(-2 + 8) = 3 \). (This is the plan's "case proof about max/min" for the core; it is a B item because C1 is frozen and STYLE caps C at four.)
- **C1** frozen; title `[C1: Challenge: The reverse triangle inequality]`.
- **C2** (find the error, true conclusion), **C3** (exit check), **C4** (faded, last half blank), **R1–R3** kept.

**Sidecars:** B4 on an integer grid and the \( 3, -5 \) check; drill (i) at \( x = 0 \).

---

## 5. Budgets and the Time line

| Section | Main line now (before Exercises) | Main-line budget | Folds |
|---|---|---|---|
| 1.1 | 4,147 | ≤ 4,000 | ≤ 250 |
| 1.2 | 6,599 (02 + 03) | ≤ 4,500 | ≤ 1,800 |
| 1.3 | 2,970 | ≤ 2,800 | ≤ 300 |
| 1.4 | 4,359 | ≤ 4,500 | ≤ 600 |
| 1.5 | 3,436 | ≤ 2,900 | ≤ 350 |
| 1.6 | 4,245 | ≤ 4,300 | ≤ 500 |
| total | 25,756 | ≤ 23,000 | ≤ 3,800 |

Every file stays under 5,000 main-line words. With exercises included the whole-file advisory count of `check_structure.py` will exceed 5,000 in 1.2, 1.4 and 1.6; that count is advisory and the binding budget is the main line.

Exercises after the revision: 6 A1, 6 A2 (drill banks, 63 items), 22 B (5 of them new: 1.1 B4, 1.2 B3, 1.3 B4, 1.4 B1, 1.6 B4; three scaffolded), 16 C (three exit checks: 1.4 C1, C3, 1.6 C3; two Challenges: 1.2 C4, 1.6 C1), 3 R: 53 exercises.

**Time (B1 formula: 15 min per 400 main-line words; 20–45 min per exercise).** Core track = main line, all of A, one B and one C per section, exit checks: reading 23,000 words ≈ 14.4 h; A1 6 × 25 min, A2 6 × 35 min, one B 6 × 30 min, one C 6 × 40 min, the second exit check of 1.4 40 min ≈ 13.7 h; **≈ 28 h, so "About 30 hours on the core track"** (down from 35). Full track: main line plus folds ≈ 26,800 words ≈ 16.8 h, all 53 exercises ≈ 29 h; **≈ 46 h, so "about 45 hours for everything"** (down from 50). The plan's 25 h target is reached only if the delivered main line is under about 21,000 words; the drafter recomputes from the delivered text and does not shade the number down (STYLE §11.9).

---

## 6. The "Section 1.x" renumbering map, and every hit outside Chapter 1

**Map, applied once and simultaneously** (never sequentially): old 1.1 → 1.1; old 1.2 → 1.2; old 1.3 → **1.2**; old 1.4 → **1.3**; old 1.5 → **1.4**; old 1.6 → **1.5**; old 1.7 → **1.6**. Ranges: "Sections 1.3–1.7" → "Sections 1.2–1.6". Inside Chapter 1, the drafters apply the map to every hit (01: 164, 212, 214, 240, 242, 249, 261, 267, 269, 276, 291, 304; 02: 3, 19, 78, 80, 105, 107, 177, 204, 206, 210, 235, 260; 03: 3, 7, 13, 86, 100, 340, 376, 411; 04: 3, 82, 97, 104, 106, 145, 204, 218, 245, 305, 337; 05: 3, 73, 146, 149, 153, 203, 232, 343, 487; 06: 3, 7, 23, 67, 93, 98, 340, 507; 07: 17, 23, 77, 83, 111, 201, 450, 571; index 3), most of which the plans above already rewrite.

**Downstream volumes: no hit.** fd2, fd3 and an1 never name a Chapter 1 section of *Logic and Proof* (every "Section 1.x" there is the volume's own; grep of `Section 1\.[0-9]` against "Logic and Proof"/`fd1` on 2026-10-12). Their mentions of "*Logic and Proof*, Chapter 1" (fd2 01:25, 02:3; fd2 ch02 02:154; an1 index:7, 01:196, 01:261) stay true: statements stay primitive, the connectives give set operations, Argument A is kept, and `exm-triangle-inequality-cases` keeps both its splits.

**fd1 Chapters 2–5, every hit** (step R6 applies these; "→" gives the new reading, ✱ marks a hit whose sentence needs more than the number):

| Hit | Now says | Should read |
|---|---|---|
| ch02 01:7 | Argument A of Section 1.1 | unchanged |
| ch02 01:16 | Section 1.1 introduced the symbols for both | unchanged (1.1 keeps ¬ and ⊥) |
| ch02 01:267 | Argument A in Section 1.1 | unchanged |
| ch02 02:84 | converse error that Section 1.5 found in Argument B | Section 1.4 |
| ch02 03:282 (×2) | @exm-wason-selection (Section 1.4); Section 1.4's affirming the consequent | Section 1.3 (both) |
| ch02 04:3 | Section 1.1 warned that "if" means different things | unchanged (the warning stays, 01:100) |
| ch02 04:382 | error of Argument B in Section 1.1 | unchanged |
| ch02 04:400 | backward chain of →E, as in Section 1.4 | Section 1.3 |
| ch02 05:232 | Section 1.6's move postpones it | Section 1.5's |
| ch02 06:7 | Each section since Section 1.3 has added a move | since Section 1.2 |
| ch02 06:11, 06:12 | Section 1.3 (table) | Section 1.2 |
| ch02 06:13 | Section 1.4 | Section 1.3 |
| ch02 06:14 | Section 1.5 | Section 1.4 |
| ch02 06:15 | Section 1.6 | Section 1.5 |
| ch02 06:16 | Section 1.7 | Section 1.6 |
| ch02 06:58 | (Section 1.3) | (Section 1.2) |
| ch02 06:59 | (Section 1.5) | (Section 1.4) |
| ch02 06:62 | (Section 1.6) | (Section 1.5) |
| ch02 06:65 | (Section 1.3); (Sections 1.4 and 2.4); (Section 1.7) | (Section 1.2); (Sections 1.3 and 2.4); (Section 1.6) |
| ch02 06:244 | the pattern that Section 1.7 called the skeleton | Section 1.6 (the word "skeleton" stays at 07:320-343) |
| ch02 06:462 | affirming the consequent (Section 1.4) | Section 1.3 |
| ch02 06:491 | converse error of Argument B in Section 1.1 | "… of Argument B, diagnosed in Section 1.4" (✱ optional sharpening; "Section 1.1" stays true) |
| ch03 01:290 ✱ | the four conventions before @def-main-connective | "the conventions before @def-main-connective" |
| ch03 01:298 ✱ | (Chapter 1's fourth convention) | (Chapter 1's rule for such mixtures) |
| ch03 01:390 | "the letters stand for arbitrary statements" (Chapter 1, Section 1.2) | unchanged (the phrase stays in 1.2) |
| ch03 02:64 | what Chapter 1 made it mean (Section 1.1) | unchanged (the convention box) |
| ch03 03:28 | @exr-proving-an-implication-b2 (a) of Section 1.5 | Section 1.4 |
| ch03 03:111 | the rule ∨I of Section 1.6 | Section 1.5 |
| ch03 04:95 (×3) | the pattern of Section 1.4; Section 1.1's Quick check; Argument B of Section 1.1 | Section 1.3; unchanged; unchanged |
| ch03 04:158 | →E treats them as different (Section 1.4) | Section 1.3 |
| ch03 04:373 | @def-derivable (Section 1.2) | unchanged |
| ch03 05:7 ✱ | ∧I is safe … (Section 1.3); →E … (Section 1.4). Each time, the book said that Chapter 3 would prove it "for every rule at once" | (Section 1.2); (Section 1.3). "Section 1.2 said once that Chapter 3 would prove it for every rule at once." (The per-rule promises are gone.) |
| ch03 05:43 ✱ | Recall from Section 1.5, just after @def-derivation, that the **context** of line k is … | Define it here: "The **context** of line \( k \) is the list of the premises together with the assumptions of every box containing line \( k \) …" (context leaves Chapter 1). Define **length** of a derivation here too, since 05:552 uses it. |
| ch03 05:284 ✱ | Chapter 1 promised, in Sections 1.1 and 1.4, that no derivation leads from P → Q and Q to P | "Chapter 1 promised, in Section 1.3, …" (1.3's Looking-ahead box; 1.1's promise is cut) |
| ch03 05:288 ✱ | the repair of Argument B that Section 1.1 considered | "that Section 1.4 considered" (1.4's "Argument B, diagnosed") |
| ch03 07:673 | (Section 1.1, and @exr-statements-and-connectives-c1) | unchanged (1.1's new "only if" passage and the frozen C1) |
| ch04 03:9 ✱ | Section 1.4 used the theorem "if a < b and b < c, then a < c" at a = √2, b = 1.5, c = 2, and said that passing from "for all a, b, c" to one instance is a rule of its own, still to be stated | "Section 1.3 used the theorem 'if an integer is divisible by 2 and by 3, then it is divisible by 6' at n = 42, taking the step from 'every integer' to the one integer 42 on trust." |
| ch04 03:229 | Section 1.4 … Section 1.5 filled the gap with a box | Section 1.3 … Section 1.4 |
| ch04 03:233 | The table of Sections 1.3–1.7 and 2.1–2.5 | Sections 1.2–1.6 (the rule cards keep their rows) |
| ch04 03:239 | in Section 1.4 | Section 1.3 |
| ch04 03:247 | a forward search … in Section 1.4 | Section 1.3 (B3 kept) |
| ch04 04:13 | (Section 1.1). It promised that Chapter 4 would explain … | unchanged (the convention box keeps the promise) |
| ch04 04:57, 04:90, 04:420 | Section 1.5 | Section 1.4 |
| ch04 04:250 | (Section 1.3) | (Section 1.2) |
| ch04 04:592, 04:600 | Section 1.7 | Section 1.6 |
| ch04 05:163 | (Section 1.3) | (Section 1.2) |
| ch04 06:223 | (Section 1.7) | (Section 1.6) |
| ch04 07:18 | (Section 1.2): the definition of a rule schema … could have no given lines | unchanged ("possibly none" stays in `def-rule-schema`) |
| ch04 07:419 | (Sections 1.3–1.7) | (Sections 1.2–1.6) |
| ch04 12:19 ✱ | (Section 1.5, recalled before @lem-context-inclusion) | (Section 3.5, before @lem-context-inclusion) |
| ch05 01:137 | Section 1.7 (@exm-triangle-inequality-cases) | Section 1.6 |
| ch05 02:137 | as Section 1.4 observed | Section 1.3 (04:108's first sentence, "to show ψ, it suffices to show φ", is kept) |
| ch05 06:38 (×2) | @def-rules-implication, Section 1.5; Argument B of Section 1.1 | Section 1.4; unchanged |
| ch05 06:39, 06:42, 06:43 | (Section 1.5) | (Section 1.4) |
| ch05 06:40, 06:41 | (Section 1.7) | (Section 1.6) |
| ch05 06:59 | Argument B of Section 1.1 | unchanged |
| ch05 06:104 | Argument B of Section 1.1, diagnosed in Section 1.5 | "… diagnosed in Section 1.4" |

**Other downstream edits this revision forces** (not "Section 1.x" hits; for R3/R6): ch02 index:3's "none explains why 'if \( x^2 < 0 \), then \( x = 7 \)' should count as true" should become "Chapter 1 read it informally, as a promise not broken; no rule yet derives it" (seam check); NOTATION row 146 (context → F1.3 §05); STATUS's promise table loses the per-rule soundness promises of F1.1 (one remains, 1.2's Looking ahead; 1.3's Looking ahead keeps the affirming-the-consequent promise; 1.1's table caption keeps the rules-agree-with-tables promise; 1.4's Looking ahead points at `thm-square-even-implies-even`'s chapter).

---

## 7. What stays exactly as it is

The two-squares hook (01:5-19); the four-card puzzle; the temporary world and the false "\( x^2 > 4 \) for every \( x \)" (05:5-23); every Idea and both directions of reasoning; the existing snapshots (03:173-190, 04:163-183); the "checking needs no idea" tables (02:254-258, 04:254-258, 05:240-246 minus its Context column); every derivation read back as prose; the near misses with numbers (\( x = -3 \), \( x = 0 \), the mixed-sign triangle case); every statement and proof of a cited `def-`, `prp-` or `exm-` label except the three wording changes listed for S2a; the key proofs `prp-curry` and `prp-distributivity` with their Try-it-first prompts; the exit checks (1.4 C1, C3; 1.6 C3); the faded triple (1.4 `prp-curry`, 1.5 B2, 1.6 C4); the proof-ordering item (1.4 B4); the find-the-error items (1.2 C2 and 1.4 C1 and 1.6 C2 with true conclusions, 1.3 C1 with a false one); the R group.

---

## 8. S2a: every new or changed claim that needs blueprint verification

**Changed wording of cited definitions (check that every later citation still holds):**
1. `def-rule-schema`: "given lines and boxes" → "given lines" (possibly none), with 1.4's widening sentence "the given part of a schema may also be a box, cited as a range". Check the ten outside citations (ch02 01:46, 04:48, 05:63, 06:496; ch03 01:29, 01:344, 05:35; ch04 04:319, 07:18) against the two together.
2. `def-rules-conjunction`: the added sentence "∧I's two given lines may be cited in either order; the new line shows which statement is its left conjunct." Check that every existing derivation in fd1–fd3 stays valid, that no text elsewhere relies on the fixed order (none found by grep), and that a checker can still decide each ∧I line mechanically.
3. `def-sequent`, reworded to name a sequent as the claim of `def-derivable` (§4.2 item 7): equivalent to the old content? Check ch02 06:1170 and 07 R1.

**New claims and examples in the main text:**
4. 1.1 connective table: each example true for every real \( x \) (\( x^2 \ge 0 \wedge x^2 + 1 > 0 \); \( x \ge 0 \vee x < 0 \); \( x > 1 \to x^2 > 1 \); \( x^2 = 0 \leftrightarrow x = 0 \); \( \neg(x^2 < 0) \)).
5. 1.1 promise table: \( x = 3, -3, 0 \) land in the rows claimed; no \( x \) has \( x > 1 \) and \( x^2 \le 1 \). Quick check: only \( x = -3 \) breaks "if \( x^2 > 4 \), then \( x > 2 \)" among \( 3, -3, 1 \).
6. 1.1 "only if" passage: each English form's reading; "\( n \) divisible by 4 only if even" true; its reverse broken by \( n = 2 \).
7. 1.1 "try to break it": the definition of a bad form; "one counterexample settles it, failing to find one settles nothing"; the claim that no integer breaks B's last step with B's content (because "\( n^2 \) even ⇒ \( n \) even" is true).
8. 1.1 the 6-argument: "If 6 is even, then 6 is prime" false; form good; the 2×2 table's placements.
9. 1.1 fold: \( n^2 + n + 41 \) prime for \( 0 \le n \le 39 \), \( 40^2 + 40 + 41 = 1681 = 41^2 \).
10. 1.1 convention box and its Quick check (\( x > 2 \vee x \le 2 \) true for every \( x \)); the remark that → groups to the right (agrees with ch03 01:297).
11. 1.2 opening: the three reasons for checking by matching (no false claim about proof assistants: only "programs that check proofs compare each step with a pattern").
12. 1.2 the Givens/Goal table for \( P \wedge Q \vdash Q \wedge P \); the new ∧I Quick check.
13. 1.2 Looking-ahead wording ("for every rule of the book at once").
14. 1.3 the 42 example and its 5-line derivation (\( 2 \mid 42 \), \( 3 \mid 42 \), \( 6 \mid 42 \); the theorem "divisible by 2 and by 3 ⇒ by 6"); the 72 Quick check (\( 72 = 4 \cdot 18 = 9 \cdot 8 = 36 \cdot 2 \); "4 and 9 divide n ⇒ 36 divides n" is true since gcd(4, 9) = 1); whether `\mid` is in NOTATION.
15. 1.3 the whole-hypothesis warning: "if \( x > 0 \) and \( y > 0 \) then \( xy > 0 \)" true; at \( x = 1, y = -1 \) the theorem and \( x > 0 \) true, \( xy > 0 \) false.
16. 1.3 Looking ahead: "no derivation leads from \( P \to Q \) and \( Q \) to \( P \)" (true by `cor-refuting-row`; check the wording does not overclaim for instances, cf. ch03 05:282's remark on \( P \to P \)).
17. 1.4 Argument B as a derivation (3 lines, line 2 "algebra"); the claim that B's box earns \( E \to S \); the repair is affirming the consequent, broken at \( x = -3 \); "a proof of \( S \to E \) must start from \( S \)" (as a statement about →I proofs: check it is phrased about the →I route, since a proof by contrapositive also starts its box elsewhere; suggested wording: "a →I proof of \( S \to E \) opens its box with \( S \)").
18. 1.4 the expect-invalid attempt at \( \vdash P \to (Q \to P) \): line 3 is rejected for exactly the stated reason; `check_fitch.py` flags it.
19. 1.4 the picture rule: "up the page, out of a box across its top, never into one across its bottom" is **equivalent** to def-derivation's scope rule for lines (every box containing line \( i \) contains line \( k \), \( i < k \)); the whole-box wording equals def-derivation's box clause. Check on the scope figure and on nested/sibling cases.
20. 1.4 scope figure: every ✓/✗ arrow and bracket, and the Quick check answer (line 10 may cite 1, 5, 6, 9 and the box 7–8).
21. 1.4 the \( x^3 \) Quick check (the claim "if \( x^3 > 8 \) then \( x > 2 \)" is true for real \( x \)).
22. 1.4 the edited checking table without the Context column; 05:343's rewritten sentence ("every earlier rule cites at least one line").
23. 1.5 the side-choice example (premise \( x > 1 \), goal \( (x > 3) \vee (x > 0) \), \( x = 2 \)) and its Quick check (\( 0 < x < 1 \), \( x = \tfrac12 \)); the ≤/≥ convention box.
24. 1.6 the outline figure (box structure of exm-disjunction-regroup) and its Quick check; the Givens/Goal sentence for ∨E; the named-moves list with first-use sections (1.2, 1.2, 1.4, 1.2, 1.5, 1.6).

**New and changed exercise answers:**
25. 1.1 A1 (e), (f) as reworded; A2 (a)–(j); B2 without (d), with parse trees for (a)–(c); B4 (a)–(d), including the two "cannot be broken" arguments.
26. 1.2 A1 (a)–(f) (merged; (d)'s "∧I 2, 4 equally right"); A2 (a)–(l); B3 (scaffold, 7 lines); C1 (c)'s reworded last sentence; C4's reworded final paragraph and marking scheme.
27. 1.3 A2 (a)–(k); B4 (scaffold, 7 lines); C1 (b) prefaced by the move.
28. 1.4 A1 (c) (available lines 1, 2 and the box 3–5); A2 (a)–(j); B1 (scaffold, 9 lines: availability of every citation).
29. 1.5 A2 (a)–(j).
30. 1.6 A1 (d)'s reworded solution; A2 (a)–(j); B4 (both equations in both cases, the deduction, the \( 3, -5 \) check).

**Routes to confirm do not rest on removed material:** every place that used the removed `@ref`s (§1.12) now gives its reason without them; `exm-derivations` (a), cited by ch02 03:128 and 04:225, is unchanged inside its fold; the must-prove \( (P \to Q) \wedge (Q \to R) \vdash P \to R \) still rests on 1.4's Remark on the main line.
