# Production pipeline (coordinator's runbook)

How each remaining chapter goes from a blueprint stub to a released chapter, and in what order the chapters go. This is the operational form of `authoring/design/research-production.md` §4–§5 and §7.1, accepted as roadmap C2 and C4. The coordinator runs it; agents receive the briefs below; the author samples (S9).

**Five rules the coordinator keeps**
1. **No author is its own only reviewer.** Every verdict comes from a fresh context with a different brief. Where a second model family is available, use it for one referee per section.
2. **Every judge gets a reference:** the frozen blueprint, the ledger, a checklist, or an independent solution. "Check the proofs" alone is not a brief.
3. **Mechanize before reading.** No referee reads a section that fails a gate.
4. **Verdicts go stale on edit.** Every verdict is recorded in `tools/ledger.py` against a content hash. A stale verdict at release is a failure.
5. **Verify ticks; do not apply them.** When an agent reports "promise paid" or "fixed", the coordinator checks the named label or line before recording it.

Aim every brief at the observed risk surfaces: **prose meta-claims, dependency bookkeeping, hidden hypotheses, exercise solutions, notation, and rendered output.** The pilots had no false theorem and no invalid proof step; they had false prose sentences and dependency gaps (research-production §3.1).

---

## Tools

First tranche, required before Wave 1 (being built now; each documents its own usage):

| Tool | Role in the pipeline | Gates |
|---|---|---|
| `blueprint/check_blueprint.py` | Blueprint consistency: labels unique book-wide; every cited label exists earlier (approved chapter, or earlier in this chapter); every must-prove item has a ledger entry (and a Lean status once `lean/` exists); prerequisites are a subset of the DAG. | S1 exit, S2 exit |
| `tools/check_structure.py` | The STYLE contract per section: opening frame, check + sibling solution, warning, A/B/C (and R in the last section), a solution after every exercise, Idea for long proofs, word budget, titles, the dependency ledger present; per chapter, exit checks and a find-the-error item. | S4 |
| `tools/check_fitch.py` | Checks every fitch.sty derivation (line availability, box scope, rule shape, cited lines, RAA placement) and every truth table; honors the expect-invalid marker for deliberate non-examples. | S4 (Part 0, and any later derivation) |
| `tools/promises.py` | Finds prose pointers without an `@ref`, reconciles them with STATUS's promise table, lists the promises a chapter must pay, and verifies that each paid one names an existing label. | S4, S8, S10 |
| `tools/check_beginner.py` | STYLE §13 on reader-facing prose, per section: sentences with more than one inline `@ref` outside a Uses line, sentences over 35 words, nested parentheses, more than two semicolons, authoring terms printed (B4; list configurable with `--terms`), codes used alone (B7); per chapter index, the old Time-line template, Named moves / Summary / Terms in the opening, What you need over five links (B8). Read-only and advisory; `--strict` fails on any finding; `--summary` prints counts per chapter. | S4 (introductory volumes), S5e |
| `tools/check_rendered.py` | Lints the built HTML and the PDF logs: backslashes in code, raw TeX or `\qedhere` on the page, MathJax errors, `??`, prose rendered as code. | S4 (after the build) |
| `tools/ledger.py` | `authoring/ledger/chNN.yaml`: every result, proof, example, check and exercise with its label, kind and content hash; verdicts (stage, reviewer, model, verdict, evidence); `--stale` lists verdicts whose hash no longer matches. Retired ledgers live in `authoring/ledger/archive/`, which the tool never reads. | every stage records here; S10 requires no stale or missing verdict |

Already in the gate (`./build.py check`): `check_forward_deps.py` (proofs citing later sections or exercises), `check_optional.py`, proof ownership, PDF errors, math source, `blueprint/originality.py` (fatal at n = 8), `check_order.py`, spelling, display widths.

Second tranche (use as soon as each lands; until then the manual fallback in brackets): `lean/` + `tools/lean_check.py` + `tools/backtranslate_check.py` [S2b skipped]; `tools/check_numbers.py` over `verify/` [run the sidecars in a shell loop]; `tools/metrics.py` [record the metrics below by hand]; `tools/seed_errors.py` [plant errors by hand in a scratch copy]; `tools/check_notation.py` [Referee B and the seam referee check notation by reading].

---

## Order: waves (C4)

