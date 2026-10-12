# fd1 *Logic and Proof*: the deepening plan (D)

**Status.** This is the plan that fixes the target. It comes from the gap matrix (`gap-matrix.md`, about 110 rows against twelve books), the twelve book reports, the five frozen or delivered blueprints (`ch01-revision.md` as delivered; `ch0{2,3,4,5}-revision.md`, frozen at S2 on 2026-10-12, not yet drafted), the atlas (`registry/chapters.yaml`, `plan-edges.yaml`, `fields.yaml`), and greps of fd2, fd3, fd4 and an1 for `@fd1:` and "*Logic and Proof*" (2026-10-12). Following the standing instruction to run the pipeline autonomously, the author-level decisions are made here; §7 lists them for the author's S9 review.

**Binding rules (in addition to STYLE §11–§12 and every rule of the frozen blueprints that this file does not replace):**
1. **No label is lost or renamed.** All 81 labels cited downstream, and every other label, keep their names and content. Some labels move to another section or chapter; §4.4 lists each one. Heading ids that other volumes cite are kept.
2. **Chapter 1's arrangement is fixed.** The six sections, their order, their titles and their one new thing per section all stay. Chapter 1 is deepened inside its sections, in its index, and in its exercises.
3. **Technique only.** No prose, example, exercise, sequent list or figure is taken from any of the twelve books, nor closely paraphrased. Classic named items (the barber, the drinker sentence, tonk, Carroll's tortoise, Darapti, Russell's theorem, the two-node Kripke model) are folklore, but each gets fd1's own wording, mathematical dress and numbers. S2 checks every new example, drill and exercise against the twelve books, as `ch02.md` already does for Huth & Ryan.
4. **The frozen revision blueprints still stand** except where §5 lists an item as superseded. Each chapter is drafted **once**, from its frozen R-blueprint together with its D-addendum.

---

## 1. Diagnosis: where fd1 is thin

fd1 is already **deeper than every comparison book** in four areas: Fitch derivations taught rule by rule, named search moves, the derivation-to-prose dictionary, and graded A/B/C/R exercises with full solutions (matrix rows 3.1, 5.1, 7.1, 7.10; device row "graded tiers"). Its thinness is elsewhere, and it is structural, not cosmetic:

**(a) Semantics gets a fraction of what derivations get.** fd1 teaches meaning only as a referee for derivations: one row refutes, soundness converts. Every book but Hurley treats semantics as a subject in its own right, with its own methods and vocabulary.
- *No search method.* Refuting rows are found by insight, using the forced cases of "working backwards from F" in 3.3 (row 2.2). There is no branching, no backtracking and no tree (row 2.4), and there is no procedure for finding counter-models (rows 4.4, 4.7).
- *No vocabulary of consistency.* The word "consistent" never appears with its logical meaning (row 2.7). Missing too are: the reduction of entailment, equivalence and tautology to unsatisfiability (row 2.6); the ⊢/⊨ parallel table (row 3.5); and the words contingent, contradictory and contrary (row 2.5).
- *No direct semantic proofs.* Nowhere does the reader argue "let M be any structure …" (row 4.6).

**(b) Theories, models of theories, definability and isomorphism are absent** (rows 4.9–4.12). This is the single largest gap, and four books point to it (vD, En, LPL, Ha). It is also the one that later volumes pay for:
- fd2's orders and equivalence relations, fd4's groups and fields, and fd3 6.5's isomorphism transfer all use "axioms as sentences, and their models";
- yet fd1 never writes an axiom system down, never proves independence with a model, and never proves that isomorphic structures satisfy the same sentences.

**(c) Identity stops at ∃! and "at most one"** (rows 6.2–6.4). fd1 lacks all of the following:
- counting with ≠ (at least, at most or exactly *n*);
- the trap that distinct letters need not name distinct objects;
- "the *x* such that φ" as licensed by ∃!, which is the logic behind every "the limit" in analysis;
- a function symbol set against its graph, which is fd2's definition of a function.

**(d) Translation is drilled lightly** (rows 1.5, 1.6, 4.2, 4.3). Section 1.1 covers only "if", "only if", "necessary" and "sufficient". There is no phrase book, no catalogue of mistranslations, no minimal pairs, no A/E/I/O square, no fixed vocabulary across a graded set, and no reading of a formula back into words.

**(e) Metatheory is not spoken about honestly** (rows 3.13, 3.18, 5.6–5.9).
- The words object language and metalanguage do not appear, although Chapter 3 proves theorems about derivations.
- Completeness never pays off in shorter derivations: there is no TAUT step.
- First-order completeness, compactness and decidability are not even stated.
- The dependence of δ on ε is never named as a function (Skolem).

**(f) Exercise volume and variety are low for a reader working alone.** The A2 drill banks hold 8–12 parts, against 15–40 short items per rule in LB, Hurley and Lemmon (exercise table, first row). Several item types are missing entirely:
- derive-or-refute, with the verdict withheld (the defining format of LPL);
- give an example or explain why it is impossible;
- one-step, missing-premise and fill-the-justification items;
- changed-semantics soundness;
- false-thesis induction;
- build a model, separate two structures, define this notion by a formula;
- a fixed-key symbolization set;
- dialogue extraction.

**(g) Pedagogical devices the books share and fd1 lacks** (device table):
- assumptions annotated with the rule that will close them;
- rule-instance galleries;
- "Not allowed" blocks;
- flowcharts for decision methods;
- arrow and Hasse pictures of finite structures (the ch04 revision plans some);
- the Ho/LB counterexample set as one idea running through the volume;
- a checklist for induction proofs;
- chapter summaries, terms lists and a glossary;
- an opening quiz of tempting misreadings.

**What is *not* thin and must not be diluted.** The one-system design (Fitch only, with every connective primitive), the mathematical register (school mathematics first, analysis as the payoff), full solutions, and the Chapter 5 hand-off to prose. No book's philosophical register, multiple proof systems or English-only example base comes in.

Hard constraint: almost every section is already at or near STYLE's **5,000 main-line words** (frozen budgets: 2.5 ≤ 4,600, 2.6 ≤ 4,900, 3.4 ≤ 4,500, 3.6 ≤ 4,700, 4.6 ≤ 4,950, 4.11 ≤ 4,950). Deepening therefore needs **new sections**, not only richer old ones. Chapter 1 is the exception: its sections run 2,800–4,500 words, which leaves about 6,000 words of headroom for content inside the fixed arrangement.

---

## 2. Target table of contents

**Shape.** The volume moves from 5 chapters and 38 sections to **6 chapters and 47 sections**. Of the 9 new section files, 5 are new core sections, 1 is the second half of the old 4.11, and 3 are optional sections; the 6th chapter is a new one on models and theories. The volume then has three parts, which mirror each other:

| Part | Chapters | Rules | Meaning |
|---|---|---|---|
| Propositional | 1–3 | 1, 2 (rules) | 3 (truth, soundness, completeness) |
| First-order | 4–5 | 4 (quantifier rules) | 5 (models and theories) |
| Prose | 6 | — | — (the hand-off to fd2) |

Keys: **K** kept; **E** expanded in place; **N** new; **M** moved or renumbered; **opt** = `.optional` (nothing depends on it). The words column gives the main-line budget, which is binding; folds are budgeted separately in each D-addendum.

### Chapter 1: Connectives and Derivations (F1.1). Arrangement unchanged

| § | Title | Key | Words | What is added |
|---|---|---|---|---|
| index | (as is) | E | ≤ 1,300 | Opening quiz, "Five tempting misreadings", each answer pointing to a section. Closing "Summary" and "Terms" blocks. |
| 1.1 | Statements, Arguments and How to Break One | E | ≤ 5,000 | Phrase book; the counterexample set; stock breakers; weak readings; two ways to attack an argument |
| 1.2 | Derivations, Starting with And | E | ≤ 5,000 | Instance gallery; goal lines; one-step and fill-the-justification drills |
| 1.3 | Using an Implication: Modus Ponens | E | ≤ 4,300 | Gallery; whole-line warning; Carroll's tortoise (fold); missing-premise items |
| 1.4 | Proving an Implication: the Rule of the Box | E | ≤ 5,000 | Purpose-annotated assumptions; dependency sets; two errors that cancel |
| 1.5 | Or, Introduced | E | ≤ 4,300 | A failed early choice redone; derive-or-break begins |
| 1.6 | Using Or: Proof by Cases | E | ≤ 5,000 | Affirming a disjunct; constructive dilemma; translate-then-derive; sequent battery |

### Chapter 2: Negation, Classical Logic and Finding Derivations (F1.2)

| § | Title | Key | Words | What is added |
|---|---|---|---|---|
| 2.1 | Contradiction: Using a Negation | E | ≤ 3,600 | Paradoxes of material implication; "name the rule you reject" |
| 2.2 | Proving a Negation | E | ≤ 2,600 | Generalising a proof: √2, then √3, then √p |
| 2.3 | Derived Rules: Proved Sequents as New Rules | E | ≤ 3,300 | Constructive dilemma and MPT; Popper on MT; a "Not allowed" block |
| 2.4 | Iff, Equivalence, and What a Definition Says | E | ≤ 3,700 | The lemma ¬(P ↔ ¬P); a TFAE item; criticising definitions |
| 2.5 | Proof by Contradiction and the Classical Rules | E | ≤ 4,800 | When RAA is needed; the paradox that needs RAA; restricted rule sets |
| 2.6 | How to Find a Derivation | E | ≤ 5,000 | The detour rule; three new moves |
| **2.7** | **Four Kinds of Task** | **N** | ≤ 4,600 | Theorem, equivalence, **inconsistency (derive ⊥)**, derive-or-break; standard-sequent library; Curry (C) |

