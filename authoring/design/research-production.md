# Research: a production process for the remaining 70 chapters

Written 2026-09-28. It answers one question: how should the remaining 70 chapters be produced so that they are correct and consistent with each other?

The report draws on four bodies of evidence:
- published work on how reliable LLM proofs are, how well LLMs judge proofs, and autoformalization;
- the histories of the two finished sibling books (`~/coding/math-atlas/books/linear-algebra`, `~/coding/math-atlas/books/regression`);
- two read-only adversarial referee passes run on this book's pilot chapters for this report;
- this repository's plan (`blueprint/book.yaml`, the blueprints, STYLE, DRAFTING, decisions).

Every claim is tagged:
- **[E]** is evidence: a source, a measurement, or a record in a git log.
- **[O]** is my opinion or a design recommendation.
- **[U]** is a published figure I could not confirm in the primary source. Treat it as indicative only.

---

## 1. Summary

1. **[E] The pilots' mathematics is sound. Their errors are in prose and in bookkeeping.**
   - In Chapter 8, about 91 items were checked. The referee found 0 false theorems, 0 invalid proof steps and 0 wrong solutions.
   - It did find 2 false prose sentences and 4 dependency gaps. One of the gaps is that `lem-integer-part` quietly uses facts about ℤ that Chapter 4 has not yet provided.
   - In Chapter 1, 43 Fitch derivations and 21 truth tables were checked by script, and all 42 exercise blocks by reading. All of them were correct. The referee found 2 errors: a false meta-claim about a proof, and a Lean cell that renders wrongly.
   - This is the same pattern the linear-algebra referees recorded chapter after chapter: "None found an error in a theorem, a proof or a solution. They found false sentences in prose, an exercise answered True that is false…"
2. **[E] Blueprints are where false mathematics enters.**
   - In linear-algebra, drafters and referees caught the blueprint wrong 3, 7, 9 and 10 times per chapter in Chapters 18–23. The errors included false inequalities, wrong hypotheses, and a proof route "that would have produced a false proof".
   - This book's 70 remaining blueprints are auto-generated stubs of about 550 words. The hand-written pilot blueprint for Chapter 8 runs to about 3,500 words, with labels and proof routes. Expanding the blueprints is therefore both unavoidable and the stage where mathematics is most likely to go wrong. It needs its own verification.
3. **[E] Self-review is weak. Independent review with a reference works.**
   - LLMs do not reliably correct their own reasoning without an outside signal (Huang et al. 2024).
   - Judges grade their own proofs worse than other models' proofs (OPC 2025).
   - Verify-and-refine loops with a separate verifier give large gains (Huang & Yang 2025).
   - Judges given a reference solution and a marking scheme agree best with experts (ProofBench 2025).
   - Unguided multi-agent debate does not beat self-consistency (Zhang et al. 2025).
4. **[E] Mathlib already covers most of this book's named theorems.** A Lean check of theorem **statements** against Mathlib is feasible for a large fraction of the must-prove lists. Its known failure mode is a statement that compiles but is not faithful to the book's statement (a 3–29 point gap in 2026 benchmarks). Faithfulness must therefore be checked separately. **[O]** The payoff is highest at the blueprint stage.
5. **[O] Recommended process.**
   - Work chapter by chapter in dependency order, in waves of 3–4 concurrent chapters. Do not draft a whole Part at once, which is what regression did.
   - Each chapter goes through a fixed pipeline: blueprint → blueprint verification (including Mathlib anchoring) → draft → gates → two independent referees with different briefs → exercise verification → revision → seam referee → human sample.
   - Every review verdict is recorded in a ledger keyed by a content hash, so an edit makes the verdict stale.
6. **[O] Rough cost.** About 6–9M tokens and about 5–7 agent-hours per chapter, so roughly 0.45–0.65B tokens and 350–500 agent-hours for 70 chapters. That is about 3–5 weeks of wall-clock time with author review as the bottleneck. Assumptions are in §7.

---

## 2. External evidence

### 2.1 How LLM proofs fail

- **[E]** Petrov et al., *Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad*, arXiv 2503.21934 (2025). https://arxiv.org/abs/2503.21934
  - Human experts graded the proofs. Gemini 2.5 Pro scored about 24%; every other model scored under 5%.
  - Four failure classes, in order of frequency: **logic** (unjustified steps; the commonest), **assumption** (an unproven or false assumption), **creativity** (a wrong strategy), and **algebra/arithmetic** (the rarest).
  - Models always claimed success, generalized from small cases, and invented citations.
  - LLM judges inflated scores by up to about 20×.
- **[E]** Guo et al., *Mathematical Proof as a Litmus Test*, arXiv 2506.17114. https://arxiv.org/abs/2506.17114
  - 200 problems, 60 of them at undergraduate level, with 10 fine-grained error types.
  - Some reasoning models were fully correct on under 20% of problems.
  - "Self-reflection is insufficient."
- **[E]** Putnam-AXIOM, arXiv 2508.08292. https://arxiv.org/abs/2508.08292
  - On Putnam problems with the variables and constants changed, o1-preview dropped from 41.9% by 19.6 points.
  - That points to memorization.
  - **[O]** The risk carries over to this book. Textbook-standard theorems are exactly where a model reproduces a remembered proof, and it may reproduce it with the wrong hypotheses for *this* book's definitions. For example, ℕ contains 0 here, and the Riemann integral is built from Darboux sums.
