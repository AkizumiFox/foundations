# fd1 *Logic and Proof*: gap matrix against twelve logic texts

Built from the twelve book reports. I checked fd1's coverage claims against the source with keyword sweeps over `fd1/src` and `fd1/authoring/blueprints`. In `src` there are no hits for: tableau, truth tree, Russell, Barber, Skolem, definab-, isomorph-, metalanguage, tonk, Leibniz, drinker, Löwenheim, contingent, Hasse, glossary. The word "consistent" appears only in the sense "replaced consistently". "At least two" and "exactly two" occur only in passing (3.1, 3.3, 3.7, 1.1, 4.9, 4.11). The ch04 revision blueprint already plans "small world" and "tiny worlds" figures (4.1, 4.4, 4.6).

## Legend

**Books** (columns):
- LB: Bergmann–Moor–Nelson, *The Logic Book*
- Hu: Hurley, *Concise Introduction*
- LPL: Barker-Plummer–Barwise–Etchemendy, *Language, Proof and Logic*
- Sm: Smith, *Introduction to Formal Logic*
- Si: Sider, *Logic for Philosophy*
- vD: van Dalen, *Logic and Structure*
- En: Enderton, *Mathematical Introduction*
- Ha: Halmos, *Naive Set Theory*
- Co: Cohnitz–Estrada-González, *Philosophy of Logic*
- Le: Lemmon, *Beginning Logic*
- Hk: Hacking, *Probability and Inductive Logic*
- Ho: Hodges, *Logic*

**Cell codes:**
- **F**: full or central treatment
- **P**: partial, brief or remark-level
- **X**: exercises only
- blank: absent

**fd1 status:**
- **absent**
- **thin**
- **comp.** (comparable)
- **deeper**

**Recommendations:**
- **ADD**: new material
- **DEEPEN**: extend what exists
- **KEEP**: no change, or one small item
- **LEAVE→**: belongs to another volume
- **OPT**: optional, second-reading or Challenge track

**fd1 section → file** (all under `fd1/src/`):

| § | file |
|---|---|
| 1.1 | `ch01-connectives-and-derivations/01-statements-and-connectives.md` |
| 1.2 | `ch01-…/02-derivations.md` |
| 1.3 | `ch01-…/04-using-an-implication.md` |
| 1.4 | `ch01-…/05-proving-an-implication.md` |
| 1.5 | `ch01-…/06-disjunction-introduction.md` |
| 1.6 | `ch01-…/07-disjunction-and-cases.md` |
| 2.1–2.6 | `ch02-negation-and-classical-logic/0{1..6}-*.md` (2.1 contradiction and vacuous truth; 2.2 negation; 2.3 derived rules; 2.4 biconditional and definitions; 2.5 reductio and classical rules; 2.6 finding derivations) |
| 3.1–3.7 | `ch03-semantics-soundness-completeness/0{1..7}-*.md` (3.1 parse trees; 3.2 induction; 3.3 valuations; 3.4 entailment and equivalence; 3.5 soundness; 3.6 completeness; 3.7 normal forms) |
| 4.1–4.12 | `ch04-predicate-logic/{01..12}-*.md` (4.1 predicates and quantifiers; 4.2 terms and substitution; 4.3 ∀E; 4.4 ∀I; 4.5 ∃I; 4.6 ∃E; 4.7 equality and uniqueness; 4.8 translation; 4.9 quantifier laws; 4.10 uniform continuity; 4.11 models; 4.12 first-order soundness) |
| 5.1–5.7 | `ch05-from-derivations-to-prose/0{1..7}-*.md` (5.1 connective rhetoric; 5.2 quantifier rhetoric; 5.3 levels of abbreviation; 5.4 reading; 5.5 writing; 5.6 checking; 5.7 excluded middle) |

---

## (1) Arguments, informal logic, translation