**Wave 0, before any new chapter.** Fix the pilot findings (C1); approve the exemplar and name it in STATUS; resolve NOTATION.md against Chapter 1 on reiteration; build the first-tranche tools; apply the accepted route changes to `book.yaml` and re-run `check_order.py`; regenerate the blueprints. Then, if time allows: set up `lean/` and run the anchoring pilot on Chapters 11–13's must-prove lists; plant 10 known errors in a copy of Chapter 11 and measure referee recall.

**Waves 1–N.** A wave is **3–4 chapters whose prerequisites are all approved**. Within a chapter, 3–4 drafting agents take about two sections each. A new wave opens when the previous wave's chapters pass S8; the author's S9 may trail one wave behind. Draft at most one dependency level ahead of approved text, so citations point at reviewed labels.

| Wave | Chapters | Why |
|---|---|---|
| 1 | 1–5, then 6, 7, 8 | Part 0's main line. The five logic chapters first, in order (1 and 2 split from the rewritten `propositional-natural-deduction`; 2 needs 1, 3 needs 1–2, 4 needs 1–3, 5 needs 4): the self-explanation training and the excluded-middle section are in Ch 5. Then sets (6), relations and induction (7), cardinality with Gate 0 (8). Pays Chapter 11's promises |
| 2 | 12, 9, 10 | 12 is the next level; 9 and 10 are optional and run beside it |
| 3 | 13, 14 | same level |
| 4 | 15, then 16 | a chain |
| 5 | 17, 22, 23 | 22 and 23 are optional and need only 11 |
| 6 | 18, then 19, 20, then 21 | Riemann–Darboux has low Mathlib coverage: give it an extra referee |
| 7+ | Part II, then Part III | as the blueprint levels allow |
| … | Parts IV and V **interleaved** | both need only Parts I–III |
| last | Part VI, then the capstone, then the whole-book pass | |

Chapter numbers are the 78-chapter `book.yaml`'s (Part 0's logic expanded to four chapters, 2026-09-28, everything from the old Chapter 3 on moving up by two; then Chapter 1 split in two the same day, everything from the old Chapter 2 on moving up by one more).

**Part pilots.** The first chapter of each Part goes through the pipeline **alone**, the author approves it, and only then does the Part fan out. At each Part pilot, measure referee recall on seeded errors (target ≥ 0.8).

---

## Per-chapter stages

Each stage: who, what the brief must contain, what it produces, exit criterion. Every agent in S2–S8 starts in a **fresh context** and never sees another reviewer's verdict unless the stage says so. Every finding carries a verdict (`correct` / `minor` / `gap` / `error`) and evidence: file:line plus a counterexample, a computation, or the quoted text.

### S1. Blueprint expansion (1 agent)
**Brief contains:** the stub `authoring/blueprints/chNN.md`; the curriculum node; the earlier chapters' label lists; STATUS's promises due to this chapter; the Chapter 11 blueprint as the model of depth; STYLE §11 (so it places the reader-alone items); the source books, for coverage only.
**Produces** a blueprint of about 3–4k words: labels; each must-prove statement with **all hypotheses**; a proof route citing specific earlier labels; examples, checks and exercises with intended answers; the 2–3 key proofs (§11.2); where the find-the-error, ordering, faded, try-it-first, R and (if last chapter of a Part) Gate items go; exit checks with marking-scheme outlines; the prerequisite ledger; notation additions; promises paid and opened.
**Exit:** `blueprint/check_blueprint.py` passes.

### S2. Blueprint verification (the most important stage)
**S2a, statement referee (1 agent).** Brief:
- "Your job is to find a false statement before it is built on. For every must-prove statement and every intended exercise answer, try small cases, boundary cases and degenerate cases (empty set, singleton, constant, zero, n = 1, endpoints), and hunt for a counterexample. Report each attempt, including those that failed."
- "For every proof route, open each earlier label it cites and confirm it says what the route needs, with the hypotheses the route has. Flag a route that uses a fact no earlier label provides."
- "Flag any route that rests on an exercise, on a later chapter, or on an optional result."
- "Check each statement's hypotheses are all needed: for each, name what fails without it, or say that it is redundant."

**S2b, Mathlib anchoring (optional until `lean/` exists).** One agent writes `lean/Book/ChNN.lean`, one `theorem <label> : <book statement over Mathlib objects> := <Mathlib lemma or short automation>` per must-prove item, with status `anchored` (compiles, no `sorry`), `stated` (compiles with `sorry`) or `n/a` (with a reason). A **third agent that never sees the book text** back-translates each Lean statement into English; `tools/backtranslate_check.py` and a judge compare hypothesis lists with the book's. Every mismatch is a finding. If the anchoring pilot anchors under about 30% of items, run S2b only for the high-coverage Parts (II, IV, VI core). For Riemann-setting chapters (17, 31, Part III's Riemann framing), replace S2b with a second independent statement referee.