- **[E]** Frontier capability is no longer the bottleneck.
  - Gemini Deep Think reached 35/42 at IMO 2025, officially graded.
  - DeepSeekMath-V2 scored 118/120 on Putnam 2024 (arXiv 2511.22570).
  - **[U]** Several systems were reported at 42/42 at IMO 2026.
- **[E] Expert-written mathematics also carries errors that LLM flagging can find.**
  - Epoch reported that an AI-assisted review flagged fatal errors in about a third of FrontierMath problems (https://x.com/EpochAIResearch/status/2053995435870892048).
  - **[U]** Secondary reports put the corrections at about 42% of problems, found by LLM flagging and confirmed by mathematicians.
- **[E] The closest analogue to this project.** Deng & Shum, *From Lecture Notes to Lean: Formalizing a Textbook on Probability Theory*, arXiv 2607.27298 (2026). https://arxiv.org/html/2607.27298
  - An agent formalizing the notes found a false theorem: additivity of the Riemann–Stieltjes integral was missing a hypothesis that appeared elsewhere in the book but not in the statement. The agent produced a counterexample.
  - Formalization also exposed many hypotheses that were "carried by context" rather than stated.
  - Referee G2 in this book's Chapter 8 (§3.1 below) belongs to the same class.

### 2.2 LLMs as proof judges

- **[E]** Ma et al., *Reliable Fine-Grained Evaluation of Natural Language Math Proofs* (ProofBench/ProofGrader), arXiv 2510.13888. https://arxiv.org/abs/2510.13888
  - The best judge was a strong reasoning model **given a reference solution and a marking scheme, with simple ensembling**.
  - It reached a mean absolute error of 0.926 on a 0–7 scale against experts.
  - Both the reference solution and the marking scheme measurably helped.
- **[E]** Dekoninck et al., *Open Proof Corpus*, arXiv 2506.21621. https://arxiv.org/abs/2506.21621
  - Two human graders agreed on 90.4% of proofs.
  - The best LLM binary judges scored 85–91%: GPT-5 89.3% single run and 90.8% by majority vote; Gemini 2.5 Pro 85.4% and 88.1%.
  - Almost every model judged **its own** proofs worse than other models' proofs.
- **[E]** Luong et al., IMO-Bench (DeepMind), arXiv 2511.01846.
  - Its ProofAutoGrader, which works from grading guidelines, correlated well with human grades. **[U]** Reported values are r ≈ 0.93–0.96.
  - Disagreements were mostly at the boundary between "partial" and "incorrect".
- **[E]** Grayzel, arXiv 2608.00004 (2026): a **unanimous "all judges pass" rule** across three cheap judges gave the best precision. The author flags this as a post-hoc finding.
- **[E]** Mahdavi et al., arXiv 2511.13027: LLM judges are highly sensitive to the prompt.
- **[O] What this means here.** An LLM referee is about as reliable as a single human grader. It misses subtle gaps more often than outright errors. It works best when given:
  - the statement;
  - an independent reference, such as a second proof, the Lean statement, or the blueprint's must-prove text;
  - a checklist.

### 2.3 Self-correction and multi-agent patterns

- **[E]** Huang et al., *LLMs Cannot Self-Correct Reasoning Yet*, ICLR 2024, arXiv 2310.01798.
  - Self-correction without outside feedback made GPT-4 on GSM8K worse: 95.5% → 91.5% → 89.0%.
  - With an oracle signal it improved to 97.5%.
- **[E]** Huang & Yang, arXiv 2507.15855.
  - A loop of generating a proof, getting a bug report from a *separate* verifier prompt, refining, and accepting only after repeated clean verifications solved 5/6 IMO 2025 problems with each of three models.
  - Best-of-32 baselines scored 21–38%.
- **[E]** DeepSeekMath-V2: a trained verifier used as the reward model, with verification compute scaled to keep a "generation–verification gap".
- **[E]** Zhang et al., *Stop Overvaluing Multi-Agent Debate*, arXiv 2502.08788.
  - Debate usually fails to beat chain-of-thought or self-consistency at equal compute.
  - Model **heterogeneity** is what helps.
  - **[U]** arXiv 2605.00914 reports that agents in homogeneous debate copy their peers' wrong answers.
- **[O] Design rules that follow:**
  - Referees work in fresh contexts, never see the drafter's reasoning, and never see each other's verdicts.
  - Referees get different briefs, so they fail differently.
  - Where available, a second model family acts as one referee.
  - A revise loop ends only when an *independent* re-review is clean. The drafter saying "fixed" does not end it.

### 2.4 Autoformalization and Lean

- **[E]** Poiroux et al., arXiv 2406.07222 (EMNLP 2025).
  - The published Lean 4 ProofNet had 31.8% misformalized entries.
  - The best statement autoformalization reached 45.1% on undergraduate statements.
- **[E]** Zhang et al., *Beyond Compilation*, arXiv 2606.31002 (2026).
  - On 400 graduate-level statements, every system showed a gap of 3–29 points between compiling and being faithful. The best compiled 89.5% but was faithful on only 60.5%.
  - The typical faults were dropped hypotheses, changed domains and weakened conclusions.
  - A consensus judge built from two different LLMs agreed with the human majority 89.7% of the time.
- **[E]** Faithfulness checks that work:
  - round-trip formalization with an equivalence check (arXiv 2604.25031);
  - back-translation with an entailment (NLI) check (arXiv 2509.22246);
  - comparing against an existing Mathlib statement, which is how Anthropic's FLT formalization (Sep 2026) certified its main statement: https://www.anthropic.com/research/formalizing-fermats-last-theorem
- **[E]** Gloeckle et al., *Automatic Textbook Formalization*, arXiv 2604.03071 (Meta, 2026). https://arxiv.org/html/2604.03071
  - A graduate textbook of more than 500 pages became 130k lines of Lean in one week, using about 30k Claude agent runs.
  - Cost was about $100k, or $300 per target statement.
  - Every change was gated by two reviewer agents, one checking mathematical faithfulness and one checking engineering. Humans only spot-checked.
  - Failures: objects defined several times over, and "agent churn" around a broken definition.
  - **[O]** Full formalization of the book's proofs costs too much here. Statement-level anchoring is the affordable part.
- **[E]** TaoBench, arXiv 2603.12744: provers lose about 26% when problems use Tao's own from-scratch definitions instead of Mathlib's.
  - **[O]** Book statements should be translated onto *Mathlib's* objects. For the few chapters that build their own objects (the constructions of Part 0 and Chapters 19–20), keep them informal.
- **[E] Blueprint tooling.**
  - LeanBlueprint (Massot): https://github.com/PatrickMassot/leanblueprint
  - verso-blueprint, the Lean-native version that tracks `sorry` and draws dependency graphs: https://github.com/leanprover/verso-blueprint
  - Tao's *Analysis I* Lean companion (2025) paraphrases Chapters 2–11 of his textbook in Lean, builds its own Riemann integral, and ties its custom definitions to Mathlib's in "epilogue" sections: https://github.com/teorth/analysis
  - **[O]** This book's engine already has its own label graph, so neither blueprint tool is needed. A small `lean/` directory keyed by book labels gives the same benefit.

### 2.5 What Mathlib covers

Sources:
- https://leanprover-community.github.io/undergrad.html
- https://leanprover-community.github.io/undergrad_todo.html
- https://leanprover-community.github.io/mathlib-overview.html

Coverage by Part:

| Part | Mathlib coverage (**[E]** from the pages above, unless marked) | Statement-check feasibility **[O]** |
|---|---|---|
| 0 logic, sets, cardinality | Propositional and first-order logic are native (`tauto`, `decide`). Sets, functions, `Cardinal`, Cantor, Schröder–Bernstein, Zorn. | High, but little value: logic statements can also be checked by `tools/check_fitch.py`. |
| I real line | ℝ as a conditionally complete linearly ordered field; sSup/sInf; Archimedean; limits, lim sup/inf, Cauchy; Bolzano–Weierstrass; series tests; IVT, EVT, uniform continuity (Heine–Cantor); derivatives, Rolle, MVT, Taylor; uniform convergence; power series. **The Riemann/Darboux integral is not a Mathlib API.** `intervalIntegral` is a Lebesgue/Bochner integral, Riemann sums exist only through `BoxIntegral`, and improper integrals are listed as TODO. | High, except Chapter 15 (Riemann–Darboux) and improper integrals: anchor those through `BoxIntegral`, or leave them informal. Note that sSup in Mathlib is total (`sSup ∅ = 0` on ℝ), so the book's "non-empty and bounded above" hypotheses must stay explicit. |
| II metric spaces, several variables | Metric and topological spaces, compactness, connectedness, completeness, Banach fixed point, Heine–Borel, **Arzelà–Ascoli**, **Stone–Weierstrass**, Baire, Fréchet derivative, **inverse and implicit function theorems**, **Picard–Lindelöf**, Grönwall. Peano existence **[U]**. Jordan content: not found. | High for Chapters 21–28 and 30–31. Chapter 29 (Riemann integral on ℝⁿ): low. |
| III Fourier (Riemann setting) | Fourier series on `AddCircle`, Riemann–Lebesgue, Parseval, Fourier transform on L¹ and L², Plancherel, inversion, Schwartz space. **Dirichlet and Fejér are TODO.** | Medium. The book's Riemann-setting statements need restating in Lebesgue form, which is itself a faithfulness risk. |
| IV measure and integration | Measures, Carathéodory, Lebesgue measure, MCT, Fatou, DCT, Fubini–Tonelli, change of variables, Lp and its completeness, Hölder, Radon–Nikodym, Lebesgue differentiation (through Vitali families) **[O: from memory, verify]**; BV and absolutely continuous functions only partly. | High. |
| V complex analysis | Cauchy integral formula on discs, Liouville, maximum modulus, analyticity of holomorphic functions **[O: from memory, verify]**. General homotopy Cauchy theory, the Riemann mapping theorem, Picard and Weierstrass products: probably absent **[O]**. | Medium for Chapters 52–54, low for 55–59. |
| VI functional analysis | Hahn–Banach, open mapping, Banach–Steinhaus, Riesz lemma, Hilbert spaces (projection, Riesz representation, Lax–Milgram), Banach–Alaoglu, Gelfand transform, spectral theory of compact operators (partial), distributions (partial) **[O: verify]**. Sobolev and Rellich: not found. | High for Chapters 60–66, low for 69–72. |

**[O] Estimate.** About 55–65% of the must-prove statements can be anchored to Mathlib. Parts II, IV and VI (core) are the highest, and the Riemann-integral and later complex/PDE chapters the lowest. The first job of Wave 0 (§5.1) is to measure this on real statements.

---

## 3. Local evidence

### 3.1 The two pilot referee passes (2026-09-28, for this report)

Each pass was one fresh agent. Read-only, it checked every statement, proof, check and solution, with python/sympy and a scratch Fitch/truth-table checker.

| | Ch 8 (least upper bound) | Ch 1 (connectives) |
|---|---|---|
| Items checked | ~91 (21 results, 13 examples, 7 checks, 44 exercises / ~120 parts) | ~150 (43 derivations, 21 truth tables, ~22 number proofs, 16 Lean cells, 7 checks, 42 exercise blocks) |
| Errors | 2, both prose: §05:86 says the classical step comes after the proof, but it happens inside; §07:160 says "everything else fails in ℚ", contradicting its own table | 2: §03:199 false meta-claim ("never assumes n odd"); §07:92 `\|` inside a code span renders as invalid Lean |
| Gaps | 4, all dependency-type: powers monotone used before proved (§06:111); ℤ facts used by `lem-integer-part` and not listed as promised; field identities outsourced to the linear-algebra book despite `index.md` saying otherwise; n > 0 by informal induction before ℕ is defined | 1: a model "contrapositive" proof that is really the RAA costume §05 tells readers to avoid |
| Minor | 7 (notation used before definition, degenerate intervals, n = 1 caveat) | ~11 (Lean terms called tactics, `absurd` ≠ ⊥E, "§01" vs "Section 1.1", NOTATION.md contradicts the chapter on reiteration) |
| Found by | reading proofs against the rule system, blueprint and STATUS; edge cases and computation found **nothing** | reading and cross-section consistency; one build-output check; mechanical Fitch/truth-table checks confirmed a clean result and found **nothing** |
| Cost | ~190k tokens, ~25–30 min | ~170k tokens, ~20–25 min |

**[E] Density.** About 1 error per 12k words and 1 finding of any severity per 1.5–2k words. **No** error in a theorem, proof or solution.

**[O] Two lessons.**
1. Referee briefs must name the actual risk surfaces: prose meta-claims, dependency bookkeeping, and rendered output. "Check the proofs" alone will pass these chapters while the errors that exist slip through.
2. Part I–VI chapters will be harder than these two, since they have longer proofs, more ε-management and more interchange of limits. Expect the proof-error rate to rise. Petrov's taxonomy says the errors will be logic and assumption errors, not algebra.

### 3.2 linear-algebra (26 chapters, ~1.9M raw words, written 2026-09-16 → 09-25)

What worked **[E]** (from `git log` and `authoring/STATUS.md`):

- **The per-chapter workflow, from Chapter 22 on.** Five section pairs each went draft → referee → revise on their own clock. Then an index was written against the delivered text, a **consistency referee** read the seams, and one pass applied its findings. That was 18 agents per chapter, "no failures".
  - The seam referee caught a section re-proving an earlier one, a result credited to the wrong chapter, a promise pointing at the wrong exercise, and an honesty ledger two entries short.
- **Referees found blueprint errors with counterexamples.** Examples: a false matrix AM–GM, a Cholesky bound with the wrong index, the Gram–Schmidt rate uκ where it is uκ², and a pointer to a theorem that "would have produced a false proof".
- **Gates born from incidents.**
  - `check_forward_deps.py` (no citation of a later section), made kind-aware and fatal for proofs.
  - Proof-ownership tests: two proofs were invisible to the gate because of how the scanner attributed them.
  - PDF errors made fatal: 38 of 178 sections had shipped damaged PDFs.
  - A non-ASCII-in-math test: pdflatex silently dropped a degree sign, so the page read "less than 13".
- **"Prove it, or state it with credit and mark it unproved, with nothing depending on it."** Seven referees tested this rule in one chapter.
- **The coordinator verifies ticks instead of applying them.** In the whole-book pass (M7) one band reported a promise unpaid that was in fact paid on a named line.

What went wrong **[E]**:

- Chapters 0–3 were rewritten wholesale on day 2, and Chapter 3 was restructured again on 09-24 ("linear maps before linear systems"). The early chapters were drafted before the exemplar and structure had settled.
- **Proofs relied on exercises** "seven times", with 44 candidate sites left for triage. There were transitive chains: Perron → a Chapter 9 proposition → an exercise.
- Notation drift was deferred to M7 (proof endings, numbering style for theorem parts).
- Hand-written reading paths were "wrong in every entry, always understating".
- Promises were made that could not be kept:
  - "Loewner proved later": needed an import, (A7).
  - "roots depend continuously; needs complex analysis": false on both counts.

### 3.3 regression (45 chapters, ~0.85M words, written 2026-09-19 → 09-21)

- **[E] Drafted Part by Part, 4–7 chapters per commit, in about 3 days, with no recorded per-chapter referee.**
- The read-only whole-book audit afterwards found **71 items, 17 of them major**. Among them:
  - a proof citing a proposition "which says the opposite";
  - Var(SSE) proved twice with disagreeing hypotheses;
  - a residual plot justified in a regime where it is false;
  - one bold **R** carrying three meanings;
  - `\G` and `\A` each with two meanings in one chapter;
  - index pages naming labels that state something else;
  - 32 chapters understating their prerequisites;
  - four proofs citing later chapters.
- **[E]** About half the older exercises still have no solution, and 38 pages lacked full A/B/C groups until a clean-up pass.
- **[E] What regression got right.** "Every computed number comes from `code/chNN/`", checked by `tools/check_numbers.py` (6,794 quoted values), so a changed number cannot go unnoticed.
- **[O] The contrast is the main lesson.** Batches of a whole Part without per-chapter referees are fast, but they push the errors into a whole-book audit. By then errors have compounded across chapters, and fixing them means touching finished text. linear-algebra's per-chapter referee workflow cost about 3× the agents and found blueprint-level falsehoods *before* they were built on.

### 3.4 This repository today

- **[E]** 72 chapters, 3,745 planned pages, and about 1.5–1.8M words at the pilots' density (about 420 words per page).
- Blueprints: 2 hand-written (Chapter 8 is about 3.5k words), 70 generated (about 550 words each, with no labels and no proof routes).
- Gates present: `check_forward_deps.py`, `check_optional.py`, proof ownership, PDF errors, math source, `originality.py`, `check_order.py`.
- **Missing:** Lean, a computation sidecar, a claim ledger, a structure lint, a rendered-output lint, a notation or promise tracker.
- **[E] Dependency structure** (from the blueprints' prerequisite lines, within each Part):
  - Levels in Part I, as the blueprints list them: level 1 is Chapter 8; level 2 is 9 and 18; level 3 is 10 and 11; then 12, then 13, then 14, 19 and 20, then 15, then 16 and 17. Chapter 18 sits at level 2 only because its prerequisite line is thin. Read as a whole it comes last in Part I.
  - Cross-Part needs (`external_prerequisites`) make the Parts sequential, except that **Parts IV and V both need only I–III** and can run side by side.
  - Chapter 8 already carries about 9 forward promises into Chapters 2–5, so Part 0's main line must come first.

---

## 4. Principles (all **[O]**, each grounded in the evidence above)

1. **Verify statements before writing proofs.** False mathematics enters through blueprints (§3.2). Statement errors are also cheap to catch before prose exists and expensive after.
2. **Never let the author of a text be its only reviewer** (§2.3). Every verdict comes from a fresh context with a different brief, and ideally at least once per chapter from a second model family.
3. **Give every judge a reference**: the blueprint's must-prove text, the Lean-anchored statement, a checklist, or an independent solution (§2.2).
4. **Mechanize everything that can be mechanized**, and gate on it. Keep referee attention for meaning.
5. **Make review stale on edit.** A verdict is bound to a content hash of what it reviewed.
6. **Aim at the observed risk surfaces**: prose meta-claims, dependencies and hidden hypotheses, exercise solutions, notation, and rendered output (§3.1, §3.3).
7. **Keep batches small, but let many run at once.** Draft at most one dependency level ahead of approved text, so citations target reviewed labels, not promises.
8. **Measure the process.** Plant known errors to measure referee recall, and sample for the human.

---

## 5. The pipeline

### 5.1 Order and batch size

**Wave 0: preparation (before any new chapter).**
- The author reviews the pilots and fixes the §3.1 findings.
- Approve an exemplar and record it in STATUS.
- Resolve NOTATION.md versus Chapter 1 on reiteration.
- Build the tools of §6.
- Set up `lean/`: Mathlib pinned, cache fetched.
- Run the statement-anchoring pilot on the must-prove lists of Chapters 8–10, to measure what fraction anchors and how many faithfulness failures occur.
- Seed-error calibration: plant 10 known errors in a copy of Chapter 8 and measure referee recall.

**Waves 1–N: chapter waves.**
- A wave is **3–4 chapters** whose prerequisites are all approved. Within a chapter, sections are drafted by 3–4 agents, as in the pilots.
- A new wave opens when the previous wave's chapters pass their gates. Author approval can trail one wave behind.
- Proposed order:

| Wave | Chapters | Why |
|---|---|---|
| 1 | 2, 3 (then 4, 5 as soon as 3 lands) | Part 0 main line; pays Chapter 8's promises |
| 2 | 9, 6, 7 (optional constructions) | 9 is the next level; 6 and 7 are off the main line and run in parallel |
| 3 | 10, 11 | same level |
| 4 | 12, then 13 | chain |
| 5 | 14, 19, 20 | 19 and 20 are optional and need only 8 |
| 6 | 15, then 16, 17, then 18 | Riemann–Darboux has low Mathlib coverage, so give it more referee budget |
| 7+ | Part II (21 → 22, 23, 30 → …), then Part III | as the blueprint levels allow |
| … | **Parts IV and V interleaved** | both need only Parts I–III |
| last | Part VI, then the capstone (72), then a whole-book pass | as linear-algebra's M7 |

- **The first chapter of each Part is a Part pilot.** It goes through the pipeline alone, and the author approves it before that Part fans out. Register, notation and proof density change sharply between Parts (logic → ε-δ → measure → complex → functional analysis).
- **Why not a whole Part at once:** that is regression's pattern and its audit bill (§3.3).
- **Why not strictly one chapter at a time:** the 18-agent workflow keeps several chapters busy, and chapters at the same dependency level do not cite each other.

### 5.2 Per-chapter stages

Each stage lists who does it, what it takes in, what it produces, and the exit criterion. Findings go to the claim ledger (§6, `tools/ledger.py`).

**S1. Blueprint expansion.**
- One agent turns the 550-word stub into a pilot-grade blueprint of about 3–4k words: labels, a statement for each must-prove item with **all hypotheses**, a proof route citing specific earlier labels, examples, checks, exercises with their intended answers, exit checks, the prerequisite ledger, notation additions, and the promises paid and opened.
- It reads the curriculum node, the earlier chapters' label lists, and the source books (for coverage only).

**S2. Blueprint verification.** This is the new stage, and the most important.
- **S2a, statement referee** (fresh agent). For every statement and every intended exercise answer, it tries small cases and boundary cases and hunts for a counterexample. It checks that every cited earlier label says what the route needs, and that no route depends on an exercise or a later chapter.
- **S2b, Mathlib anchoring** (a separate agent). For each must-prove statement it writes `lean/Book/ChNN.lean`:
  - `theorem <label> : <book statement over Mathlib objects> := <Mathlib lemma or short automation>`
  - Statuses: `anchored` (compiles with no `sorry`), `stated` (compiles with `sorry`: well-typed but unverified), or `n/a` (with a reason: the object is book-specific, or the topic is not in Mathlib).
  - A **third agent**, which never sees the book text, back-translates each Lean statement into English. A script and a judge compare the hypothesis lists with the book's. Any mismatch is a finding.
- **Exit:** no open findings. The blueprint is frozen and its hash recorded.

**S3. Drafting.** As now in DRAFTING.md, with three additions:
1. Every non-trivial computation and every chosen constant gets a sidecar script, `verify/chNN/<label>.py`, instead of an unrecorded CAS session.
2. Every section ends with a **dependency ledger**: each fact a proof uses that is not an `@ref`. G2 in Chapter 8 would have surfaced here.
3. Every prose sentence that asserts a mathematical fact about the book ("the classical step comes afterwards", "everything else fails") must be checkable against something on the page.

**S4. Mechanical gates** (`./build.py check` plus the new tools). All must pass before a human or referee reads anything:
- forward dependencies and proofs citing exercises;
- the optional-result gate;
- the section-structure contract;
- rendered HTML and PDF lint;
- the Fitch and truth-table checker (Part 0);
- the sidecar computations;
- Lean compile;
- originality;
- spelling;
- display widths.

**S5. Adversarial referees.** Two per section, in fresh contexts, blind to each other. They get the section, the frozen blueprint, the labels it cites, the ledger entries, and the Lean statuses.
- **Referee A, proofs:** every step's reason; quantifier order and what each constant depends on; hypotheses of every limit interchange; each hypothesis used. It must write a counterexample attempt for each theorem with a dropped hypothesis.
- **Referee B, claims and bookkeeping:** every prose meta-claim; consistency between the section's tables, its prose and earlier sections; the dependency ledger against what each proof actually uses; notation against NOTATION.md; the section's worked examples against the style advice it gives itself.
- **Where feasible:** one of the two runs on a different model family (§2.3). If that is not available, use a different prompt persona and a different reading order (B reads bottom-up, from the exercises).
- **Verdicts are per ledger item:** correct / minor / gap / error. Each non-correct verdict carries evidence (file:line, a counterexample, or a computation).

**S6. Exercise and solution verification** (one agent per chapter).
- It solves every B and C exercise **before** reading the book's solution, then compares the two.
- It checks every numeric answer with a sidecar script.
- It confirms every B-type task has a worked example, and the flawed-proof exercise really is flawed exactly where the solution says.
- **[E] Why this stage exists:** linear-algebra had "an exercise answered True that is false", and regression left half its exercises unsolved.

**S7. Revision.**
- The drafter, or a fresh reviser, fixes the findings. A fix is accepted only when a **fresh** re-referee on the diff agrees (Huang & Yang's acceptance rule).
- Disputes, where the drafter says a finding is wrong, go to a third agent with both arguments. If still unresolved, they go to the author.

**S8. Seam referee** (one per chapter), as linear-algebra did:
- index versus sections;
- re-proofs of earlier results;
- promises paid and opened (`tools/promises.py`);
- notation collisions across the chapter;
- the chapter's contribution to the spiral table.

**S9. Human sampling** (the author).
- Read `index.md`, **one randomly chosen section in full**, every finding with verdict `error` or `gap` (with its fix), and every dispute.
- Stratified random sample: 3 proofs and 3 C-solutions.
- If the author finds any error the pipeline missed, the chapter goes back to S5 with that class of error added to the referee briefs.
- **[O]** This is acceptance sampling. The escape rate it measures is the book's real quality metric.

**S10. Release.**
- STATUS is updated by the coordinator. The coordinator *verifies* each "paid" claim against a label (§3.2).
- Deploy, and commit with the stage metrics in the message body.

### 5.3 Whole-book passes

- **After each Part.** A notation and consistency pass across the Part: symbol meanings, duplicate results, spiral recalls. It runs as a workflow over disjoint chapter bands, as linear-algebra's M7 did.
- **At the end:**
  - an M7-style pass;
  - a TFAE/duplicate auditor;
  - reading paths regenerated;
  - a re-run of all gates;
  - Lean re-compile against a pinned Mathlib;
  - one last seeded-error calibration run.

---

## 6. Tools to add

All **[O]**. Names follow the repo's conventions.

| Tool | What it checks | Origin of the need |
|---|---|---|
| `tools/check_structure.py` | The STYLE contract per section: opening frame; ≥1 check followed by a sibling solution; ≥1 warning; `## Exercises` with A/B/C headings; every `exr-` followed by a `.solution`; Idea present for proofs over 3 lines; prose word count within 2.5–5k; `[Name]` titles; C items include an exit check and a flawed-proof exercise per chapter. Fatal. | regression's unsolved exercises and missing groups (§3.3) |
| `tools/check_fitch.py` (+ truth tables) | Parses the `\fsc`/`\fhyp`/`\rulename` arrays. Checks line availability, box scope, rule shape, cited lines and RAA placement, and evaluates every truth table. Supports a `% expect-invalid` marker for deliberate non-examples. Start from the Chapter 1 referee's scratch `fitch.py` and `tt.py` (in this session's scratchpad). Extend to ∀/∃ for Chapter 2. | 43 derivations in Chapter 1 alone; checked by script in minutes |
| `tools/ledger.py` → `authoring/ledger/chNN.yaml` | Extracts every result, proof, example, check and exercise with its label, kind and a **content hash**. Stores verdicts (stage, reviewer, model, verdict, evidence) and Lean status. `--stale` lists verdicts whose hash no longer matches. `check` fails on a stale or missing verdict for a released chapter. | "the coordinator verifies ticks"; review invalidated by later edits |
| `lean/` (lake project, Mathlib pinned) + `tools/lean_check.py` | Compiles `lean/Book/ChNN.lean`. Maps declaration names to book labels. Reports anchored / stated / n-a per label. Forbids `sorry` in anything the ledger marks anchored, and forbids `axiom`. | §2.4, §2.5 |
| `tools/backtranslate_check.py` | Sends each Lean statement, without the book text, to a judge that writes it in English. Then diffs its hypotheses and conclusion against the book statement. Outputs a mismatch list for the referee. | the gap between compiling and being faithful (§2.4) |
| `verify/chNN/*.py` + `tools/check_numbers.py` | Runs every sidecar. Each script asserts the values the text quotes, with the label as the key, and fails if a quoted value in the source disagrees with the script. | regression's `code/chNN` + `check_numbers.py` (6,794 values) |
| `tools/check_rendered.py` | Lints `_build/html` and the PDF logs: backslash in `<code>`; raw TeX or `\qedhere` in the page; red MathJax error nodes; `??`; code blocks that should be prose (indented continuation). | Chapter 1's `\|`; regression's `\qedhere` and sentences printed as source code |
| `tools/promises.py` | Finds prose pointers ("Chapter N", "in Chapter N") without an `@ref`. Reconciles them with STATUS's promise table. When a chapter is drafted, lists the promises it must pay and verifies each paid one names an existing label. | linear-algebra's 50 → 3 open promises; Chapter 8's 9 promises into Part 0 |
| `tools/check_notation.py` | Collects symbols introduced in definitions ("write", "denote", `\coloneqq` in a def block) and macro uses per chapter. Flags a symbol that gains a second meaning within a Part, and a symbol missing from NOTATION.md. Advisory. | regression's bold R, `\G`, `\A` |
| `check_forward_deps.py --exercises` made fatal for proof/idea/claim kinds, with an allow-list in the ledger for attribution-only citations | proofs resting on exercises | linear-algebra's "seven times"; Chapter 8's G1 (§01 B1(b)) |
| `blueprint/check_blueprint.py` | Labels unique book-wide; every label a blueprint cites exists in an earlier approved chapter or is created earlier in the same chapter; every must-prove item has a ledger entry and a Lean status; the prerequisite ledger is a subset of the DAG. | linear-algebra's blueprints wrong 3–10 times per chapter |
| `tools/metrics.py` | Produces §7's per-chapter table from the ledger, `check` output and git. Appends to `authoring/metrics.csv`. | measuring the process |
| `tools/seed_errors.py` | Copies a chapter to the scratchpad and plants N known errors from a catalogue (drop a hypothesis, swap quantifiers, off-by-one in a constant, false prose claim, solution to the wrong variant). Scores referee recall. | calibrating referees (§2.2: about 85–90% judge accuracy) |

Existing tools stay in the gate: `check_optional.py`, proof ownership, PDF errors, `originality.py` (make it fatal at n = 8), `check_order.py`, and `_measure.html`.

---

## 7. Metrics and cost

### 7.1 Metrics to track per chapter (**[O]**, all from `tools/metrics.py`)

- **Size and completeness:**
  - prose words per section against budget;
  - results, proofs, examples, exercises;
  - % of exercises with solutions (target 100%);
  - exit checks present.
- **Findings per 10k words, by severity and stage:** blueprint (S2), referee A and B (S5), exercises (S6), seam (S8), human (S9).
  - Pilot baseline: about 1 error and about 5 findings of any severity per 10k words.
- **Escape rate:** errors found at S8, S9 or in later chapters, divided by all errors in the chapter. This is the headline number. Target: 0 at S9.
- **Referee recall on seeded errors:** measured per Part pilot. Target ≥ 0.8.
- **Blueprint defects caught:** S2 findings, and defects that reached drafting.
- **Lean:**
  - % of must-prove statements anchored / stated / n-a;
  - back-translation mismatches;
  - faithfulness disputes.
- **Dependencies:** forward citations (0); proofs citing exercises (0 unexcused); dependency-ledger items; promises opened and paid.
- **Hygiene:** notation advisories; originality hits (0); rendered-lint hits (0); LaTeX overfull boxes; stale verdicts (0 at release).
- **Cost:** agents, tokens, wall-clock time per stage.

### 7.2 Cost and time estimate (**[O]**, with its assumptions)

**Assumptions:**
- An average chapter has 7 sections and about 22k words (3,745 pages × about 420 words per page ÷ 72).
- A full-read referee pass on 25k words costs about 170–190k tokens and 20–30 minutes (**[E]**: the two pilot referee runs). Drafting a section costs 0.3–0.6M tokens, including reads of STYLE, the blueprint and the exemplar, build loops and CAS checks. **[O]**: inferred from those runs; drafting tokens were not measured.
- Tokens are mostly cached context re-reads. Output is about 3–5% of the total.
- One model family, except where a second is used for referee A or B.

| Stage | Agents per chapter | Tokens per chapter | Agent-time |
|---|---|---|---|
| S1 blueprint | 1 | 0.4–0.6M | 30–45 min |
| S2 verification: statements + Lean + back-translation | 3 | 1.0–2.0M (Lean compile loops dominate) | 60–120 min |
| S3 drafting (3–4 agents, 2 sections each) | 3–4 | 1.5–2.5M | 90–150 min |
| S4 gates | 0 (scripts) | ~0 | 5–10 min of build time |
| S5 referees (2 per section, chunked by section pair) | 6–8 | 1.2–1.8M | 90–120 min |
| S6 exercises | 1–2 | 0.4–0.6M | 30–45 min |
| S7 revision + re-referee | 2–4 | 0.8–1.2M | 45–90 min |
| S8 seam | 1 | 0.2–0.3M | 20–30 min |
| **Total per chapter** | **~18–23** | **~6–9M** | **~6–10 agent-hours** |

For 70 chapters:
- **About 0.4–0.65B tokens and 400–700 agent-hours.**
- Add about 10% for Wave 0, the per-Part passes and the final M7.
- Tokens only; convert with current pricing and cache rates.

**Wall-clock time:**
- With a wave of 3–4 chapters, each running 6–10 agents at a time, a chapter completes in about 4–8 hours. **[E]** linear-algebra's 18-agent chapters took 4–11 hours between commits.
- That gives 8–12 chapters per day of machine time, so **about 7–10 days of machine time** for 70 chapters.
- **The binding constraint is S9.** At about 45–60 minutes of author time per chapter (one section plus findings plus samples), that is about 60–70 author-hours. Spread across the waves, this puts the realistic calendar at **3–5 weeks**.
- For comparison, **[E]** regression took 3 days and linear-algebra about 9. Each then spent days on whole-book repair.

**Lean one-off:**
- Setup: installing elan/lake and fetching the Mathlib cache (about 5 GB) takes about 1 hour. The machine has 24 cores and 60 GB of RAM, which is adequate.
- About 1–2 agent-days to build `lean_check.py` and the Chapter 8–10 anchoring pilot.
- If less than about 30% of must-prove items anchor in that pilot, drop S2b to the high-coverage Parts only (II, IV, VI core). **[O]**

---

## 8. What this does not settle

- **[O] Whether a second model family is available.** The evidence for heterogeneity is strong (§2.3), but this setup runs on Claude. Without another family, rely on different briefs, blind contexts and seeded-error calibration.
- **[U]/[O] Mathlib coverage for Parts V and VI** is from memory and needs checking against `Mathlib/Analysis/Complex/*`, `MeasureTheory/*` and `Analysis/Distribution/*` during Wave 0.
- **[O] Riemann-setting chapters** (15, 29, and Part III's Riemann framing) have no good Mathlib target. Give them an extra independent referee in place of S2b.
- **[E] No published study measures the error rate of an AI-written textbook.** The per-10k-word baselines here come from this book's two pilots and the siblings' records, and they will move once Part I proofs get long.
