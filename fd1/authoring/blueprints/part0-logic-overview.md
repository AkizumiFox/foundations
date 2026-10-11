<!-- hand-written -->
# Part 0 logic block: overview of Chapters 1–5

One page for the coordinator and the drafters: how the five logic chapters divide the material, where the former pilot Chapter 1 (`src/ch01-propositional-natural-deduction/`, seven sections, refereed S2–S8; now archived in `authoring/pilot-archive/`) went when the author split it into Chapters 1 and 2 (2026-09-28), and how Chapter 5 hands over to the rest of the book. The two chapters are drafted as `src/ch01-connectives-and-derivations/` and `src/ch02-negation-and-classical-logic/`, and Chapter 3 as `src/ch03-semantics-soundness-completeness/`. The chapter blueprints (`ch01.md` … `ch05.md`) are binding; this file only maps them.

## The author's direction for the logic chapters (2026-09-28)

Much more weight, early, on the logic of Fitch-style proof: long form, more explanation, more examples; go slowly. **Each section introduces one new thing.** **Each rule is defined directly by its Fitch schema** (an `nd` block with metavariables \( \varphi, \psi, \chi \), `\vdots` gaps and the `% schema` marker, inside the definition block), followed by a clause-by-clause reading. Every rule section has 3–5 worked derivations of increasing difficulty, each with an Idea saying why each rule was chosen (goal-directed and premise-directed reasoning, introduced in Chapter 1 §03, built up rule by rule, systematized in Chapter 2 §06, extended to quantifiers in Chapter 4 §08), "how this rule looks in a mathematical proof", common errors, a Quick check, and A/B/C exercises; 3,000–5,000 words per section. Chapters 1, 2 and 4 are written this way; Chapters 3 and 5 keep their form.

## The division

| Ch | Slug | Question it answers | Level reference (depth only) | Sections (one new thing each) |
|---|---|---|---|---|
| 1 | `connectives-and-derivations` | What is a derivation, and what are the rules for "and", "implies", "or"? | Huth & Ryan §1.1–1.2.1 | §01 statements and connectives; §02 the derivation format (no boxes); §03 \( \wedge \)I, \( \wedge \)E; §04 \( \to \)E; §05 \( \to \)I and the box (scope, repetition, the full `def-derivation`); §06 \( \vee \)I; §07 \( \vee \)E, proof by cases |
| 2 | `negation-and-classical-logic` | What are the rules for "not", "iff" and contradiction, which of them are classical, and how do I find a derivation? | Huth & Ryan §1.2 | §01 \( \neg \)E, \( \bot \)E, vacuous truth; §02 \( \neg \)I, \( \sqrt 2 \) irrational; §03 derived rules (MT, CP, DS); §04 \( \leftrightarrow \) and definitions; §05 RAA and classical logic (\( \neg\neg \)E, LEM, De Morgan, Peirce, interderivability); §06 finding derivations (the method, the rules in one place) |
| 3 | `semantics-soundness-completeness` | Are the rules right — do they prove exactly the truth-table consequences? | §1.3–1.5 (no Horn, no SAT) | formulas, parse trees, unique readability; `ax-induction`, `thm-strong-induction`, `thm-structural-induction`; valuations, \( \models \); `thm-soundness` and `thm-completeness`, both proved in full; CNF/DNF; adequate connectives |
| 4 | `predicate-logic` | What are the rules for "for every", "there exists" and "=", and what do their side conditions protect? | §2.1–2.4 | §01 predicates and quantifiers; §02 terms, substitution; §03 \( \forall \)E; §04 \( \forall \)I; §05 \( \exists \)I; §06 \( \exists \)E; §07 equality and \( \exists! \); §08 translation; §09 quantifier laws; §10 uniformly continuous \( \Rightarrow \) continuous, rule by rule; §11 models (the last main-line section); §12 first-order soundness (**optional**: `thm-first-order-soundness` and everything else in it is `.optional`) |
| 5 | `from-derivations-to-prose` | How do derivations become the prose mathematicians write, and how do I read, write and check that prose? | — | the rhetoric dictionary; four levels of abbreviation; the self-explanation training passage; `exm-not-allowed-catalogue` (N1)–(N11); the excluded-middle dispute |

Then Part 0 continues: 6 sets and functions, 7 relations and induction, 8 cardinality (Gate 0); Part I starts at Chapter 11.

## The rule system (one decision for all five chapters)

