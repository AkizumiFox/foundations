# fd1 *Logic and Proof*: the final layout (Layout B, with grafts)

**Status.** This is the binding whole-book layout for the deepening. It replaces §2 and §4 of `plan.md` and supersedes layouts A, B and C. It takes Layout B, which two of the three judges chose as the frame. It grafts in the ideas the judges recommended from A and C, and it settles each conflict between them in §0. The **Critic review** in `plan.md` stays binding, and §9 checks it item by item. Nothing in fd1, fd2, fd3, fd4, an1 or math-atlas has been changed.

**Inputs and counts (re-measured 2026-10-12; `_build` excluded throughout).**
- `fd1/src` has 38 section files and **490 anchors**: 479 block labels, 2 equation labels and 9 heading ids. Layout C's figure of 482 left out the two `eq-` labels and seven uncited heading ids; Layout B's 490 is right.
- Downstream, fd2, fd3, fd4 and an1 (`src` and `authoring`) cite **83 distinct `@fd1:` labels**, 79 of them from `src`, in 1,055 occurrences (636 in `src`). All 83 exist today. `cited.txt` lists 77 because it left out six labels that only an1 cites: `def-rules-disjunction`, `exm-abs-product-cases`, `exm-square-plus-one`, `exm-triangle-inequality-cases`, `exr-negation-and-contradiction-c1` and `prp-equivalence-cycle`. Its counts (`ax-induction` 2,754) include rendered output and should not be quoted. The bracketed counts in this file are occurrences in `src` and `authoring` (`ax-induction` 300). The refreshed list is `final-cited.txt`, next to this file.
- Downstream prose pointers of the form "*Logic and Proof*, Chapter N / Section N.M / Chapters a–b": **about 216 phrases**, extracted by `final/ptrs.py` and listed in §5.2.
- **Banks of 15** mean Chapters 1 and 2 as numbered here. These are also the two rule chapters of Part I, so the phrase can be read only one way. Every other chapter has banks of 12, and the prose sections have banks of 8, as in B.

**The book in one paragraph.** fd1 stays proof-first and is rebuilt as two halves that mirror each other, followed by the prose hand-off. Each half moves through **rules**, then **tasks** with those rules alone, then **meaning**. Each meaning chapter opens on the one question its tasks chapter cannot settle: "how do we show that something is *not* derivable?" The propositional half closes with soundness and completeness, both proved on the core. The first-order half closes with structures, counter-models, theories and definability. Chapter 1 stays as delivered and keeps its number. Sections 2.1–2.5 keep their numbers. Whole chapters move as blocks: old 3 becomes 4 and old 5 becomes 8, so most downstream "Chapter N" pointers map mechanically. The one structural cut is old Chapter 4, which splits into Chapters 5, 6 and 7.

---

## 0. How the judges' grafts were resolved