### Chapter 3: Truth, Soundness and Completeness (F1.3)

| § | Title | Key | Words | What is added |
|---|---|---|---|---|
| 3.1 | Formulas as Objects | E | ≤ 4,600 | Object language and metalanguage; repairing almost-formulas; Polish notation (C) |
| 3.2 | Induction on Numbers and on Formulas | E | ≤ 4,900 | Induction checklist; sets built from a base (fold); a recursion non-example; false-thesis and inventor's-paradox items |
| 3.3 | Valuations and Truth Tables | E | ≤ 3,900 | Truth-functionality; the game reading; a backward-computation drill; tonk (fold); two puzzles |
| 3.4 | Tautologies, Entailment and Equivalence | E | ≤ 5,000 | Contingent, contradictory and contrary; **satisfiable and consistent sets**; reductions to unsatisfiability; "one row against every row"; the rows-as-regions picture |
| **3.5** | **Hunting for a Refuting Row** | **N** | ≤ 4,600 | The counterexample set searched systematically: forced moves, splitting, the search drawn as a tree, a closed tree as a proof of ⊨, testing a set for satisfiability, a flowchart, refutation tactics |
| 3.6 | Soundness (was 3.5) | M, E | ≤ 4,200 | A two-level box (object and metalanguage); rule-circularity; satisfiable implies consistent; "test the subgoal"; changed-semantics and nonstandard-semantics items |
| 3.7 | Completeness (was 3.6) | M, E | ≤ 5,000 | Consistent iff satisfiable; the ⊢/⊨ table completed; **the TAUT step**; structural properties of ⊢; Kreisel (fold); a remove-a-rule item |
| 3.8 | Normal Forms and Adequate Connectives (was 3.7; second pass) | M, E | ≤ 5,000 | Calculating with equivalences; **positive and negative occurrences, and monotonicity**; the set-algebra bridge; interpolation (C) |
| **3.9** | **Compactness and Maximal Consistent Sets** | **N, opt** | ≤ 4,500 | Lindenbaum; truth lemma; completeness for infinite Γ; compactness; graph colouring |

### Chapter 4: Predicate Logic and the Quantifier Rules (F1.4)

| § | Title | Key | Words | What is added |
|---|---|---|---|---|
| 4.1 | Predicates and Quantifiers | E | ≤ 5,000 | ∀ read as a long "and" over a finite domain; existential import; staged translation; minimal pairs |
| 4.2 | Terms, Formulas, Free Variables and Substitution | E | ≤ 4,400 | Repair items; simultaneous and sequential substitution; partial terms |
| 4.3 | Using "For Every": Instantiation | E | ≤ 3,500 | Gallery with compound terms; ∀E as ∧E over {0, 1, 2}; "is this application correct?" drill |
| 4.4 | Proving "For Every": Let x Be Arbitrary | E | ≤ 4,200 | Critiques inside the section; relation-property derivations |
| 4.5 | Proving "There Exists": Exhibit a Witness | E | ≤ 3,400 | Gallery; derive-or-break items |
| 4.6 | Using "There Exists": Name a Witness | E | ≤ 5,000 | The twin figure (∃E beside ∨E); the trapped contradiction; **the barber and Russell's theorem**; finite choice |
| 4.7 | Equality (∃! moves to 4.8) | E | ≤ 4,000 | Leibniz's Law; an opacity warning; the logical half of extensionality |
| **4.8** | **Unique Existence, Counting and Descriptions** | **N** | ≤ 4,800 | ∃! (moved from 4.7); at least, at most and exactly *n*; only, except and superlatives; **"the x such that φ"**; a function symbol against its graph |
| 4.9 | Translating Mathematics (was 4.8) | M, E | ≤ 4,600 | A traps gallery; one fixed ℕ key over 20 items; "infinitely many" against "eventually"; the propositional core; why induction and the supremum property are second-order (box) |
| 4.10 | Negating and Moving Quantifiers (was 4.9) | M, E | ≤ 4,800 | The A/E/I/O square; contrary and contradictory; twin-law boxes; prenex form and alternation; the replacement step; drinker and Darapti (C) |
| 4.11 | Uniformly Continuous Implies Continuous, Rule by Rule (was 4.10) | M, E | ≤ 3,600 | **Witness functions δ(ε) and δ(ε, x)**; the game reading; critique of a "proof" of the converse; R items |

### Chapter 5: Models and Theories (new; atlas id **F1.6**)

| § | Title | Key | Words | Source |
|---|---|---|---|---|
| index | Models and Theories | N | ≤ 1,000 | The motivating problem: *do the group axioms prove that xy = yx?* No derivation search can settle it; a model of two letters can. |
| 5.1 | Structures and Satisfaction | M, E | ≤ 4,600 | First half of old 4.11, with the frozen R4 §4.11 plan kept. New: arrow and Hasse pictures; evaluating in two structures; game reading; **direct semantic proofs** |
| 5.2 | Counter-models | M, E | ≤ 4,600 | Second half of old 4.11. New: **the counter-model procedure**; small domains by expansion; the hierarchy tautology ⊂ valid ⊂ true in ℕ; "a failed search proves nothing" |
| 5.3 | Theories and Their Models | N | ≤ 4,800 | Axioms as sentences (equivalence relations, orders, groups, fields); consistency and **independence by a model**; separating sentences; describing every model |
| 5.4 | Definability and Isomorphism | N | ≤ 4,200 | A formula defines a set; ∃ as projection; isomorphic structures satisfy the same sentences; automorphisms prove non-definability; R items |
| 5.5 | Soundness for Predicate Logic (was 4.12) | M, opt | 5,178, unchanged | Old 4.12, kept |
| 5.6 | What First-Order Logic Can and Cannot Say | N, opt | ≤ 4,200 | Completeness (stated, with a Henkin sketch in a fold); compactness, with "finite" shown not first-order; Löwenheim–Skolem; non-standard ℕ; undecidability; incompleteness named |

### Chapter 6: From Derivations to Mathematical Prose (F1.5; was Chapter 5)

| § | Title | Key | Words | What is added |
|---|---|---|---|---|
| 6.1 | The Connective Rules in Prose | M, E | ≤ 4,900 | Rows for constructive dilemma and TFAE cycles; spoken assumption purposes |
| 6.2 | The Quantifier Rules in Prose | M, E | ≤ 4,200 | Rows: "it suffices to prove something stronger", "the limit", double inclusion |
| 6.3 | Four Levels of One Proof | M, E | ≤ 4,200 | The "it suffices to show" chain |
| 6.4 | Reading a Proof: Self-Explanation | M, E | ≤ 2,400 | Argument extraction; naming the unstated fact |
| 6.5 | Writing a Proof | M, E | ≤ 2,800 | A generalisation item |
| 6.6 | Checking Proofs, and What Is Not Allowed | M, E | ≤ 3,000 | (N12)–(N14) appended; improper-but-valid; dialogue R item |
| 6.7 | The Dispute over Excluded Middle | M, E | ≤ 3,900 | Table of which direction of each law survives without RAA |
| **6.8** | **Stages of Knowledge: Kripke Models** | **N, opt** | ≤ 3,600 | Two- and three-node countermodels; heredity; soundness of the rules without RAA |

### Why these, and why not the others

- **Model chapter inserted as Chapter 5, prose moved to Chapter 6.** This was the main structural choice. The alternative was to append models as a Chapter 6 after prose, which needs no renumbering. That was rejected for three reasons:
  1. Rules followed by meaning is the volume's own pattern (Chapters 1–2, then 3), and the first-order half should repeat it.
  2. The prose chapter is the hand-off to fd2 and should be what the reader finishes on.
  3. Theories and isomorphism are *used* by fd2, fd3 and fd4, so they cannot sit after the hand-off as an appendix.

  The cost is one mechanical renumbering sweep (§4.4). Atlas ids are stable, so F1.5 keeps its id and only its displayed number changes.
- **Old 4.11 split into 5.1 and 5.2.** The frozen R4 rewrite already runs to 4,950 words. Adding pictures, direct semantic proofs and the counter-model procedure needs about 4,000 more, so the section splits at its existing seam: meaning first, then counter-models.
- **New 2.7 instead of a strategy chapter.** fd1 is already the strongest book on search (2.6, 4.9). What is missing is *tasks*: inconsistency, equivalence pairs, verdict withheld. That is one section of worked searches and drill batteries, placed where the propositional rules are complete. It also introduces the syntactic "inconsistent", which 3.4 and 3.7 then pair with "unsatisfiable".
- **New 3.5 instead of a separate trees chapter.** The search for a refuting row, drawn as a branching tree, *is* the truth tree, presented as fd1's "working backwards from F" made systematic. It is not offered as a second proof system. It gives Chapter 3 a decision method, a second view of completeness (a Challenge sequence in 3.7), and the template for the counter-model procedure in 5.2. Renumbering 3.5–3.7 is cheap: no downstream volume names those sections (grep, 2026-10-12).
- **New 4.8 Unique Existence, Counting and Descriptions.** Every "the" in analysis (the limit, the supremum, the inverse) rests on it, and fd2 defines a function as a relation with ∀∃!. ∃! moves from 4.7 so that each section keeps one new thing: 4.7 is equality, 4.8 is uniqueness and counting.
- **5.3 Theories and 5.4 Definability are core, not optional.** fd2 (orders, equivalence relations), fd3 6.5 (an isomorphism carries every element-level property) and fd4 (groups up to isomorphism) all draw on them. The atlas has **no later logic volume**: model theory is only a branch hook (`fields.yaml`: model-theory `hook: [F1.4, ST.4]`). So fd1 is the only place these ideas can be taught. They are kept to the logic of theories. Relation theory proper (classes, partitions, order theory) is left to fd2.
- **5.6 is optional, and its results are stated, not proved.** `fields.yaml` records that first-order completeness and compactness are not in the trunk ("analysis-book 已刪 VDL.3"). Marking the section `.optional` respects that and still answers the reader's question "is that all of first-order logic?", which Smith's Interludes, Sider §4.5 and LPL all answer.
- **3.9 is optional.** The maximal-consistent-set proof is the template behind Zorn (fd2, ST.4) and maximal ideals (AL2.3). It is valuable as a second-pass route, but nothing in the trunk needs it.
- **6.8 is optional, and there is no "Beyond classical logic" chapter.** Kripke models turn three claims that 5.7 now states without proof into theorems, so they earn a section at the end of the dispute chapter. Many-valued semantics are kept to C items in 3.6, where they teach what "sound for a semantics" means. Tonk and Curry are a fold and a C item.
- **Not adopted.** None of these earns its cost for a mathematics reader. Each has a home elsewhere or gets at most one remark:
  - modal logic;
  - inductive logic and probability (one second reading in 1.1 only);
  - a standalone translation chapter (translation stays distributed through 1.1, 4.1, 4.9 and 4.10, beside the rules it serves);
  - Hilbert systems (one fold in 3.7);
  - syllogistic as a unit;
  - philosophy of logic beyond single remarks;
  - set theory, ordinals and cardinals (fd2, ST);
  - advanced model theory and proofs of incompleteness.