- Primitive: \( \wedge \)I/E, \( \to \)I/E, \( \vee \)I/E, R (Chapter 1); \( \neg \)E, \( \bot \)E, \( \neg \)I, \( \leftrightarrow \)I/E, **RAA** (Chapter 2); \( \forall \)I/E, \( \exists \)I/E, =I/E (Chapter 4).
- RAA is the only classical rule. "PBC" is not a separate rule (it is RAA under another name). \( \neg\neg \)E, LEM, MT, contrapositive, DS, De Morgan are **derived** (Chapter 2), each proved once and then used as one line (`def-derived-rule`, Chapter 2 §03).
- \( \bot \)E is kept primitive although RAA derives it, so that "all primitive rules but RAA" is the intuitionistic system of Chapter 5 §07 (the remark is in Chapter 2 §05).
- Every rule name has a `fitch-book.sty` macro; the derived rules without one are cited with `\by{…}{…}`.
- **Single-rule labels.** Where a section introduces one half of an I/E pair, that half gets its own label (`def-rule-implication-elimination`, `def-rule-disjunction-introduction`, `def-rules-contradiction`, `def-rule-universal-elimination`, `def-rule-existential-introduction`), and the pair label (`def-rules-implication`, `def-rules-disjunction`, `def-rules-negation`, `def-rules-universal`, `def-rules-existential`) sits in the section of the other half, whose definition block recalls the first schema. The pair labels are the ones later chapters cite.
- **Tool gap (coordinator):** `tools/check_fitch.py` rejects a box that does not begin with an assumption and the \( i \)–\( i \) citation of such a box, so every \( \forall \)I schema and derivation (a flagged box `\open[x_0]` with no assumption line) fails the gate until the tool accepts flagged boxes. Checked on 2026-09-28.

## Where the pilot Chapter 1 went (history)

The pilot chapter `src/ch01-propositional-natural-deduction/` (now `authoring/pilot-archive/ch01-propositional-natural-deduction/`) was the material reused and expanded in the split; the current chapters are `src/ch01-connectives-and-derivations/` and `src/ch02-negation-and-classical-logic/`. The *Migrates* line of each section of `ch01.md` and `ch02.md` gives the passage-level detail.

| Drafted section | New home |
|---|---|
| 01 statements-and-connectives | Ch 1 §01 (almost whole; exercise labels kept) |
| 02 conjunction-implication-derivations | the reading of a derivation → Ch 1 §02; the \( \wedge \) rules, `exm-product-in-unit-interval`, `prp-and-commutes` → Ch 1 §03; \( \to \)E → Ch 1 §04; \( \to \)I, the box, `def-derivation`, `prp-implication-transitive`, `prp-curry`, the scope warnings and the exercises → Ch 1 §05 |
| 03 disjunction-and-cases | \( \vee \)I and one direction of `exm-cases-on-hypothesis` → Ch 1 §06; the rest (\( \vee \)E, the absolute-value examples, `prp-distributivity`, the exercise labels) → Ch 1 §07 |
| 04 negation-and-contradiction | \( \neg \)E, \( \bot \)E, ex falso, vacuous truth, `thm-square-even-implies-even` (new proof by cases and \( \bot \)E) → Ch 2 §01; \( \neg \)I, the \( \neg P \approx P \to \bot \) remark, `thm-sqrt2-irrational`, the √3/√4/√6 exercises (labels `exr-negation-and-contradiction-*` kept) → Ch 2 §02; MT, CP, DS, `def-derived-rule` and the proof-ordering item → Ch 2 §03 |
| 05 biconditional-and-definitions | Ch 2 §04 (whole) |
| 06 reductio-and-classical-rules | Ch 2 §05 (with `prp-peirce` moved in from 07) |
| 07 finding-derivations | Ch 2 §06 (the search method, the worked searches, the rules in one place, the R group) |