| # | Graft (source; who asked) | Decision | Reason |
|---|---|---|---|
| G1 | `def-truth-function` onto the core, in the valuations section (C; J1, J3) | **Adopted**: it goes in 4.4 | It is cited downstream (2 occurrences; `cited.txt`'s "15" counted rendered output), and it is the definition behind truth-functionality. Second-pass 4.9 then cites it. |
| G2 | `lem-weakening-cut` into 2.3 (C; J1, J3) | **Adopted** | It is purely syntactic and needs no induction, and it is the reason derived rules are legitimate. It is uncited downstream, and 2.3 keeps its number. |
| G3 | Weave the prose dictionaries into the parts (C; J1 conditional, J2) | **Rejected. Dictionaries stay in Chapter 8**, with J1's fallback: the "we define" and "the limit" rows are introduced at their source (5.8) and collected in 8.2 | Old 5.1 is written for a reader who already knows the quantifiers. It cites four quantifier-law labels (`prp-quantifier-negation`, `prp-negated-implication`, `prp-bounded-quantifier-negation`, `prp-arbitrarily-close-equal`) and negates "upper bound". The solution of the downstream-cited `exr-connective-rhetoric-c1` (fd3 3.3 cites it twice) uses ∀I. Moving 5.1 in front of Chapter 5 would therefore change the content of a cited label, which breaks constraint 2. Layout C's claim that "old 5.1 cites no Chapter 3 or 4 label" is false (grep). Old 5.2 cites `exm-uniform-implies-continuous`. Weaving it alone would split the dictionary in two for little gain, and keeping both together keeps F1.5's file numbers. |
| G4 | Split old 3.2 at "Structural induction" (A, C; J1, J3) | **Adopted**: 4.2 covers the natural numbers, 4.3 covers formulas | B's combined 4.2 would go over the 5,000-word cap once the plan's additions land. The seam already exists (line 189). Downstream "Section 3.2" pointers (7, all about numerical induction) get a clean target, 4.2, and the file stem `02-induction` keeps the label prefix. |
| G5 | Retroactive paragraphs at soundness and at counter-models (C; J1, J3) | **Adopted** in 4.7 and 7.2 | Each names the earlier informal moves it now certifies: 1.1's breaking, the derive-or-break items of 1.5 onwards, 3.2's withheld verdicts, and the counter-readings of 5.3–6.4. |
| G6 | Syntactic replacement rule with C's exact statement (C; J1, J3) | **Adopted** in 6.2 as `prp-replacement` | If ⊢ φ ↔ ψ, then ⊢ χ[φ] ↔ χ[ψ], by induction on χ. The connective cases use 2.4, the quantifier cases use ∀I and ∃E with the flag checked, and completeness is never invoked. The proof is in a fold. |
| G7 | "Check it against meaning" as tables, not boxes (A; J1, J2, J3) | **Adopted** as two tables. In 4.7, each row is a rule case of soundness, tied to the Ch1–2 section that introduced the rule. In 7.2, each row is a side-condition counter-model (∀I flag, ∀E free-for or capture, ∃E witness name), with the WRONG version beside the RIGHT one | This keeps A's pairing without putting semantics in front of the negation rules. The tables live in sections that are already budgeted (≤ 400 words each, as a table plus captions). |
| G8 | Theories off the hard trunk (A; J1, J2) | **Adopted, stated honestly.** `F1.5: {s: [F1.8], b: [F1.6]}`. Must-read to F2.1 and AN1.1 is about 229 h | Chapter 8 cites Chapter 7 only for the *statement* that counter-models rule out derivations (old 5.7:18, 77, 258 cite "Section 4.11"). That is a black-box borrowing. **But F2.3 (fd2 Chapter 3) uses 7.1–7.2 for real**: fd2 3.6 builds a counter-model and 3.1 cites `exr-models-c1/c2`. So F2.3 gets `s: [F1.6]`, and F1.6 is on the trunk to AN1.3 and later. The atlas says exactly that. |
| G9 | "Test the subgoal" as a named move (A; J1) | **Adopted, in 4.7 (soundness), not 4.6** | Refuting a subgoal by a row shows that it is not derivable only *because of* soundness. 4.6 teaches the search and points forward. 4.7 names the move, with a look-back to 3.1's moves. Putting it before soundness would assert something not yet proved. |
| G10 | Word the informal counter-readings in 5.3–6.4 so that 7.2 can upgrade them (A; J1) | **Adopted** as a STYLE wording rule (D1) | Before 4.7, the text may say "the form breaks" or "invalid", but never "not derivable" except as a forward claim citing 4.7. For first-order logic before 7.2, the same rule applies to "counter-reading" and 7.2. |
| G11 | TAUT timing (A; J3) | **Adopted.** `def-rule-taut` is defined *propositionally* in 4.8. The propositional skeleton and its licence come in 6.3, once first-order syntax and rules exist | The licence is stated as propositional completeness plus **uniform substitution of formulas into a Fitch derivation**, a syntactic induction on derivations, as `prp-taut-skeleton`. The non-example ∀x∀y R ⊢ ∀y∀x R is kept. 6.4 (the capstone) and 8.3 (silent steps) use it. |
| G12 | Keep the propositional completeness proof on the core (B; J1, J3 against J2's C) | **Adopted**: 4.8 is core | It is the one cheap, central metatheorem fd1 can prove, and fd1 is the series' only logic volume. `thm-completeness` keeps its statement and its proof together, so no detached-proof convention is needed. |
| G13 | Named mirror table and Looking-back boxes (B; J2) | **Adopted** (§1.2) | Each twin section names its twin once and spends its words on what is new. |
| G14 | "Minimum for fd2" line in every index (A; J2) | **Adopted** | The line reads: "**Minimum before *Sets, Relations, and Cardinality*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Chapter 3." (prose names the book, not "fd2"; S7 of Chapter 1) |
| G15 | Keep plan.md's F1.6 = Models (A, B; J2) | **Adopted.** New ids: F1.7 for Finding Derivations and F1.8 for Working with Quantifiers | No id changes meaning. F1.3 still means truth tables, soundness and completeness, and its file numbers 01 and 02 still mean formulas and induction. |
| G16 | D2 (the sweep) once, before Wave 1, with a split-aware map (C; J2, J3) | **Adopted** (§8) | The drafters then write in the final numbering, and no drafted text is swept twice. |
| G17 | Counting old 2.6/2.7 items against the bank budget (J2 on C) | **Moot.** In this layout 2.6 and 2.7 are in Chapter 3, whose battery section (3.3) replaces an A2 bank, as in B | — |

---

## 1. Final table of contents

### 1.1 Shape

| Part | Ch | Atlas id | Title | Role | Sections (core / 2p / opt) | Core h | Full h |
|---|---|---|---|---|---|---|---|
| I Propositional | 1 | F1.1 | Connectives and Derivations | rules (∧, →, ∨) | 6 / – / – | 39 | 62 |
| | 2 | F1.2 (retitled) | Negation and Classical Logic | rules (⊥, ¬, ↔, RAA) | 5 / – / – | 29 | 47 |
| | 3 | **F1.7** (new) | Finding Derivations | tasks | 3 / – / – | 16 | 27 |
| | 4 | F1.3 | Truth, Soundness and Completeness | meaning and metatheory | 8 / 1 / 1 | 46 | 86 |
| II First-order | 5 | F1.4 | Predicate Logic and the Quantifier Rules | rules (∀, ∃, =, ∃!) | 8 / – / – | 45 | 72 |
| | 6 | **F1.8** (new) | Working with Quantifiers: Translation, Laws and Search | tasks, ending on the capstone | 4 / – / – | 21 | 36 |
| | 7 | **F1.6** (new; plan.md's id) | Models and Theories | meaning | 4 (7.5 partly 2p) / – / 2 | 21 | 56 |
| III Prose | 8 | F1.5 | From Derivations to Mathematical Prose | the hand-off to fd2 (last core chapter) | 7 / – / 1 | 33 | 55 |
| | | | **Total** | | **45 core, 1 2p (+ half of 7.5), 4 opt = 50 files** | **≈ 250** | **≈ 441** |

Keys used below:
- **K**: kept in place.
- **E**: expanded in place (the D additions).
- **M**: moved or renumbered.
- **S**: split.
- **N**: new.
- **core**; **2p** (second pass, excluded from core hours); **opt** (`.optional`; nothing core depends on it).

Words are binding **main-line** maxima under the STYLE cap of 5,000. Folds are budgeted in the S1 addenda. "D" names the `plan.md` §3 item carried, and "C" names a Critic-review correction honoured.

### 1.2 The mirror (named in each twin's Looking-back box)

| Propositional | First-order | Shared idea |
|---|---|---|
| Ch1–2, one rule per section | 5.3–5.8, one rule per section | intro/elim pairs, rule card, gallery, "Not allowed" block |
| 3.1 How to Find a Derivation | 6.3 Finding First-Order Derivations | backward/forward search, named moves |
| 3.2 Four Kinds of Task (syntactic **consistent**) | 6.3 (the four tasks with quantifiers), 6.2 (equivalence tasks) | the task decides the search |
| 3.3 From Argument to Derivation | 6.1 Translating Mathematics | informal → formal, then derive |
| 4.4 Valuations and Truth Tables | 7.1 Structures and Satisfaction | meaning by recursion on formulas |
| 4.5 (**satisfiable**) – 4.6 Hunting for a Refuting Row | 7.2 Counter-models | the counterexample set, searched |
| 4.7 Soundness (rule-by-rule meaning table) | 7.3 Soundness for Predicate Logic (opt); 7.2 side-condition table | same induction, more cases |
| 4.8 Completeness (proved) | 7.6 completeness (stated, Henkin sketch folded) | ⊢ and ⊨ agree |
| 4.9 Normal Forms (2p) | 7.5 Definability and Isomorphism | what the language can say |
| 4.10 Compactness (opt) | 7.6 compactness, Löwenheim–Skolem (opt) | finite character |
| — | 7.4 Theories and Their Models | no propositional twin |

**The counterexample set runs as one thread**, and each link comes after the one before:
1. break it (1.1);
2. inconsistent, Γ, ¬φ ⊢ ⊥ (3.2);
3. refuting row and search tree (4.5–4.6);
4. certified by soundness (4.7);
5. counter-model and the side-condition table (7.2);
6. consistency and independence of a theory (7.4).

### 1.3 Sections

#### Part I. Propositional logic

**Chapter 1. Connectives and Derivations (F1.1): arrangement unchanged.** Drafted only from `ch01-deepen.md` (plan.md §3.1). The renumbering touches Chapter 1 at **4 forward pointers**:
- "Chapter 3" ×3 becomes "Chapter 4";
- "Chapter 4" ×1 becomes "Chapter 5".

There are also 3 "Chapter 2" hits, checked by hand for "search", which becomes Chapter 3. `ch01-deepen.md` writes these pointers in the new numbering, so D2 does not touch ch01 files while the pilot is in flight.

| § | Title | Words | Status | Key | Carries |
|---|---|---|---|---|---|
| idx | Opening quiz "Five tempting misreadings"; roadmap; Summary, Terms, Minimum for fd2 | ≤ 1,300 | core | E | D 3.1 |
| 1.1 | Statements, Arguments and How to Break One | ≤ 5,000 | core | E | D 3.1 (1.1) |
| 1.2 | Derivations, Starting with And | ≤ 5,000 | core | E | D 3.1 (1.2) |
| 1.3 | Using an Implication: Modus Ponens | ≤ 4,300 | core | E | D 3.1 (1.3) |
| 1.4 | Proving an Implication: the Rule of the Box | ≤ 5,000 | core | E | D 3.1 (1.4) |
| 1.5 | Or, Introduced | ≤ 4,300 | core | E | D 3.1 (1.5) |
| 1.6 | Using Or: Proof by Cases (15-sequent battery of fd1's own laws: C small 7) | ≤ 5,000 | core | E | D 3.1 (1.6) |

**Chapter 2. Negation and Classical Logic (F1.2, retitled).** Sections 2.1–2.5 keep their numbers, so the frozen R3 rule "section numbers do not change" stays true for them.

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Roadmap; Summary, Terms; Minimum for fd2 | ≤ 1,000 | core | E | D 3.0 (8) |
| 2.1 | Contradiction: Using a Negation | ⊥ rules, ex falso, vacuous truth; paradoxes of material implication | ≤ 3,600 | core | E | D 3.2 (2.1) |
| 2.2 | Proving a Negation | ¬I; √2 → √3 → √p | ≤ 2,600 | core | E | D 3.2 (2.2) |
| 2.3 | Derived Rules: Proved Sequents as New Rules | MT, contrapositive, DS; **`lem-weakening-cut` moved in from old 3.6** (statement and proof, syntactic) as the reason a derived rule is legitimate; "Not allowed" block | ≤ 3,500 | core | E, M(label) | D 3.2 (2.3); G2 |
| 2.4 | Iff, Equivalence, and What a Definition Says | ↔ rules, provable equivalence, TFAE; `lem-not-iff-own-negation` | ≤ 3,700 | core | E | D 3.2 (2.4) |
| 2.5 | Proof by Contradiction and the Classical Rules | RAA, DN, LEM, Peirce, De Morgan; restricted rule sets; **new chapter R items** `exr-reductio-and-classical-rules-r1…r3` | ≤ 4,800 | core | E | D 3.2 (2.5); C1 |

**Chapter 3. Finding Derivations (new; F1.7).** *Motivating question:* "You know every propositional rule. Given a sequent, how do you find a derivation, or decide to stop looking?" The chapter owns the syntactic counterexample set and the word **consistent**.

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Motivating question; the named moves gathered; Summary, Terms; Minimum for fd2 | ≤ 1,000 | core | N | D 3.0 (8) |
| 3.1 | How to Find a Derivation (was 2.6) | Partial derivations, backward/forward, postponing ∨, RAA last; **the detour rule**; three new moves; a failed search; Harman (fold) | ≤ 5,000 | core | M, E | D 3.2 (2.6) |
| 3.2 | Four Kinds of Task | Theorem, equivalence, **inconsistency** (derive ⊥), derive-or-break with the verdict withheld; `def-inconsistent-set`, `prp-inconsistent-derives-everything`, `prp-derivable-iff-negation-inconsistent`; A2 bank of 12 | ≤ 4,600 | core | N | D 3.2 (2.7, first half) |
| 3.3 | From Argument to Derivation | One fixed integer key; extracting the argument from a paragraph; two-column items (informal proof, then the derivation that mirrors it); a one-page **library of standard sequents grouped by use** (fd1's own order, C small 7); Curry as a C item; a 15-item B battery **in place of** an A2 bank; **the chapter's R items**: `exr-finding-derivations-r1…r3` (moved from 3.1, prefix kept) plus a dialogue-extraction item | ≤ 3,400 | core | N | D 3.2 (2.7, second half); D 3.6 (6.4 argument extraction moved here) |

3.3's Looking-ahead box carries the question "how could we show something is *not* derivable?", and Chapter 4's index opens with it. This is today's 2.6 → Chapter 3 seam, one chapter later.

**Chapter 4. Truth, Soundness and Completeness (F1.3; was Chapter 3).**

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Opens with 3.3's question; frozen R3 "Where this goes" gains 7.4, 7.5; Summary with "what is proved, what is open" (not "Interlude") | ≤ 1,000 | core | E | C small 7 |
| 4.1 | Formulas as Objects (was 3.1) | Parse trees, subformulas, height; object language and metalanguage; Polish notation C | ≤ 4,600 | core | M, E | D 3.3 (3.1) |
| 4.2 | Induction on the Natural Numbers (old 3.2, lines 1–188) | `ax-induction`, worked examples, strong induction, threes and fives; **induction checklist** box (reused in 4.3, 4.7, 7.3); false-thesis and inventor's-paradox C items | ≤ 3,400 | core | S, E | D 3.3 (3.2); G4 |
| 4.3 | Induction and Recursion on Formulas (old 3.2, lines 189–425; new file `03-structural-induction.md`) | Structural induction, parenthesis count, **unique readability with its proof on the main line** (the core recursion must not rest on an unproved statement: J3), structural recursion; dots picture | ≤ 3,400 | core | S, E | D 3.3 (3.2); G4 |
| 4.4 | Valuations and Truth Tables (was 3.3) | Valuations by recursion (4.3), coincidence, tables, backwards from F; **truth-functionality with `def-truth-function` moved in from old 3.7**; game reading; tonk (fold); two integer puzzles | ≤ 4,100 | core | M, E | D 3.3 (3.3); G1 |
| 4.5 | Tautologies, Entailment and Equivalence (was 3.4) | ⊨, ≡, `lem-replacement`, `lem-substitution`; contingent, contradictory, contrary; **satisfiable** = existing `def-satisfiable` (no duplicate: C1); reduction to unsatisfiability; paired in a box with 3.2's *consistent* | ≤ 5,000 | core | M, E | D 3.3 (3.4); C1 |
| 4.6 | Hunting for a Refuting Row | Forced moves, splitting, search tree, closed tree ⇒ ⊨, satisfiability testing, flowchart; `prp-search-decides` (proof folded); a Looking-ahead line saying the move "test the subgoal" is licensed in 4.7 | ≤ 4,600 | core | N | D 3.3 (3.5) |
| 4.7 | Soundness (was 3.5) | `thm-soundness`, `cor-refuting-row`, `thm-raa-independent`; two-level box; **rule-by-rule meaning table** (one row per primitive rule: the section that introduced it, its case in the induction, and for →I, ∨E, ¬I and RAA the WRONG variant with its refuting row: G7); **retroactive paragraph** (G5); **"test the subgoal"** named, with a look-back to 3.1 (G9); "satisfiable ⇒ consistent" in the text | ≤ 4,500 | core | M, E | D 3.3 (3.6); G5, G7, G9 |
| 4.8 | Completeness (was 3.6) | `thm-completeness`, `cor-derivable-iff-valid` (statement and proof together); "consistent ⇔ satisfiable" in the text; the ⊢/⊨ table; **`def-rule-taut` for propositional formulas only** (G11); structural properties of ⊢; Kreisel (fold); Challenge **closed tree ⇒ Fitch derivation** (C2); **the chapter's R items**: `exr-normal-forms-r1…r3` (moved, prefix kept) | ≤ 5,000 | core | M, E | D 3.3 (3.7); C2; G11, G12 |
| 4.9 | Normal Forms and Adequate Connectives (was 3.7) | DNF, CNF, adequacy (citing 4.4's `def-truth-function`); calculating with equivalences; `thm-monotonicity`; set-algebra bridge; interpolation C | ≤ 5,000 | 2p | M, E | D 3.3 (3.8) |
| 4.10 | Compactness and Maximal Consistent Sets | **⊢ and ⊨ defined for infinite Γ** (derivable from a finite sub-list: C small 1); Lindenbaum, truth lemma, compactness; graph colouring | ≤ 4,500 | opt | N | D 3.3 (3.9); C small 1 |

#### Part II. First-order logic

**Chapter 5. Predicate Logic and the Quantifier Rules (F1.4; was 4.1–4.7).** The index keeps Chapter 4's frozen motivating question. The models paragraph moves to Chapter 7's index.

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Summary, Terms; Minimum for fd2 | ≤ 1,000 | core | E | — |
| 5.1 | Predicates and Quantifiers (was 4.1) | Reading ∀, ∃, bounded quantifiers; finite-domain ∀ as a long ∧; existential import; **seam:** the `cor-refuting-row` citation becomes a counter-reading with a Looking-ahead to 7.2 (staged translation and minimal pairs move to 6.1) | ≤ 4,600 | core | M, E | D 3.4 (4.1) |
| 5.2 | Terms, Formulas, Free Variables and Substitution (was 4.2) | Syntax by recursion (4.3); free-for; simultaneous against sequential | ≤ 4,400 | core | M, E | D 3.4 (4.2) |
| 5.3 | Using "For Every": Instantiation (was 4.3) | ∀E; gallery; ∀E as ∧E over {0,1,2} | ≤ 3,500 | core | M, E | D 3.4 (4.3) |
| 5.4 | Proving "For Every": Let x Be Arbitrary (was 4.4) | ∀I and the flag; critique; relation-property items | ≤ 4,200 | core | M, E | D 3.4 (4.4) |
| 5.5 | Proving "There Exists": Exhibit a Witness (was 4.5) | ∃I; derive-or-break with counter-readings worded for 7.2 (G10) | ≤ 3,400 | core | M, E | D 3.4 (4.5) |
| 5.6 | Using "There Exists": Name a Witness (was 4.6) | ∃E; twin figure with ∨E; **the barber and Russell's theorem** (`thm-barber`); finite choice | ≤ 5,000 | core | M, E | D 3.4 (4.6) |
| 5.7 | Equality (old 4.7, lines 1–249 and 409–444) | =I, =E, congruence, calculation chains; Leibniz's Law; opacity; logical half of extensionality; **`rule-phrase-lean-table` ends this, the last rule section** (C1; it has no ∃! rows) | ≤ 4,000 | core | S, E | D 3.4 (4.7); C1 |
| 5.8 | Unique Existence, Counting and Descriptions (old 4.7, lines 250–408, + new; file `08-counting-and-descriptions.md`) | ∃! (labels kept with their `equality-and-uniqueness` prefix); at least, at most and exactly *n*; distinct letters need not be distinct objects; "the x such that φ"; function symbol against its graph; **definitional extension** (C small 6) with the **"we define …" and "the limit" phrases introduced here** (G3 fallback); only, except and superlatives **as drills** (C3); **the chapter's R items** (new `exr-counting-and-descriptions-r*`) | ≤ 4,800 | core | S, N | D 3.4 (4.8); C3; C small 6 |

**Chapter 6. Working with Quantifiers: Translation, Laws and Search (new; F1.8).** *Motivating question:* "You know every quantifier rule. Can you turn a definition from analysis into a formula, negate it without error, and find the derivation it needs?"

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Motivating question; mirror of Chapter 3; Summary, Terms; Minimum for fd2 | ≤ 1,000 | core | N | — |
| 6.1 | Translating Mathematics (was 4.8) | Nested and bounded quantifiers, `prp-bounded-quantifier-rules`, `exm-translate-limit`; staged translation and minimal pairs (from 4.1, as drills); traps gallery; one ℕ key over 20 items; translation error against derivation error. "The search method, extended" moves out to 6.3 | ≤ 4,200 | core | M, E | D 3.4 (4.9) |
| 6.2 | Negating and Moving Quantifiers (was 4.9) | Quantifier negation and passage laws; negating definitions; A/E/I/O square; prenex form; **`prp-replacement`, the syntactic replacement rule** (G6; proof folded); ∃ := ¬∀¬ C | ≤ 4,600 | core | M, E | D 3.4 (4.10); C2; G6 |
| 6.3 | Finding First-Order Derivations | Search with flags and witnesses: open ∃E boxes early, postpone ∀E until the term is known; the **propositional core** move; **`def-propositional-skeleton` and `prp-taut-skeleton`** (TAUT for first-order formulas, licensed by propositional completeness plus uniform substitution into a Fitch derivation; non-example ∀x∀y R ⊢ ∀y∀x R; G11); the four tasks of 3.2 with quantifiers ("break it" by counter-reading until 7.2); drinker C, Darapti C; a first-order library of sequents; a B battery **in place of** an A2 bank | ≤ 4,500 | core | N | D 3.4 (4.9 search extended, propositional core; 4.10 drinker, Darapti); C2 |
| 6.4 | Uniformly Continuous Implies Continuous, Rule by Rule (was 4.10) | Capstone derivation; **witness functions** δ(ε), δ(ε, x); critique of a "proof" of the converse (its search stalls, which hooks Chapter 7); **shortened with TAUT (skeleton)**; **the chapter's R items** (new `exr-uniform-continuity-rule-by-rule-r*`: C1) | ≤ 3,600 | core | M, E | D 3.4 (4.11); C1 |

**Chapter 7. Models and Theories (new; F1.6).**
- *Motivating question* (C3): "Do the axioms of a partial order prove that any two elements are comparable?" A two-point antichain settles it. The groups version returns in 7.4 with the six symmetries of a triangle.
- *How to read this chapter* (C1): the statement "a counter-model rules out every derivation" is on the trunk in 7.2, and its proof is optional, in 7.3, directly after it.

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Motivating question; reading note; Summary with "what is proved, what is open"; Terms; Minimum for fd2 | ≤ 1,000 | core | N | C1, C3 |
| 7.1 | Structures and Satisfaction (old 4.11, lines 1–238) | Structures, assignments, satisfaction, `lem-free-coincidence` (proof folded), ⊨; `#why-domains-are-non-empty`; the ℂ square-root check (fd4 1.4 pays it); arrow and Hasse pictures; a clause-by-clause direct semantic proof (C small 7); drinker checked semantically | ≤ 4,600 | core | S, E | D 3.5 (5.1) |
| 7.2 | Counter-models (old 4.11, lines 239–316, + new) | Three pictured counter-models (frozen R4 plan); `#from-counter-models-to-non-derivability` with its statement; the **counter-model procedure** (4.6's template); small domains by expansion (the monadic bound as a remark only: C small 5); the hierarchy *instance of a tautology (skeleton sense, 6.3) ⊂ valid ⊂ true in (ℕ; 0, S, +, ·, <)* (C small 4); **side-condition table** (G7); **retroactive paragraph** certifying the counter-readings of 5.1–6.4 one by one (G5); the converse of extensionality | ≤ 4,600 | core | S, N | D 3.5 (5.2); C small 4, 5; G5, G7 |
| 7.3 | Soundness for Predicate Logic (was 4.12) | `lem-term-substitution`, renaming, `thm-first-order-soundness`, **`cor-counter-model` beside it** (C1); pointer to the 4.2 checklist | 5,178 (unchanged) | opt | M | D 3.5 (5.5); C1 |
| 7.4 | Theories and Their Models | `def-theory`, `def-model-of-theory`; axioms as sentences (equivalence relation; strict, partial, linear and dense order; group; field) with drawn models and non-models; **`def-inconsistent-theory`: T ⊢ ⊥ from finitely many axioms** (C small 2); `prp-model-shows-consistency` and `prp-model-shows-independence`, citing 7.2's heading, "proved in the optional Section 7.3" (C1); the triangle group (table given, associativity checked by a D0 script: C3); independence of reflexive, symmetric and transitive | ≤ 4,800 | core | N | D 3.5 (5.3); C1; C3; C small 2 |
| 7.5 | Definability and Isomorphism | **Core:** a formula defines a set; ∃ as projection; "define this by a formula". **Second pass:** `def-isomorphism-of-structures`, `thm-isomorphism-invariance` (proof folded), automorphisms prove non-definability, on finite pictured structures and (ℤ, <) (C3). **The chapter's R items:** `exr-models-r1…r4` (moved, prefix kept: C1) | ≤ 4,200 (core ≤ 2,600, 2p ≤ 1,600) | core, part 2p | N | D 3.5 (5.4); C1; C3 |
| 7.6 | What First-Order Logic Can and Cannot Say | All stated without proof: completeness (Henkin sketch folded), compactness, Löwenheim–Skolem, non-standard ℕ, the induction schema against the second-order axiom, Church, monadic decidability, incompleteness named | ≤ 4,200 | opt | N | D 3.5 (5.6) |

#### Part III. Prose

**Chapter 8. From Derivations to Mathematical Prose (F1.5; was Chapter 5).** File numbers 01–07 are kept, so every `F1.5 §0N` tag stays valid.
- *What you need:* Chapters 1–6. 7.2's statement is cited as a black box (`b` edge).
- *Minimum for fd2:* this chapter.

| § | Title | Content | Words | Status | Key | Carries |
|---|---|---|---|---|---|---|
| idx | | Summary, Terms; glossary pointer | ≤ 1,000 | core | E | — |
| 8.1 | The Connective Rules in Prose (was 5.1) | Dictionary rows; constructive dilemma; TFAE cycles; spoken assumption purposes | ≤ 4,900 | core | M, E | D 3.6 (6.1) |
| 8.2 | The Quantifier Rules in Prose (was 5.2) | Rows collected: "it suffices to prove something stronger", "the limit" and "we define …" (introduced in 5.8), double inclusion | ≤ 4,200 | core | M, E | D 3.6 (6.2); C small 6 |
| 8.3 | Four Levels of One Proof (was 5.3) | Levels; silent steps tied to TAUT (4.8, 6.3); the "it suffices to show" column | ≤ 4,200 | core | M, E | D 3.6 (6.3) |
| 8.4 | Reading a Proof: Self-Explanation (was 5.4) | Self-explanation; argument extraction recalled from 3.3 | ≤ 2,200 | core | M, E | D 3.6 (6.4, part) |
| 8.5 | Writing a Proof (was 5.5) | From derivation to prose; a generalisation item | ≤ 2,800 | core | M, E | D 3.6 (6.5) |
| 8.6 | Checking Proofs, and What Is Not Allowed (was 5.6) | (N1)–(N11) **untouched**; (N12) distinct letters, (N13) empty "and so on", (N14) hidden premise **appended** | ≤ 3,000 | core | M, E | D 3.6 (6.6) |
| 8.7 | The Dispute over Excluded Middle (was 5.7) | One extra rule, ¬¬LEM, √2^√2; which direction of each law survives without RAA; R items r1–r4 stay; stated claims point to 8.8 (C small 3) | ≤ 3,900 | core | M, E | D 3.6 (6.7) |
| 8.8 | Stages of Knowledge: Kripke Models | Two- and three-node countermodels; heredity; soundness without RAA by reusing 4.7 | ≤ 3,600 | opt | N | D 3.6 (6.8) |

### 1.4 New labels (names fixed at S1; none collides with an existing label)

| § | Labels |
|---|---|
| 2.4 | `lem-not-iff-own-negation` |
| 2.5 | `exr-reductio-and-classical-rules-r1…r3` |
| 3.2 | `def-inconsistent-set`, `prp-inconsistent-derives-everything`, `prp-derivable-iff-negation-inconsistent` |
| 4.3 | new exercises take the stem `structural-induction` (`exr-structural-induction-*`) |
| 4.6 | `prp-search-decides` |
| 4.8 | `def-rule-taut` |
| 4.9 | `thm-monotonicity` |
| 4.10 | `def-infinite-entailment`, `lem-lindenbaum`, `thm-compactness` |
| 5.6 | `thm-barber` |
| 5.8 | counting definitions, `def-definite-description`, `prp-definitional-extension`, `exr-counting-and-descriptions-*` (with R items) |
| 6.2 | `prp-replacement` |
| 6.3 | `def-propositional-skeleton`, `prp-taut-skeleton` |
| 6.4 | `exr-uniform-continuity-rule-by-rule-r*` |
| 7.4 | `def-theory`, `def-model-of-theory`, `def-inconsistent-theory`, `prp-model-shows-consistency`, `prp-model-shows-independence` |
| 7.5 | `def-definable-set`, `def-isomorphism-of-structures`, `thm-isomorphism-invariance` |

No `def-satisfiable-set` and no `def-semantically-consistent` (C1). "Satisfiable ⇒ consistent" and "consistent ⇔ satisfiable" are stated in the text of 4.7 and 4.8. Label prefixes follow the **file stem at the time a label was born** and never change. The addenda say so explicitly, so that nobody "fixes" `exr-equality-and-uniqueness-b2` in 5.8, `exr-induction-b2` in 4.3, `exr-models-c1` in 7.2, `exr-finding-derivations-r*` in 3.3 or `exr-normal-forms-r*` in 4.8.

---

## 2. Reading path and dependency rules

- **First reading** (printed in the preface and in each index): 1 → 2 → 3 → 4.1–4.8 → 5 → 6 → 7.1, 7.2, 7.4, 7.5 (core part) → 8.1–8.7.
- **Second pass:** 4.9, and the isomorphism half of 7.5.
- **Optional:** 4.10, 7.3, 7.6, 8.8.
- **Minimum for fd2:** Chapters 1–6 and 8, core. 7.1–7.2 come before fd2 Chapter 3, and 7.4–7.5 are recommended.

Rules that S1 writes into every addendum, and that D1 writes into STYLE:
1. **Non-derivability wording (G10).** Before 4.7, no text asserts that something is not derivable except as a forward claim citing 4.7. For first-order logic, the same holds before 7.2. The frozen counter-reading sentence ("Section 4.11 states that a counter-reading rules out every derivation") becomes "Section 7.2".
2. **Statements on the trunk, proofs optional, only where already frozen.** This applies to 7.2 → 7.3 (C1). Propositional soundness and completeness keep statement and proof together on the core (G12).
3. **TAUT.** `\by{TAUT}` is allowed only in propositional derivations from 4.8, and on skeletons from 6.3. `check_fitch.py` enforces both (D0).
4. **Forward citations removed by the move** (listed for the addenda):
   - 5.1 → `cor-refuting-row` becomes a counter-reading;
   - 5.2 → `lem-substitution` (4.5) stays backward, and is fine;
   - 6.2 → `thm-raa-independent` (4.7) stays backward, and is fine;
   - 8.7 → "Section 4.11" becomes 7.2, a black box.

   No core section cites forward into 4.9, 4.10, 7.3 or 7.6 except as "(optional)".

---

## 3. Size and time

The formula is plan.md's B1, under which plan.md's own structure comes to 248 h:
- 15 min per 400 main-line words;
- per section, about 3.5 h of exercises with banks of 15, 3.0 h with banks of 12, 2.5 h for the prose sections (banks of 8), 1.6 h for the battery sections 3.3 and 6.3, and 1.5 h for 7.5's core part;
- index pages are not counted (about 8,300 words, about 5 h of reading in all).

| Ch | Atlas | Core §§ | Core main-line words | A2 parts (core) | Core h | Full h | Was (plan.md) |
|---|---|---|---|---|---|---|---|
| 1 | F1.1 | 6 | 28,600 | 90 | **39** | 62 | 39 / 62 |
| 2 | F1.2 | 5 | 18,200 | 75 | **29** | 47 | (Ch2 41 h, with 2.6–2.7) |
| 3 | F1.7 | 3 | 13,000 | 24 + battery | **16** | 27 | (from Ch2) |
| 4 | F1.3 | 8 (+1 2p, +1 opt) | 34,600 | 96 | **46** | 86 | 45 / 81 |
| 5 | F1.4 | 8 | 33,900 | 96 | **45** | 72 | (Ch4 63 h in all) |
| 6 | F1.8 | 4 | 16,900 | 36 + battery | **21** | 36 | (from Ch4) |
| 7 | F1.6 | 4 (7.5 partly 2p) | 16,600 | 42 | **21** | 56 | 26 / 56 |
| 8 | F1.5 | 7 | 25,200 | 56 | **33** | 55 | 34 / 57 |
| **Σ** | | **45** | **~187,000** | **~515 + 2 batteries** | **≈ 250** | **≈ 441** | **248 / 422** |

- **Against the target.** Core is about 250 h, +0.7% over 248. The 2 h come from the 4.2/4.3 split (one more exercise set, about +3 h), offset by B's choices: banks of 12 in Chapter 3, batteries in place of banks in 3.3 and 6.3, and the isomorphism half of 7.5 as second pass.
- **Levers to reach exactly 248**, each about 0.5 h:
  - (a) 3.3's library as a reference table outside the main-line count;
  - (b) 8.1's dictionary table counted as reference;
  - (c) 4.2 and 4.3 sharing one A2 bank of 12.
  
  plan.md's 12-part lever (about −10 h) stays in reserve.
- **Trunk.** Must-read to F2.1 and AN1.1 is about 229 h, which is everything except Chapter 7's 21 core hours (`F1.5 b: F1.6`). Through F2.3 and onwards to AN1.3 it is the full ~250 h, because fd2 Chapter 3 uses 7.1–7.2.
- **Largest chapter:** Chapter 4 at 46 h, against today's Chapter 4 at 56.5 h and plan.md's 63 h. **Smallest:** Chapter 3 at 16 h, a tasks chapter by design. Each of its sections carries one new idea (the detour rule; task types and `def-inconsistent-set`; argument extraction and two-column items).
- Each index recomputes its Time line from the delivered text (STYLE §11.9).

---

## 4. Migration

### 4.1 Files

| Old file | New file | Operation |
|---|---|---|
| `ch01-connectives-and-derivations/*` | same | none (deepened in place; file numbers 01, 02, 04–07 kept) |
| `ch02-negation-and-classical-logic/01–05`, `index.md` | same | in place; index rewritten (search leaves); 03 gains `lem-weakening-cut` |
| `ch02…/06-finding-derivations.md` | `ch03-finding-derivations/01-finding-derivations.md` | `git mv`; R items move to 03 |
| — | `ch03-finding-derivations/{index,02-four-kinds-of-task,03-from-argument-to-derivation}.md` | new |
| `ch03-semantics-soundness-completeness/` | `ch04-semantics-soundness-completeness/` | `git mv` of the directory |
| `ch03…/01-formulas-and-parse-trees.md` | `ch04…/01-…` | kept |
| `ch03…/02-induction.md` | `ch04…/02-induction.md` (lines 1–188 + numerical exercises) **and** `ch04…/03-structural-induction.md` (lines 189–425 + formula exercises) | split at "## Structural induction" |
| `ch03…/03`, `04`, `05`, `06`, `07` | `ch04…/04`, `05`, `07`, `08`, `09` | `git mv` (renumber); 06 loses `lem-weakening-cut`; 07 loses `def-truth-function` and its R items |
| — | `ch04…/06-refuting-row-search.md`, `10-compactness.md` | new |
| `ch04-predicate-logic/01–06`, `index.md` | `ch05-predicate-logic/01–06`, `index.md` | `git mv` of the directory |
| `ch04…/07-equality-and-uniqueness.md` | `ch05…/07-equality-and-uniqueness.md` **and** `ch05…/08-counting-and-descriptions.md` | split (∃! to 08) |
| `ch04…/08-translation.md`, `09-quantifier-laws.md`, `10-uniform-continuity-rule-by-rule.md` | `ch06-working-with-quantifiers/01-translation.md`, `02-quantifier-laws.md`, `04-uniform-continuity-rule-by-rule.md` | `git mv`; 01 loses "The search method, extended" to 03 |
| — | `ch06-working-with-quantifiers/{index,03-first-order-search}.md` | new |
| `ch04…/11-models.md` | `ch07-models-and-theories/01-structures-and-satisfaction.md` + `02-counter-models.md` | `git mv` to 01, then split at "## Counter-models" (line 239) |
| `ch04…/12-first-order-soundness.md` | `ch07-models-and-theories/03-first-order-soundness.md` | `git mv`, verbatim |
| — | `ch07-models-and-theories/{index,04-theories-and-models,05-definability-and-isomorphism,06-limits-of-first-order-logic}.md` | new |
| `ch05-from-derivations-to-prose/` (01–07, index) | `ch08-from-derivations-to-prose/` (01–07, index) | `git mv` of the directory; file numbers kept |
| — | `ch08…/08-kripke-models.md` | new |
| `src/index.md` (preface) | same | "What it covers" rewritten (8 rows, 3 parts); "Why rules before truth tables" re-pointed |
| — | `src/glossary.md` | new (D 3.0 (8)) |

That makes 38 old files, 12 new files and 50 in all. Kinds:
- **kept with their number:** 11 (1.1–1.6, 2.1–2.5);
- **chapter number changed, index kept:** 4.1, and 5.1–5.6, 8.1–8.7, 15 in all;
- **moved:** 2.6 → 3.1; 3.3–3.7 → 4.4, 4.5, 4.7, 4.8, 4.9; 4.8–4.10 → 6.1, 6.2, 6.4; 4.12 → 7.3, 10 in all;
- **split:** 3 (old 3.2, 4.7, 4.11);
- **new:** 3.2, 3.3, 4.6, 4.10, 6.3, 7.4, 7.5, 7.6, 8.8, plus the split-off files 4.3, 5.8 and 7.2.

### 4.2 Every current label (490 anchors), by old file

**Totals:**
- 163 labels keep their section number: Chapter 1, and 2.1–2.5;
- 327 change their displayed number;
- 77 change atlas id: old 2.6 → F1.7; old 4.8–4.10 → F1.8; old 4.11–4.12 → F1.6; `lem-weakening-cut` F1.3 → F1.2;
- no label is renamed or lost.

A bracketed number is a downstream-cited label with its occurrence count. "→ **x.y**" marks a label that does not follow its file.

| Old file | Old § | New § (file) | New file | Labels |
|---|---|---|---|---|
| `ch01…/01-statements-and-connectives.md` | 1.1 | 1.1 | ch01-connectives-and-derivations/01-statements-and-connectives.md | `def-statement`, `exm-statements`, `def-main-connective`, `exr-statements-and-connectives-a1`, `exr-statements-and-connectives-a2`, `exr-statements-and-connectives-b1`, `exr-statements-and-connectives-b2`, `exr-statements-and-connectives-b3`, `exr-statements-and-connectives-b4`, `exr-statements-and-connectives-c1` |
| `ch01…/02-derivations.md` | 1.2 | 1.2 | ch01-…/02-derivations.md | `def-rule-schema`, `def-box-free-derivation`, `exm-chaining-derivation`, `exm-not-a-derivation`, `def-derivable` [2], `def-sequent`, `exm-derivations`, `def-rules-conjunction` [1], `exm-conjunction-warm-ups`, `prp-and-commutes` [3], `prp-and-associative` [3], `exm-product-in-unit-interval`, `exr-derivations-a1`, `exr-derivations-a2`, `exr-derivations-b1`, `exr-derivations-b2`, `exr-derivations-b3`, `exr-derivations-c1`, `exr-derivations-c2`, `exr-derivations-c3`, `exr-derivations-c4` |
| `ch01…/04-using-an-implication.md` | 1.3 | 1.3 | ch01-…/04-using-an-implication.md | `exm-wason-selection`, `def-rule-implication-elimination`, `exm-implication-chains`, `exr-using-an-implication-a1`, `exr-using-an-implication-a2`, `exr-using-an-implication-b1`, `exr-using-an-implication-b2`, `exr-using-an-implication-b3`, `exr-using-an-implication-b4`, `exr-using-an-implication-c1`, `exr-using-an-implication-c2` |
| `ch01…/05-proving-an-implication.md` | 1.4 | 1.4 | ch01-…/05-proving-an-implication.md | `def-rules-implication` [3], `prp-implication-transitive`, `def-derivation`, `exm-illegal-citation`, `exm-first-boxes`, `prp-curry`, `exr-proving-an-implication-a1`, `exr-proving-an-implication-a2`, `exr-proving-an-implication-b1`, `exr-proving-an-implication-b2`, `exr-proving-an-implication-b3`, `exr-proving-an-implication-b4`, `exr-proving-an-implication-c1`, `exr-proving-an-implication-c2`, `exr-proving-an-implication-c3` |
| `ch01…/06-disjunction-introduction.md` | 1.5 | 1.5 | ch01-…/06-disjunction-introduction.md | `def-rule-disjunction-introduction`, `exm-disjunction-introduction-derivations`, `exm-or-hypothesis-split`, `exm-product-zero`, `exr-disjunction-introduction-a1`, `exr-disjunction-introduction-a2`, `exr-disjunction-introduction-b1`, `exr-disjunction-introduction-b2`, `exr-disjunction-introduction-b3`, `exr-disjunction-introduction-c1`, `exr-disjunction-introduction-c2` |
| `ch01…/07-disjunction-and-cases.md` | 1.6 | 1.6 | ch01-…/07-disjunction-and-cases.md | `def-rules-disjunction` [1], `exm-disjunction-first-derivations` [4], `exm-cases-on-hypothesis`, `prp-distributivity` [11], `exm-disjunction-regroup` [3], `exm-abs-at-least-x`, `exm-abs-product-cases` [1], `exm-triangle-inequality-cases` [3], `exr-disjunction-and-cases-a1`, `exr-disjunction-and-cases-a2`, `exr-disjunction-and-cases-b1`, `exr-disjunction-and-cases-b2`, `exr-disjunction-and-cases-b3`, `exr-disjunction-and-cases-b4`, `exr-disjunction-and-cases-c1`, `exr-disjunction-and-cases-c2`, `exr-disjunction-and-cases-c3`, `exr-disjunction-and-cases-c4`, `exr-disjunction-and-cases-r1`, `exr-disjunction-and-cases-r2`, `exr-disjunction-and-cases-r3` |
| `ch02…/01-contradiction-and-vacuous-truth.md` | 2.1 | 2.1 | ch02-…/01 (same file) | `def-rules-contradiction` [1], `exm-first-contradictions`, `prp-ex-falso`, `prp-vacuous-implication` [9], `exm-manufactured-clash`, `exm-impossible-case`, `thm-square-even-implies-even` [7], `exm-vacuous-square`, `exr-contradiction-and-vacuous-truth-a1`, `exr-contradiction-and-vacuous-truth-b1`, `exr-contradiction-and-vacuous-truth-b2`, `exr-contradiction-and-vacuous-truth-b3`, `exr-contradiction-and-vacuous-truth-c1`, `exr-contradiction-and-vacuous-truth-c2` |
| `ch02…/02-negation-and-contradiction.md` | 2.2 | 2.2 | ch02-…/02 (same file) | `def-rules-negation` [16], `exm-double-negation-introduction`, `exm-triple-negation`, `exm-square-plus-one` [1], `thm-sqrt2-irrational` [35], `exr-negation-and-contradiction-a1`, `exr-negation-and-contradiction-b1`, `exr-negation-and-contradiction-b2`, `exr-negation-and-contradiction-b3`, `exr-negation-and-contradiction-b4`, `exr-negation-and-contradiction-c1` [2], `exr-negation-and-contradiction-c2` |
| `ch02…/03-derived-rules.md` | 2.3 | 2.3 | ch02-…/03 (same file) | `prp-modus-tollens`, `prp-contrapositive` [17], `def-derived-rule` [6], `prp-disjunctive-syllogism`, `exm-derived-rules-in-use`, `exm-modus-tollens-instance`, `exm-square-even-via-contrapositive` [1], `exr-derived-rules-a1`, `exr-derived-rules-b1`, `exr-derived-rules-b2`, `exr-derived-rules-b3`, `exr-derived-rules-c1`, `exr-derived-rules-c2`, `exr-derived-rules-c3` |
| `ch02…/04-biconditional-and-definitions.md` | 2.4 | 2.4 | ch02-…/04 (same file) | `def-rules-biconditional` [1], `exm-iff-symmetric`, `prp-iff-two-implications` [10], `exm-iff-negations` [3], `def-provable-equivalence`, `prp-provable-equivalence-basics`, `thm-odd-iff-square-odd`, `thm-squares-order` [7], `exm-strictly-increasing-both-ways`, `prp-equivalence-cycle` [2], `exm-unit-interval-tfae`, `exr-biconditional-and-definitions-a1`, `exr-biconditional-and-definitions-b1`, `exr-biconditional-and-definitions-b2`, `exr-biconditional-and-definitions-b3`, `exr-biconditional-and-definitions-c1`, `exr-biconditional-and-definitions-c2` |
| `ch02…/05-reductio-and-classical-rules.md` | 2.5 | 2.5 | ch02-…/05 (same file) | `exm-raa-zero`, `def-rule-raa` [27], `prp-double-negation` [1], `prp-contrapositive-converse` [2], `prp-excluded-middle` [12], `prp-peirce`, `prp-de-morgan` [21], `prp-implication-as-disjunction`, `thm-classical-rules-interderivable`, `exr-reductio-and-classical-rules-a1`, `exr-reductio-and-classical-rules-b1`, `exr-reductio-and-classical-rules-b2`, `exr-reductio-and-classical-rules-b3`, `exr-reductio-and-classical-rules-b4`, `exr-reductio-and-classical-rules-c1`, `exr-reductio-and-classical-rules-c2`, `exr-reductio-and-classical-rules-c3` |
| `ch02…/06-finding-derivations.md` | 2.6 | 3.1 | ch03-finding-derivations/01-finding-derivations.md | `def-partial-derivation`, `exm-search-distribute`, `exm-search-cases`, `exm-search-postpone-or`, `exm-search-raa`, `exm-skeleton-odd-product`, `exr-finding-derivations-a1`, `exr-finding-derivations-b1`, `exr-finding-derivations-b2`, `exr-finding-derivations-b3`, `exr-finding-derivations-c1`, `exr-finding-derivations-c2`, `exr-finding-derivations-c3`, `exr-finding-derivations-c4`, `exr-finding-derivations-r1` → **3.3**, `exr-finding-derivations-r2` → **3.3**, `exr-finding-derivations-r3` → **3.3** |
| `ch03…/01-formulas-and-parse-trees.md` | 3.1 | 4.1 | ch04-semantics-soundness-completeness/01-formulas-and-parse-trees.md | `def-formula` [2], `exm-formation-sequences`, `exm-not-formulas`, `def-parse-tree`, `exm-parse-trees`, `def-subformula`, `def-height`, `exm-shorthand-translation`, `exr-formulas-and-parse-trees-a1`, `exr-formulas-and-parse-trees-b1`, `exr-formulas-and-parse-trees-b2`, `exr-formulas-and-parse-trees-c1` |
| `ch03…/02-induction.md` | 3.2 | 4.2 | ch04-…/02-induction.md (numbers) + 03-structural-induction.md (split) | `ax-induction` [300], `exm-sum-consecutive-products` [6], `exm-power-inequality` [6], `thm-strong-induction` [51], `exm-threes-and-fives` [9], `thm-structural-induction` [5] → **4.3**, `lem-parenthesis-count` → **4.3**, `thm-unique-readability` [7] → **4.3**, `thm-structural-recursion` [10] → **4.3**, `exm-recursive-definitions` → **4.3**, `exr-induction-a1`, `exr-induction-b1` [2], `exr-induction-b2` → **4.3**, `exr-induction-b3` → **4.3**, `exr-induction-c1` → **4.3**, `exr-induction-c2` → **4.3**, `exr-induction-c3` → **4.3** |
| `ch03…/03-valuations-and-truth-tables.md` | 3.3 | 4.4 | ch04-…/04-valuations-and-truth-tables.md | `def-valuation`, `def-truth-value` [1], `exm-value-down-the-tree`, `lem-coincidence`, `def-truth-table`, `exm-truth-table-modus-ponens`, `exm-table-contrapositive`, `exm-backwards-from-f`, `exr-valuations-and-truth-tables-a1`, `exr-valuations-and-truth-tables-b1`, `exr-valuations-and-truth-tables-b2`, `exr-valuations-and-truth-tables-b3`, `exr-valuations-and-truth-tables-c1`, `exr-valuations-and-truth-tables-c2` |
| `ch03…/04-entailment-and-equivalence.md` | 3.4 | 4.5 | ch04-…/05-entailment-and-equivalence.md | `def-tautology` [2], `def-satisfiable`, `def-valid-argument` [2], `exm-affirming-the-consequent`, `exm-three-premise-entailment`, `exm-grouping-of-implications`, `def-semantic-equivalence` [1], `prp-standard-equivalences` [9], `lem-replacement`, `lem-substitution`, `exr-entailment-and-equivalence-a1`, `exr-entailment-and-equivalence-b1`, `exr-entailment-and-equivalence-b2`, `exr-entailment-and-equivalence-b3`, `exr-entailment-and-equivalence-c1`, `exr-entailment-and-equivalence-c2` |
| `ch03…/05-soundness.md` | 3.5 | 4.7 | ch04-…/07-soundness.md | `lem-context-inclusion`, `thm-soundness` [1], `exm-soundness-run`, `cor-refuting-row` [3], `thm-raa-independent`, `exr-soundness-a1`, `exr-soundness-b1`, `exr-soundness-b2`, `exr-soundness-c1`, `exr-soundness-c2` |
| `ch03…/06-completeness.md` | 3.6 | 4.8 | ch04-…/08-completeness.md | `lem-weakening-cut` → **2.3**, `lem-connective-rows`, `lem-truth-table-line`, `exm-truth-table-line-run`, `lem-atom-splitting`, `thm-completeness` [5], `exm-completeness-run`, `cor-derivable-iff-valid`, `exr-completeness-a1`, `exr-completeness-b1`, `exr-completeness-b2`, `exr-completeness-b3`, `exr-completeness-c1`, `exr-completeness-c2` |
| `ch03…/07-normal-forms.md` | 3.7 | 4.9 | ch04-…/09-normal-forms.md (second pass) | `eq-many-term-values`, `def-literal`, `def-dnf`, `def-cnf`, `eq-row-conjunct`, `exm-dnf-exclusive-or`, `thm-dnf`, `thm-cnf`, `exm-normal-forms-two-routes`, `prp-cnf-validity`, `exm-cnf-validity-glance`, `def-truth-function` [2] → **4.4**, `def-adequate`, `thm-adequate-connectives`, `exr-normal-forms-a1`, `exr-normal-forms-b1`, `exr-normal-forms-b2`, `exr-normal-forms-b3`, `exr-normal-forms-c1`, `exr-normal-forms-c2`, `exr-normal-forms-c3`, `exr-normal-forms-c4`, `exr-normal-forms-r1` → **4.8**, `exr-normal-forms-r2` → **4.8**, `exr-normal-forms-r3` → **4.8** |
| `ch04…/01-predicates-and-quantifiers.md` | 4.1 | 5.1 | ch05-predicate-logic/01-predicates-and-quantifiers.md | `exm-reading-quantified-sentences`, `def-bounded-quantifier` [8], `exm-quantifier-order-sum`, `exr-predicates-and-quantifiers-a1`, `exr-predicates-and-quantifiers-b1`, `exr-predicates-and-quantifiers-b2`, `exr-predicates-and-quantifiers-c1`, `exr-predicates-and-quantifiers-c2` |
| `ch04…/02-terms-formulas-substitution.md` | 4.2 | 5.2 | ch05-…/02-terms-formulas-substitution.md | `def-term`, `def-first-order-formula` [8], `def-free-variable`, `def-sentence`, `exm-free-and-bound-limit`, `def-substitution`, `exm-computing-substitutions`, `def-free-for`, `exr-terms-formulas-substitution-a1`, `exr-terms-formulas-substitution-b1`, `exr-terms-formulas-substitution-b2`, `exr-terms-formulas-substitution-c1`, `exr-terms-formulas-substitution-c2` |
| `ch04…/03-universal-elimination.md` | 4.3 | 5.3 | ch05-…/03-universal-elimination.md | `def-rule-universal-elimination` [1], `exm-universal-elimination-derivations`, `exr-universal-elimination-a1`, `exr-universal-elimination-b1`, `exr-universal-elimination-b2`, `exr-universal-elimination-b3`, `exr-universal-elimination-c1`, `exr-universal-elimination-c2` |
| `ch04…/04-universal-introduction.md` | 4.4 | 5.4 | ch05-…/04-universal-introduction.md | `def-rules-universal` [16], `exm-universal-introduction-derivations`, `prp-forall-and`, `every-element-of-the-empty-set`, `exr-universal-introduction-a1`, `exr-universal-introduction-b1`, `exr-universal-introduction-b2`, `exr-universal-introduction-b3`, `exr-universal-introduction-c1`, `exr-universal-introduction-c2` |
| `ch04…/05-existential-introduction.md` | 4.5 | 5.5 | ch05-…/05-existential-introduction.md | `def-rule-existential-introduction` [4], `prp-forall-implies-exists`, `exm-existential-introduction-derivations`, `exr-existential-introduction-a1`, `exr-existential-introduction-b1`, `exr-existential-introduction-b2`, `exr-existential-introduction-b3`, `exr-existential-introduction-c1`, `exr-existential-introduction-c2` |
| `ch04…/06-existential-elimination.md` | 4.6 | 5.6 | ch05-…/06-existential-elimination.md | `def-rules-existential` [21], `prp-exists-and`, `exm-existential-elimination-derivations`, `prp-exists-forall-swap` [8], `existential-renaming`, `exm-sum-of-evens`, `exr-existential-elimination-a1`, `exr-existential-elimination-b1`, `exr-existential-elimination-b2`, `exr-existential-elimination-b3`, `exr-existential-elimination-c1`, `exr-existential-elimination-c2` |
| `ch04…/07-equality-and-uniqueness.md` | 4.7 | 5.7 | ch05-…/07-equality-and-uniqueness.md + 08-counting-and-descriptions.md (split) | `def-rules-equality` [11], `prp-equality-symmetric-transitive` [6], `def-unique-existence` [9] → **5.8**, `prp-unique-existence-use` [7] → **5.8**, `rule-phrase-lean-table`, `exr-equality-and-uniqueness-a1`, `exr-equality-and-uniqueness-b1`, `exr-equality-and-uniqueness-b2` → **5.8**, `exr-equality-and-uniqueness-b3` → **5.8**, `exr-equality-and-uniqueness-c1` → **5.8**, `exr-equality-and-uniqueness-c2` → **5.8** |
| `ch04…/08-translation.md` | 4.8 | 6.1 | ch06-working-with-quantifiers/01-translation.md | `exm-translate-limit` [4], `prp-bounded-quantifier-rules` [10], `exr-translation-a1`, `exr-translation-b1`, `exr-translation-b2`, `exr-translation-c1`, `exr-translation-c2` |
| `ch04…/09-quantifier-laws.md` | 4.9 | 6.2 | ch06-…/02-quantifier-laws.md | `prp-quantifier-negation` [43], `prp-negated-implication` [40], `prp-bounded-quantifier-negation` [65], `prp-quantifier-distribution`, `prp-quantifier-passage`, `exm-negating-definitions`, `prp-arbitrarily-close-equal` [8], `exr-quantifier-laws-a1`, `exr-quantifier-laws-b1`, `exr-quantifier-laws-b2`, `exr-quantifier-laws-b3`, `exr-quantifier-laws-c1`, `exr-quantifier-laws-c2` |
| `ch04…/10-uniform-continuity-rule-by-rule.md` | 4.10 | 6.4 | ch06-…/04-uniform-continuity-rule-by-rule.md | `exm-uniform-implies-continuous` [2], `exm-converse-fails`, `exm-square-not-uniform`, `exr-uniform-continuity-rule-by-rule-a1`, `exr-uniform-continuity-rule-by-rule-b1`, `exr-uniform-continuity-rule-by-rule-b2`, `exr-uniform-continuity-rule-by-rule-b3`, `exr-uniform-continuity-rule-by-rule-c1`, `exr-uniform-continuity-rule-by-rule-c2`, `exr-uniform-continuity-rule-by-rule-c3` |
| `ch04…/11-models.md` | 4.11 | 7.1 | ch07-models-and-theories/01-structures-and-satisfaction.md + 02-counter-models.md (split) | `def-structure`, `def-assignment`, `def-satisfaction`, `lem-free-coincidence`, `def-first-order-entailment`, `why-domains-are-non-empty`, `exm-counter-model-swap` [7] → **7.2**, `from-counter-models-to-non-derivability` [1] → **7.2**, `exr-models-a1`, `exr-models-b1` → **7.2**, `exr-models-b2`, `exr-models-b3` → **7.2**, `exr-models-c1` [2] → **7.2**, `exr-models-c2` [2] → **7.2**, `exr-models-c3` → **7.2**, `exr-models-r1` → **7.5**, `exr-models-r2` → **7.5**, `exr-models-r3` → **7.5**, `exr-models-r4` → **7.5** |
| `ch04…/12-first-order-soundness.md` | 4.12 | 7.3 | ch07-…/03-first-order-soundness.md (optional, verbatim) | `lem-term-substitution`, `cor-renaming-bound-variables`, `thm-first-order-soundness` [1], `counter-models-prove-non-derivability`, `cor-counter-model` [1], `exr-first-order-soundness-a1`, `exr-first-order-soundness-b1`, `exr-first-order-soundness-b2`, `exr-first-order-soundness-c1`, `exr-first-order-soundness-c2` |
| `ch05…/01-connective-rhetoric.md` | 5.1 | 8.1 | ch08-from-derivations-to-prose/01-connective-rhetoric.md | `exm-rhetoric-conjunction`, `exm-rhetoric-implication`, `exm-rhetoric-cases`, `exm-rhetoric-negation`, `exm-rhetoric-contradiction`, `exm-rhetoric-biconditional`, `exm-costume-direct`, `exm-costume-contrapositive`, `exr-connective-rhetoric-a1`, `exr-connective-rhetoric-b1`, `exr-connective-rhetoric-b2`, `exr-connective-rhetoric-c1` [3], `exr-connective-rhetoric-c2` |
| `ch05…/02-quantifier-rhetoric.md` | 5.2 | 8.2 | ch08-…/02-quantifier-rhetoric.md | `exm-rhetoric-universal` [1], `exm-rhetoric-existential` [1], `exm-rhetoric-equality`, `exm-rhetoric-induction` [4], `what-the-sentence-does-not-say`, `exr-quantifier-rhetoric-a1`, `exr-quantifier-rhetoric-b1`, `exr-quantifier-rhetoric-b2`, `exr-quantifier-rhetoric-c1`, `exr-quantifier-rhetoric-c2` |
| `ch05…/03-levels-of-abbreviation.md` | 5.3 | 8.3 | ch08-…/03-levels-of-abbreviation.md | `def-levels-of-proof` [6], `def-silent-steps` [3], `exm-sqrt2-four-levels`, `exm-uniform-four-levels`, `exr-levels-of-abbreviation-a1`, `exr-levels-of-abbreviation-b1`, `exr-levels-of-abbreviation-b2`, `exr-levels-of-abbreviation-c1`, `exr-levels-of-abbreviation-c2` |
| `ch05…/04-reading-proofs.md` | 5.4 | 8.4 | ch08-…/04-reading-proofs.md | `exm-self-explanation`, `exr-reading-proofs-a1`, `exr-reading-proofs-b1`, `exr-reading-proofs-b2`, `exr-reading-proofs-c1` |
| `ch05…/05-writing-proofs.md` | 5.5 | 8.5 | ch08-…/05-writing-proofs.md | `exm-annotate-abs`, `exm-write-from-derivation`, `exm-subset-bounded-above`, `exr-writing-proofs-a1`, `exr-writing-proofs-b1`, `exr-writing-proofs-b2`, `exr-writing-proofs-b3`, `exr-writing-proofs-c1`, `exr-writing-proofs-c2` |
| `ch05…/06-checking-proofs.md` | 5.6 | 8.6 | ch08-…/06-checking-proofs.md | `exm-not-allowed-catalogue` [110], `exm-verify-cases`, `exm-verify-converse`, `exm-verify-negation`, `exm-verify-scope`, `exr-checking-proofs-a1`, `exr-checking-proofs-b1`, `exr-checking-proofs-b2`, `exr-checking-proofs-c1`, `exr-checking-proofs-c2`, `exr-checking-proofs-c3` |
| `ch05…/07-excluded-middle.md` | 5.7 | 8.7 | ch08-…/07-excluded-middle.md | `one-extra-rule`, `prp-not-not-excluded-middle`, `what-a-proof-provides`, `thm-irrational-power-rational` [1], `prp-log2-9-irrational` [1], `exr-excluded-middle-a1`, `exr-excluded-middle-b1`, `exr-excluded-middle-b2`, `exr-excluded-middle-b3`, `exr-excluded-middle-c1`, `exr-excluded-middle-c2`, `exr-excluded-middle-r1`, `exr-excluded-middle-r2`, `exr-excluded-middle-r3`, `exr-excluded-middle-r4` |

S1 checks:
- **`exr-induction-a1`** stays in 4.2. Its formula parts go to a new 4.3 A1.
- **`exr-equality-and-uniqueness-a1` and `-b1`** stay in 5.7. b1, "the identity is unique", is an equality chain. If any part of a1 is about ∃!, that part becomes a new 5.8 A1.
- **`exr-models-a1` and `-b2`** stay in 7.1.
- **The moved R labels are still uncited outside fd1** (grep 2026-10-12): `exr-finding-derivations-r*`, `exr-normal-forms-r*`, `exr-models-r*`.

### 4.3 The 83 downstream-cited labels

All 83 keep their name and content. 31 keep their number (Chapter 1: 11; 2.1–2.5: 20). 52 are renumbered: Chapter 4 gets 19, Chapter 5 11, Chapter 6 7, Chapter 7 6 and Chapter 8 9. Links follow labels, so the only visible change is the displayed number. The heading ids cited downstream are `from-counter-models-to-non-derivability` (fd2 bp ch03, → 7.2) and `why-domains-are-non-empty` (→ 7.1, cited in fd3 prose). Both move with their sections.

| Label | Occurrences | Old § | New § | |
|---|---|---|---|---|
| `prp-and-commutes` | 3 | 1.2 | 1.2 | same number |
| `prp-and-associative` | 3 | 1.2 | 1.2 | same number |
| `def-derivable` | 2 | 1.2 | 1.2 | same number |
| `def-rules-conjunction` | 1 | 1.2 | 1.2 | same number |
| `def-rules-implication` | 3 | 1.4 | 1.4 | same number |
| `prp-distributivity` | 11 | 1.6 | 1.6 | same number |
| `exm-disjunction-first-derivations` | 4 | 1.6 | 1.6 | same number |
| `exm-disjunction-regroup` | 3 | 1.6 | 1.6 | same number |
| `exm-triangle-inequality-cases` | 3 | 1.6 | 1.6 | same number |
| `def-rules-disjunction` | 1 | 1.6 | 1.6 | same number |
| `exm-abs-product-cases` | 1 | 1.6 | 1.6 | same number |
| `prp-vacuous-implication` | 9 | 2.1 | 2.1 | same number |
| `thm-square-even-implies-even` | 7 | 2.1 | 2.1 | same number |
| `def-rules-contradiction` | 1 | 2.1 | 2.1 | same number |
| `thm-sqrt2-irrational` | 35 | 2.2 | 2.2 | same number |
| `def-rules-negation` | 16 | 2.2 | 2.2 | same number |
| `exr-negation-and-contradiction-c1` | 2 | 2.2 | 2.2 | same number |
| `exm-square-plus-one` | 1 | 2.2 | 2.2 | same number |
| `prp-contrapositive` | 17 | 2.3 | 2.3 | same number |
| `def-derived-rule` | 6 | 2.3 | 2.3 | same number |
| `exm-square-even-via-contrapositive` | 1 | 2.3 | 2.3 | same number |
| `prp-iff-two-implications` | 10 | 2.4 | 2.4 | same number |
| `thm-squares-order` | 7 | 2.4 | 2.4 | same number |
| `exm-iff-negations` | 3 | 2.4 | 2.4 | same number |
| `prp-equivalence-cycle` | 2 | 2.4 | 2.4 | same number |
| `def-rules-biconditional` | 1 | 2.4 | 2.4 | same number |
| `def-rule-raa` | 27 | 2.5 | 2.5 | same number |
| `prp-de-morgan` | 21 | 2.5 | 2.5 | same number |
| `prp-excluded-middle` | 12 | 2.5 | 2.5 | same number |
| `prp-contrapositive-converse` | 2 | 2.5 | 2.5 | same number |
| `prp-double-negation` | 1 | 2.5 | 2.5 | same number |
| `def-formula` | 2 | 3.1 | 4.1 | renumbered |
| `ax-induction` | 300 | 3.2 | 4.2 | renumbered |
| `thm-strong-induction` | 51 | 3.2 | 4.2 | renumbered |
| `thm-structural-recursion` | 10 | 3.2 | 4.3 | renumbered |
| `exm-threes-and-fives` | 9 | 3.2 | 4.2 | renumbered |
| `thm-unique-readability` | 7 | 3.2 | 4.3 | renumbered |
| `exm-sum-consecutive-products` | 6 | 3.2 | 4.2 | renumbered |
| `exm-power-inequality` | 6 | 3.2 | 4.2 | renumbered |
| `thm-structural-induction` | 5 | 3.2 | 4.3 | renumbered |
| `exr-induction-b1` | 2 | 3.2 | 4.2 | renumbered |
| `def-truth-value` | 1 | 3.3 | 4.4 | renumbered |
| `prp-standard-equivalences` | 9 | 3.4 | 4.5 | renumbered |
| `def-tautology` | 2 | 3.4 | 4.5 | renumbered |
| `def-valid-argument` | 2 | 3.4 | 4.5 | renumbered |
| `def-semantic-equivalence` | 1 | 3.4 | 4.5 | renumbered |
| `cor-refuting-row` | 3 | 3.5 | 4.7 | renumbered |
| `thm-soundness` | 1 | 3.5 | 4.7 | renumbered |
| `thm-completeness` | 5 | 3.6 | 4.8 | renumbered |
| `def-truth-function` | 2 | 3.7 | 4.4 | renumbered |
| `def-bounded-quantifier` | 8 | 4.1 | 5.1 | renumbered |
| `def-first-order-formula` | 8 | 4.2 | 5.2 | renumbered |
| `def-rule-universal-elimination` | 1 | 4.3 | 5.3 | renumbered |
| `def-rules-universal` | 16 | 4.4 | 5.4 | renumbered |
| `def-rule-existential-introduction` | 4 | 4.5 | 5.5 | renumbered |
| `def-rules-existential` | 21 | 4.6 | 5.6 | renumbered |
| `prp-exists-forall-swap` | 8 | 4.6 | 5.6 | renumbered |
| `def-rules-equality` | 11 | 4.7 | 5.7 | renumbered |
| `def-unique-existence` | 9 | 4.7 | 5.8 | renumbered |
| `prp-unique-existence-use` | 7 | 4.7 | 5.8 | renumbered |
| `prp-equality-symmetric-transitive` | 6 | 4.7 | 5.7 | renumbered |
| `prp-bounded-quantifier-rules` | 10 | 4.8 | 6.1 | renumbered |
| `exm-translate-limit` | 4 | 4.8 | 6.1 | renumbered |
| `prp-bounded-quantifier-negation` | 65 | 4.9 | 6.2 | renumbered |
| `prp-quantifier-negation` | 43 | 4.9 | 6.2 | renumbered |
| `prp-negated-implication` | 40 | 4.9 | 6.2 | renumbered |
| `prp-arbitrarily-close-equal` | 8 | 4.9 | 6.2 | renumbered |
| `exm-uniform-implies-continuous` | 2 | 4.10 | 6.4 | renumbered |
| `exm-counter-model-swap` | 7 | 4.11 | 7.2 | renumbered |
| `exr-models-c1` | 2 | 4.11 | 7.2 | renumbered |
| `exr-models-c2` | 2 | 4.11 | 7.2 | renumbered |
| `from-counter-models-to-non-derivability` | 1 | 4.11 | 7.2 | renumbered |
| `thm-first-order-soundness` | 1 | 4.12 | 7.3 | renumbered |
| `cor-counter-model` | 1 | 4.12 | 7.3 | renumbered |
| `exr-connective-rhetoric-c1` | 3 | 5.1 | 8.1 | renumbered |
| `exm-rhetoric-induction` | 4 | 5.2 | 8.2 | renumbered |
| `exm-rhetoric-universal` | 1 | 5.2 | 8.2 | renumbered |
| `exm-rhetoric-existential` | 1 | 5.2 | 8.2 | renumbered |
| `def-levels-of-proof` | 6 | 5.3 | 8.3 | renumbered |
| `def-silent-steps` | 3 | 5.3 | 8.3 | renumbered |
| `exm-not-allowed-catalogue` | 110 | 5.6 | 8.6 | renumbered |
| `thm-irrational-power-rational` | 1 | 5.7 | 8.7 | renumbered |
| `prp-log2-9-irrational` | 1 | 5.7 | 8.7 | renumbered |

Most-cited labels:
- unmoved: `def-rule-raa` and `prp-de-morgan` (2.5), `def-rules-negation` (2.2), `thm-sqrt2-irrational` (2.2), `prp-contrapositive` (2.3);
- moved mechanically: `ax-induction` and `thm-strong-induction` (3.2 → 4.2), `prp-bounded-quantifier-negation`, `prp-quantifier-negation` and `prp-negated-implication` (4.9 → 6.2), `def-rules-existential` (4.6 → 5.6), `exm-not-allowed-catalogue` (5.6 → 8.6, (N1)–(N11) frozen).

---

## 5. Renumbering map for prose and atlas pointers

### 5.1 The map, applied once and simultaneously by `pointers.py` with a split-aware extension (D0)

| Old | New | Kind |
|---|---|---|
| Chapter 1; Sections 1.1–1.6 | unchanged | — |
| Chapter 2 | Chapter 2 (where it means search or 2.6: Chapter 3) | read by hand |
| Sections 2.1–2.5 | unchanged | — |
| Section 2.6 | Section 3.1 | mechanical |
| Chapter 3 | Chapter 4 | mechanical |
| Section 3.1 | 4.1 | mechanical |
| Section 3.2 | 4.2 (numerical induction); 4.3 (structural induction, unique readability, recursion) | mechanical downstream (all 7 are numerical); by hand inside fd1 |
| Sections 3.3 / 3.4 / 3.5 / 3.6 / 3.7 | 4.4 / 4.5 / 4.7 / 4.8 / 4.9 | mechanical |
| Chapter 4 | 5 (rules, syntax, equality, ∃!), 6 (translation, laws, uniform continuity), 7 (models, counter-models, first-order soundness) | **read by hand** |
| Sections 4.1–4.6 | 5.1–5.6 | mechanical |
| Section 4.7 | 5.7 (equality) or 5.8 (∃!) | by hand |
| Sections 4.8 / 4.9 / 4.10 | 6.1 / 6.2 / 6.4 | mechanical |
| Section 4.11 | 7.1 (structures, ℂ square root, non-empty domains) or 7.2 (counter-models, the soundness statement) | by hand |
| Section 4.12 | 7.3 | mechanical |
| Chapter 5; Sections 5.1–5.7 | Chapter 8; 8.1–8.7 | mechanical |
| Ranges | endpoints mapped: "Chapters 1–5" → "1–8", "2–5" → "2–8", "3–5" → "4–8"; "Chapters 2–4", "4 and 5", "2 and 4" | the first three mechanical; the rest by hand (e.g. fd3 "Chapters 4 and 5" (quantifier rules and prose) → "Chapters 5, 6 and 8") |
| Counts | "The five chapters of *Logic and Proof*" (fd2 `07-gate-0.md:3`) → "The eight chapters" | by hand (one hit) |

### 5.2 Downstream hits (fd2, fd3, fd4, an1; `src` and `authoring`; ≈ 216 phrases)

| Old pointer | fd2 | fd3 | fd4 | an1 | Σ | New | Method |
|---|---|---|---|---|---|---|---|
| Chapter 3 | 24 | 15 | 5 | 1 | **45** | Chapter 4 | mechanical |
| Chapter 4 | 24 | 10 | 0 | 3 | **37** | 5 / 6 / 7 (label hints: mostly 5) | by hand |
| Chapter 5 | 19 | 6 | 0 | 0 | **25** | Chapter 8 | mechanical |
| Chapter 2 | 5 | 9 | 0 | 5 | 19 | 2 (no hit's labels point to search) | screened |
| Chapter 1 | 4 | 3 | 0 | 3 | 10 | unchanged | — |
| Section 3.2 | 3 | 0 | 4 | 0 | 7 | 4.2 | mechanical |
| Section 4.11 | 2 | 1 | 4 | 0 | 7 | fd2 ×2 → 7.2; fd3 and fd4 ×5 → 7.1 | by hand |
| Section 4.6 | 6 | 0 | 0 | 0 | 6 | 5.6 | mechanical |
| Chapters 1–5 / 1 to 5 | 5 | 2 | 0 | 0 | 7 | 1–8 | mechanical |
| Chapters 1 and 2 / 1–2 | 5 | 0 | 0 | 1 | 6 | unchanged | — |
| Sections 5.3 / 5.6 / 5.7 / 5.1 / 5.2 / 5.2–5.3 | 11 | 3 | 2 | 0 | 16 | 8.3 / 8.6 / 8.7 / 8.1 / 8.2 / 8.2–8.3 | mechanical |
| Sections 2.1 / 2.4 / 2.5 | 2 | 4 | 0 | 0 | 6 | unchanged | — |
| Chapters 2–5 / 3–5 | 0 | 3 | 0 | 1 | 4 | 2–8 / 4–8 | mechanical |
| Sections 3.1 / 3.3 / 3.5 | 1 | 3 | 0 | 0 | 4 | 4.1 / 4.4 / 4.7 (3.3 hits checked: two may be fd3's own) | mechanical, checked |
| Sections 4.1 / 4.2 / 4.5 / 4.3–4.6 | 3 | 1 | 0 | 0 | 4 | 5.1 / 5.2 / 5.5 / 5.3–5.6 | mechanical |
| Sections 4.9 / 4.10 | 3 | 0 | 0 | 0 | 3 | 6.2 / 6.4 (the fd2 Gate 0 map, 07:94 and 07:363) | mechanical |
| Section 4.7 | 1 | 0 | 0 | 0 | 1 | 5.7 or 5.8 | by hand |
| Chapters 2–4 / 4 and 5 / 2 and 4 / 2, 4 / 1, 2 and 5 | 1 | 7 | 0 | 0 | 8 | by content | by hand |
| Section 1.3 | 0 | 1 | 0 | 0 | 1 | unchanged | — |

**Summary:**
- about 174 of 216 phrases change: about 121 mechanically and about 53 by hand;
- the 19 "Chapter 2" hits are screened;
- about 42 are unchanged.

For comparison, B estimated about 200 and about 70, and C estimated about 75 and about 40. This layout sits near B, because old Chapter 3 becomes 4. But that shift is a single whole-chapter move, and it covers the largest group (45 hits) mechanically. About half the hits come from fd2 and fd3 "What you need" lines, which `pointers.py` already handles.

### 5.3 fd1 internal hits (`fd1/src`, current text)

| Old pointer | Hits | New | Method |
|---|---|---|---|
| Chapter 3 | 72 | 4 | mechanical |
| Chapter 4 | 37 | 5 / 6 / 7 | by hand |
| Chapter 5 | 15 | 8 | mechanical |
| Chapter 2 | 117 | 2, or 3 where it means search | screened |
| Section 2.6 | 37 | 3.1 | mechanical |
| Sections 3.1, 3.3–3.7 | 80 | 4.1, 4.4, 4.5, 4.7, 4.8, 4.9 | mechanical |
| Section 3.2 | 14 | 4.2 / 4.3 | by hand |
| Sections 4.1–4.6 | 234 | 5.1–5.6 | mechanical |
| Section 4.7 | 19 | 5.7 / 5.8 | by hand |
| Sections 4.8, 4.9, 4.10, 4.12 | 67 | 6.1, 6.2, 6.4, 7.3 | mechanical |
| Section 4.11 | 31 | 7.1 / 7.2 (includes the counter-reading convention sentence) | by hand |
| Sections 5.1–5.7 | 33 | 8.1–8.7 | mechanical |

**Summary:**
- about 639 internal pointers change, about 538 of them mechanically;
- about 101 are read by hand, plus the 117 "Chapter 2" hits screened;
- the frozen blueprints `ch0{2,3,4,5}-revision.md` are swept by the same map in the same commit, and their §2 section maps are marked superseded (§6).

### 5.4 Atlas-form tags (`F1.x §NN`: file numbers in ledgers, dependency lines, blueprints, STATUS)

| Old tag | New tag | Downstream hits | fd1 hits |
|---|---|---|---|
| F1.1 §any; F1.2 §01–05; F1.3 §01; F1.4 §01–06; F1.5 §01–07 | unchanged | 58 | ~410 |
| F1.2 §06 | F1.7 §01 | 0 | 27 |
| F1.3 §02 | F1.3 §02 (numbers) or §03 (formulas) | 9 (read) | 10 (read) |
| F1.3 §03 / §04 / §05 / §06 / §07 | F1.3 §04 / §05 / §07 / §08 / §09 | 0 | 9 / 10 / 8 / 2 / 3 |
| F1.4 §07 | F1.4 §07 or §08 | 10 (by hand) | 4 |
| F1.4 §08 / §09 / §10 | F1.8 §01 / §02 / §04 | 0 / 2 / 0 | 10 / 13 / 11 |
| F1.4 §11 | F1.6 §01 or §02 | 11 (by hand) | 23 |
| F1.4 §12 | F1.6 §03 | 3 | 18 |

So about 35 downstream and about 148 fd1 tags change. Because F1.5's file numbers are kept, all its downstream tags survive (20 hits).

**Atlas ranges are read in reading order.** `F1.1–F1.5` still means the whole volume, since F1.5 stays last. `F1.3–F1.5` (fd2 bp ch03:100) now also covers F1.4, F1.8 and F1.6, which is correct for what it names. `F1.3–F1.4` (fd3 bp ch03:205) stays right.

### 5.5 Gates after D2

- grep `Logic and Proof\*?,? *(Chapter [3-5]|Section (2\.6|3\.[1-7]|4\.([1-9]|1[0-2])|5\.[1-7]))` and confirm by hand that every hit is new-style;
- grep `F1\.(2 §06|3 §0[3-7]|4 §(0[7-9]|1[0-2]))`;
- grep `five chapters`;
- build all five volumes, then run `check_rendered.py`, `check_structure.py` and `atlas.py check`;
- re-check the fd2 Gate 0 map (07:94, 07:363, 07:365).

---

## 6. What stands and what is superseded

### 6.1 Revision blueprints

| Blueprint | Stands | Superseded or re-housed |
|---|---|---|
| `ch01-revision.md` (R2, delivered) | All of it; Ch1 is changed only by `ch01-deepen.md` | §6 (old "Section 1.x" map) is history. The 4 forward pointers are written new-style by `ch01-deepen` |
| `ch02-revision.md` (R3) | §1, §3 for 2.1–2.5, §4.1–§4.5, §7, §8 (2.1–2.5 items), §9; binding rule "section numbers do not change" (true for 2.1–2.5) | §2 section map (2.6 leaves); **§4.6 stands as content but is re-housed in `ch03-finding-derivations.md` as 3.1**; §4.0 index (search leaves; R items now new in 2.5); §5 budgets and Time line; §6 pointers (re-mapped by D2) |
| `ch03-revision.md` (R3) | Content of §4.1, §4.3–§4.7 (now 4.1, 4.4, 4.5, 4.7, 4.8, 4.9); §7; §8 items | §2 sentence "Section numbers … do not change"; **§4.2 split between 4.2 and 4.3** (the addendum assigns each item); §4.0 reading path (4.6 new, 4.9 second pass, 4.10 optional; "Where this goes" gains 7.4, 7.5); §5 budgets; `lem-weakening-cut` to 2.3, `def-truth-function` to 4.4; §6 pointers |
| `ch04-revision.md` (R4) | Content of §4.1–§4.6 (5.1–5.6), §4.8, §4.9, §4.10 (6.1, 6.2, 6.4; 4.8's "search method, extended" subsection re-housed in 6.3), §4.11 frozen plan (three pictured counter-models first; well-definedness and the `lem-free-coincidence` proof folded) carried into 7.1 and 7.2, §4.12 "kept" (7.3); §7; §8 items | §2 section map; **§4.7 split 5.7/5.8**; binding rule 1 "in its current section" for the ∃!, 4.8–4.12 labels; §4.0 (models paragraph moves to Ch7's index); §5 budgets; "4 R (4.11)" decision (Ch5's R items are new in 5.8; Ch6's are new in 6.4; `exr-models-r*` go to 7.5) |
| `ch05-revision.md` (R5) | All of §4.1–§4.7 as content (now 8.1–8.7); "every result of 5.7 stays `.optional`" (8.7); the (N1)–(N11) freeze | Chapter number (5 → 8); "What you need" (Chapters 1–6, 7.2 as a black box); §5 budgets of 8.1, 8.2, 8.4, 8.6; exercise totals; argument extraction (old 6.4 plan item) moves to 3.3 and is only recalled in 8.4 |
| `ch01.md`–`ch05.md`, `part0-logic-overview.md` (pre-revision) | Historical reference only (already superseded by the R blueprints) | Chapter list in `part0-logic-overview.md` superseded by §1 here |

### 6.2 New and changed S1 units (8)

1. `ch01-deepen.md`, a delta on the delivered text.
2. `ch02-deepen.md`, on R3 §§4.1–4.5.
3. **`ch03-finding-derivations.md`**, a full blueprint: R3 §4.6 plus the 2.7 plan split into 3.2 and 3.3.
4. `ch04-deepen.md`, on R3. It includes the 4.2/4.3 split map and the new sections 4.6 and 4.10.
5. `ch05-deepen.md`, on R4 §§4.1–4.7, with the new 5.8.
6. **`ch06-working-with-quantifiers.md`**, a full blueprint: R4 §§4.8–4.10 and the new 6.3.
7. **`ch07-models-and-theories.md`**, a full blueprint: R4 §4.11 and §4.12, the new 7.4–7.6, and 7.3 placed after 7.2.
8. `ch08-deepen.md`, on R5.

Each addendum lists, item by item, what it supersedes. PIPELINE S2 then re-opens only those items.

### 6.3 `plan.md`

| plan.md section | Status |
|---|---|
| §1 Diagnosis | **stands** |
| §2 Target TOC, "Why these", Size and time | **superseded** by §1 and §3 here. The "why not the others" list (no modal or inductive logic, no Hilbert system, no standalone translation chapter) stands |
| §3.0 Volume-wide devices | **stands**. It gains: the mirror Looking-back box, the rule-by-rule meaning table (4.7), the side-condition table (7.2), the "Minimum for fd2" line, and the non-derivability wording rule (G10) |
| §3.1 Chapter 1 | **stands** |
| §3.2 Chapter 2 | **stands** for 2.1–2.5; 2.6 → 3.1; **2.7 split** into 3.2 and 3.3 |
| §3.3 Chapter 3 | **stands as content**, renumbered (3.1 → 4.1; 3.2 → 4.2 + 4.3; 3.3 → 4.4; 3.4 → 4.5; 3.5 → 4.6; 3.6 → 4.7; 3.7 → 4.8; 3.8 → 4.9; 3.9 → 4.10). TAUT is now propositional in 4.8 (G11); the skeleton moves to 6.3 |
| §3.4 Chapter 4 | **stands as content**: 4.1–4.7 → 5.1–5.7; 4.8 → 5.8; 4.9 → 6.1; 4.10 → 6.2 (replacement now `prp-replacement`); 4.11 → 6.4. "Search extended", the propositional core, drinker and Darapti → 6.3; staged translation and minimal pairs → 6.1 |
| §3.5 Chapter 5 | **stands as content** → Chapter 7 (5.1 → 7.1, 5.2 → 7.2, 5.5 → 7.3, moved forward, 5.3 → 7.4, 5.4 → 7.5, 5.6 → 7.6) |
| §3.6 Chapter 6 | **stands as content** → Chapter 8 (6.k → 8.k); 6.4's argument extraction → 3.3 |
| §4.1 Packaging | **superseded** by §6.2 |
| §4.2 Stands and superseded | **superseded** by §6.1 |
| §4.3 Atlas | **superseded** by §7 |
| §4.4 Renumbering map | **superseded** by §5 |
| §5 Order of work and cost | **superseded** by §8. The S-stage definitions and the D0 (a)–(e) items stand |
| §6 Risks | **stands**, with §10 here added |
| §7 Decisions | 3, 4 and 6 stand (6 amended: TAUT propositional, then on the skeleton). 1, 2 and 5 are superseded by §10 |
| Critic review | **binding**; checked in §9. C3's 225 h target is overridden by the author's choice of 248 h. The trunk still drops to about 229 h to F2.1 (G8) |

---

## 7. Atlas changes (one math-atlas commit in D2; `atlas.py check` must pass)

`registry/chapters.yaml`, F1 in reading order (display numbers are generated from the order):
```yaml
F1:
  - {id: F1.1, title: "Connectives and Derivations", title_zh: 連接詞與推導, src: ab:1}
  - {id: F1.2, title: "Negation and Classical Logic", title_zh: 否定與古典邏輯, src: ab:2}
  - {id: F1.7, title: "Finding Derivations", title_zh: 推導的尋找, src: new}
  - {id: F1.3, title: "Truth, Soundness, and Completeness", title_zh: 真值、健全性與完備性, src: ab:3}
  - {id: F1.4, title: "Predicate Logic and the Quantifier Rules", title_zh: 述詞邏輯與量詞規則, src: ab:4}
  - {id: F1.8, title: "Working with Quantifiers: Translation, Laws, and Search", title_zh: 量詞的運用：翻譯、定律與搜尋, src: new}
  - {id: F1.6, title: "Models and Theories", title_zh: 模型與理論, src: new}
  - {id: F1.5, title: "From Derivations to Mathematical Prose", title_zh: 從推導到數學文字, src: [ab:5, la:ch00/01, la:ch00/02]}
```

`registry/plan-edges.yaml`:
```yaml
# ───────────── F1 邏輯與證明 ─────────────
F1.2: {s: [F1.1]}
F1.7: {s: [F1.2]}
F1.3: {s: [F1.7]}          # 4.5/4.7/4.8 pair "satisfiable" with 3.2's def-inconsistent-set; 4.6 answers 3.2's withheld verdicts
F1.4: {s: [F1.7, F1.3]}    # 5.2 builds syntax by 4.3's recursion; the searches use 3.1's moves
F1.8: {s: [F1.4, F1.3]}    # 6.3's TAUT licence is 4.8's completeness; 6.2 cites 4.5
F1.6: {s: [F1.8], see: [F1.3]}
F1.5: {s: [F1.8], b: [F1.6], why: {F1.6: "8.7 cites 7.2's statement that a counter-model rules out every first-order derivation, as a black box"}}
F2.1: {s: [F1.5]}          # unchanged
F2.2: {s: [F2.1], see: [F1.6]}   # orders and relations as theories (C3)
F2.3: {s: [F2.2, F1.6]}    # fd2 3.1 cites exr-models-c1/c2; 3.6 builds a counter-model by 7.2's procedure
F3.4: {s: [F3.10, F3.9, F3.5], see: [F3.3, F1.6]}   # 6.5 may cite thm-first-order-soundness, thm-isomorphism-invariance (see only: C3)
F4.1: {..., see: [F1.6]}   # 1.4 pays 7.1's ℂ square-root school fact (keep the existing s/b/scope)
F4.3: {s: [F2.1, F3.5], see: [F1.6]}   # groups as models (C3; not "AL1.1")
```

The current `F1.4: {s: [F1.2], see: [F1.3]}` becomes hard on F1.3, because 5.2 uses 4.3's recursion. The atlas already treated it as needed reading, so this only records the fact.

`registry/fields.yaml`:
- mathematical-logic `ch: [F1.1, F1.2, F1.7, F1.3, F1.4, F1.8, F1.6]`. The note "一階邏輯的完備性與緊緻性定理不在主幹" stays true, since 7.6 is optional.
- model-theory `hook: [F1.6, ST.4]`.
- proof-theory `hook: [F1.3, F1.7, F1.4]`.
- computability `hook: [F1.6, F2.3]` (7.6 names Church).

`registry/statements.yaml`: `thm-quant-negation` changes F1.4 → **F1.8**. The others are unchanged.

`registry/terms.yaml`: re-run `import_labels.py` / `seed_terms.py`. 11 entries change `ch:`, because their defining labels change id: `def-structure`, `def-assignment`, `def-satisfaction`, `def-first-order-entailment` (F1.4 → F1.6) and `def-partial-derivation` (F1.2 → F1.7). `computed/labels.yaml` is regenerated.

Outside the registry:
- `foundations/authoring/series.json` gains F1.6, F1.7 and F1.8.
- STATUS promise table and `tools/promises.py` are remapped by §5.4.
- The library landing page and the reading-order diagram get eight F1 rows, with 7.3, 7.6, 4.10 and 8.8 drawn as optional (commit 88e88e4 is the pattern).

---

## 8. Order of work, gates and cost

The pipeline runs autonomously. Only S9 author sampling and merges stay with the author.

| Step | What | Depends on | Runs |
|---|---|---|---|
| **G0** | Author approves this layout | — | author |
| **D0 tooling** | plan.md D0 (a)–(e), and in addition: (f) `pointers.py` **split-aware section map** (old § → new §, with a hand-read list for Chapter 2 and 4, Sections 3.2, 4.7 and 4.11, and ranges), plus an atlas-tag map (§5.4); (g) `check_fitch.py` TAUT for propositional derivations, then on skeletons (computes the skeleton; refuses ∀x∀y R ⊢ ∀y∀x R); (h) a finite-structure model checker for S3 and S6 (antichain, triangle group, side-condition counter-models) | — | 4–5 |
| **D1 STYLE** | §12.8 banks (15 in Ch1–2, 12 elsewhere, 8 in prose sections, battery sections); §12.13 devices plus the mirror Looking-back box, the meaning tables (4.7, 7.2), the "Minimum for fd2" line, and the **non-derivability wording rule**; NOTATION entries for consistent and satisfiable, counterexample set, TAUT, propositional skeleton, ≠-counting | — | 1 |
| **Pilot Ch1** | S1 `ch01-deepen` → S2 → S3 → S4–S8 (pointers new-style) | D0, D1 | ~40 |
| **D2 restructure** (parallel with pilot S3–S8; ch01 files excluded) | One branch per repo: `git mv` and the three splits at their seams on the current text; the §5 sweep (fd1 `src`, the frozen blueprints, ledgers; fd2, fd3, fd4, an1 `src` and `authoring`); ledgers split (`ch02` → `ch02` + `ch03`; `ch03` → `ch04` with the 4.2/4.3 split; `ch04` → `ch05` + `ch06` + `ch07`; `ch05` → `ch08`); `series.json`, STATUS, promises; the atlas commit (§7); all §5.5 gates; one checking referee | D0 (f) | 4–5 |
| **G1 (S9)** | Author's S9 on the deepened Ch1, together with the pending R2 S9. Density, drill volume and the Time line are fixed in the addenda before anything else is drafted. **The author also merges the D2 branches** | Pilot, D2 | author |
| **S1/S2 wave A** | `ch02-deepen`, `ch03-finding-derivations`, `ch04-deepen` | D1; can start during the pilot | ~24 |
| **Wave 1, Part I** | Ch2, Ch3 and Ch4 drafted in the final numbering, then S4–S8 each. 3.2's `def-inconsistent-set` is blueprinted, so Ch3 and Ch4 run together | G1 | ~40 + ~35 + ~70 |
| **G2 (S9)** | Packet: Part I (Ch2–4). Checks the rules → tasks → meaning rhythm, the 4.7 meaning table and the retroactive paragraph | Wave 1 | author |
| **S1/S2 wave B** | `ch05-deepen`, `ch06-working-with-quantifiers`, `ch07-models-and-theories` (the heaviest S2: `thm-isomorphism-invariance`, `prp-replacement`, `prp-taut-skeleton`, `def-inconsistent-theory`) | during Wave 1 | ~26 |
| **Wave 2, Part II** | Ch5, Ch6, Ch7. Ch7 waits for Ch6's 6.3 skeleton and Ch5's labels | G2, wave B | ~65 + ~40 + ~55 |
| **G3 (S9)** | Packet: Part II. Checks the late counter-models (risk 1) and the theories' density | Wave 2 | author |
| **Wave 3** | `ch08-deepen` → Ch8; whole-volume pass: preface, glossary, Time lines, seams (3.3 → 4 index; 4.7 ↔ 1.1/3.2; 6.4 → 7 index; 7.2 ↔ 5.1–6.4; 5.8 → 8.2; 4.8/6.3 → 8.3), fd2 Gate 0 re-check, optional downstream upgrades (fd2 1.1 cites the barber; fd3 6.5 cites `thm-isomorphism-invariance`) | G3 | ~50 + ~8 |
| **G4 (S9)** | Packet: Ch8 and the whole volume; author merges | Wave 3 | author |

**Cost:**
- about **400 agent runs** (B 390; +6 for the 4.2/4.3 split and its exercise set; +4 for D0 (f)–(h));
- **60–100M tokens**;
- about **12 pipeline days**, plus four S9 reads (G1–G4) and the D2 merge;
- words to draft: about 44,000 in new files and the split-off halves, plus about 22,000 in place;
- about 200 new A2 parts and about 80 new B and C items, all with full solutions.

---

## 9. Critic corrections: where each is honoured

| Correction | Where |
|---|---|
| C1 `cor-counter-model` with `thm-first-order-soundness` | Both in 7.3 (opt), directly after 7.2. 7.2 keeps `#from-counter-models-to-non-derivability` with its statement. 7.4 cites the heading. The Ch7 reading note says so |
| C1 R items | `exr-models-r1–r4` → 7.5; new R labels in 2.5, 5.8 and 6.4; old 2.6 R → 3.3; old 3.7 R → 4.8 |
| C1 4.7 labels by name | ∃! labels and `exr-equality-and-uniqueness-{b2,b3,c1,c2}` → 5.8; `-a1`, `-b1` and `rule-phrase-lean-table` stay in 5.7, the last rule section |
| C1 no `def-satisfiable-set` | Existing `def-satisfiable` only (4.5) |
| C1 internal sweep | §5.3 (~639 internal pointers, swept before drafting) |
| C2 replacement | `prp-replacement` in 6.2, syntactic, by induction on the context; no completeness |
| C2 TAUT | Propositional in 4.8; skeleton plus uniform-substitution licence in 6.3; `check_fitch.py` computes the skeleton |
| C2 Challenge | 4.8: closed tree ⇒ Fitch derivation |
| C3 group example | The opener is the partial-order antichain; 7.4 has the triangle group (table given, script-checked) |
| C3 isomorphism | Second-pass half of 7.5; edges F2.2 and F4.3 `see`; fd3 (F3.4) `see` only |
| C3 trunk | Author override to ~248 h (here ~250). Must-read to F2.1 is ~229 h (G8). "Only/except" and minimal pairs are drills (5.8, 6.1) |
| small 1 | 4.10 defines ⊢ and ⊨ for infinite Γ |
| small 2 | 7.4 `def-inconsistent-theory` |
| small 3 | 8.7 points to 8.8 |
| small 4, 5 | 7.2 |
| small 6 | 5.8 subsection plus the "we define" phrase; 8.2 row |
| small 7 | Batteries are fd1's own; "clause-by-clause"; no "Interlude"; puzzles in integer dress |
| small 8 | `lpl.txt` is not an input to any stage |

---

## 10. Risks and decisions for S9

**Risks:**
1. **First-order counter-models arrive late** (7.2 at about 180 h).
   - Mitigation: the counter-reading convention is kept, worded for upgrade (G10).
   - The 7.2 side-condition table and retroactive paragraph certify the earlier readings one by one.
   - G3 tests this.
2. **Sweep size.** About 174 downstream and about 639 internal pointers change.
   - Mitigation: one simultaneous split-aware map, run before drafting.
   - About 53 downstream and about 101 internal hits are read by hand, and the §5.5 gates run after the sweep.
3. **A short Chapter 3** (16 h), next to the 45–46 h Chapters 4 and 5. Each of its sections has its own new idea, and its battery makes it a drill chapter as well.
4. **The mirror may read as repetition.** Each twin names its twin once and spends its words on what is new for quantifiers.
5. **Eight chapters in a first volume.** The preface groups them into three Parts.

**Decisions made on the author's behalf:**
1. Layout B frame, with 8 chapters in 3 Parts. New ids F1.7 and F1.8; F1.6 is Models and Theories; F1.2 is retitled.
2. Chapter 1 unchanged as Chapter 1.
3. Prose dictionaries stay in Chapter 8 (G3, for constraint 2).
4. Old 3.2 is split into 4.2 (numbers) and 4.3 (formulas).
5. Propositional soundness and completeness proved on the core. First-order soundness optional, directly after its statement.
6. TAUT propositional in 4.8, extended to skeletons in 6.3.
7. Banks: 15 in Chapters 1–2, 12 elsewhere, 8 in prose sections. Batteries replace banks in 3.3 and 6.3.
8. Core about 250 h, full about 441 h. Must-read to F2.1 about 229 h.
9. D2 runs once, before Wave 1, and is merged at G1.