| # | Topic (synonyms merged) | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | Validity vs truth; the truth-value combinations a valid form allows; "sound argument" | F | F | P | F | P | | | | P | P | F | F | comp. (1.1 "Good form, false sentences") | KEEP + A-drill: all eight premise/conclusion/validity cases, "give an example or explain why impossible", plus construct-your-own items. One sentence in 1.1 or 3.5: other books call a valid argument with true premises "sound", which is not Theorem 3.5. |
| 1.2 | Counterexample method; stock breakers; decide-then-justify | P | F | F | F | X | X | X | | | P | | F | comp. as a method (1.1 "Try to break it"); **thin** in the exercises, which nearly always say "derive" | DEEPEN: a "stock breakers" sub-move in 1.1 (n=2, 0, −1, ∅; choose the false conclusion first). Mixed-verdict items ("derive it or break it"; from 3.5 on "…or give a refuting row"; from 4.11 on "…or a counter-model"), with invalid look-alikes seeded in every rule section 1.2–2.6 and 4.3–4.10. |
| 1.3 | One argument, many forms; a bad form refutes a step, not the conclusion; invalid forms have valid instances | | F | | F | P | | | | F | | P | P | thin (1.1 Argument B touches it) | ADD: second reading in 1.1 after Argument B; recall it at 3.4 `exm-affirming-the-consequent`; payoff in 4.1 (a valid first-order argument whose propositional form breaks). |
| 1.4 | Counterexample set (premises + ¬conclusion) as the one unifying search | F | P | P | P | | P | | | | | | F | thin (the search is scattered across 1.1, 3.5, 4.11) | ADD: name it in 1.1. Thread it through 2.5 (RAA shows the set inconsistent), 3.4, 3.5 (refuting row) and 4.11 (counter-model). |
| 1.5 | English connective idioms: unless, provided, whenever, neither/nor vs not both, but, exactly one of, at least two of three; collective "and"; restrictive clauses; non-conditional "if"; inseparable modifiers | F | F | P | P | | P | X | | | P | | F | thin (1.1 has only if / necessary / sufficient, plus a C item on unless) | ADD to 1.1: a glossary table (phrase → paraphrase → formula), a "Not:" catalogue of mistranslations in mathematical dress ("a and b are coprime", "A, B, C collinear", "approximate root"), and a 15–20 item symbolization drill. |
| 1.6 | Staged paraphrase translation (mixed English/symbol stage); reading the formula back; one fixed key across a set | F | P | F | F | | | F | | | P | | F | comp. at 4.8 (outside-in); thin at 1.1 | DEEPEN: explicit mixed stage in 1.1 and 4.1; one fixed mathematical key (ℕ with Prime, Even, <, ∣) across a graded set in 4.8; reading back as a named check. |
| 1.7 | Truth-functionality; non-truth-functional operators (because, it is known that, subjunctive if) | F | P | P | F | | | | | P | | | F | absent | ADD: short subsection in 3.3 (or a fold in 1.1) with partial truth tables as an A item. It explains why the mathematical "if" is material. |
| 1.8 | Weak vs strong readings; conversational implicature ("some" allows "all"; inclusive or; a definition's "if" means iff) | | P | F | | | | | | | | | F | thin | ADD: remark boxes in 1.1 and 4.1, plus one "implied or merely suggested?" A item each. |
| 1.9 | Enthymemes; supplying the missing premise | | F | | P | | | | | | | | P | thin (5.3 silent steps) | ADD: "supply the missing premise" items in each Ch1–2 rule section; "name the unstated fact" in 5.3–5.4. |
| 1.10 | Argument / proof dependency diagrams | | F | | | | | | | | | | | thin | OPT: one lemma-dependency diagram of an analysis proof in 5.4, plus an exercise. |
| 1.11 | Criticizing definitions (too broad, too narrow, circular, needlessly negative) | | F | | | | | | P | | | | | thin (2.4) | ADD: B exercise in 2.4 (a candidate definition of "bounded" or "increasing": find a wrong inclusion or exclusion). |
| 1.12 | Informal fallacies as proof errors (circular proof, equivocation, amphiboly, composition and division, false dichotomy / incomplete cases, affirming a disjunct, hasty generalization) | P | F | | P | | | | | | P | | P | comp. (5.6 N1–N11; n²+n+41 in 1.1) | DEEPEN: add any missing entries to the 5.6 catalogue under mathematical names; add "affirming a disjunct" to the 1.6 common errors. |
| 1.13 | Two fallacies that cancel; circular chaining (valid overall, wrong proof) | | | | F | | | | | | | | | thin | ADD: worked example after the Argument B diagnosis in 1.4, or in 5.6. |
| 1.14 | Two ways to attack an argument (false premise vs broken step); for models, translation error vs derivation error | P | P | | P | | | | | | | F | | thin (pieces in 1.1 and in 5.6's two columns) | ADD: named move in 1.1; call back in 5.6; Ch4 version in 4.8. |
| 1.15 | Deduction vs induction; Peirce's "every case vs most cases"; monotonicity contrast; abduction = affirming the consequent; Popper's refutation by MT | P | F | | P | | | | | P | | F | P | thin (1.1 second reading on n²+n+41) | DEEPEN the 1.1 second reading (Peirce, abduction); add a Popper remark in 2.3 (MT); one sentence in 3.4 "More premises" on monotonicity. LEAVE→ inductive logic proper. |

## (2) Propositional semantics

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.1 | Valuations, truth tables, coincidence lemma | F | F | F | F | F | F | F | | F | F | | F | comp./deeper (3.3) | KEEP. Optional B: connectives as arithmetic on {0,1}; ⊨φ→ψ iff v(φ)≤v(ψ) (vD). |
| 2.2 | Shortened / indirect tables with branching and backtracking; split heuristic ("fewest ways"; "split on the deciding atom"); "a clash from a guess refutes nothing"; tactics (conclusion first, prune rows); failed search with every choice forced = proof | F | F | | F | F | | F | | | P | | P | thin (3.3 "working backwards from F"; forced examples only) | DEEPEN 3.3–3.4: named procedure "Hunt for a refuting row" with a worked example that must branch, a warning box, a flowchart, a B set including set-satisfiability tests, and the remark linking it to 2.6 "A search that fails". |
| 2.3 | Backward-computation and partial-valuation drills (sub-skill first) | | F | | | | | | | | | | | absent | ADD: A2 drill in 3.3 before the search procedure. |
| 2.4 | Truth trees / tableaux (closed and open branches, reading a row off an open branch, tree soundness and completeness) | F | P | | F | | | | | | | | F | absent | OPT: a section in Ch3 (after 3.4) presented as a systematic refuting-row search, not a second proof system. Readers derive the branch rules from the tables (Ho). A C sequence in 3.6 for tree completeness gives a second, constructive completeness proof. |
| 2.5 | Property catalogue: tautology / contradiction / **contingent**; pair relations: equivalent, **contradictory**, **contrary / subcontrary**, consistent | F | F | P | P | | | | | | F | | | comp. minus contingent, contradictory, contrary (3.4) | DEEPEN 3.4: add the three words and a three-way classification drill; contradictory = "what negating a definition must produce" (tie to 4.9); contrary vs contradictory as a C item. |
| 2.6 | Reductions to (un)satisfiability (Γ⊨ψ iff Γ,¬ψ unsatisfiable; the corresponding conditional); table of what one row or model shows vs what needs every one | F | P | F | P | | P | | | | P | | F | thin | ADD: a proposition with B "prove it" items in 3.4, and the one-row-vs-all-rows table; mirror table in 4.11 for models. |
| 2.7 | Consistency of a set, semantic and syntactic (Γ⊬⊥ and its equivalent forms); "consistent or not?" tasks; independence of a formula or premise | F | F | F | P | P | F | X | | | P | | F | thin (only "satisfiable" in 3.4; the word "consistent" is absent) | ADD: semantic version in 3.4; syntactic version and "Γ∪{¬φ} inconsistent ⇒ Γ⊢φ" in 3.5–3.6; "completeness = consistent iff satisfiable" remark in 3.6; paired "valuation or derivation of ⊥" items. |
| 2.8 | Substitution for atoms, replacement of equivalents, duality; every contingency has tautologous and inconsistent instances | P | | P | P | | F | X | P | | F | | F | comp. (3.4 lem-substitution, lem-replacement; 3.7) | KEEP + C items: duality (if missing); contingent-instances (Le). |
| 2.9 | Calculation: chains of cited equivalences; "simplify this formula" | | P | F | | | F | | P | | P | | | thin (2.4 provable-equivalence chains only) | ADD: worked subsection and "simplify" drills in 3.4 (the same skill fd2 uses for set algebra). |
| 2.10 | DNF/CNF; a full DNF's disjuncts form a partition | P | | F | P | P | F | F | | | F | P | | comp. (3.7) | KEEP + one sentence on the partition (Hk). |
| 2.11 | Expressive completeness; Sheffer and NOR; inadequacy by an invariant; NAND/NOR the only single adequate connectives; counting 2^(2^n); the proof cost of defined connectives | F | | F | F | F | F | F | | | F | | F | comp./deeper (3.7) | KEEP; optional C items: the count and the table of 16 binary connectives (En); proving ¬(¬p∨¬q) from p, q vs ∧I, i.e. why fd1 keeps every connective primitive (LPL). |
| 2.12 | Positive and negative occurrences; monotonicity theorem | | | | | | F | | | | | | | absent | ADD to 3.4 or 4.9, plus a 5.2 dictionary row ("a stronger hypothesis gives a weaker theorem"; "it suffices to prove something stronger"). |
| 2.13 | Propositional interpolation; eliminating an atom | | | | | | X | X | | | | | F | absent | OPT: C pair in 3.7. |
| 2.14 | Cost of tables (2^n, P vs NP); counting satisfying rows / inclusion–exclusion | P | | P | P | | | P | | | | F | P | absent | ADD: Looking-ahead box in 3.6. OPT: row-counting C item in 3.4 or 3.7 (φ⊨ψ ⇒ #φ≤#ψ). |
| 2.15 | Logic puzzles (truth-tellers, suspects) | | X | | | | | X | | | | | | absent | ADD: 2 original B items in 3.3–3.4. |
| 2.16 | Game (defender/challenger) reading of the truth clauses | | | F | | | | | | | | | | thin (informal prenex game in 4.1) | ADD in 3.3 (¬ swaps roles); reuse in 4.11; link to strategies and witness functions in 4.10. |
| 2.17 | Rows as regions (entailment = containment) picture | | P | P | | | | | P | | | F | | absent | ADD: figure in 3.4, with a forward pointer to fd2's ∪/∩/complement. |

## (3) Propositional proof systems and metatheory

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.1 | Natural deduction rule by rule, informal first, bad rule refuted by a row | F | F | F | P | F | F | | | P | F | | | deeper (Ch1–2) | KEEP. |
| 3.2 | Alternative formats: dependency column / Lemmon sequents / Gentzen trees | P | | | P | F | F | | | F | F | | | thin (context Γ_n appears only inside the 3.5 proof) | ADD: C exercise in 1.4 or 1.6 (annotate each line with its open assumptions and read off its sequent) as the bridge to 3.5. OPT: box in 3.5 showing one derivation as a tree. |
| 3.3 | Derived rules and a library of standard sequents (MT, HS, DS, **CD**, **MPT**, the four modi) | F | F | P | | | | | | | F | | | comp. (2.3) | DEEPEN: constructive dilemma and MPT as B items in 2.3; a page of "standard sequents grouped by use" at the end of 2.6 and 4.9; schematic-generality remark (LPL). |
| 3.4 | Replacement rule (swap a provably equivalent part inside a line); whole-line vs inside-a-line | F | F | | | | F | | | | P | | | thin (semantic lem-replacement only) | ADD: a derived replacement rule in 2.4 or 2.5, justified by structural induction in 3.4; use it in 4.9 to push ¬ through quantifier prefixes. Whole-line warning in 1.3 common errors. |
| 3.5 | Syntactic / semantic parallel table (⊢ vs ⊨, theorem vs tautology, provably equivalent vs equivalent, inconsistent vs unsatisfiable) | F | | P | P | | P | | | | | | | thin (3.4 "Two questions, side by side" covers sequents only) | ADD: the full two-column table in 3.4, previewing soundness and completeness as "the columns agree". |
| 3.6 | Task types: theorem, equivalence (two derivations), **inconsistency (derive ⊥)**, TFAE by a cycle | F | P | F | | | | | | | P | | | comp. minus inconsistency and TFAE | ADD: a "derive ⊥ from these premises" family with a worked clash-partner case in 2.6; a TFAE-cycle example and exercise in 2.4 or 5.5. |
| 3.7 | Paradoxes of material implication; "name the rule you reject"; the cost of → (Read); mathematical "if" sits under ∀ | P | P | P | F | P | P | P | | F | F | | P | thin (2.1 vacuous truth; 1.1 promise reading) | ADD: subsection at the end of 2.1 (or after the → table in 3.3), with a C item (derive Q⊢P→Q without ∨I). |
| 3.8 | Tonk and harmony; why derived rules are conservative | | | | | | | | | F | | | | absent | ADD: C item or second reading in 3.3 "Reading a table off the rules"; pointers in 3.5 and 2.3. |
| 3.9 | Carroll's tortoise (a rule is not a premise) | | | | | | | | | F | | | | absent | ADD: second-reading box in 1.3. |
| 3.10 | Structural properties of ⊢ and ⊨ (reflexivity, weakening, cut, order and repetition) | | | | | P | P | | | F | | | F | thin (lem-weakening-cut in 3.6) | ADD: subsection in 3.4 (⊨ proofs, cut by case split) and 3.6 (⊢); name cut as the reason 2.3's derived rules are legitimate. |
| 3.11 | Rule independence and redundancy; restricted rule sets; invariant puzzles | X | | | | X | X | | | | X | | | comp. (2.5 B3; thm-raa-independent in 3.5) | ADD C items: "remove ∨I or ¬I: which completeness lemma breaks?" in 3.6; an MIU-style invariant puzzle in 3.5; the restricted-rule paradoxes in 2.5. |
| 3.12 | Induction for metatheory: structural and strong induction; four-question checklist; sets generated from a base (top-down = bottom-up); recursion non-example without freeness; inventor's paradox; false-thesis items; Polish notation | F | | F | P | F | F | F | P | | P | | P | deeper on core (3.1–3.2) | DEEPEN 3.2: checklist box (reuse it in 3.5 and 4.12); "sets built from a base" subsection; a ℤ recursion non-example after thm-structural-recursion; inventor's-paradox and false-thesis C items; C items on Polish and one-sided-parenthesis notations; formula height as a recursion B item. |
| 3.13 | Object language vs metalanguage; use/mention; rule-circularity of soundness; Kreisel's squeezing argument | F | | P | F | F | | P | | F | | | | absent | ADD: paragraph in 3.1; a two-level box at the start of 3.5; Kreisel as a second reading in 3.6 "Two roads" and again in 4.12. |
| 3.14 | Propositional soundness and its variants (change a table; a rule with a box; "finish the proof") | F | | F | F | F | F | F | | | F | | F | comp./deeper (3.5) | KEEP + C items: changed-semantics soundness; boxed-rule case; leave two rule cases to the reader. |
| 3.15 | Completeness, Kalmár style | | | | | | | | | | F | | | comp. (3.6) | KEEP + a fully expanded 2-atom glued derivation as a figure (Le). |
| 3.16 | Completeness via maximal consistent sets (Lindenbaum, truth lemma); compactness and its applications (graph colouring) | F | | F | F | F | F | F | | | | | F | thin (remark on compactness) | OPT: section 3.6b, with the trade-off named (constructive vs maximal object); compactness as a two-line corollary; a de Bruijn–Erdős C item. |
| 3.17 | Hilbert systems; deduction theorem | | P | | P | F | | F | | | | | | absent | OPT: an "other proof systems" box in 3.6 or 5.7; a deduction-theorem C item for a modus-ponens-only system. |
| 3.18 | TAUT rule: one-line tautological steps licensed by completeness | | | F | | | | P | | | | | | absent | ADD after 3.6, restricted to steps an informal proof would leave unsaid; use it to shorten Ch4 derivations (4.8, 4.10); tie to 5.3 silent steps. |
| 3.19 | Normalisation / detour rule ("never introduce then immediately eliminate"); subformula property | | | | | | F | | | | | | | absent | ADD: named move in 2.6 and 4.8, stated without proof. |
| 3.20 | Independence by a nonstandard semantics as a named technique | | | | | F | | | | F | | | | thin (one use, thm-raa-independent) | DEEPEN 3.5: name it; C items (⊥ read as a letter shows ⊥E is needed; Kleene and LP tables, see 9.3). |

## (4) First-order language, translation, semantics and models

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.1 | Syntax: free and bound variables, capture, simultaneous substitution | F | | F | F | F | F | F | P | P | F | | P | deeper (4.2) | KEEP + an A2 "repair this almost-sentence" drill (LPL); a simultaneous-vs-sequential swap item (vD). |
| 4.2 | Translation traps: ∀→ / ∃∧ with both wrong versions refuted; ∨ in the restrictor; only / none but; any vs every; donkey and anaphora; not-every vs every-not; ambiguity needing two readings | F | F | F | F | P | P | F | | | F | P | F | comp./thin (4.1, 4.8, 5.2) | DEEPEN: traps gallery in 4.8; minimal-pair families in 4.1 and 4.9; a ~20-item mathematical drill bank in 4.1 and 4.8; check each trap against small structures. |
| 4.3 | A/E/I/O, square of opposition (diagonal contradictories), existential import, Darapti, Venn pictures | F | F | P | F | | | | | P | F | | | absent (vacuous truth itself is covered in 2.1, 4.4, 4.11) | ADD: A/E/I/O square figure in 4.9; existential import line in 4.1; Venn sketch as a monadic counter-model tool in 4.11; a Darapti C item. No syllogistic unit. |
| 4.4 | Finite-domain expansion (∀ as ∧, ∃ as ∨); quantifier negation as De Morgan; finite-universe counter-model method; monadic bound | F | F | | | | P | | | | F | | P | thin (4.5 remark; counter-models found by insight in 4.11) | ADD: reading in 4.1; Lemmon twin figure (∃E beside ∨E over {m,n}) in 4.6 and ∀E = ∧E in 4.3; a "Small domains, by expansion" subsection in 4.11 (fails at n=1, succeeds at n=2), with the infinite-domain limit stated. |
| 4.5 | Structures, assignments, satisfaction; evaluation in fixed finite structures; pictures (arrow and Hasse diagrams) | F | | F | F | F | F | F | | F | | | F | comp. (4.11; small-world figures planned in the ch04 revision) | DEEPEN: arrow diagrams for every finite counter-model; drills evaluating sentences in two given structures; richer examples (P(ℕ) with ⊆, ℤ/n). |
| 4.6 | Direct semantic proofs that Γ⊨φ ("let M be any structure") | | | P | | F | F | F | | | | | | thin | ADD: subsection in 4.11, with one fully expanded proof, then condensed ones, plus B items. |
| 4.7 | Counter-model procedure (start from the witness of failure; minimal domain; existential demands first); infinite-only models | F | F | P | F | F | F | | | | P | | F | comp. (4.11, C1 and C2 on infinite models) | DEEPEN: named procedure in 4.11, the semantic twin of "name the witness early". |
| 4.8 | Hierarchy: tautology ⊂ FO-valid ⊂ true in ℕ/ℝ; propositional skeleton | P | | F | P | | | | | P | | | P | thin (4.11 "Why a row is not enough") | ADD: subsection in 4.11 or 4.9 with an Euler diagram and a three-way classification drill. |
| 4.9 | **Theories and their models**: axioms as sentences (equivalence, orders, groups, fields); models and non-models; independence and consistency shown by a model | | P | F | | P | F | F | P | | | | | absent | ADD: new section 4.11b "Theories and their models" (or a close to Ch4). The single biggest structural gap, and it feeds fd2, fd3 and fd4. |
| 4.10 | Definability in a structure; an open formula denotes a set; ∃ as projection | | | | | P | F | F | | | | | | absent | ADD: subsection in 4.11 (≥0 by squares in ℝ; primes and < in ℕ). |
| 4.11 | Isomorphism invariance; automorphisms prove non-definability | | | | | | P | F | | P | | | | absent | ADD: C proposition with a structural-induction sketch in 4.11 (x↦x+1 on (ℤ,<)). |
| 4.12 | "Find a sentence true in A and false in B"; "describe every model of σ" | | | P | | | F | F | | | | | | absent | ADD: B items in 4.11. |
| 4.13 | Properties of relations as derivations and models (asymmetric ⇒ irreflexive; irreflexive + transitive ⇒ asymmetric; the "symmetric + transitive ⇒ reflexive" trap; independence of R, S, T; empty relation; siblings) | P | | P | F | | P | X | F | | F | | F | absent | ADD: B/C derivation items in 4.4–4.9 and model items in 4.11. LEAVE→ fd2 for relation theory. |
| 4.14 | Prenex normal form; quantifier alternation as complexity | | | F | F | | F | F | | | | | | thin (4.9 C1) | DEEPEN 4.9: one worked conversion and an alternation paragraph (∀∃∀ for limits). |
| 4.15 | Quantifier laws beside their propositional twins; drinker sentence; non-laws with counter-models | F | F | F | F | P | F | P | | | F | | P | comp./deeper (4.9) | KEEP + twin boxes; drinker C item (derived and checked semantically). |
| 4.16 | Empty domains; free logic; partial terms (1/x, lim) | P | P | | F | F | | | | F | | | P | comp. (4.11 "Why domains are non-empty"; M3 totality) | KEEP + a remark in 4.2 or 4.10 that partial terms are guarded by hypotheses rather than handled by free logic. |
| 4.17 | Generalized / analysis quantifiers ("infinitely many", "all but finitely many"); many-sorted letters | | | P | | P | P | P | | | | | P | comp. (bounded quantifiers in 4.1) | ADD in 4.8: ∀N∃n≥N and ∃N∀n≥N; sorted letters as bounded quantifiers. |
| 4.18 | Second-order statements: induction and LUB quantify over sets | | | P | | P | F | F | | F | | | | absent | ADD: box in 4.8 explaining why fd2 and fd3 build ℕ and ℝ in set theory. |
| 4.19 | Language of set theory as a worked signature (extensionality, pairing translated) | | | P | | | | P | F | | | | | thin | ADD: example in 4.2 or 4.8. |

## (5) First-order proof and metatheory

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5.1 | Quantifier rules with side conditions, each motivated by a faulty derivation and a counter-model | F | F | F | P | P | F | P | | P | F | | P | deeper (4.3–4.6, 4.10) | KEEP; audit for one named bad derivation plus counter-reading per clause (planned small worlds); a single-step "is this application correct, and why?" drill. |
| 5.2 | Quantifier strategy: contradiction trapped in an ∃E box; "propositional core"; elimination before introduction | F | P | F | F | P | P | P | | | F | | P | comp. (4.6, 4.8 named moves) | ADD: trapped-contradiction worked case in 4.6; "propositional core" named move in 4.8. |
| 5.3 | Russell / Barber theorem ¬∃y∀x(R(x,y)↔¬R(x,x)) as pure logic | | | F | | | X | | F | P | | | | absent | ADD: lemma ¬(P↔¬P) in 2.4 or 2.5; derivation in 4.6 (barber, then sets); Barber hidden-premise check in 5.6; pointer to fd2. |
| 5.4 | Defining ∃ as ¬∀¬ and deriving its rules | | | | | | F | | | | X | | | absent | ADD: C item in 4.9. |
| 5.5 | First-order soundness | F | | F | F | | F | F | | | P | | F | comp. (4.12) | KEEP. |
| 5.6 | First-order completeness: statement and sketch (Henkin or systematic search; old/new names mirror freshness) | F | | F | F | P | F | F | | P | P | | P | thin (remark only) | OPT: 4.13 with a statement, its consequence, and a sketch; mandatory at least as a stated theorem in 4.12. |
| 5.7 | Compactness, Löwenheim–Skolem, "finite" is not first-order, non-standard models | | | F | P | P | F | F | | F | | | | absent | OPT: closing section "What first-order logic can and cannot say" (stated, not proved; one compactness C exercise on finiteness). |
| 5.8 | Decidability (truth tables yes; FO no, Church; monadic yes); Gödel incompleteness named | F | P | P | P | P | F | F | | P | P | | F | thin (4.12 remark) | DEEPEN: fold into 5.7's section; a 4.11 remark that a failed counter-model search proves nothing. LEAVE→ later volume for proofs. |
| 5.9 | Skolem / witness functions (δ(ε) vs δ(ε,x)); game strategies | | | P | | | F | F | | | | | | absent | ADD: subsection in 4.10; one sentence that choosing all witnesses needs AC (fd2). |
| 5.10 | First-order trees / Herbrand instantiation | F | | | F | | | | | | | | F | absent | LEAVE (only inside the optional 4.13 sketch). |

## (6) Identity, functions, definite descriptions

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6.1 | =I and =E; Leibniz's Law; identity as the smallest equivalence relation; opaque contexts ("obvious that") | F | F | F | F | F | F | F | P | P | F | | F | comp. (4.7; Leibniz not named) | DEEPEN 4.7: name Leibniz's Law; an extensionality remark and an opacity warning box; the predication-vs-identity "is" test as an A item. |
| 6.2 | Counting with equality: at least / at most / exactly n; only, except, other than, superlatives; distinct variables need not name distinct objects | F | F | F | F | F | P | | | P | F | | F | thin (4.7: ∃! and "at most one"; passing mentions only) | ADD: subsection "Counting with equality" in 4.7; "exactly two" proved as at least plus at most; an N-entry in the 5.6 catalogue; a C derivation (exactly one F, exactly one G, none both ⇒ exactly two). |
| 6.3 | Definite descriptions: "the x with φ" licensed by ∃!; Russell's unpacking; scope of "lim aₙ ≠ 0" | F | F | P | F | F | P | | | | F | | F | thin (4.7 uses "the maximum") | ADD: subsection "Naming the unique witness" in 4.7. Every "the" in analysis rests on it. |
| 6.4 | Function symbol vs functional relation (graph plus ∀∃!); totality | P | | F | F | F | P | | | | P | | | comp./thin (4.2; 4.11 M3) | ADD: worked example and exercise in 4.7 (fd2's definition of a function). |
| 6.5 | Extensionality split: logical half (=E) vs axiom half (counter-model); uniqueness of ∅ and {a,b} from extensionality | | | | | | | | F | | | | | absent | ADD: exercise pair in 4.7 and 4.11. |
| 6.6 | Composites of injections / surjections derived formally | | | | | | X | | | | | | | absent | ADD: B item in 4.7 or 4.8. |

## (7) Proof strategy and mathematical writing

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7.1 | Goal-directed search; named moves; "find the goal in the premises"; atom bookkeeping; derive before opening a box; clash partner already on a line; **test the subgoal semantically** | F | F | F | P | P | P | P | | P | P | | | deeper/comp. (2.6, 4.8) | ADD these four moves; a "test the subgoal" box in 3.5 revisiting 2.6's failed search, and again in 4.11. |
| 7.2 | When RAA is needed (non-effective premises → effective conclusion) | | | | | | F | | | | | | | absent | ADD: heuristic in 2.5 and 2.6. |
| 7.3 | Informal proof first, then the mirroring derivation; translate an argument, then derive | F | F | F | | | | | | | F | | | comp. ("How this looks in a mathematical proof") | ADD: two-column exercise type in 2.6, 4.8, 4.10; a closing translate-and-derive item per rule section. |
| 7.4 | Critiquing purported proofs inside rule sections; "Not allowed" blocks; "improper but valid" | F | F | F | P | | P | | | | F | P | | comp. (C find-the-error; 5.6) | DEEPEN: critique items in 4.4, 4.6, 4.10; a "Not allowed" block per rule card; the improper-but-valid category in 5.6; an "and so on" iteration error in 5.6 (Ha). |
| 7.5 | Double inclusion and element chasing | | | P | | | | | F | | | | | thin | ADD: dictionary row and annotated example in 5.1 or 5.2. |
| 7.6 | Unfolding defined notation to primitives and back | | | | | | | | F | | P | | | thin (5.3 "Expand to check") | ADD: exercises in 4.8. |
| 7.7 | Lemmas: schematic generality and minimal premises; proof generalisation (√2 → √3 → √p) | | | F | | | | | | | P | | | comp. (2.3) | KEEP + remark in 2.3; a generalisation item in 2.2 or 5.5. |
| 7.8 | Argument extraction from prose (premises, conclusion, suppressed premises) | | P | | P | | | | | | | | F | comp. (5.4) | ADD: extraction exercise in 5.4. |
| 7.9 | Logic licenses but does not choose (Harman); which premise to drop | | | | | | | | | F | | | | absent | OPT: remarks in 2.6 and 5.6. |
| 7.10 | Abbreviation levels; derivation-to-prose dictionary | | | P | | P | | P | | | | | | deeper (5.1–5.5) | KEEP; optionally an "it suffices to show" chain layout in 5.3 (En). |

## (8) Set-theoretic and neighbouring material (mostly fd2's ground)

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8.1 | Set primer: relations, functions, countability, diagonal argument, Russell's paradox as set theory | | | F | | F | | P | F | | P | | | absent | LEAVE→ fd2 (pass on Sider's "just add d to the list" device). fd1 keeps only the logical core (5.3). |
| 8.2 | Connectives ↔ set algebra (∪/∨, ∩/∧, complement/¬, ⊆/→, duality, symmetric difference) | | | | | | P | | F | | P | P | | thin | ADD: bridge C item in 3.4 or 3.7 so fd2 can cite the laws. |
| 8.3 | Peano arithmetic by recursion; set-theoretic recursion theorem; ω | | | F | | | X | F | F | | | | | comp. for formulas (3.2) | One guided C item in 3.2 (commutativity of + via lemmas; recursion as a set of pairs). LEAVE→ fd2/fd3. |
| 8.4 | Finite choice is logic (n uses of ∃E); AC for infinite families | | | | | | P | P | F | | | | | absent | ADD: Looking-ahead box in 4.6. LEAVE→ fd2 for AC. |
| 8.5 | Ordinals, cardinals, Zorn, ZFC | | | F | | | | P | F | | | | | absent | LEAVE→ fd2. |
| 8.6 | Advanced model theory (categoricity, QE, nonstandard analysis, interpretations) | | | P | | | F | F | | P | | | | absent | LEAVE→ a later logic volume. |
| 8.7 | Recursion theory, incompleteness proofs | | | P | | | F | F | | P | | | | absent | LEAVE→ later; one remark (5.8). |
| 8.8 | Resolution, Horn clauses, unification; switching circuits; phrase-structure grammars | | | F | | | | P | | | | | F | absent | LEAVE (optional C at most: height of equivalent formulas; one BNF display in 3.1). |
| 8.9 | Probability, decision theory, statistics | | F | | | | | | | | | F | P | absent | LEAVE (out of scope). |

## (9) Philosophical and non-classical material

Items marked **OPT-CH** fit a mathematics-oriented volume as an optional chapter or optional section. The suggested container is a new optional **Chapter 6, "Beyond classical logic: other semantics and their uses"**, or optional sections at the end of 3.5 and 5.7.

| # | Topic | LB | Hu | LPL | Sm | Si | vD | En | Ha | Co | Le | Hk | Ho | fd1 | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9.1 | Intuitionistic logic: BHK; derivations without RAA; one-way laws; Glivenko; disjunction property | | | | P | F | F | | | F | P | | | deeper/comp. (5.7; 3.5 thm-raa-independent) | KEEP + a table of which direction of each law survives without RAA; a C item on the disjunction property. |
| 9.2 | Kripke "stages of knowledge" models (countermodels to LEM, ¬¬P→P, (P→Q)∨(Q→P), De Morgan; heredity) | | | | | F | F | | | P | | | | absent (several claims in 5.7 are stated without proof) | **OPT-CH** (high value): optional subsection in 5.7 or the core of optional Ch6. It turns 5.7's unproved claims into theorems. |
| 9.3 | Many-valued logics (Kleene K3, LP, Łukasiewicz, FDE); three readings of LEM; supervaluations | | | | | F | | | | F | | | | thin (one Gödel 3-valued use in 3.5) | **OPT-CH**: C items in 3.5 (which rules survive which tables; Kleene as partial information for undefined terms). Skip supervaluations and the philosophy. |
| 9.4 | Material vs subjunctive / counterfactual / strict conditional; Jackson; Grice | | P | P | F | F | P | | | F | P | | P | thin (1.1 promise reading; 2.1) | ADD: a second-reading fold (with 3.7 above), including Smith's elimination argument. Counterfactual logic LEAVE. |
| 9.5 | Modal logic K–S5 and the countermodel procedure | | | | | F | | | | P | | | P | absent | LEAVE (borrow only the procedure in 2.2 and 4.7; at most a scope exercise in 5.2). Low-priority OPT-CH. |
| 9.6 | Relevance and paraconsistent logic; explosion | | | | P | P | | | | F | | | | deeper on explosion (2.1) | KEEP + a one-line pointer in 2.1. |
| 9.7 | Self-reference: Liar, Curry, validity Curry | | | | | | | | | F | | | | absent | ADD: OPT C item, Curry in Fitch, in 2.6 or 3.5, pointing to fd2's comprehension. |
| 9.8 | Second-order logic; plural quantification | | | P | | F | F | F | | F | | | | absent | Remark only (4.18 box). |
| 9.9 | Philosophy of logic: nature of consequence, logical constants (permutation invariance), pluralism, normativity, scandal of deduction, docens/utens | | | | P | F | | | | F | | | | absent | LEAVE; at most remarks (logical constants held fixed, in 1.1; scandal of deduction, in 5.4; docens/utens framing, in 5.7). |
| 9.10 | Inductive logic and probability | | F | | P | | | | | | | F | | thin | LEAVE; second readings only (see 1.15). |
| 9.11 | Vagueness, bivalence, intensional contexts, sense and reference | | | | F | P | | | | P | | | F | absent | One sentence in 1.1 (mathematical predicates are sharp); opacity warning in 4.7. |

---

## Pedagogy devices across the books, and fd1's current use

fd1 status: **uses** / **partial** / **absent**.

| Device | Books | fd1 | Note / where to adopt |
|---|---|---|---|
| Purpose-annotated assumptions ("asm, for →I"; "flag x₀, for ∀I") | LB | absent | Ch1, 2, 4; links to the 5.1 rhetoric ("suppose, for contradiction"). |
| Goal lines with blank citations; derivation shown growing in snapshots | LB, Co, Si | partial (2.6 partial derivations) | Early Ch1 examples. |
| Bad rule refuted by a row; WRONG printed beside RIGHT; "Not allowed" lists with a one-clause diagnosis | LB, Hu, Hk, Le | partial (1.2 C1 bad rule; Common errors) | A "Not allowed" block per rule card. |
| Informal (mathematical) version first, then formal | LB, LPL, Le, Sm | uses ("How this looks in a mathematical proof") | Add a two-column exercise type. |
| Paraphrase intermediate stage; reading the formula back | LB, Sm, Ho, En, LPL | partial (4.8 outside-in) | 1.1 and 4.1. |
| Fixed symbolization key across a whole set | LB, Sm | absent | 4.8 (ℕ key), 1.1. |
| Parallel semantic/syntactic tables; "what establishes / what refutes" tables | LB | absent | 3.4, 4.11. |
| Strategy lists that grow section by section; two-rule "combos" | Hu, LB, LPL | uses (named moves); combos absent | 2.6, 4.8. |
| Chapter glossary, end-of-chapter summary, Interlude pages, "Remember" boxes, key-terms list | LB, Sm, LPL, Hu, Hk | absent (no glossary or chapter-close recap found) | Every chapter index; Interludes after Ch3 and Ch4. |
| Rule-instance galleries (compound substitutions plus one non-instance) | Hu | absent | Each rule card in 1.2–1.6 and 4.3–4.6. |
| Flowcharts for decision methods | Hu | absent | 3.4–3.5 refuting-row search; 4.11 counter-model search. |
| Isolate a sub-skill and drill it first | Hu | partial (A2 drills) | Backward computation in 3.3. |
| Decide-then-justify (verdict withheld) | LPL, Si, En | thin | B items in every rule section. |
| Small finite worlds as pictures (arrow, Hasse, blocks) | LPL, vD, Si, En, Ho | partial (ch04 revision plans small-world figures) | All of 4.11, plus 3.3. |
| Game semantics | LPL | partial (4.1 informal) | 3.3, 4.11, 4.10. |
| Guided "you try it" builds | LPL | partial (Quick checks) | Ch4 rule sections. |
| Nonsense predicates (validity is independent of meaning) | LPL | absent | 1.1 or 4.11, one example. |
| Deliberate failure shown (misused name, infinite branch, failed search) | Sm, Le, Si | uses (2.6 failed search; side-condition errors) | Keep. |
| Near misses stopped at the exact line where a restriction bites | Le, LB | uses (2.6, 4.6, 4.10) | Audit completeness. |
| Finite-universe twin derivation (∃E beside ∨E) | Le | absent | 4.6 figure. |
| First semantic proof "in excessive detail", then condensed | Si | uses for derivations (5.3); absent for semantic proofs | 3.3, 4.11. |
| Checklist for inductive proofs | Si | absent (Ch5 has a writing procedure) | 3.2 box. |
| Several systems compared, trade-off named; two proofs of one theorem | Si, vD, En | partial (normal forms done two ways) | Completeness (3.6b); trees. |
| Deviant semantics as a lens on classical laws | Si, Co | partial (one use) | 3.5, 5.7. |
| Heuristic stories (promise reading, office board, stages of knowledge, painting for recursion) | vD, En, Hu | uses (promise reading) | Kripke stages if 9.2 is adopted. |
| Inline "(why?)" micro-prompts with folded answers | Ha | partial (Quick checks) | Main-line examples. |
| Morals / slogans | Ha, Hk, Sm | uses (named moves) | Add Halmos's "prove it cannot be false" for ∅ in 4.9. |
| Diagnostic pretest of tempting misreadings ("Odd Questions") | Hk | absent | Volume or Ch1 opening page. |
| Stock characters / dialogues | Hk, Co, Hu | absent | Tortoise (1.3); tonk (3.3); dialogue R items in Ch2 and Ch5. |
| Rule discovery: derive rules from tables | Ho | absent (only the reverse direction, 3.3) | 3.3, 4.11. |
| One unifying idea: counterexample set / "describe a situation" | Ho, LB | absent | 1.1 → 4.11. |
| "Not:" mistranslation catalogues; minimal pairs | Ho, LB, Hu | thin | 1.1, 4.1, 4.9. |
| Answers with commentary on alternatives | Ho | uses (full folded solutions) | Keep. |
| Numbered library of results cited by number | Le, LB | partial (labels, derived rules, rule cards) | A standard-sequents page. |
| Prose commentary after each proof | Le, Si | uses | Keep. |
| Challenge to doubters ("name the rule you reject") | Le | absent | 2.1, 5.7. |
| Twin-law boxes (propositional ↔ quantified) | Le, LB | thin | 4.9. |
| "Used later" marking on exercises the text cites | En | absent | All chapters. |
| Decision tree "how to show ⊢ or ⊬" | Co | absent | 3.5, 4.11. |
| Philosophical arguments as numbered, rule-tagged derivations | Co | absent | 5.4–5.6 exercises. |
| Graded tiers / stars | LPL, En | uses (A/B/C/R; better than every book) | Keep. |
| Machine checking (BERTIE, Fitch, Tarski's World) | LB, LPL | partial (Lean column; internal Fitch checker, not reader-facing) | A reader-facing checker for the drill banks. |
| Proof dependency diagrams | Hu | absent | 5.4 (optional). |

### Exercise types (fd1 status)

| Exercise type | Books | fd1 |
|---|---|---|
| Large drill batteries (15–20 per bank, 2-line to 10-line ramp) | LB, Hu, Le, vD | thin (A2 banks of about 10) |
| Derive or refute, verdict withheld | LPL, Si, En, Sm | thin |
| Give an example or explain why it is impossible | LB | absent |
| True/false metalogical claims with justification | LB, Sm, Hk | partial |
| Write the one line this rule gives (one-step items) | Hu, Le | absent |
| Supply the missing premise | Hu | absent |
| Fill in the justification column | Hu, LB | partial |
| Is this single rule application correct? | Le | partial |
| Changed-semantics soundness; remove a rule and find the broken lemma | LB | partial (safe/unsafe-rule C1 only) |
| False thesis: find where the induction breaks; inventor's paradox | LB, LPL | absent |
| Build a model / smallest model / independence by two models | LPL, vD, En, Ha | thin |
| Sentence separating two structures; describe every model of σ | En, vD | absent |
| Define this notion by a formula | vD, En | absent |
| Symbolization set on one fixed key | LB, Sm, Le, Ho | absent |
| Logic → English decoding in arithmetic | Sm | absent |
| Sorites / long chain puzzles | Sm | absent |
| Logic puzzles | En, Hu | absent |
| Dialogue extraction (R item) | Hu | absent |
| Parallel-form recognition ("which argument has the same form?") | Hu, Le | absent |