**Exit:** no open finding; `check_blueprint.py` passes; the blueprint is **frozen** and its hash recorded in the ledger. A later change to a frozen blueprint re-opens S2 for the changed items.

### S3. Drafting (3–4 agents, about two sections each)
**Brief:** `authoring/DRAFTING.md`, plus the section assignment, the frozen blueprint, the exemplar chapter, and the promises this chapter pays. DRAFTING already requires sidecar scripts `verify/chNN/<label>.py`, the dependency ledger, checkable meta-claims, fitch.sty derivations, the R group, marking schemes, the Time line, and its reply format.
**The coordinator checks the reply** has every heading of DRAFTING's reply format, and copies the promises and ledger `(promised)` lines into a working list for S8 and S10.
**Exit:** every section delivered; blueprint deviations sent back to S2a before S5 starts on the affected sections.

### S4. Mechanical gates (scripts, no agent)
Run, on a clean copy: `./build.py check`; `tools/check_structure.py`; `tools/check_fitch.py`; `tools/promises.py`; in an introductory volume (fd1–fd3, and fd4 as it is drafted) `tools/check_beginner.py` on the chapter (advisory: its findings go to the drafter with the S4 output, and a finding the drafter keeps must be listed in the reply with a reason); the sidecars (`verify/chNN/*.py`, later `tools/check_numbers.py`); `./build.py html` and `pdf`, then `tools/check_rendered.py`; `blueprint/originality.py`; `tools/ledger.py` to register the chapter's blocks and hashes; Lean compile once `lean/` exists.
**Exit:** all pass. A failure goes back to the drafter with the tool's output; no referee reads the chapter until S4 is clean.

### S5. Two blind referees per section, and a beginner reader for new or reworded text
Referees A and B each get: the section, the frozen blueprint, the text of every label it cites, its dependency ledger, its sidecars, and the Lean statuses. Neither sees the other's report. Chunk by section pairs if needed for context. In an introductory volume (STYLE §13), **Referee C** also reads every section whose text is new or reworded.

**Referee A brief (proofs):**
- "Your job is to find a false or unjustified step. For every proof, idea and claim: name the reason for each step (hypothesis, definition, cited label) and check the cited label says that, with the hypotheses available here. A reason may be inline, in the block's Uses line (`::: {.uses}`, its last block) or in the dependency ledger (STYLE §13 B1–B2): a step whose source is in any of the three is justified. Do not ask for an inline citation of routine arithmetic or algebra; if a source is missing, the fix is a Uses entry or a ledger line."
- "Write out the quantifier order of every ε/δ/N argument and what each chosen constant depends on. Flag any constant that depends on something chosen after it."
- "For every exchange of limits, sums, integrals or derivatives, name the licensing theorem and check its hypotheses on the page."
- "Check each hypothesis of each theorem is used somewhere in its proof."
- "For each theorem, write a counterexample attempt with one hypothesis dropped, and report it."
- "Check each proof uses only earlier material, no exercise, and no optional result."

**Referee B brief (claims and bookkeeping); reads bottom-up, starting from the exercises:**
- "Your job is to find false sentences and missing bookkeeping. List every prose meta-claim (a sentence about the book's own text: 'the classical step comes later', 'everything else fails', 'we never used X') and check each against the page."
- "Check every table, and every claim of the form 'all/none/only', against the prose and the earlier sections."
- "Read each proof and list every fact it uses without an `@ref` (a reference in the block's Uses line is an `@ref`). Diff your list against the dependency ledger; each fact missing from the ledger is a finding, and each `chNN (promised)` source must be in STATUS's promise table. In an introductory volume the other direction counts too: a sentence with two or more inline references, or an inline citation of a routine step that STYLE §13 B2 leaves to the Uses line, is a `minor` finding (the fix moves it; it never deletes a source)."
- "Check notation against NOTATION.md: every symbol introduced before use, none with a second meaning. Check every meta-claim names the mathematics it is about, not a device of the page (STYLE §13 B3)."
- "Check the forward-reference budget (STYLE §12.1): no `@ref` to a result the reader has not met used as a reason, in a proof or in prose; in an introductory volume, at most one 'Looking ahead' box per section. Check effort is proportional to difficulty (§12.2): a trivial rule or notion read clause by clause, or a hard one rushed, is a finding. Close every second-reading fold and check the main line still teaches the section (§12.0)."
- "Check the worked examples obey the advice the section gives the reader, and the section obeys STYLE §9's checklist and §11's counts."
- "Look at the rendered page for anything check_rendered.py cannot see (a sentence that reads wrongly after rendering)."