### Size and time

Time is computed with the B1 formula: 15 minutes per 400 main-line words; A1 items 25 minutes; a drill bank counts as one exercise per four parts, at 30 minutes; one B (30 minutes) and one non-Challenge C (40 minutes) per section; exit checks extra. The core track excludes optional and second-pass sections. The first two columns are the figures of the frozen and delivered R-blueprints.

| Ch | Core h, now | Full h, now | Main-line words, core | Core h, D | Full h, D | A2 parts | New sections |
|---|---|---|---|---|---|---|---|
| 1 | 35 | 50 | ~28,000 | **~39** | ~62 | 63 → 90 | — |
| 2 | 31 | 50 | ~27,600 | **~41** | ~67 | 65 → 105 | 2.7 |
| 3 | 33 | 56 | ~33,100 (+3.8 at 5,000, second pass) | **~45** | ~81 | 46 → 108 | 3.5; 3.9 opt |
| 4 | 56.5 | 90 | ~47,400 | **~63** | ~99 | 90 → 132 | 4.8 |
| 5 (new) | — | — | ~19,100 | **~26** | ~56 | 60 | 5.3, 5.4; 5.6 opt (5.1, 5.2, 5.5 moved) |
| 6 (was 5) | 31 | 47 | ~26,050 | **~34** | ~57 | 36 → 56 | 6.8 opt |
| **Total** | **~187** | **~293** | **~181,000** | **~248** | **~422** | 360 → 551 | 9 files |

Totals and levers:
- The core track grows by about a third and the full track by about 44%.
- About 40% of the core growth is drill (A2 banks of 15 in Chapters 1–2 and 12 elsewhere). That is deliberate: the matrix's sharpest finding is that a reader working alone gets about a tenth of Hurley's short repetitions.
- **Lever if the author finds this too heavy at S9:** cap every A2 bank at 12 and move the extra parts into an optional B "battery" item. That brings the core down to about 238 h with no loss of content.
- Each index recomputes its Time line from the delivered text and does not shade it down (STYLE §11.9).

---

## 3. What each chapter gains, and from which book (technique only)

Book keys are the matrix's: LB (Bergmann–Moor–Nelson), Hu (Hurley), LPL, Sm (Smith), Si (Sider), vD (van Dalen), En (Enderton), Ha (Halmos), Co (Cohnitz–Estrada-González), Le (Lemmon), Hk (Hacking), Ho (Hodges). A bracket names the book whose *technique* is borrowed. All content is fd1's own.

### 3.0 Volume-wide devices (adopted in every chapter; STYLE amendment D1, §6)

1. **Purpose-annotated assumptions.** An assumption line reads "asm, for →I", "asm, for ¬I", "asm, for RAA", "asm, for ∨E", "flag x₀, for ∀I", "witness x₀, for ∃E" [LB]. The renderer *infers* the purpose from the rule that closes the box (tool step D0), so no derivation is edited by hand. The 6.1 dictionary row "suppose, for contradiction" becomes a reading of a line the reader has seen since 1.4.
2. **Rule-instance gallery** in every rule section of Chapters 1, 2 and 4.3–4.6, placed beside the rule card. It shows three instances with large compound substitutions (compound terms such as f(f(c)) and ε/2 in Chapter 4) and one look-alike that is not an instance, with its reason [Hu].
3. **"Not allowed" block** per rule card: three to five one-line wrong steps, each tagged with the clause it breaks [Hu, Le]. It is shown *WRONG beside RIGHT* where a side condition bites [Hk, LB].
4. **The counterexample set** (premises together with the negated conclusion) is named once, in 1.1, and recalled each time it returns [Ho, LB]:
   - "try to break it" (1.1);
   - RAA, which shows the set inconsistent (2.5, 2.7);
   - the refuting row (3.4–3.5);
   - the counter-model (5.2);
   - consistency and independence (5.3).
5. **Derive-or-break items with the verdict withheld.** At least one B item per rule section from 1.5 on, seeded with invalid look-alikes [LPL, Si, En]. The method of refutation grows with the book: "break it" until Chapter 3, "or give a refuting row" from 3.6, "or give a counter-model" from 5.2.
6. **A2 drill banks of 12–16 parts** (15 in Chapters 1–2) in a ramp from recognition to construction [LB, Hu, Le]. The ramp runs: one-step ("write the line this rule gives"), then missing premise, then fill the justification column, then "is this application correct?", then 2–8-line derivations [Hu, Le].
7. **One fixed symbolization key per chapter's translation set** (integers in 1.1; ℕ with Prime, Even, <, ∣ in 4.9) [LB, Sm], and **reading back** a formula into words as a named check [LB, Sm].
8. **Chapter close.** Each `index.md` ends with **Summary** (what is now proved, what is still open) and **Terms** (a definitions glossary, each entry linked) [Sm, Hu, LB]. A volume **glossary page** `src/glossary.md` collects the Terms lists (build support checked at D0; if the engine cannot add a non-chapter page, the glossary goes at the end of the preface). An "Interlude"-style "what is proved / what is open" paragraph closes the Summaries of Chapters 3 and 5 [Sm].
9. **"Used later" marker** on exercises that a later section cites [En]. **One inline "(Why?)" prompt** per main-line worked example, answered in a fold [Ha].
10. **Pictures where the structure is spatial**, drawn in TikZ, which the engine supports (`engine/filters/tikz.lua`) [Si, vD, En, Ho, LPL]:
    - arrow and Hasse diagrams for every finite structure;
    - a dots picture of structural induction;
    - search trees;
    - rows as regions;
    - an Euler diagram of the hierarchy;
    - the A/E/I/O square;
    - the twin ∃E/∨E figure;
    - flowcharts.

### 3.1 Chapter 1 (in place; the arrangement is unchanged)

- **1.1**
  - A *phrase book* table, phrase → paraphrase → formula: unless, provided, whenever, neither/nor against not both, exactly one of, at least two of three, "but". It comes with a *"Not:" catalogue* of mistranslations in mathematical dress: "a and b are coprime" (collective "and"), "A, B, C are collinear", "an approximate root" [Ho, LB, Hu].
  - A *weak-reading* box: inclusive "or"; "some" allows "all"; a definition's "if" means "iff"; mathematical predicates are sharp [LPL, Ho].
  - The *counterexample set* named inside "Try to break it" [Ho].
  - A *stock breakers* sub-move: try 0, 1, −1, 2 and the empty case; choose the false conclusion first [Hu, Sm].
  - A second reading after Argument B: *a bad form refutes a step, not the conclusion* [Hu, Sm].
  - The named move *two ways to attack an argument* (a false premise or a broken step) [Hk].
  - The second reading on n² + n + 41 is extended with "every case against most cases" and with abduction as affirming the consequent [Hk].
  - New exercises:
    - an A item on the eight truth-value combinations ("which is impossible?") [Hk, LB];
    - an A item of the form "give an example or explain why it is impossible" [LB];
    - a 16-part symbolization drill on one integer key [LB, Sm];
    - a B item, "which of four short arguments has the same form?" [Hu, Le];
    - a B item, "valid or breakable?", with look-alikes [LPL].
- **1.2**
  - An instance gallery for ∧I and ∧E.
  - One snapshot with a goal line whose citation is still blank ("__ ∧I") [LB].
  - The A2 bank gains one-step and fill-the-justification parts [Hu].
- **1.3** (budget raised from 2,800 to 4,300)
  - An instance gallery for →E with large compound antecedents [Hu].
  - Two more worked chains, one forwards and one backwards.
  - A whole-line common error: →E applied to part of a line [Hu, LB].
  - Carroll's tortoise as a half-page fold ("a rule is not one more premise") [Co].
  - A missing-premise B item [Hu].
- **1.4**
  - The purpose annotation is introduced here, with the box.
  - A worked non-example, *two errors that cancel*: a correct conclusion reached through two illegal steps [Sm].
  - A C item: annotate each line with its set of open assumptions and read off the sequent it proves. This is the bridge to the induction in 3.6 [Le].