The older pilot `src/ch01-logic-connectives/` (archived in `authoring/pilot-archive/`) was mapped into the drafted chapter earlier; its truth tables went to Chapter 3, and its annotating, writing and checking material and the "costume" examples to Chapter 5 §01, §05, §06 (`ch05.md`'s migration list).

## Labels that must survive the split

**Chapter 11 cites exactly these eleven** (Chapter 11 S8 seam review, table (a)); they keep their names:
- in Chapter 1: `def-rules-disjunction`, `exm-abs-product-cases`, `exm-triangle-inequality-cases`;
- in Chapter 2: `exm-square-plus-one`, `thm-sqrt2-irrational`, `def-rules-negation`, `prp-contrapositive`, `prp-vacuous-implication`, `exr-negation-and-contradiction-c1`, `prp-equivalence-cycle`, `def-rule-raa`. The exercise label embeds the drafted §04 slug; Chapter 2 §02 keeps the slug `negation-and-contradiction`, but the label is kept exactly in any case, since exercise labels are global ids.

The Chapter 3–8 blueprints cite further labels, all kept: `def-statement`, `def-derivable`, `def-derivation`, `def-rules-conjunction`, `def-rules-implication`, `def-rule-schema` (new, Chapter 1 §02), `prp-distributivity`, `exm-search-postpone-or`, `def-rules-biconditional`, `def-derived-rule`, `prp-ex-falso`, `prp-disjunctive-syllogism`, `prp-double-negation`, `prp-de-morgan`, `prp-excluded-middle`, `prp-iff-two-implications`, `prp-contrapositive-converse`, `prp-implication-as-disjunction`, `prp-peirce`, `thm-classical-rules-interderivable`, `thm-square-even-implies-even`, `thm-squares-order`, `exm-skeleton-odd-product`. Positions other blueprints rely on, preserved by the split: Chapter 2 §06 C2 is \( \vdash (P \to Q) \vee (Q \to P) \); Chapter 2 §06 B1(b) is \( \neg(P \to Q) \vdash P \wedge \neg Q \); Chapter 1 §01 holds Argument A and Argument B.

## Induction arrives early

Chapter 3 needs induction for soundness and completeness. It states `ax-induction` (a basic property of ℕ, taken as given) and proves `thm-strong-induction` and `thm-structural-induction`. Chapter 7 cites these and does not re-derive them; it keeps well-ordering (and its equivalence with induction), recursion on ℕ, and the induction pitfalls. Chapter 1 §03 C1 (a "first bad line" argument) is a deliberate preview, with a signpost to Chapter 3 (`@thm-strong-induction`, in the solution).

## How Chapter 5 hands over to the rest of the book

- **Level 3 prose from Chapter 6 on.** Chapter 5 §03 defines the four levels and `def-silent-steps` (which rules may go unstated). Chapters 6–8 may still use level-2 rule tags (`[\( \rulename{\forall I} \)]`, STYLE §10: Part 0 only); from Chapter 11 on, proofs are level 3 with no tags.
- **The dependency parenthesis.** "Choose \( N \) (depending on \( \varepsilon \))" is explained in Chapter 4 §10 and Chapter 5 §02 as the record of open \( \forall \)I boxes; STYLE §4's rule "say what each constant depends on" now has its logical justification, and later chapters may point to Chapter 5 §02.
- **The catalogue.** Warnings in every later Part cite `@exm-not-allowed-catalogue` with the entry number (N1)–(N11) when the error is one of them (STYLE §10). Its entries point back to Chapter 1 §05 (the converse, scope, availability), Chapter 1 §07 (cases), Chapter 2 §05 (a wrong negation) and Chapter 4 §04, §06, §09, §10 (quantifiers).
- **Self-explanation.** The one training passage is Chapter 5 §04; every later *Before reading on* prompt assumes it (STYLE §11.1).
- **Checking.** The two-column check of Chapter 5 §06 is the method behind every later find-the-error item; after Part 0 the solution names the missing hypothesis or illegal step instead of the rule (STYLE §10).
- **Non-constructive steps.** Chapter 5 §07 is where later chapters point when they flag a use of LEM (Bolzano–Weierstrass bisection, the sup of a non-located set) or of choice (Chapter 8's `ax-choice`).
- **Lean.** The rule / phrase / Lean table is started in Chapter 1, continued in Chapter 2 and completed in Chapter 4 §07; the Lean column of the dictionary (Chapter 5 §01–§02) is the last place Lean appears systematically.

## Chapter 11's prose pointers into Part 0

Chapter 11 (the pilot Part I chapter, formerly ch08, then ch10) already uses the split numbering: "Chapter 1" for proof by cases and the absolute-value examples, "Chapter 2" for \( \sqrt 2 \), the negation rules, the contrapositive and the equivalence cycle (Chapter 11 S8 seam review: every chapter number it gives for a Chapter 1 or 2 label is right). Remaining items: the quantifier-negation law (`prp-quantifier-negation`, Chapter 4 §09) is a prose pointer in Chapter 11 §05 and becomes `@ref`-able **once Chapter 4 is drafted**; induction is Chapter 3 (`ax-induction`, `thm-strong-induction`); well-ordering and recursion are Chapter 7; countable sets are Chapter 8. (The former item "Chapter 1 explains why a statement with no instances counts as true" is obsolete: Chapter 11 §02 cites `@prp-vacuous-implication` directly.) The STATUS promise rows "full proof of soundness" and "¬¬P ⊢ P, P ∨ ¬P not derivable without RAA; the people who refused the rule" are paid by Chapter 3 §05 and Chapter 5 §07.

*(Done: the STATUS rows that gave drafted-chapter homes "Ch 1 §04–§07" were re-pointed to Chapter 2 §01–§06, and the Chapter 1 rows' section numbers updated, at Ch 1 S7 and the Ch 1/Ch 2 S8 seams.)*

## Open for the author

- `blueprint/book.yaml`'s Chapter 4 outline still lists the former nine sections; `ch04.md` now has twelve (one rule per section).
- Chapter 1's exit check (2) in book.yaml is a printed direction of `prp-distributivity`; `ch01.md` replaces it by an unprinted sequent of the same shape (reason there). Chapter 2's exit checks for LEM and De Morgan (d) coincide with results its text proves (see `ch02.md`).
- *(Done, history.)* `NOTATION.md` has the row for the schema metavariables \( \varphi, \psi, \chi \) from Chapter 1 §02, and its pointers for \( \dashv\vdash \), \( \mathsf{X} \), \( \mathsf{Y} \), \( d \mid n \) name Chapter 2.