**Referee C brief (a beginner reader; introductory volumes, new or reworded text only):**
- "You have just finished school and are reading this book alone, with no one to ask. Read the main line only, top to bottom, with every second-reading fold closed. Do not read the ledger, the blueprint, the sidecars or the Uses lines' sources. You may look back at earlier sections, but not ahead."
- "Report every place you stop, with file:line, the quoted text, a category, a severity and a plainer wording that keeps the mathematics: categories `process-jargon` (the book talks about how it was made: core track, fold, prompt, method box, Givens/Goal, ...), `undefined-term`, `citation-clutter`, `step-size` (too big a step, or a fuss over the obvious), `long-sentence`, `tone` (hedging, talking to readers of other books), `meta-talk` (sentences about the page itself), `notation-load` (a code like (Eq3) or a symbol you have to look up), `abstract-before-example`, `nominal-style`; severities `stuck` (you could not go on), `slowed` (you had to reread) and `annoyed` (you understood, but were interrupted)."
- "Give each section an overall difficulty from 1 to 5 and say in two sentences what made it hard."
- Verdicts: `stuck` is a `gap`, `slowed` a `minor`, `annoyed` a note. Each goes through S7 like any other finding, and the fix must not change the mathematics (a fix that does goes to Referee A). Referee C's verdicts are recorded per section in the review file, and in the ledger on the items it names (`--stage S5c`). The brief and categories are those of the readability audit (`authoring/design/beginner-readability-audit.md` §1).

Where a second model family is available, run one of A or B on it; otherwise vary the persona and reading order as above. At a Part pilot, also run both referees on a copy with seeded errors and record recall.
**Exit:** every ledger item has an A and a B verdict recorded; in an introductory volume, every new or reworded section has Referee C's report with no `stuck` left open.

### S6. Exercise verification (1 agent per chapter; 2 for a long chapter)
**Brief:**
- "Solve every B, C and R exercise **before** reading the book's solution. Then compare. Report every disagreement, and every solution that is incomplete or a sketch."
- "Check every numeric answer with a script of your own (not the drafter's sidecar)."
- "Confirm every B-type task has a worked example in the section."
- "Confirm each find-the-error item is flawed exactly where the solution says, and nowhere else; that at least one per chapter has a true conclusion; and that the solution's counterexample defeats the illegal step."
- "Confirm each proof-ordering solution's order is admissible and each distractor really fails; each faded blank has one reasonable completion."
- "Grade the book's own solution, and one different correct proof you write, against each marking scheme. Flag a scheme that fails your alternative proof or rewards wording."
- "Check each hint rung names a tool or a first line and does not execute the key idea; each R item hides its source and its solution names it with `@ref`."
**Exit:** verdicts recorded for every exercise.

### S7. Revision
The drafter or a fresh reviser fixes every `minor`, `gap` and `error`. A fix is accepted only when a **fresh re-referee, given the finding and the diff**, agrees. A dispute (the drafter says a finding is wrong) goes to a third agent with both arguments; if still open, to the author. Re-run S4 after the fixes.
**Exit:** no open finding; `tools/ledger.py --stale` empty for re-refereed items.

### Wording-only rewrites (S5e: equivalence re-review)
A rewrite whose purpose is the wording, not the mathematics (STYLE §13 applied to reviewed text; moving sources into Uses lines; renaming printed devices; splitting sentences; adding a worked instance before a statement), does not go back through S5 and S6 from scratch. Rule 4 still holds: every edited item's verdicts go stale, and each must get a fresh one.

**The rewrite (S3e).** One reviser per section (a strong model: wording quality is the point), given STYLE §13, the section, its ledger and the readability findings for it. The reviser keeps every label, every statement, every proof step in its order and every number; it may move a citation between the sentence, the Uses line and the ledger, but never drop one. It reports any change it could not make without touching the mathematics, and makes none of them: those are listed for the author.