- **1.5** (budget raised from 2,900 to 4,300)
  - A worked search in which choosing a side too early fails, then redone [Sm, Si: deliberate failure].
  - The first derive-or-break items (P ∨ Q ⊢ P is refuted by 1.1's move) [LPL].
- **1.6**
  - "Affirming a disjunct" added to the common errors [Hu].
  - Constructive dilemma worked as a derivation from ∨E and →E [Hu, LB].
  - A closing translate-then-derive exercise [Hu, LB].
  - A 15-sequent battery of standard laws as a B item [Le, vD].
- **index:** the opening quiz [Hk], the Summary and the Terms.

### 3.2 Chapter 2

- **2.1:** A subsection on the *paradoxes of material implication*: Q ⊢ P → Q and ¬P ⊢ P → Q derived, with the challenge "name the rule you reject" [Le]. It explains why mathematics does not suffer from them: the mathematical "if" sits under a ∀, where the promise reading is exact [Sm, Co]. Explosion gets a one-line pointer [Co].
- **2.2:** A generalisation item: √2, then √3, then √p for prime p [LPL].
- **2.3:**
  - Constructive dilemma and MPT as B items [LB, Hu].
  - A Popper remark on MT: one failed prediction refutes; passing tests only corroborates [Hk].
  - A remark on schematic generality [LPL].
- **2.4:**
  - The lemma ⊢ ¬(P ↔ ¬P), labelled `lem-not-iff-own-negation`, which feeds the barber in 4.6 and fd2 1.1 [Ha, LPL].
  - A TFAE-cycle exercise on `prp-equivalence-cycle`.
  - A B item on criticising a candidate definition of "bounded": too broad or too narrow [Hu].
- **2.5:**
  - A heuristic for when RAA is needed: from weak premises to a disjunction or an existence claim [vD].
  - ⊢ (P → Q) ∨ (Q → P) as the paradox that needs RAA [Le].
  - A C item on restricted rule sets: derive MT without it, and derive the paradoxes without ∨I [Le].
- **2.6:**
  - The *detour rule* as a named move ("never introduce a connective and eliminate it at once"), stated without proof [vD].
  - Three moves [LB]: find the goal among the premises; derive what you can before opening a box; look first for a clash partner already on a line.
  - A fold with Harman's remark that logic permits but does not choose [Co].
- **2.7 Four Kinds of Task** (new):
  - **One new thing:** a task type decides the shape of the search, and the syntactic notion `def-inconsistent-set` (Γ ⊢ ⊥).
  - Worked searches for each type, each with snapshots:
    - a theorem (no premises);
    - an equivalence (two derivations);
    - **an inconsistency** (derive ⊥, with the clash partner found);
    - **derive or break** (decide first by trying to break it).
  - The propositions `prp-inconsistent-derives-everything` and `prp-derivable-iff-negation-inconsistent` (Γ ⊢ φ iff Γ ∪ {¬φ} ⊢ ⊥), the syntactic counterexample set [LB, vD].
  - A one-page *library of standard sequents grouped by use* [Le, LB].
  - Two-column items: the informal proof first, then the derivation that mirrors it [LPL, Le].
  - A 15-sequent B battery.
  - A Challenge C, Curry's paradox in Fitch [Co].
  - The chapter's R items, including one dialogue-extraction item [Hu].
  - The closing question of 2.6 ("how could we show something is *not* derivable?") is kept there. The Looking-ahead box of 2.7 points to Chapter 3.

### 3.3 Chapter 3

- **3.1:**
  - A paragraph on *object language and metalanguage*, with a Quick check classifying sentences [Co, Si, En].
  - An A2 part "repair this almost-formula" [LPL].
  - A C item on the unique readability of Polish notation [En, LPL].
- **3.2:**
  - A checklist box for an induction proof: what objects, what property, what starting points, what operations. It is reused in 3.6 and 5.5 [Si].
  - A dots picture of structural induction [Si].
  - A fold on sets built from a base, top-down equal to bottom-up [En, Ha].
  - A non-example after `thm-structural-recursion`: recursion fails without free generation [En].
  - C items:
    - *false thesis*: find where the induction breaks [LB];
    - *inventor's paradox*: strengthen the claim in order to prove it [LPL].
- **3.3:**
  - A subsection on *truth-functionality*, with partial tables for "because" and "it is known that" [Sm, Ho].
  - The *game reading* of the clauses in three bullets: ¬ swaps the players [LPL].
  - An A2 drill on backward computation and partial valuations, so the sub-skill comes before 3.5 [Hu].
  - Tonk as a fold in "Reading a table off the rules" [Co].
  - Two puzzles of fd1's own (truth-tellers and suspects) as B items [En, Hu].
- **3.4:**
  - Contingent; contradictory, contrary and subcontrary pairs, with a three-way classification drill [LB, Le].
  - `def-satisfiable-set` and `def-semantically-consistent`. If "consistent" alone is ambiguous, the text says "satisfiable" and reserves "consistent" for the syntactic notion of 2.7 [LB, vD].
  - `prp-reduction-to-unsatisfiability`: entailment, tautology and equivalence each reduced to unsatisfiability [LB, Ho].
  - A table of what one row establishes against what needs every row [LB].
  - A *rows-as-regions* figure: entailment is containment [Hk].
  - Structural properties of ⊨ in a fold: cut proved by a case split [Co].
- **3.5 Hunting for a Refuting Row** (new):
  - **One new thing:** a systematic search through the counterexample set.
  - The search:
    - forced moves first;
    - when nothing is forced, split on the atom that leaves the fewest ways [Hu, En];
    - the split drawn as a tree with closed and open branches [Sm, Ho, LB];
    - a row read off an open branch;
    - every branch closed means **Γ ⊨ ψ**, so a failed search is itself a proof [Si].
  - A warning box: a clash produced by a guess refutes nothing [Hu].
  - Testing a set for satisfiability.
  - A flowchart [Hu].
  - Named refutation tactics: the conclusion first, steps that do not branch first, close branches early [Sm].
  - Readers *derive* the splitting rules from the truth tables before seeing them [Ho].
  - `prp-search-decides`, stated on the main line and proved in a fold.
  - Exercises: branching items, consistency puzzles, a Challenge in which every rule of the tree is derived from a table.
  - The existing `exm-backwards-from-f` stays in 3.3 as the forced case and is cited here.
- **3.6 Soundness** (was 3.5):
  - A two-level box at the start: theorems *about* derivations, in ordinary mathematics. With it, an honest paragraph on rule-circularity [Co, En].
  - `cor-satisfiable-consistent`.
  - A "test the subgoal" box that revisits 2.6's failed search: refute a subgoal before chasing it [LPL].
  - **Independence by a nonstandard semantics** named as a technique, generalising `thm-raa-independent` [Si, Co].
  - C items:
    - change a table, then decide which rules stay sound [LB];
    - read ⊥ as a letter, which shows ⊥E is needed [Si];
    - Kleene and LP tables: which rules survive [Co, Si];
    - "finish the proof": two cases of the soundness proof left to the reader [Si].
  - From here on, derive-or-refute lists.
- **3.7 Completeness** (was 3.6):
  - `cor-consistent-iff-satisfiable` [vD].
  - The ⊢/⊨ parallel table completed: "the columns agree" [LB].
  - **`def-rule-taut`**: any tautological consequence of earlier lines as one step, licensed by `cor-derivable-iff-valid`. By convention it is used only for steps a prose proof would leave unsaid, which ties it to `def-silent-steps` [LPL].
  - Structural properties of ⊢: cut is why 2.3's derived rules are legitimate [Co].
  - A fully expanded two-atom glued derivation as a figure [Le].
  - A Looking-ahead box on 2ⁿ growth, with the scale made concrete [En].
  - A fold with Kreisel's squeezing argument [Co].
  - C items:
    - remove ∨I and find the lemma that breaks [LB];
    - a Challenge sequence: completeness of the search tree of 3.5 [Ho, Sm].
- **3.8 Normal Forms** (was 3.7; second pass):
  - A subsection, *calculating with equivalences*: chains of equivalences, each step citing its law, with "simplify" drills [vD, LPL].
  - **Positive and negative occurrences, and the monotonicity theorem** (`thm-monotonicity`, proof in a fold): "a stronger hypothesis gives a weaker theorem" and "it suffices to prove something stronger" [vD].
  - A bridge C item from connectives to set algebra, so fd2 can cite these laws [Ha].
  - The full DNF as a partition, with a row-counting C item [Hk].
  - An interpolation C pair [vD, En].
- **3.9 Compactness and Maximal Consistent Sets** (optional):
  - Formulas enumerated; Lindenbaum's chain built by recursion on ℕ; truth lemma by structural induction; completeness for infinite Γ.
  - The trade-off named: gluing rows constructively against extending to a maximal object [vD, Si, En].
  - Compactness as a two-line corollary.
  - A C item on colouring an infinite graph [vD, En].

### 3.4 Chapter 4

- **4.1:**
  - Over a finite domain, ∀ is a long "and" and ∃ a long "or", which previews quantifier negation as De Morgan [LB, Hu, Le].
  - Existential import in one line: every element of ∅ is positive [Ho, Sm].
  - A staged translation, going through a stage that mixes English and symbols [Sm, En, LB].
  - Minimal pairs: "not every" against "not any" [Ho].
  - An implicature box [LPL].
  - One example with nonsense predicates: validity does not depend on meaning [LPL].
  - A 16-part translation drill on one key.
- **4.2:**
  - An A2 repair part [LPL].
  - A simultaneous-against-sequential swap item [vD].
  - A remark that partial terms (1/x, lim) are guarded by hypotheses, not by free logic [Sm, Si].
- **4.3:**
  - A gallery with compound terms [Hu].
  - A remark that ∀E over {0, 1, 2} is ∧E [Le].
  - An A2 part on single steps: "is this application correct? why?" [Le].
- **4.4:**
  - A critique of a purported proof inside the section [LPL].
  - B items deriving relation properties: irreflexive and transitive imply asymmetric; asymmetric implies irreflexive [Le, Sm, Ho].
- **4.5:** a gallery, and derive-or-break items.
- **4.6:**
  - A **twin figure**: an ∃E derivation beside the same argument done by ∨E over {m, n} [Le].
  - A worked case of a contradiction trapped inside an ∃E box [LB].
  - **The barber and Russell's theorem**, ⊢ ¬∃y ∀x (R(x, y) ↔ ¬R(x, x)), as a worked example built on 2.4's lemma. Once it exists, fd2 1.1 may cite it [LPL, Ha].
  - A Looking-ahead box: *n* choices are *n* uses of ∃E; infinitely many need the axiom of choice (fd2) [Ha].
- **4.7 Equality:**
  - Leibniz's Law named [Sm].
  - A warning box: "it is obvious that …" contexts are opaque [Ho].
  - x = y → ∀z (z ∈ x ↔ z ∈ y) derived by =E. Its converse is *not* logic; the counter-model goes in 5.2 [Ha].
  - ∃! and its labels move to 4.8 (§4.4).
- **4.8 Unique Existence, Counting and Descriptions** (new):
  - ∃!, with `def-unique-existence`, `prp-unique-existence-use` and their examples, moved verbatim from 4.7.
  - *At least, at most and exactly n* built from ≠.
  - **Distinct letters need not name distinct objects**, which becomes the new (N12) in 6.6 [LPL, Le, Sm].
  - "Exactly two" proved as "at least two" together with "at most two"; "x² = 1 has exactly two real solutions" [LPL, Hu].
  - Only, except, other than; the maximum against the maximal [Hu, Ho].
  - **"The x such that φ"**: it may be written only after ∃!. Russell's unpacking, and the scope ambiguity of "lim aₙ ≠ 0" when there is no limit [Sm, Si, Ho].
  - A function symbol against its graph predicate with the axiom ∀∃!, which is fd2's definition of a function [LPL, Si].
  - B items:
    - existence from an axiom and uniqueness from extensionality (∅ is unique) [Ha];
    - composites of injections derived [vD].
- **4.9 Translating Mathematics** (was 4.8):
  - A *traps gallery*: ∀ with → and ∃ with ∧, each wrong swap refuted on a pictured structure; ∨ in the restrictor; "only"; "any" against "every"; a hidden ∀ in "if a number … then it" [LB, Hu, Sm, Ho].
  - **One ℕ key across a 20-item graded set**, plus logic-to-English decoding [Sm, LB].
  - "Infinitely many" (∀N ∃n ≥ N) against "eventually" (∃N ∀n ≥ N) [LPL, Si].
  - The named move *propositional core*: instantiate, reason propositionally, generalise [Le].
  - Two-rule combinations: ∀E then →E; ∃E then ∃I with a term built from available names [Hu].
  - Unfolding ⊆ and ∪ to primitives and back [Ha].
  - The named distinction *translation error against derivation error* [Hk].
  - The section's Looking-ahead box: induction and the supremum property quantify over sets, which is why fd2 and fd3 build ℕ and ℝ inside set theory [vD, En].
- **4.10 Negating and Moving Quantifiers** (was 4.9):
  - The **A/E/I/O square** with its diagonals.
  - Contrary against contradictory: the negation of "every x is positive" is not "every x is non-positive" [LB, Hu, Le].
  - Twin-law boxes, each quantifier law beside its propositional twin [Le, LB].
  - One worked conversion to prenex form, and alternation as a measure of complexity (∀∃∀ for limits) [LPL, vD, En].
  - The *replacement step* (swap a provably equivalent part inside a line), used to push ¬ through a prefix. It rests on 3.4's `lem-replacement` and 3.7's completeness [LB].
  - The named move *prove it cannot be false* for ∅ [Ha].
  - C items:
    - ∃ defined as ¬∀¬, with its rules derived [vD, Le];
    - the drinker sentence, derived here and checked semantically in 5.1 [vD, En];
    - Darapti with an empty A [Co].
- **4.11 Uniform Continuity** (was 4.10):
  - A subsection on *witness functions*: uniform continuity gives a function δ(ε) and continuity a function δ(ε, x), as Skolem functions and as winning strategies [vD, En, LPL]. The axiom of choice gets one sentence, inside the Looking-ahead box.
  - A critique of a purported proof of the converse [LPL].
  - TAUT shortens the long derivation [LPL].
  - The chapter's R items move here from old 4.11.

### 3.5 Chapter 5: Models and Theories (new)

- **5.1 Structures and Satisfaction:**
  - Old 4.11 up to its counter-model subsection, with the frozen R4 §4.11 plan (three pictured counter-models first). The square-root Quick check (cited by fd4) and "Why domains are non-empty" (id kept; cited by fd3) stay here.
  - New:
    - **arrow and Hasse pictures** for every finite structure [vD, Si, En, Ho];
    - a drill evaluating sentences in two given structures [Sm, LPL];
    - the game reading of satisfaction [LPL];
    - **direct proofs that Γ ⊨ φ**, one "in excessive detail" with each step citing a clause, then condensed [Si].
- **5.2 Counter-models:**
  - Old 4.11's counter-model material, with `cor-counter-model`, `exm-counter-model-swap`, `exr-models-c1`, `exr-models-c2` and the heading id `from-counter-models-to-non-derivability` kept.
  - New:
    - **the counter-model procedure**: start from the element that witnesses the failure; meet existential demands before universal constraints; add only forced elements; move to an infinite domain when no finite one works [Si, Sm];
    - **small domains, by expansion**, with an example that fails at size 1 and succeeds at size 2, the monadic bound as a remark, and the limit on infinite domains [Hu, LB];
    - the hierarchy *tautology ⊂ first-order valid ⊂ true in ℕ*, with an Euler diagram and a three-way classification drill [LPL];
    - "a failed search proves nothing here" (undecidability in a fold) [Ho];
    - B items showing that each side condition is needed, by a counter-model [vD];
    - mixed lists in which the reader chooses between a derivation, a counter-model and a semantic proof [LPL, Si, En];
    - the counter-model to the converse of extensionality [Ha].
- **5.3 Theories and Their Models:**
  - Definitions: `def-theory` and `def-model-of-theory`.
  - Axioms written as sentences, each with drawn models and non-models: equivalence relation; strict, partial, linear and dense order; group; field.
  - One theorem derived in a theory: a strict order is asymmetric.
  - `prp-model-shows-consistency` (by first-order soundness).
  - **`prp-model-shows-independence`**: a non-abelian group of fd1's own shows that commutativity does not follow; three small relations show that reflexive, symmetric and transitive are independent [vD, Ha, En].
  - B and C items:
    - construct a relation with given properties, or show none exists (the empty relation; the trap "symmetric and transitive implies reflexive") [Le, Sm];
    - **find a sentence true in A and false in B**: ℕ against ℤ, ℤ against ℚ [vD, En];
    - **describe every model of σ** [En].
  - The Looking-ahead box points to fd2's orders and relations.
- **5.4 Definability and Isomorphism:**
  - A formula defines a set in a structure, with examples: x ≥ 0 by squares in (ℝ, +, ·); < in (ℕ, +); "prime" in (ℕ, ·). ∃ acts as a projection, and set-builder notation is the reading of a formula [En, vD].
  - "Define this notion by a formula" items: maximum against maximal; supremum [vD].
  - `def-isomorphism-of-structures`.
  - **`thm-isomorphism-invariance`** (isomorphic structures satisfy the same sentences), stated on the main line with its structural-induction proof in a fold [En, vD, Co]. fd3 6.5 may then cite it.
  - Automorphisms prove non-definability: x ↦ x + 1 shows that 0 is not definable in (ℤ, <) [En, Co].
  - The chapter's R items.
- **5.5 Soundness for Predicate Logic** (optional): old 4.12 kept verbatim, renumbered, with a pointer to the 3.2 checklist.
- **5.6 What First-Order Logic Can and Cannot Say** (optional; every result marked "stated without proof"):
  - Gödel's completeness theorem, with a Henkin sketch in a fold; old and new names mirror the freshness conditions [Sm, Si, LPL].
  - Compactness, with a guided C item: no sentence says "the domain is finite" [Si, Co, vD].
  - Löwenheim–Skolem; non-standard models of arithmetic; the induction schema against the second-order axiom [vD, En].
  - Decidability: tables, yes; first-order logic, no (Church); the monadic fragment, yes. Incompleteness named [Si].

### 3.6 Chapter 6: From Derivations to Mathematical Prose (was 5)

- **6.1:** dictionary rows for constructive dilemma and for TFAE by a cycle; the spoken purposes of assumptions.
- **6.2:** rows for "it suffices to prove something stronger" and "a stronger hypothesis gives a weaker theorem" (from 3.8) [vD]; "the limit" (from 4.8); double inclusion and element chasing [Ha].
- **6.3:** "it suffices to show" written as a column of reductions [En].
- **6.4:** an argument-extraction exercise: premises, "therefore", and the suppressed premises supplied (*name the unstated fact*) [Ho, Hu]; a non-mathematical argument annotated line by line with fd1's rule names [Co].
- **6.5:** a proof-generalisation item [LPL].
- **6.6:**
  - Entries **(N12)** distinct letters assumed to be distinct objects, **(N13)** an "and so on" iteration with nothing behind it, and **(N14)** a hidden premise (the barber) are *appended*. (N1)–(N11) are untouched, since they are cited 923 times [LPL, Ha].
  - One sentence on steps that are improper but valid [Hu].
  - Informal fallacies cross-referenced under mathematical names [Hu].
  - A dialogue R item [Hu].
- **6.7:** a table of which direction of each classical law survives without RAA [vD]; the stated-without-proof claims point to 6.8.
- **6.8 Stages of Knowledge: Kripke Models** (optional):
  - Two- and three-node models refute excluded middle, ¬¬P → P, (P → Q) ∨ (Q → P) and De Morgan (d).
  - Heredity by structural induction.
  - Soundness of the rules without RAA by reusing the 3.6 proof (in a fold) [Si, vD].

---

## 4. Interaction with the frozen blueprints and the atlas

### 4.1 How the work is packaged

| Chapter | Base (stands) | New file (stage S1) | Kind |
|---|---|---|---|
| 1 | delivered R2 text | `fd1/authoring/blueprints/ch01-deepen.md` | delta on the delivered text |
| 2 | `ch02-revision.md` (frozen R3) | `ch02-deepen.md` | addendum; drafted together with R3 |
| 3 | `ch03-revision.md` (frozen R3) | `ch03-deepen.md` | addendum; drafted together with R3 |
| 4 | `ch04-revision.md` §§1–4.10 (frozen R4) | `ch04-deepen.md` | addendum; drafted together with R4 |
| 5 (new) | `ch04-revision.md` §4.11 and §4.12, as the base for 5.1, 5.2 and 5.5 | `ch05-models-and-theories.md` | full blueprint (mostly new) |
| 6 | `ch05-revision.md` (frozen R5) | `ch06-deepen.md` | addendum; drafted together with R5 |

Each addendum lists, item by item, what it supersedes in its base. Under PIPELINE S2 ("a later change to a frozen blueprint re-opens S2 for the changed items"), S2 then reviews **only** the addendum and the superseded items, never the whole frozen file again.

### 4.2 What stands and what is superseded

- **ch02-revision (R3):** everything stands.
  - Superseded: §2 "No file is added" (2.7 is added); §5 budgets and the Time line (2.1 → ≤ 3,600, 2.2 → ≤ 2,600, 2.3 → ≤ 3,300, 2.4 → ≤ 3,700, 2.5 → ≤ 4,800, 2.6 → ≤ 5,000); the exercise totals; §4.0's index items (roadmap and named moves gain 2.7; Summary and Terms are added).
  - The R items move from 2.6 to 2.7. The R content stands, but its labels must stay in the chapter's last section, so the three `exr-…-r*` labels move with it. They are uncited outside the chapter (to be confirmed at S1).
  - Binding rule 4 ("section numbers do not change") remains true for 2.1–2.6.
- **ch03-revision (R3):** the content of every section stands.
  - Superseded:
    - the §2 sentence "Section numbers … do not change". 3.5, 3.6 and 3.7 become 3.6, 3.7 and 3.8; no downstream volume names them, and fd1 Chapters 4–6 are swept;
    - §4.0's reading path (3.8 is second pass, 3.5 is new and core);
    - §5 budgets (3.3 → ≤ 3,900, 3.4 → ≤ 5,000, 3.6 → ≤ 4,200, 3.7 → ≤ 5,000, 3.8 → ≤ 5,000);
    - the Time line.
  - The frozen "Where this goes" note in the index gains 5.3 and 5.4 as destinations.
- **ch04-revision (R4):** §§4.1–4.10 stand as content.
  - Superseded:
    - §2, the section map: 4.11 and 4.12 leave the chapter; 4.8, 4.9 and 4.10 become 4.9, 4.10 and 4.11; 4.7 is split;
    - binding rule 1's "in its current section", for the ∃! labels and the 4.11 and 4.12 labels only;
    - §4.0: the index's last paragraph about models moves to Chapter 5's index, and Ch4's motivating question stays as it is;
    - §5 budgets;
    - "4 R (4.11)": Chapter 4's R items go to the new 4.11 (uniform continuity), and Chapter 5 writes its own R items in 5.4.
  - The frozen §4.11 plan (three pictured counter-models first; the well-definedness paragraph and the proof of `lem-free-coincidence` folded) **stands as content** and is carried into 5.1 and 5.2 by `ch05-models-and-theories.md`.
  - §4.12 ("kept") stands, as 5.5.
- **ch05-revision (R5):** everything stands.
  - Superseded: the chapter number (5 → 6); the "What you need" lists ("Chapters 1–4" becomes "Chapters 1–5", now including Chapter 5's counter-models); the §5 budgets of 6.1, 6.2, 6.4 and 6.6; the exercise totals.
  - "Every result of 5.7 stays `.optional`" stands for 6.7, and 6.8 is optional as a whole.
  - The rule that `exm-not-allowed-catalogue` keeps (N1)–(N11) stands; (N12)–(N14) are appended after them.
- **ch01 (delivered R2, awaiting S9):** nothing is undone. The R2 S9 packet and the D S9 packet go to the author **together** (§5), so the author judges the deepened chapter and not a version about to be replaced.

### 4.3 Atlas changes (math-atlas, one commit, `atlas.py check` must pass)

- `registry/chapters.yaml`: insert, **between F1.4 and F1.5**,
  `- {id: F1.6, title: "Models and Theories", title_zh: 模型與理論, src: new}`.
  The list order is the reading order, so F1.5 (prose) displays as Chapter 6 and keeps its id.
- `registry/plan-edges.yaml`:
  - `F1.6: {s: [F1.4], see: [F1.3]}`, since 5.5 and 5.6 reuse Chapter 3's soundness and completeness only as motivation;
  - `F1.5: {s: [F1.4, F1.6]}`, since 6.x cites `exm-counter-model-swap` and the counter-model method;
  - soft edges `see: [F1.6]` on F2.2 (orders and relations as theories), F3.x for fd3 6.5 (isomorphism transfer; exact chapter id at S1) and AL1.1 (groups as models).
  - `F2.1: {s: [F1.5]}` is unchanged.
- `registry/fields.yaml`:
  - mathematical-logic `ch: [F1.1, F1.2, F1.3, F1.4, F1.6]`. The note about first-order completeness and compactness stays true (5.6 is optional).
  - model-theory `hook: [F1.6, ST.4]`.
- The library landing page and reading-order diagram (recent commit 88e88e4 shows they list volume chapters) get the new chapter.
- `foundations/authoring/series.json` and STATUS rows: F1.6 is added, and F1.3/F1.4/F1.5 notes are updated.

### 4.4 Renumbering map and sweep (applied once, simultaneously, by script, step D2)

| Old | New | Downstream hits (grep 2026-10-12) |
|---|---|---|
| 3.5 / 3.6 / 3.7 | 3.6 / 3.7 / 3.8 | none outside fd1 |
| 4.7 (the ∃! part) | 4.8 | "Section 4.7" ×2 (fd2 and fd3): check each against what it names |
| 4.8 / 4.9 / 4.10 | 4.9 / 4.10 / 4.11 | "Section 4.9" ×4, including the fd2 Gate 0 map (07:94, 07:363); "Section 4.10" ×2 (Gate 0, 07:363) |
| 4.11 | 5.1 (structures, the ℂ square-root check, non-empty domains) or 5.2 (counter-models) | "Section 4.11" ×12 (fd2 03/06:281 → 5.2; fd4 01/04 → 5.1; Gate 0 07:365 → 5.2; fd3 01/01:245 → 5.1) |
| 4.12 | 5.5 | none by section number; `thm-first-order-soundness` cited by label (20) |
| Chapter 5 / 5.k | Chapter 6 / 6.k | "Chapter 5" ×~46; "Section 5.x" ×~20 (5.7 ×8, 5.6 ×4, 5.3 ×4, 5.2, 5.1) |
| "Chapter 4", where it means models | "Chapter 5" | read by hand: every "Chapter 4" hit near "model", "structure" or "counter" |
| "Chapters 1–5", "Chapters 2–5" | "Chapters 1–6", "Chapters 2–6" | ×~20 |

- **Files.**
  - `ch05-from-derivations-to-prose/` → `ch06-from-derivations-to-prose/`.
  - New `ch05-models-and-theories/`: `01-structures-and-satisfaction.md` and `02-counter-models.md` (split from `ch04/11-models.md` at drafting), `03-theories-and-models.md`, `04-definability-and-isomorphism.md`, `05-first-order-soundness.md` (git mv of `ch04/12`), `06-limits-of-first-order-logic.md`.
  - `ch03/05–07` → `06–08`, plus a new `05-refuting-row-search.md` and `09-compactness.md`.
  - `ch04/08–10` → `09–11`, plus a new `08-counting-and-descriptions.md`.
  - `ch02/07-four-kinds-of-task.md`.
  - `ch06/08-kripke-models.md`.
- **Labels moving section** (their names are unchanged, so `@fd1:` links survive):
  - `def-unique-existence`, `prp-unique-existence-use` and the ∃! examples (4.7 → 4.8);
  - `exm-counter-model-swap`, `cor-counter-model`, `exr-models-c1`, `exr-models-c2` (4.11 → 5.2);
  - `thm-first-order-soundness` and the rest of old 4.12 (→ 5.5);
  - all of Chapter 5 (→ Chapter 6), with no change of section within the chapter.
- **Ledger and promise bookkeeping:** fd1 `authoring/ledger/ch0*.yaml` (and a new ch06), the dependency-ledger lines that close each section in fd2, fd3 and fd4 ("Logic and Proof, Section 4.11 …"), STATUS's promise table, and `tools/promises.py`.
- **Gates.** After the sweep:
  - grep for `Logic and Proof\*?,? (Chapter 5|Section (4\.(8|9|1[0-2])|5\.[0-9]|3\.[5-7]))` and confirm by hand that every hit is new-style;
  - build all five volumes;
  - `check_rendered.py`;
  - `atlas.py check`.

---

## 5. Order of work and cost

The pipeline runs autonomously. Only S9 author sampling and merges stay with the author. Stages are as in PIPELINE.

| Step | What | Depends on | Agent runs (estimate) |
|---|---|---|---|
| **D0** tooling | (a) renderer and `check_fitch.py` infer and print the purpose of each assumption; (b) `check_fitch.py` accepts `\by{TAUT}` and checks it by truth table; (c) TikZ templates for arrow and Hasse diagrams, trees, the square and flowcharts, rendered in HTML and PDF; (d) build support for `glossary.md`; (e) a renumbering script taking a simultaneous map | — | 3–4 |
| **D1** STYLE | §12.8 banks of 12–16 (15 in fd1 Ch1–2); new §12.13 covering the purpose annotation, instance gallery, "Not allowed" block, derive-or-break item, chapter Summary and Terms, the "used later" marker; NOTATION entries for consistent and satisfiable, counterexample set, TAUT, ≠-counting | — | 1 |
| **D-pilot** Ch1 | S1 `ch01-deepen.md` → S2 (2 referees plus a derivations referee, 2–3 rounds) → S3 (3 drafters) → S4 → S5 (2 blind referees per section plus skeptics) → S6 → S7/S7r → S8 → **S9 to the author, together with the pending R2 S9** | D0, D1 | ~40 |
| **D-S1 wave** | S1 and S2 of `ch02-deepen`, `ch03-deepen`, and the atlas commit (§4.3) | D1; runs in parallel with the D-pilot's S3–S8 | ~16 |
| **Gate** | Author's S9 verdict on the deepened Ch1. Density, drill volume and the Time line are adjusted in the D-addenda before anything is drafted | D-pilot | — |
| **Wave 1** | Ch2 (R3 + D) and Ch3 (R3 + D) drafted at once, then S4–S8 each. Ch3's references to `def-inconsistent-set` are blueprinted, so the two can run in the same wave | Gate | ~45 + ~55 |
| **D2** renumbering | One commit: file moves, the simultaneous map, the downstream sweep, ledgers and promises, all gates (§4.4) | after Wave 1's S7, before Wave 2 drafting | 2–3 (script plus one checking referee) |
| **D-S1 wave 2** | S1 and S2 of `ch04-deepen`, `ch05-models-and-theories` (the heaviest S2: about 15 new claims, including `thm-isomorphism-invariance` and `prp-search-decides`-style items for 5.2) and `ch06-deepen` | can start during Wave 1 | ~22 |
| **Wave 2** | Ch4 (R4 + D) and Ch5 (new), then Ch6 (R5 + D). Ch6 waits for Ch5's labels to exist | D2, D-S1 wave 2 | ~65 + ~50 + ~50 |
| **Whole volume** | Preface table (six chapters), Time lines recomputed, seam pass across chapter boundaries (2.7 → 3.4, 3.5 → 5.2, 4.8 → 6.2), glossary assembled, fd2 Gate 0 map re-checked, optional downstream upgrades (fd2 1.1 cites the barber; fd3 6.5 cites `thm-isomorphism-invariance`) | Wave 2 | ~8 |
| **S9** | One packet per chapter for Chapters 2–6, which may be batched | each wave | author |

**Total: about 360 agent runs.** At the token cost of the Ch1 R2 run (roughly 150–250k tokens per run), that is about **55–90M tokens**. In wall-clock time, about 2 days for D0, D1 and the pilot to S9; then, after the author's verdict, about 3 days for Wave 1 and about 4 days for D2 and Wave 2. That is roughly **10 working days of pipeline time** plus the author's six S9 reads. The heaviest single costs are S5 and S6 on Ch4 (11 sections, about 130 drill parts plus new B and C items with full solutions) and S2 on Ch5 (new metatheorems).

**Words to draft:** about 37,000 new main-line words in the 9 new section files (including about 17,500 in optional sections), about 25,000 words added inside existing sections, and about 190 new A2 parts plus about 70 new B and C items, all with full solutions.

---

## 6. Risks

1. **The core time rises to about 248 h**, from about 187 h, and a first-year reader working alone may stall.
   - Mitigation: about 40% of the rise is drill, and it can be trimmed without loss of content (the 12-part lever, about 238 h).
   - Chapter 3's 3.8 stays second pass. 3.9, 5.5, 5.6 and 6.8 are optional.
   - Each index states a first-reading path.
   - The author's S9 on the Ch1 pilot is the gate for the whole density.
2. **The renumbering sweep breaks references.** About 100 hand-written "*Logic and Proof*, Chapter/Section …" hits sit in fd2, fd3, fd4 and an1, the Gate 0 map among them, plus ledger lines and the promise table.
   - Mitigation: one simultaneous map applied by script (never sequentially, as the Ch1 R2 map did); hand reading of every "Chapter 4" hit that means models; label links are unaffected; grep gates, five builds, `check_rendered.py` and `atlas.py check`.
   - Fallback, if the author vetoes the renumbering at S9: append the models chapter as Chapter 6 after prose. §2 records why that is worse.
3. **Conflicts with frozen blueprints, and S2 being re-opened.** Mitigation: the addenda list superseded items by section and line, and S2 reviews only those. Chapter 1's delivered text is changed only by `ch01-deepen.md`, under the rule that no label is lost.
4. **Copyright and closeness to the twelve books.**
   - The danger is greatest for classic items (barber, drinker, tonk, tortoise, Darapti, the two-node Kripke model, Russell's theorem) and for fixed-key drill sets.
   - Mitigation:
     - every item is fd1's own, in mathematical dress with fd1's numbers;
     - S2 compares each new item with the twelve books, as `ch02.md` does for Huth & Ryan;
     - the drafters are never given book text;
     - the LPL text left in the scratchpad (`lpl.txt`) is not an input to any drafter, and should be deleted after this plan is approved.
5. **Scope creep into fd2, ST or a model-theory volume.**
   - 5.3 and 5.4 stop at the logic of theories: axioms, models, independence, definability, invariance.
   - Equivalence classes, partitions, order theory, function theory and choice stay in fd2.
   - 5.6 is optional and states its results without proof.
   - Relation-property items in 4.4 and 5.3 are exercises in logic, and fd2 keeps the theory.
6. **Gaps in tooling.**
   - Purpose annotations, TAUT checking, trees and diagrams must render in HTML and PDF before drafting. D0 is a hard prerequisite: no drafting until its checks pass.
   - The Lean column needs entries for ∃!-counting and TAUT (`tauto`).
7. **Load on exercise verification.** About 260 new items with full solutions and marking schemes, including new kinds (build a model, separating sentence, false thesis). Mitigation: two S6 agents for Ch4 and Ch5, with a model-checking script for the finite structures (each structure is a small table that a script can evaluate), added to D0 if cheap.
8. **The forward-pointer rule** (one Looking-ahead box per section) limits how often new material can point to fd2, fd3 and fd4. Mitigation: those pointers are gathered in each index's "Where this goes" note, as the frozen R3 and R4 already do.
9. **Vocabulary drifts across chapters.** "Consistent" means the syntactic notion (2.7) and "satisfiable" the semantic one (3.4), and the "counterexample set" must be used throughout. Mitigation: the D1 NOTATION entries, the volume glossary, and an S8 seam check on the words.
10. **The frozen catalogue.** `exm-not-allowed-catalogue` is cited 923 times. (N12)–(N14) are strictly appended; (N1)–(N11) keep their numbering, wording and instances.
11. **Difficulty spikes in the new metatheory.** `thm-isomorphism-invariance` needs induction over formulas *with assignments*, and `prp-search-decides` needs a termination argument. Mitigation: statements and meanings stay on the main line and proofs go in folds (STYLE §12.12), and S2a gives both its strongest referee.

---

## 7. Decisions made on the author's behalf (for S9)

1. A new Chapter 5, *Models and Theories* (F1.6), is inserted; prose becomes Chapter 6, with a mapped sweep. *Fallback:* append it as Chapter 6.
2. New core sections 2.7, 3.5 and 4.8; old 4.11 split into 5.1 and 5.2; new core sections 5.3 and 5.4. New optional sections 3.9, 5.6 and 6.8. No "Beyond classical logic" chapter, no modal or inductive logic, no standalone translation or strategy chapter.
3. Chapter 1 is deepened in place, its arrangement untouched, and the D pilot goes to S9 together with the pending R2 S9.
4. Volume-wide devices (§3.0), including assumption purposes inferred by the renderer, A2 banks of 15 in Chapters 1–2 and 12 elsewhere, chapter Summary and Terms, and a glossary page.
5. The core time rises to about 248 h (full track about 422 h), with the 12-part lever (about 238 h) held in reserve.
6. "Consistent" is syntactic (Γ ⊬ ⊥) and "satisfiable" semantic. TAUT is admitted after 3.7, only for steps prose would leave unsaid.

---

## Critic review

The reviewer read this plan and `gap-matrix.md` as a logic teacher and as series editor, and checked them against `fd1/src`, the frozen `ch04-revision.md`, `registry/{chapters,plan-edges}.yaml`, and a fresh grep of the `@fd1:` citations in fd2, fd3 and fd4 (77 distinct labels; **all 77 exist today**, so the only risk to them is the move list). The corrections below are binding on the S1 addenda unless the author overrides them at S9. They are listed most important first.

### C1. The Chapter 5 move list is wrong, and core 5.2 and 5.3 depend on a theorem placed in optional 5.5 (blocking)
- **`cor-counter-model` is not in 4.11.** It is in `ch04/12-first-order-soundness.md:236`, the optional section, beside `thm-first-order-soundness`. So §4.4's line "`cor-counter-model` … (4.11 → 5.2)" is false. 4.11 holds only the *unlabelled* statement under `#from-counter-models-to-non-derivability`. fd2 ch03 cites that statement by heading id, with the note "proof in optional F1.4 §12".
- **The new order makes the core results rest on something later and optional.** 5.2 (counter-models prove non-derivability), and also `prp-model-shows-consistency` and `prp-model-shows-independence` in 5.3, all hold *by first-order soundness*. In the plan, soundness is proved only in 5.5, which is optional and comes after 5.3 and 5.4.
- **Fix:**
  - keep `thm-first-order-soundness` and `cor-counter-model` together in 5.5, with their labels and content unchanged;
  - 5.2 keeps the heading `#from-counter-models-to-non-derivability` and its statement, as today;
  - 5.3 cites *that heading* (not the 5.5 labels) for the two `prp-model-shows-*` results, and says once "proved in the optional Section 5.5";
  - the Ch5 "How to read this chapter" note puts this statement-on-the-trunk, proof-optional arrangement in writing, in the form R4 used for 4.11/4.12.
  
  In §4.4, correct the move line to "`exm-counter-model-swap`, `exr-models-c1`, `exr-models-c2` (4.11 → 5.2); `cor-counter-model` with old 4.12 (→ 5.5)".
- **The R items cannot go to 4.11.** `exr-models-r1` to `exr-models-r4` sit in 4.11 today. R4 asks "true in (ℕ, <)? derivable?", and its answer needs a counter-model, which is Ch5 material. **Fix:** `exr-models-r1` to `exr-models-r4` stay in Chapter 5, in 5.4 (its last core section), with their labels unchanged. Chapter 4's new R items in the new 4.11 are *new* labels (`exr-uniform-continuity-r*`). §4.2's line "Chapter 4's R items go to the new 4.11" must be rewritten to match.
- **Labels in 4.7.** List by name which of `exr-equality-and-uniqueness-{a1,b1,b2,b3,c1,c2}` go to 4.8 with ∃! (those whose content is ∃!), and keep `rule-phrase-lean-table` at the end of the last *rule* section (it is cited from ch05 01:70 by id). The labels keep their `equality-and-uniqueness` prefix even when they sit in 4.8, and the addendum says so, so that no one "fixes" them.
- **Do not duplicate `def-satisfiable`.** It already exists (3.4:28) and covers lists of formulas. Do not add `def-satisfiable-set`. Add only `def-semantically-consistent`, if it is needed at all; given decision 6, prefer no new label and have the text say "satisfiable".
- **The renumbering sweep must cover fd1 itself.** fd1 has about 150 internal hits: "Section 3.5" ×14, "3.6" ×11, "3.7" ×4, "4.7" ×9, "4.8" ×25, "4.9" ×12, "4.10" ×16, "4.11" ×30, "4.12" ×12, "Chapter 5" ×14. This includes the 4.3–4.10 counter-reading convention, "Section 4.11 states that a counter-reading rules out every derivation" (→ 5.2), and "Section 4.12" (→ 5.5). The D2 map must cover these, as well as the downstream volumes.

### C2. The first-order replacement step and TAUT in Chapter 4 are licensed by results that do not cover them (mathematical error)
- **The problem with replacement.** §3.4 (4.10) rests the *replacement step* on 3.4's `lem-replacement` and 3.7's completeness. Both are propositional.
  - Pushing ¬ through a prefix replaces a subformula *under a quantifier*, with a *first-order* equivalence (¬∀xφ ↔ ∃x¬φ).
  - Neither result licenses that. The first-order semantic route would need first-order completeness, which is only stated, in optional 5.6.
- **Fix for replacement.** State it as a derived rule proved *syntactically*: if ⊢ φ ↔ ψ, with the free variables of φ, ψ arbitrary, then ⊢ χ[φ] ↔ χ[ψ].
  - The proof is an induction on the context χ. The connective cases reuse 2.4. The ∀ and ∃ cases use ∀I and ∃E, with the flag condition checked.
  - Statement and meaning go on the main line, and the proof goes in a fold. Frozen 4.9 already uses "a law may be used on a part under a quantifier", and this proof is what supports it.
  - Propositional completeness may be cited *only* for propositional contexts.
- **Fix for TAUT in Chapter 4.** `def-rule-taut` must be defined on the **propositional skeleton**: atomic *and quantified* subformulas are treated as letters. It is licensed by 3.7's completeness applied to the skeleton, together with `lem-substitution`. It is never a licence for first-order validities (∀x∀y R ⊢ ∀y∀x R is not a TAUT step). `check_fitch.py` (D0 b) must compute the skeleton before it builds the truth table. Item 6 of §7 should say "propositional-skeleton tautological steps".
- **Related correction.** The 3.7 Challenge "completeness of the search tree of 3.5" duplicates `prp-search-decides` (trees decide ⊨). Its worthwhile form is *closed tree ⇒ Fitch derivation*, which translates each closing rule into a derived step. That is a genuinely second, constructive completeness proof. Rewrite the item that way.

### C3. Chapter 5's prerequisites, its motivating example and its place on the trunk need tightening (editor)
- **The group example is impossible as written.** The Ch5 index motivator says the group axioms vs xy = yx can be settled by "a model of two letters". But **every group with at most five elements is abelian**, so no two- (or small-) element model exists.
- **Fix for the example.**
  - Either open with an order example that genuinely has a two-element counter-model: "do the axioms of a partial order prove that any two elements are comparable?", answered by a two-point antichain.
  - Or keep groups and use the six symmetries of a triangle, with the table given and associativity inherited from "doing one motion after another" (checked by a D0 script, not by the reader).
  - Either way, 5.3's "non-abelian group of fd1's own" has at least six elements, and its verification burden is budgeted.
- **Isomorphism comes before functions.** `thm-isomorphism-invariance` needs bijections, inverses and composition with assignments (h∘ℓ). fd2 F2.1 defines these properly, and fd1 has them only in their everyday sense. The claimed downstream need is weak: fd3 6.5 (`05-axioms-or-model.md`) already proves its own transfer facts (P1)–(P6) from `def-cof-order-preserving-map`, so citing fd1 is an optional upgrade only. And "AL1.1" is not an atlas id (groups are F4.3).
- **Fix for 5.4.**
  - Definability (formula defines a set, ∃ as projection, "define this by a formula") stays core.
  - `def-isomorphism-of-structures`, `thm-isomorphism-invariance` and automorphism non-definability go **second pass** inside 5.4, marked on the index's first-reading path. They use finite pictured structures with the bijection given as a table, plus (ℤ, <) with x ↦ x + 1.
  - The soft edges in §4.3 become F2.2 and F4.3 (not AL1.1), and fd3's edge is `see` only.
- **The trunk cost.** `F1.5: {s: [F1.4, F1.6]}` puts all of core Chapter 5 (about 26 h) on the hard path to F2.1 and AN1.1. The core total is about 248 h for a first volume, against today's 187 h. That is not realistic for a reader working alone who still has fd2 and fd3 ahead before analysis.
- **Fix for the trunk.**
  - Adopt the 12-part lever **by default**, not in reserve: A2 banks of 12, with the surplus in optional batteries.
  - Move the second-pass part of 5.4 off the core.
  - Keep 4.8's "only/except/superlatives" and minimal-pair material as drills, not new main line.
  
  Target ≤ 225 h core. The full track may stay large. Recompute the §2 size table after these moves.

### Smaller corrections
1. **A missing definition for 3.9.** fd1's Γ is a *finite list* (`def-satisfiable`: "φ₁, …, φₙ, n ≥ 0"). So 3.9's "completeness for infinite Γ" and compactness need ⊢ and ⊨ for infinite sets (derivable from a finite sub-list). 3.9 must define these itself; nothing earlier gives them.
2. **First-order "inconsistent" needs its own statement.** 2.7's `def-inconsistent-set` is propositional. 5.3 needs "a theory T is inconsistent iff T ⊢ ⊥ from finitely many axioms", stated in 5.3, since theories can be infinite (field axioms are finite, but the induction schema in 5.6 is not).
3. **A wrong cross-reference.** §2's "Kripke models turn three claims that 5.7 now states" should say 6.7.
4. **A correction to the hierarchy in 5.2.** "Tautology ⊂ first-order valid ⊂ true in ℕ": "true in ℕ" is relative to a signature with an intended reading. Say "sentences of the signature (0, S, +, ·, <)". "Tautology" here means "instance of a propositional tautology" (the skeleton sense of C2). Define it once.
5. **5.2's "monadic bound" stays a remark with no proof**, and "move to an infinite domain" names the drill limit honestly. The reader is never asked to find an infinite counter-model they cannot verify, except ℕ, ℤ and ℚ.
6. **What is missing from the trunk.**
   - Nothing essential at the level of coverage. The one item a maths reader needs that the plan only touches is **definitional extension**: introducing a new predicate or function symbol by a definition (|x|, "continuous", ⌊x⌋ via ∃!), and why doing so proves nothing new. Give it one subsection in 4.8, after the function-symbol-against-graph material, and a 6.2 dictionary row ("we define …").
   - Many-sorted quantifiers are rightly left to bounded quantifiers (`def-bounded-quantifier`, 93 citations).
7. **Technique-only risks.**
   - The 15-sequent batteries (1.6, 2.7), sourced [Le, vD], must not reproduce Lemmon's numbered sequent list or its order. Choose fd1's own laws, grouped by fd1's named moves.
   - Do not take Sider's "in excessive detail" as a heading or a running label. Call it fd1's own "clause-by-clause" proof.
   - Do not name the 3/5 closing paragraphs "Interlude".
   - Write the truth-teller and suspect puzzles from scratch, in mathematical dress (statements about integers), rather than in the knights-and-knaves frame.
   - The other borrowings in §3 are devices, and pass.
8. **Delete `lpl.txt`** from the scratchpad now, not "after approval". No drafter or reviewer stage needs it, and the plan's own rule 3 forbids it as an input.