**The equivalence re-referee (S5e).** One fresh agent per section, given the diff (old and new text side by side), the section's ledger and `tools/check_beginner.py`'s output on both versions. It checks, per ledger item:
1. the item's label, statement and proof steps correspond one to one with the old ones; a statement is word for word unless the item is a wording-only change to a statement, and then means exactly the same;
2. every `@ref` of the old text is still in the item, inline or in its Uses line, or its fact is in the ledger (an inline-to-Uses or Uses-to-ledger move is not a mathematical change, and needs no other review);
3. no new forward reference, no new reference to an exercise or an optional result, and no new fact used without a source;
4. every number is unchanged, and the sidecars still pass;
5. every new sentence is true (a new worked instance is checked like an example: its arithmetic, and a sidecar if it quotes a computed value).

It records one verdict per item, like S7r: `tools/ledger.py set <ch> <key> --stage S5e --verdict correct --by <agent> --evidence "wording only: <one line>"`, or `gap`/`error` with the line where the mathematics changed. A `gap` or `error` sends the item to Referee A (S5) and, for an exercise, to S6. Then Referee C reads a sample of the rewritten sections (five or six per volume, or every section of a chapter opening) to confirm the reading improved; its `stuck` findings go through S7.
**Exit:** every edited item has an S5e verdict `correct` (or has passed S5/S6 again); `tools/ledger.py stale` is empty; S4 is clean, including `./build.py check`; `check_beginner.py`'s counts for the section went down, and any finding kept is listed with its reason.

### S8. Seam referee (1 agent per chapter)
**Brief:**
- "Read `index.md` and the Chapter review page `review.md` against the sections: What you need, Time, Roadmap, Proof methods (formerly Named moves), Summary, Terms and Results used from earlier volumes are true of the delivered text. In an introductory volume, the opening is for someone who has not read the chapter (STYLE §13 B8): What you need has at most five items and five links, and the opening uses no word the chapter defines."
- "Find any result re-proved from an earlier chapter or section, and any result credited to the wrong place."
- "Run `tools/promises.py`: every promise this chapter owed is paid by a named, existing label; every promise it opened is in the list for STATUS and targets a chapter whose blueprint delivers it."
- "Check notation across the chapter's sections, and against the Part so far."
- "Check the chapter's entries in the spiral table (`curriculum.md`) are written out as STYLE §10 requires, and its R items reach back as §11.5 requires."
**Exit:** findings fixed through S7's acceptance rule.

### S9. Author sampling
Give the author, in one message: `index.md`; **one randomly chosen section** in full; every finding with verdict `error` or `gap`, with its fix; every dispute; and a stratified random sample of **3 proofs and 3 C-solutions** (draw them with a seeded random choice and record the seed). If the author finds any error the pipeline missed, the chapter returns to S5 with that class of error **added to the referee briefs** in this file, and it counts as an escape.

### S10. Release
The coordinator updates STATUS (state; promises opened and paid, each paid one verified against its label), confirms `tools/ledger.py --stale` is empty, deploys, and commits with the stage metrics in the commit body.

---

## Whole-book passes
- **After each Part:** a notation and consistency pass across the Part (symbol meanings, duplicate results, spiral recalls), run over disjoint chapter bands in parallel.
- **At the end:** a band-by-band whole-book pass; a TFAE and duplicate-result auditor; reading paths regenerated and verified (`tools/reading_path.py --verify`); every gate re-run; Lean re-compiled against the pinned Mathlib; a last seeded-error calibration.

---

## Metrics to record per chapter (research-production §7.1)

Into `authoring/metrics.csv` (by `tools/metrics.py` once it exists; by hand until then), and summarized in the S10 commit body.

- **Size:** prose words per section against budget; counts of results, proofs, examples, exercises; % of exercises with solutions (100%); exit checks present.
- **Findings per 10k words**, by severity and by stage: S2, S5 (A and B separately), S6, S8, S9. Pilot baseline: about 1 error and 5 findings per 10k words.
- **Escape rate** (headline): errors found at S8, S9 or in later chapters, over all errors in the chapter. Target 0 at S9.
- **Referee recall on seeded errors** at each Part pilot. Target ≥ 0.8.
- **Blueprint defects:** caught at S2, and those that reached S3 or later.
- **Lean** (once it exists): % anchored / stated / n-a; back-translation mismatches; faithfulness disputes.
- **Dependencies:** forward citations (0); proofs citing exercises (0); dependency-ledger lines; promises opened and paid.
- **Hygiene:** notation advisories; originality hits (0); rendered-lint hits (0); overfull boxes; stale verdicts at release (0).
- **Cost:** agents, tokens and wall-clock time per stage. Budget: about 6–9M tokens and 6–10 agent-hours per chapter (§7.2).
