<!-- hand-written -->
# Revision blueprint: F1.4 Predicate Logic and the Quantifier Rules (fd1 Chapter 4), R4

**What this is.** A **delta** blueprint (stage S1) for revising the released Chapter 4 of *Logic and Proof* so that a first-year reader gets in more easily. It is complete on its own: a drafter executes it with this file, the current `fd1/src/ch04-predicate-logic/`, the original blueprint `fd1/authoring/blueprints/ch04.md` (for anything this file does not change), `authoring/STYLE.md` (§11, §12), `DRAFTING.md` and `NOTATION.md`. The approved pilot `ch01-revision.md` is the model of format and register, and the frozen `ch02-revision.md` and `ch03-revision.md` show how a later chapter applies it; where this file is silent on a convention, do what those files did. All line numbers below are of the **current** files (commit `da6e12e`), written `06:162` for `06-existential-elimination.md` line 162, and so on; `ix` is `index.md`.

**Inputs.** The novice-reader report on Chapter 4 (workflow journal `wf_d5bd0807-139`, result `novice:ch04`), the corpus and classic-texts comparisons as digested in the fd1 revision plan (§2 Chapter 4 rows, §3 Chapter 4 items, §4–§6), the pilot and the two frozen revision blueprints. Reference books were used for teaching technique only (small pictured worlds before infinite domains, a skeleton before the full derivation, drill volume, a cheat sheet after the rules). **Every new example, figure, drill and exercise below is the book's own**; none is taken from any book. The S2 rules recorded in `ch04.md` still bind (no Huth & Ryan exercise lists come back; `exr-existential-elimination-b1` stays off H&R 2.3.9(r)).

**What this revision assumes is already true.** Chapter 1 as delivered (R2): its §6 edits to this chapter are already in the current text (03:9, 03:229, 03:233, 03:239, 03:247, 04:13, 04:57, 04:90, 04:250, 04:420, 04:592, 04:600, 05:163, 06:223, 07:18, 07:419, 12:19). Chapters 2 and 3 as planned by their frozen blueprints: Chapter 2's rule cards end with the thirteen-rule card of 2.6, its index carries the global quantifier note, `exm-raa-zero` stays in 2.5; Chapter 3's 3.3 ends with a Looking-ahead box "Chapter 4 looks inside atoms", `lem-coincidence` is proved by one written case and a table, `lem-context-inclusion` (b)'s proof is in a fold of 3.5. The two edits those blueprints ask of this chapter are made **here**, in the same drafting pass: ch03-revision §6 row "fd1 ch04 01:25" (item 2 of §4.1 below) and ch02-revision §6 row "ch04 09:700" (§4.9 item 6).

**Binding rules for this revision.**
1. **No label is lost.** Every label now in the chapter survives, in this chapter and in its current section, with its content. Only uncited `exr-` labels change, each named in §3. Every label cited anywhere (fd1 Ch1–3 and Ch5, fd2, fd3, fd4, an1) keeps its name and its section; heading ids keep their spelling (two of them move into folds as attributes, §1 item 1).
2. **Reviewed content of cited results does not change.** A statement or proof of a cited result is either kept on the main line or moved **verbatim** into a second-reading fold. The only rewordings inside labelled blocks are listed for S2a (§8, items 1–7): the replaced part (b) of `exm-universal-introduction-derivations` (its old content moves verbatim into a fold) and one pointer phrase in its part (c), bound-letter renamings in `exm-reading-quantified-sentences` (c) and `exm-translate-limit` (d), (e), and the parenthesized compound term in `exm-computing-substitutions` (b).
3. **Forward pointers.** No `@ref` to an unseen result is a reason. Each section's main line and folds carry **at most one** pointer to a later chapter or another volume, in its Looking-ahead box (STYLE §12.1). The pointers to *Analysis on the Real Line* and *Sets, Relations, and Cardinality* now spread over 4.1, 4.2, 4.7, 4.8, 4.9, 4.10 and 4.11 are gathered into one "Where this goes" note in `index.md` (§4.0); the index is not a section, and its budget (§5) covers the note. Pointers to later sections **of this chapter** stay where they help, never as reasons. After drafting, grep each section's main line and folds for `Chapter [5-9]`, `Analysis on the Real`, `Sets, Relations`, `Number Systems`; every hit other than the box is cut. Plain pointers inside exercise solutions stay only where this file keeps them (01:352, 11:441, and the in-chapter ones).
4. **Depends on R0 and R1 only as Chapter 1 did.** The fold, Looking-ahead, drill-bank and Challenge markup follow STYLE §12 as amended by R1. The derivation renderer of R0 changes nothing in this file; the long derivations of 4.8 and 4.10 stay as wide as they are (R0 scrolls them) and gain a short skeleton display beside them (§4.8 item 6, §4.10 item 3).

---

## 1. The volume-wide conventions, as applied to Chapter 4

Chapter 1's §1 (conventions 1–14 of `ch01-revision.md`) applies, with these Chapter 4 specifics. The rule sections are 4.3–4.7 (STYLE §12.2, §12.6, §12.8); snapshots and Givens/Goal tables are for 4.4–4.6 (STYLE §12.4, §12.5).

1. **Second-reading folds.** `::: {.second-reading title="…"}`. Every fold is listed by current file:line in its section's plan; nothing else goes into a fold. No fold holds a statement a later proof cites, a definition the main line uses, a section's only Quick check or only warning, or a heading. A fold never sits inside a `.proof`, `.claim` or `.solution` div; where part of a proof is folded, the fold follows the proof as a sibling. Folded proofs of cited results move **verbatim**. Where a heading with an id moves into a fold (06:434 `existential-renaming`), the id goes on the fold, `::: {.second-reading #existential-renaming title="…"}`; if R1's engine does not take ids on folds, the fold's first line is the empty span `[]{#existential-renaming}`. The heading becomes a bold lead-in.
2. **Looking ahead.** `::: {.remark}`, title line `[Looking ahead]`, a blank line, one or two sentences, no `@ref`, the last block before `## Exercises`, at most one per section (STYLE §12.1 template, as delivered in Chapter 1). 4.1, 4.4, 4.7, 4.9 and 4.10 get one (texts per section); the others get none. Each box replaces a pointer cut elsewhere in its section, and STATUS's promise rows move with them (§6).
3. **Effort in proportion to difficulty** (STYLE §12.2). ∀E, ∃I and =I get **three bullets** each (schema, one line of reading, one example) in place of their clause-by-clause readings (03:41-47, 05:39-45, 07:49). ∀I and ∃E keep their full readings, each introduced by the sentence *"This rule has conditions that matter; read each one."* =E keeps its clauses 2–4 (07:50-52), which already are two lines each.
4. **Snapshots** (STYLE §12.4), in 4.4–4.6 only. Chapter 1's convention 4 applies with its exemption classes (i)–(vi), quoted by number. Every other main-line derivation of four or more lines in 4.4–4.6 gets **two snapshots** in its Idea (or, where it has no Idea, in one new sentence "Here is how the search grows it" before it), in the delivered markup (`% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)`, gap rows `\have[\ ][0] {} {\vdots}`, every written line carrying its final number). A snapshot is written below as `S1`/`S2`, listing what stands on the page; "unjustified" means the line is written as a goal with no justification yet. A flagged box with no assumption is shown open by its flag and a gap row. The per-section plans list every snapshot; S5 checks that no main-line derivation of 4.4–4.6 outside (i)–(vi) lacks them. Sections 4.3 and 4.7–4.12 get none (STYLE scopes them to 4.4–4.6); the long derivations of 4.8 and 4.10 get a skeleton display instead.
5. **Givens/Goal tables** (STYLE §12.5). Drawn in 4.4 (one), 4.5 (one) and 4.6 (one), at the places named. Sections 4.3 and 4.7 each say in one line what their rules do to the table (texts per section). The quantifier rules change the table as STYLE says: ∀I puts a fresh name among the Givens and makes the instance the goal; ∃E puts a witness (its name and its assumption) among the Givens and keeps the goal; ∀E adds an instance at the term the goal names; ∃I replaces the goal by an instance once a Given shows one.
6. **Rule card** (STYLE §12.6). The run of rule sections is 4.3–4.7. Each of 4.3–4.6 replaces its "What the rule sounds like" table by a card with columns `Rule | Shape | Side condition | You write | Lean`, one row per rule **of Chapter 4 so far**, under the lead sentence "Chapters 1 and 2's thirteen rules are on the card at the end of Section 2.6; here are this chapter's so far." (The Side condition column is the novice report's "cheat sheet": for quantifier rules the side condition is the content.) The card at the end of 4.6 is the cumulative card of the four quantifier rules and is followed by the quantifier rows of the decision chart (§4.6 item 12). 4.7 ends with the table of the whole calculus (`rule-phrase-lean-table`), which is the volume's one-page reference: columns `Rule | Shape | You write`, the Lean column collapsed into a box (§4.7 item 10). The rows, used cumulatively in 4.3–4.6:

   | Rule | Shape | Side condition | You write | Lean |
   |---|---|---|---|---|
   | ∀E | \( \forall x\, \varphi \) \( \Longrightarrow \) \( \varphi[t/x] \) | \( t \) free for \( x \) in \( \varphi \) | "In particular, for \( x = t \), …"; "applying the hypothesis to \( t \), …" | `h t` (or `specialize h t`) |
   | ∀I | box \( [x_0] \) … \( \varphi[x_0/x] \) \( \Longrightarrow \) \( \forall x\, \varphi \) | \( x_0 \) in no premise, in no open assumption, not in \( \forall x\, \varphi \) | "Let \( x \) be arbitrary. … Since \( x \) was arbitrary, …" | `intro x` |
   | ∃I | \( \varphi[t/x] \) \( \Longrightarrow \) \( \exists x\, \varphi \) | \( t \) free for \( x \) in \( \varphi \) | "Take \( x = t \). Then …"; "\( 2k + 1 \) will do." | `use t` (or `Exists.intro t h`) |
   | ∃E | \( \exists x\, \varphi \), box \( [x_0] \) \( \varphi[x_0/x] \) … \( \chi \) \( \Longrightarrow \) \( \chi \) | \( x_0 \) not in \( \chi \), not in \( \exists x\, \varphi \), in no premise, in no open assumption | "Choose \( k \) with \( n = 2k \). Then …"; "let \( x_0 \) be such a point." | `obtain` (or `Exists.elim h`) |

   The You-write and Lean entries are the current ones (03:237, 04:417-418, 05:258, 06:584). Each section keeps its Lean sentence (03:239, 04:420, 05:254's "nothing later depends on the last column", 06:580's).
7. **Quick-check density** (STYLE §12.7): about one per 800–1,000 main-line words. The new checks are written out per section.
8. **Drill banks.** `exr-<slug>-a2`, titled `[A2: Drill]`, in 4.1–4.9 and 4.11 (the rule sections 4.3–4.7 must have one; 4.1, 4.2, 4.8, 4.9 and 4.11 get one because the plan's translation, substitution, negation and counter-model skills are drill skills). 8–12 lettered parts, recall and judgement first, then the illegal line, then short derivations; **one folded solution** answering every part in one or two lines. 4.10 and 4.12 get none (the centerpiece and the second-pass section). Every drill part is written out with its answer below; every drill derivation was run through `tools/check_fitch.py` when this file was written.
9. **Scaffolded B items and Challenges.** At least one scaffolded B item per rule section (STYLE §12.8): premises and the last line shown, the gap marked, lines numbered as at the end, "*Name the move, then complete it.*" 4.3 B4 (new), 4.4 B1 (recast), 4.5 B1 (recast), 4.6 B2 (existing, the faded triple's middle), 4.7 B4 (new). A C item that is a meta-proof is titled `[Cn: Challenge: …]` and is not the section's core C: 4.2 C1 (§4.2).
10. **Notation.**
    - **Compound terms in substitutions** are parenthesized (STYLE §12.10): a term built with an infix operation symbol is written in parentheses inside the brackets, \( \varphi[(y + 1)/x] \), \( [(n + 1)/n] \), \( [(e \cdot e')/z] \). A term that is a variable, a constant or a function letter applied to terms (\( f(c) \), \( f(z) \)) is written bare. The sweep (all hits of the current text): 02:262 (the paragraph goes, §4.2 item 5), 02:275, 02:333, 02:339, 02:375, 02:433, 02:436, 02:479, 02:481, 07:518; and any hit the drafter's grep `\[[^]]*[+\\-][^]]*/` finds. NOTATION row 165 changes with it (§6).
    - **\( p, q \) are not variables for primes.** Following the plan, the chapter writes a prime as \( m \) or \( n \): `exm-reading-quantified-sentences` (c) (01:128, 01:139), the Quick check 01:231-235, `exm-translate-limit` (d), (e) (08:60-70), the procedure step 3 (08:23), and the paragraph 09:669-680. Each is a renaming of bound variables (Section 4.2), so no content changes (S2a item 3). The variable lists 01:35 and 02:33 drop "for primes and other natural numbers \( p, q \)". Small \( p, q, r \) stay atoms of Chapter 3 wherever a truth table reads a formula (01:13-19, 11:5-19, 11:548-584).
11. **Counter-readings.** The repeated disclaimer "a stalled search proves nothing … Section 4.11 gives a counter-model … proved in Section 4.12" is said **once**, in 4.3 (§4.3 item 9), with the name **counter-reading** for a reading that makes the premises true and the line or conclusion false. After 4.3 the main line says "a counter-reading" and gives one, with at most "(Section 4.11)" after it: 05:58, 06:206, 06:432, 09:348, 10:156, 10:188 (texts per section). Exercise solutions keep their wording, except where a section plan changes them.
12. **Spelling.** "nonempty" → "non-empty", "nonzero" → "non-zero", "nonnegative" → "non-negative" wherever a grep finds them (01:243, 07:528, 07:536 and others), verbatim blocks included; labels exempt. As in the pilot, a spelling change alters neither label, tier nor content.

---

## 2. Section map

| Sec | Title (the `#` line, unchanged) | File (unchanged) | Kind | What changes |
|---|---|---|---|---|
| index | Predicate Logic and the Quantifier Rules | `index.md` | rewritten | the keys-and-locks hook before the continuity one; an explicit first-reading path; "Where this goes" gathers the cross-volume pointers; named moves with the section of first use |
| 4.1 | Predicates and Quantifiers | `01-predicates-and-quantifiers.md` | rewritten | small pictured worlds before ℝ; the letter clash as a table; the game in three bullets and a move table; a new translation subsection over keys and locks; the one-domain convention cut to two sentences (in full in 4.8) |
| 4.2 | Terms, Formulas, Free Variables and Substitution | `02-terms-formulas-substitution.md` | rewritten | a core main line (binding arrows, substitution by example, capture, the practical rule) with every definition kept; the symbol list, recursive descriptions, the claim's proof, well-definedness, the status of renaming and induction as a formula folded; C1 guided and a Challenge |
| 4.3 | Using "For Every": Instantiation | `03-universal-elimination.md` | edited | ∀E in three bullets; three tiny counter-worlds for the three errors; the one explanation of counter-readings; C2(c) moves to 4.4 |
| 4.4 | Proving "For Every": Let x Be Arbitrary | `04-universal-introduction.md` | edited | the first flagged box right after the schema; the minimal open-assumption counterexample; worked (b) replaced, the renaming derivation folded; flagged-box fine print after the examples; snapshots and a Givens/Goal table |
| 4.5 | Proving "There Exists": Exhibit a Witness | `05-existential-introduction.md` | edited (lightly) | ∃I in three bullets; snapshots, one Givens/Goal table, drills |
| 4.6 | Using "There Exists": Name a Witness | `06-existential-elimination.md` | rewritten | rule, then the \( n + 2 \) derivation, then `prp-exists-and`, then the three counterexamples with counter-worlds; the core wording of freshness; "Why early?" in two sentences; existential renaming folded; the Chapter 4 rule card and decision chart |
| 4.7 | Equality and Unique Existence | `07-equality-and-uniqueness.md` | edited | =E by marking the holes; the bound-variable warning cut to its reading; the equality-axiom claim, the well-definedness argument and the proof of `prp-unique-existence-use` folded; the Lean column in a box |
| 4.8 | Translating Mathematics: Nested and Bounded Quantifiers | `08-translation.md` | edited | the one-domain convention arrives in full; the admissibility proof of the bounded rules folded; a skeleton of the limit derivation with the abbreviation \( G(N, \varepsilon) \) beside the full derivation |
| 4.9 | Negating and Moving Quantifiers | `09-quantifier-laws.md` | edited | the negation procedure moved up, before the distribution and passage laws, which move to the end; the replacement paragraph to one sentence and two folds |
| 4.10 | Uniformly Continuous Implies Continuous, Rule by Rule | `10-uniform-continuity-rule-by-rule.md` | edited | the bare skeleton \( \exists \delta\, \forall x\, K \vdash \forall x\, \exists \delta\, K \) first; a picture of \( \delta \)-windows for \( x^2 \) |
| 4.11 | Models and Counter-models | `11-models.md` | rewritten | three pictured counter-models first, then structures and satisfaction; the well-definedness paragraph and the proof of `lem-free-coincidence` folded |
| 4.12 | Soundness for Predicate Logic | `12-first-order-soundness.md` | kept | second pass on the reading path (already optional); no text change beyond the spelling sweep |

Section numbers, titles and file names do not change (fd1 Ch5, fd2, fd3 and fd4 name "Section 4.1" … "Section 4.11" and "Chapter 4" about 60 times; §6). Kept by name because later volumes or Chapter 5 name them: the subsections "Negating a definition, mechanically" (4.9; fd2 ch03 07:94), "From counter-models to non-derivability" (4.11, id kept; fd2 ch03 06:281, ledger lines in fd2 and fd1 ch05), "The rule, phrase and Lean table, completed" (4.7, id kept; ch05 01:70), "Renaming bound variables" (4.2; fd3 ch01 01:48), "Why domains are non-empty" (4.11, id kept; fd3 ch01 01:245), the Quick check on square roots in \( \nC \) (4.11; fd4 ch01 04:3, 04:74), "Every element of the empty set" (4.4, id kept; ch05 01:172), the bounded-sequence example in 4.6 (ch05 05:444), and the 16-line limit derivation with its line numbers (4.8; ch05 02:7, 02:13, 02:57).

---

## 3. Labels

### 3.1 Every label now in the chapter

Citation counts are `@label` / `@fd1:label` hits (grep of 2026-10-12): fd1 = fd1 Chapters 1–3 and 5; fd2; fd3; an1. **fd4 and an1 cite no Chapter 4 label** (zero hits; fd4 names Section 4.11 in prose only, §6). "in-ch" counts hits inside Chapter 4, dependency-ledger comments included. Every label stays in its current section; "verbatim" means statement (and proof, where there is one) unchanged in content.

| Label | Now | fd1/fd2/fd3/an1 | in-ch | Status |
|---|---|---|---|---|
| `exm-reading-quantified-sentences` | 01:120 | 0/0/0/0 | 0 | kept; (c) with the bound letters \( m, n \) for \( p, q \) (S2a 3) |
| `def-bounded-quantifier` | 01:150 | 2/6/0/0 | 14 | kept verbatim |
| `exm-quantifier-order-sum` | 01:199 | 0/0/0/0 | 7 | kept verbatim; 01:218 → fold F4.1-b |
| `exr-predicates-and-quantifiers-a1`, `-b1`, `-b2`, `-c1`, `-c2` | 01:258–355 | 0 | 0 | kept |
| `def-term` | 02:47 | 0/0/0/0 | 6 | kept verbatim, main line |
| `def-first-order-formula` | 02:85 | 0/0/4/0 | 10 | kept verbatim, main line (fd3 cites it: never folded) |
| `def-free-variable` | 02:146 | 0/0/0/0 | 3 | kept verbatim, main line |
| `def-sentence` | 02:161 | 0/0/0/0 | 2 | kept verbatim |
| `exm-free-and-bound-limit` | 02:187 | 0/0/0/0 | 0 | kept verbatim, **moved into fold F4.2-d** (the analysis payoff of the subsection; STYLE §12.9) |
| `def-substitution` | 02:236 | 0/0/0/0 | 10 | kept verbatim, main line |
| `exm-computing-substitutions` | 02:268 | 0/0/0/0 | 1 | kept; (b) written \( [(y + 1)/x] \) (S2a 4); moved before `def-substitution` |
| `def-free-for` | 02:347 | 0/0/0/0 | 12 | kept verbatim, main line, with its four special cases |
| `exr-terms-formulas-substitution-a1`, `-b2`, `-c2` | 02:442, 497, 600 | 0 | 0 | kept |
| `exr-terms-formulas-substitution-b1` | 02:471 | 0 | 0 | kept; (c), (e) with parenthesized terms |
| `exr-terms-formulas-substitution-c1` | 02:535 | 0 | 0 | **changed**: guided (statement strengthened in the item, only the quantifier case asked), title `[C1: Challenge: What substitution does to the free variables]` |
| `def-rule-universal-elimination` | 03:23 | 0/1/0/0 | 4 | kept verbatim; clause reading → three bullets |
| `exm-universal-elimination-derivations` | 03:69 | 0/0/0/0 | 1 | kept verbatim |
| `exr-universal-elimination-a1`, `-b1`, `-b2`, `-b3`, `-c1` | 03:253–379 | 0 | 0 | kept |
| `exr-universal-elimination-c2` | 03:438 | 0 | 0 | **changed**: part (c) and its marking line move to `exr-universal-introduction-b4`; (a), (b) kept, marking scheme rebalanced (§4.3) |
| `def-rules-universal` | 04:25 | 3/5/3/0 | 10 | kept verbatim |
| `exm-universal-introduction-derivations` | 04:161 | 0/0/0/0 | 5 | kept; **part (b) replaced** by \( \forall x\, (P(x) \to Q(x)), \forall x\, P(x) \vdash \forall x\, Q(x) \); old (b) (the front renaming) moves verbatim into fold F4.4-c after the example; (a), (c) verbatim (06:436, 08:461, 08:477, 10:99, 10:300 cite (b) or (c): §4.6 item 9 rewords the one that cites (b)) (S2a 1) |
| `prp-forall-and` | 04:241 | 0/0/0/0 | 2 | kept verbatim |
| `every-element-of-the-empty-set` (heading id) | 04:300 | 0 | 0 | kept, main line |
| `exr-universal-introduction-a1` | 04:432 | 0 | 0 | kept; D3 changed (§4.4) |
| `exr-universal-introduction-b1` | 04:511 | 0 | 0 | kept; recast as the scaffolded item (content and answer unchanged) |
| `exr-universal-introduction-b2` | 04:547 | 0 | 1 | **frozen** (cited by `exr-models-b3`) |
| `exr-universal-introduction-b3`, `-c1`, `-c2` | 04:589–692 | 0 | 0 | kept |
| `def-rule-existential-introduction` | 05:23 | 1/1/3/0 | 6 | kept verbatim; clause reading → three bullets and one paragraph |
| `prp-forall-implies-exists` | 05:96 | 0/0/0/0 | 7 | kept verbatim |
| `exm-existential-introduction-derivations` | 05:136 | 0/0/0/0 | 2 | kept verbatim; snapshots added |
| `exr-existential-introduction-a1`, `-b2`, `-b3` | 05:270–349 | 0 | 0 | kept |
| `exr-existential-introduction-b1` | 05:297 | 0 | 0 | kept; recast as the scaffolded item |
| `exr-existential-introduction-c1` | 05:376 | 0 | 1 | **frozen** (cited by 12:270) |
| `exr-existential-introduction-c2` | 05:425 | 0 | 3 | **frozen** (cited by 11:3, 11:277, 12:252) |
| `def-rules-existential` | 06:26 | 2/8/7/0 | 7 | kept verbatim |
| `prp-exists-and` | 06:166 | 0/0/0/0 | 8 | kept verbatim; snapshots added; moves after the \( n + 2 \) derivation |
| `exm-existential-elimination-derivations` | 06:211 | 0/0/0/0 | 2 | kept verbatim; snapshots added |
| `prp-exists-forall-swap` | 06:313 | 3/3/0/0 | 10 | kept verbatim (key proof); Idea gains a Givens/Goal table and snapshots; 06:362 → fold F4.6-c |
| `existential-renaming` (heading id) | 06:434 | 0 | 0 | kept, **on fold F4.6-a** (§1 item 1) |
| `exm-sum-of-evens` | 06:473 | 1/0/0/0 | 2 | kept verbatim; snapshots added |
| `exr-existential-elimination-a1`, `-b1`, `-b2`, `-b3`, `-c1` | 06:596–760 | 0 | 0 | kept |
| `exr-existential-elimination-c2` | 06:822 | 0 | 1 | **frozen** (cited by 12:281) |
| `def-rules-equality` | 07:24 | 0/7/4/0 | 4 | kept verbatim |
| `prp-equality-symmetric-transitive` | 07:101 | 0/6/0/0 | 7 | kept verbatim |
| `def-unique-existence` | 07:256 | 1/3/0/0 | 2 | kept verbatim; the well-definedness argument → fold F4.7-d, its substitution fact stated on the main line |
| `prp-unique-existence-use` | 07:314 | 1/4/0/0 | 2 | kept verbatim: statement, meaning and Idea on the main line, proof verbatim → fold F4.7-f |
| `rule-phrase-lean-table` (heading id) | 07:417 | 0 | 0 | kept |
| `exr-equality-and-uniqueness-a1` … `-c2` | 07:449–584 | 0 | 0 | kept |
| `exm-translate-limit` | 08:27 | 1/0/2/0 | 2 | kept; (d), (e) with bound letters \( m, n \) for \( p, q \) (S2a 3); (a)–(c) verbatim (the cited parts) |
| `prp-bounded-quantifier-rules` | 08:93 | 5/7/2/0 | 7 | kept verbatim: statement and Idea main line, proof verbatim → fold F4.8-b |
| `exr-translation-a1`, `-b1`, `-b2`, `-c2` | 08:339–447 | 0 | 0 | kept |
| `exr-translation-c1` | 08:426 | 0 | 1 | **frozen** (cited by 10:3) |
| `prp-quantifier-negation` | 09:13 | 7/2/16/0 | 12 | kept verbatim (key proof, main line) |
| `prp-negated-implication` | 09:134 | 4/6/18/0 | 14 | kept verbatim |
| `prp-bounded-quantifier-negation` | 09:199 | 8/11/29/0 | 14 | kept verbatim |
| `prp-quantifier-distribution` | 09:297 | 0/0/0/0 | 2 | kept verbatim; moves to the end of the section |
| `prp-quantifier-passage` | 09:352 | 1/0/0/0 | 9 | kept verbatim; moves to the end of the section |
| `exm-negating-definitions` | 09:608 | 2/0/0/0 | 6 | kept verbatim; moves up (§4.9) |
| `prp-arbitrarily-close-equal` | 09:704 | 4/0/4/0 | 2 | kept verbatim |
| `exr-quantifier-laws-a1` … `-c2` | 09:726–901 | 0 | 0 | kept (C2 exit check) |
| `exm-uniform-implies-continuous` | 10:30 | 6/1/0/0 | 2 | kept verbatim (key proof; ch05 03:214 copies its 11 lines) |
| `exm-converse-fails` | 10:107 | 3/0/0/0 | 2 | kept verbatim |
| `exm-square-not-uniform` | 10:160 | 9/0/0/0 | 2 | kept verbatim |
| `exr-uniform-continuity-rule-by-rule-a1` … `-c3` | 10:198–403 | 0 | 0 | kept (B2 ordering, C1 faded, C3 exit check) |
| `def-structure` | 11:27 | 0/0/0/0 | 3 | kept verbatim |
| `def-assignment` | 11:69 | 0/0/0/0 | 1 | kept verbatim |
| `def-satisfaction` | 11:106 | 0/0/0/0 | 7 | kept verbatim |
| `lem-free-coincidence` | 11:158 | 0/0/0/0 | 16 | kept verbatim: statement and one-sentence meaning main line, Idea and proof verbatim → fold F4.11-d |
| `def-first-order-entailment` | 11:207 | 0/0/0/0 | 6 | kept verbatim |
| `why-domains-are-non-empty` (heading id) | 11:227 | 0 | 0 | kept |
| `exm-counter-model-swap` | 11:243 | 0/3/0/0 | 3 | kept verbatim |
| `from-counter-models-to-non-derivability` (heading id) | 11:303 | 0 | 0 | kept (named in fd2 and in ledger lines) |
| `exr-models-a1`, `-b2`, `-r1`, `-r3`, `-r4` | 11:321–674 | 0 | 0 | kept |
| `exr-models-b1`, `-b3`, `-c3`, `-r2` | 11:359, 395, 500, 585 | 0 | 1–2 | **frozen** (cited inside the chapter) |
| `exr-models-c1`, `-c2` | 11:412, 457 | 0/1/0/0 each | 0 | **frozen** (cited by fd2 ch03 01) |
| `lem-term-substitution`, `cor-renaming-bound-variables`, `thm-first-order-soundness`, `cor-counter-model` | 12:57–236 | 0/0/0/0; thm 0/0/1/0 | 19, 1, 8, 4 | kept verbatim (4.12 unchanged) |
| `counter-models-prove-non-derivability` (heading id) | 12:232 | 0 | 0 | kept |
| `exr-first-order-soundness-a1` … `-c2` | 12:292–407 | 0 | 0 | kept |

### 3.2 New labels

`exr-predicates-and-quantifiers-a2`; `exr-terms-formulas-substitution-a2`; `exr-universal-elimination-a2`, `-b4`; `exr-universal-introduction-a2`, `-b4`; `exr-existential-introduction-a2`; `exr-existential-elimination-a2`; `exr-equality-and-uniqueness-a2`, `-b4`; `exr-translation-a2`; `exr-quantifier-laws-a2`; `exr-models-a2`. No new `def-`, `prp-`, `exm-`, `lem-` or `thm-` label; the new worked derivation of 4.6 (\( n + 2 \)) and the skeletons of 4.8 and 4.10 are unlabelled. Grep `fd1/src` before creating each (DRAFTING rule).

### 3.3 Bookkeeping (coordinator, S4)

- `fd1/authoring/ledger/ch04.yaml` (labelled blocks and Quick checks only): no item is retired. `exr-universal-elimination-c2` keeps its key; part (c) leaves it, so its hash changes and the item is re-reviewed. The new `exr-universal-introduction-b4` is a new entry (its content is old C2(c), but its label is new: no verdict carried). `exr-universal-introduction-b1` and `exr-existential-introduction-b1` keep their keys (recast as scaffolds; hashes change). `exr-terms-formulas-substitution-c1` keeps its key (guided: re-reviewed). `exr-universal-introduction-a1` keeps its key (D3 changed). `exm-universal-introduction-derivations` keeps its key (part (b) replaced: re-reviewed). Items that move into folds keep their keys and files; no labelled item changes file. **Quick-check keys are ordinal per file** (`check:<file>:<n>`): the new Quick checks of 4.1 (two), 4.3, 4.4, 4.5, 4.6, 4.7, 4.8 and 4.11 and the moves in 4.2 and 4.9 shift the ordinals, so the coordinator re-keys every `check:` entry of those files by its new position (kept checks carry their verdicts as stale, as for any changed hash; new checks are new entries).
- The dependency-ledger comments at the end of each section file: lines whose evidence moves follow it (the one-domain convention, cited by 02's and 08's ledger lines as "conventions of F1.4 §01", is now stated in full in 08 and briefly in 01: both citations stay true); new lines for every new claim of §8 items 8–22; the lines of moved text keep their wording.
- `fd1/verify/ch04/`: new sidecars `exr-predicates-and-quantifiers-a2.py` (the world W of 4.1 as finite structures: every truth value of §4.1 item 5 and drill (a)–(d); the keys-and-locks world), `exr-universal-elimination-a2.py` (none needed beyond school arithmetic; may be omitted), `def-rules-existential.py` gains the \( n + 2 \) arith line and the three counter-worlds of 4.6, `def-rule-universal-elimination.py` gains the three counter-worlds of 4.3, `exm-square-not-uniform.py` gains the \( \delta \)-window values of §4.10 item 7, `def-satisfaction.py` or `exm-counter-model-swap.py` gains the three pictures of 4.11, and `exr-models-a2.py`, `exr-equality-and-uniqueness-a2.py` check their finite claims. `exr-terms-formulas-substitution-c1.py` is unchanged (the mathematics is the same).
- `NOTATION.md` rows 162, 163, 165 (§6).

---

## 4. Per-section plans

Budgets: **main line** = prose words by `tools/check_structure.py`'s `prose_words`, counted over the section file **outside `.second-reading` folds and before `## Exercises`**. Folds are budgeted beside it. Exercises are budgeted separately (drill answers one or two lines each). Totals and the Time line in §5. Word counts quoted for current lines are `prose_words` of those lines.

### 4.0 `index.md` (rewritten)

**Budget:** ≤ 1,100 words (now 916), the "Where this goes" note included.

1. **Opening (new, ~170 words; replaces ix:3-5).** Two sentences about a building's keys and locks: "*Every lock in this building has a key that opens it.* *Some key opens every lock in this building.* The two sentences use the same words, and the second says far more: it promises a master key. Swap 'every lock' and 'some key', and a claim about each lock becomes a claim about one key for all of them." Then the square-root argument of ix:3, kept: the statements of analysis are made of "for every" and "there exists"; to a truth table each such sentence is one atom, and "every positive real has a square root; 2 is positive; so 2 has a square root" has the invalid form \( p, q \therefore r \). Then one sentence each: this chapter adds predicates, terms and the two quantifiers, and gives their rules one per section, as Chapters 1 and 2 did for the connectives; analysis has the keys-and-locks trap too, since continuity and uniform continuity differ only in the order of two quantifiers, and Section 4.10 shows, rule by rule, why one implies the other and not conversely. The sentence about side conditions and analysts (ix:3, last sentence) moves to the end of the Roadmap (item 5).
2. **What you need (four lines; replaces ix:7):** "Chapters 1–3. From Chapters 1 and 2: the rules of every connective, derivations with boxes and the scope rule (@def-derivation), derived rules (@def-derived-rule), and the search method of Section 2.6, which each rule section here extends by one step. From Chapter 3: formulas as objects (@def-formula), structural induction and recursion (@thm-structural-induction, @thm-structural-recursion), and refuting rows (@cor-refuting-row). School arithmetic and the order of \( \nN \), \( \nZ \), \( \nQ \), \( \nR \) are used in examples as facts."
3. **Time:** recomputed from the delivered text (§5), drill banks at one exercise per four parts. No figure is fixed in advance; §5's estimate is about 56 hours on the core track and about 90 for everything.
4. **How to read this chapter (new, ~150 words; bold lead-in, the explicit first-reading path):** "A first reading: Section 4.1; Section 4.2 with its folds closed; Sections 4.3–4.6, the four rules, and the card at the end of 4.6; the search method in Section 4.8; the negation procedure in Section 4.9; Section 4.10; and the three pictures and the definitions of Section 4.11. Left for a second reading: unique existence in Section 4.7 (from 'Unique existence' on), the distribution and passage laws at the end of Section 4.9, the folded parts of Section 4.11, and Section 4.12, which is optional. Folds hold edge cases and longer arguments; they are not optional, and later proofs may use them."
5. **Roadmap:** the twelve bullets of ix:13-24, one sentence each, kept, with 4.1's bullet "… how to read 'for every' and 'there exists' in a small pictured world and over the numbers, …", 4.6's bullet "… and the card of the four quantifier rules", 4.11's bullet "… three pictured counter-models first, then a meaning for every formula …". After the list, ix:3's last sentence: "Each quantifier rule comes with a side condition about names, and the side conditions turn out to be exactly the rules that analysts break when a \( \delta \) secretly depends on an \( x \), or when a witness is treated as if it were arbitrary."
6. **Named moves:** ix:26-35 kept, each followed by the section where it is first used: instantiate at the term you need (4.3), let \( x \) be arbitrary (4.4), postpone the witness (4.5), name the witness early (4.6), fix, obtain, choose (4.6), negate quantifier by quantifier (4.9), refute with a model (first as a picture in 4.1 and a counter-reading in 4.3; exact in 4.11), read the dependency off the order (4.1). Then one sentence: "The four quantifier rules, with their side conditions and phrases, are on one card at the end of Section 4.6."
7. **Where this goes (new, ~150 words; bold lead-in).** "*Sets, Relations, and Cardinality*, Chapter 1 develops sets, membership, the empty set, pairs and functions, which this chapter uses in their everyday sense (Sections 4.1, 4.2 and 4.11). *Analysis on the Real Line*, Chapter 1 proves from the axioms of the real numbers the school facts used in examples here: that \( \sqrt 2 \) exists (4.1), the field and order facts behind mixed chains (4.7), the Archimedean property (4.8), and the rules for absolute value (4.9); its Chapters 5 and 6 define continuity and uniform continuity properly, which Section 4.10 uses only as quantifier patterns." These are the pointers cut from 01:39, 01:41, 01:101, 01:184, 02:110, 07:228, 07:248, 08:305, 09:118, 09:718, 10:7 and 11:42; STATUS rows move their source to "index" (§6).

### 4.1 Section 4.1: Predicates and Quantifiers (`01-predicates-and-quantifiers.md`)

**Budget:** main line ≤ 5,000 words (now 4,670; about 650 folded, moved or cut and about 1,000 new); folds ≤ 300. Looking ahead: "Chapter 5 names the convention that a letter introduced nowhere in a theorem is read with 'for every' in front, with the other conventions written mathematics relies on." (01:246's pointer, moved; STATUS row F1.4 §01 for F1.5.)

**New order of material.**
1. Opening (01:3), cut to two sentences (~60 words): Chapters 1–3 treated an atomic statement as a closed box; this section opens it, introduces predicates, variables, domains and the two quantifiers, and teaches how to **read** a quantified sentence, first in a small picture and then over the numbers. The rules come one per section in 4.3–4.6.
2. `## An argument the truth table rejects`: 01:5-21 kept. 01:23 → fold F4.1-a. 01:25 → "This is the warning of Section 3.3 come true: a truth table sees only the connectives, and everything inside an atom is invisible to it. Section 3.3 closed with the remark that this chapter looks inside atoms. We now do. …" (the rest of 01:25 kept; ch03-revision §6 row "fd1 ch04 01:25").
3. `## Predicates: statements with holes`: 01:29-51 kept, with: 01:35's variable list ends "…, and in analysis also \( \varepsilon, \delta, N, n \)" (no \( p, q \)); 01:39 → cut the sentence "*Sets, Relations, and Cardinality*, Chapter 1 develops sets and membership properly." and start the next with "Here a set is understood informally …"; 01:41 → cut "*Sets, Relations, and Cardinality*, Chapter 1 defines functions as sets of pairs;" keeping "here a function symbol is simply a way of naming one object in terms of others". The remark 01:53-55 is **replaced** by a table (~90 words), lead "Some letters change their job in this chapter:":

   | Letter | In Chapters 1–3 | In this chapter | How to tell |
   |---|---|---|---|
   | \( P, Q, R \) | a whole statement (Chapters 1–2); an atom or any formula (Chapter 3) | a predicate symbol | followed by its holes: \( P(x) \), \( R(x, y) \); a bare \( P \) is a statement letter from earlier chapters |
   | \( p, q, r \) | atoms of a truth table | atoms still, only where a truth table reads a formula (the argument above; review exercises) | never inside a formula of this chapter |
   | \( x, y, n, \varepsilon \) | one fixed number in an example ("let \( x \) be a real number") | variables: holes of predicates, closed by quantifiers | a quantifier in front of them, or a hole still open |

   One sentence after it: "A property \( P(n) \) of natural numbers, as in the principle of induction (@ax-induction), was already a one-place predicate in this sense." (the last sentence of 01:54).
4. `## Quantifiers and the domain`: 01:59-82 kept (01:63's domain paragraph, the two quantifiers, 01:74, the first premise over \( \nR \), the → inside). The remark 01:84-86 cut to one sentence, kept on the main line (~40 words): "'True' here means what it means in ordinary mathematics: look at the domain and ask whether every element, or some element, makes the sentence true. Section 4.11 turns this reading into a definition; until then, a claim that a sentence can be **derived** is always proved by a derivation."
5. `### Quantifiers in a small world` **(new, ~380 words).** "Before the numbers, a picture. A **world** here is a few dots, the objects of the domain, with some dots labeled \( P \) or \( Q \) (the dots the one-place predicates hold of) and arrows between dots (the pairs a two-place predicate \( R \) holds of: an arrow from \( u \) to \( v \) means \( R(u, v) \))." Then **Figure W (new TikZ)**: four dots in a square, named \( a \) (top left), \( b \) (top right), \( c \) (bottom right), \( d \) (bottom left); next to each dot its labels, \( a \): \( P \); \( b \): \( P, Q \); \( c \): \( Q \); \( d \): none (letters only: no colour carries meaning; colour may repeat it); arrows \( a \to b \), \( b \to c \), a loop at \( c \), and \( d \to a \). Caption: "World W: domain \( \{a, b, c, d\} \); \( P \) holds of \( a, b \); \( Q \) of \( b, c \); \( R \) is the four arrows." Then six readings, each one sentence, in a list:
   - \( \exists x\, P(x) \): true; the witness \( a \).
   - \( \forall x\, P(x) \): false; the counterexample \( c \) (or \( d \)).
   - \( \forall x\, (P(x) \vee Q(x)) \): false at \( d \), which has neither label.
   - \( \exists x\, (P(x) \wedge Q(x)) \): true at \( b \).
   - \( \forall x\, \exists y\, R(x, y) \): true; every dot has an arrow leaving it (\( a \to b \), \( b \to c \), \( c \to c \), \( d \to a \)).
   - \( \exists y\, \forall x\, R(x, y) \): false; no dot receives an arrow from all four (\( c \) receives from \( b \) and \( c \) only).
   Closing sentence: "In a finite world every quantifier can be checked dot by dot. Over \( \nN \) or \( \nR \) it cannot, and the reading needs an argument, as the next subsection shows." **Quick check (new):** "In world W, is \( \forall x\, (Q(x) \to R(x, c)) \) true? Is \( \exists x\, \forall y\, \neg R(y, x) \) true?" Solution: the first is true: \( Q \) holds of \( b \) and \( c \), and both have an arrow to \( c \); at \( a \) and \( d \) the hypothesis \( Q(x) \) is false, so the implication holds. The second is true, with the witness \( d \): no arrow ends at \( d \).
6. `### The same sentence over different domains`: 01:90-114 kept, except 01:101's parenthesis → "(Its existence is a school fact here.)". 01:106's in-chapter pointer stays.
7. `### Reading a quantified sentence`: 01:118 and `exm-reading-quantified-sentences` kept, (c) written \( \neg\exists m\, \bigl( \mathrm{Prime}(m) \wedge \forall n\, (\mathrm{Prime}(n) \to n \le m) \bigr) \), "\( \mathrm{Prime}(m) \) is the one-place predicate '\( m \) is prime'", and its solution and 01:139 with the same letters ("a largest prime"; "every prime \( n \) is at most \( m \)"). 01:142 kept.
8. `## Bounded quantifiers`: 01:146-176 kept (`def-bounded-quantifier` verbatim, the \( A = \{1, 2\} \) demonstration, the warning). 01:165 (the induction display read as a bounded form) → fold F4.1-c. 01:178-182 ("One domain per formula") **moves to 4.8** verbatim (§4.8 item 2), leaving two sentences here (~50 words): "**Mixing kinds of number.** A sentence of analysis often mixes real numbers and natural numbers; the convention is to take the larger kind as the domain and let the smaller kind enter as a bound, as in \( \forall \varepsilon > 0\; \exists N \in \nN \), with a sequence \( (a_n) \) read as a function symbol \( a \), \( a_n = a(n) \). Section 4.8 states the convention in full." (4.2's `exm-free-and-bound-limit`, now in a fold, its shorthand at 02:63, and 10:7's "as with sequences in Section 4.1" rely on these two sentences.) 01:184-193 kept, with 01:184's parenthesis "(*Sets, Relations, and Cardinality*, Chapter 1 introduces it properly)" cut.
9. `## The order of quantifiers`: `exm-quantifier-order-sum` kept verbatim, except its solution's last paragraph 01:218 → fold F4.1-b. **The game (replaces 01:221 and the bullets 01:223-224):** the bold lead-in "**Quantifiers as a game.**", one sentence ("Read a sentence as a game between two players, the challenger, who tries to make it false, and the defender, who tries to make it true."), then three bullets:
   - Each \( \forall \) is a move of the challenger, who picks a value; each \( \exists \) is a move of the defender.
   - The moves are made in the order the quantifiers are written, left to right, and each player sees every move made so far.
   - When every variable has a value, the inside is checked. The sentence is true exactly when the defender can win whatever the challenger does.

   Then the **move table (new)**:

   | | (i) \( \forall x\, \exists y\, (x + y = 0) \) | (ii) \( \exists y\, \forall x\, (x + y = 0) \) |
   |---|---|---|
   | first move | challenger picks \( x \), say \( x = 5 \) | defender picks \( y \) without knowing \( x \), say \( y = 3 \) |
   | second move | defender answers \( y = -x = -5 \) | challenger answers \( x = 1 - y = -2 \) |
   | check | \( 5 + (-5) = 0 \): defender wins | \( -2 + 3 = 1 \ne 0 \): challenger wins |
   | who always wins | the defender, with \( y = -x \) | the challenger, with \( x = 1 - y \) |

   Then the caveats of 01:221 as one short remark (`::: {.remark}`, ~60 words): "The game reads sentences whose quantifiers all stand at the front, unnegated, before an inside with no quantifiers. A bounded quantifier such as \( \forall \varepsilon > 0 \) counts, its bound checked with the inside. Under a \( \neg \), or in the hypothesis of an implication, a quantifier changes sides; Section 4.9 proves the laws behind this." 01:226 and 01:228 kept. Quick check 01:230-236 kept, written \( \forall n\, \exists m\, \bigl( \mathrm{Prime}(m) \wedge m > n \bigr) \), the swapped form \( \exists m\, \forall n\, (\dots) \), and the solution with \( m \) ("take \( n = m \)").
10. `## Words that hide quantifiers`: warning 01:242-244 kept. 01:246 kept without its sentence "Chapter 5 names this convention and lists the others that written mathematics relies on." (→ Looking ahead). 01:248 → "**An implication inside \( \exists \).** This is the warning after @def-bounded-quantifier once more, and it comes up in analysis: 'there is an \( N \) such that, if \( n \ge N \), then …' is not the shape of 'for every \( \varepsilon > 0 \) there is \( N \in \nN \) such that for every \( n \ge N \), …', where the implication \( n \ge N \to \dots \) sits under \( \forall n \in \nN \). The implication belongs under a \( \forall \)."
11. `## Translating into symbols` **(new, ~420 words; the translation drill's worked passage).** Lead: "Translation is reading run backwards. Here is a domain with no numbers in it: the objects of a building, with \( \mathrm{Key}(x) \): '\( x \) is a key', \( \mathrm{Lock}(x) \): '\( x \) is a lock', and \( \mathrm{Opens}(x, y) \): '\( x \) opens \( y \)'." Then the pattern table:

    | English | Formula | Note |
    |---|---|---|
    | every key opens lock \( f \) | \( \forall x\, (\mathrm{Key}(x) \to \mathrm{Opens}(x, f)) \) | \( \to \) under \( \forall \) |
    | some key opens lock \( f \) | \( \exists x\, (\mathrm{Key}(x) \wedge \mathrm{Opens}(x, f)) \) | \( \wedge \) under \( \exists \) |
    | no key opens lock \( f \) | \( \forall x\, (\mathrm{Key}(x) \to \neg\mathrm{Opens}(x, f)) \), or \( \neg\exists x\, (\mathrm{Key}(x) \wedge \mathrm{Opens}(x, f)) \) | two equally good forms |
    | only keys open lock \( f \) | \( \forall x\, (\mathrm{Opens}(x, f) \to \mathrm{Key}(x)) \) | "only" turns the arrow round |
    | every lock has a key that opens it | \( \forall y\, (\mathrm{Lock}(y) \to \exists x\, (\mathrm{Key}(x) \wedge \mathrm{Opens}(x, y))) \) | every … some |
    | some key opens every lock | \( \exists x\, (\mathrm{Key}(x) \wedge \forall y\, (\mathrm{Lock}(y) \to \mathrm{Opens}(x, y))) \) | some … every |

    (\( f \) is a constant, "the front lock".) Then the hook settled by a picture: **Figure K (new TikZ)**: two keys \( k_1 \), \( k_2 \) (drawn as dots labeled "key") on the left, two locks \( \ell_1 \), \( \ell_2 \) (labeled "lock") on the right, arrows \( k_1 \to \ell_1 \) and \( k_2 \to \ell_2 \). Caption: "A building where every lock has a key that opens it, and no key opens every lock." Two sentences: in this building the fifth sentence is true (\( \ell_1 \) has \( k_1 \), \( \ell_2 \) has \( k_2 \)) and the sixth false (\( k_1 \) fails at \( \ell_2 \), \( k_2 \) at \( \ell_1 \)); the sixth implies the fifth (a master key opens each lock), so the order "some … every" says more, exactly as in @exm-quantifier-order-sum. Last, the classic slip (~60 words): "'Some key opens lock \( f \)' is **not** \( \exists x\, (\mathrm{Key}(x) \to \mathrm{Opens}(x, f)) \): that formula is true in every building, since the lock \( f \) is not a key, so \( f \) itself makes the hypothesis \( \mathrm{Key}(f) \) false. It is the warning after @def-bounded-quantifier again." **Quick check (new):** "Translate 'no key opens every lock'. Is it true in the building of Figure K?" Solution: \( \neg\exists x\, (\mathrm{Key}(x) \wedge \forall y\, (\mathrm{Lock}(y) \to \mathrm{Opens}(x, y))) \), or \( \forall x\, (\mathrm{Key}(x) \to \neg\forall y\, (\mathrm{Lock}(y) \to \mathrm{Opens}(x, y))) \); true, since \( k_1 \) does not open \( \ell_2 \) and \( k_2 \) does not open \( \ell_1 \).
12. `## What comes next` (replaces 01:250-252, ~40 words): "We can read quantified sentences, and translate into them. We cannot yet reason with them. Section 4.2 makes the language exact, because every rule will put a term in for a variable; Sections 4.3–4.6 give the four rules."
13. **Looking ahead** (as above).

**Folds.** F4.1-a `title="Why the truth table is not wrong"`: 01:23 verbatim. F4.1-b `title="What makes the pair work"`: 01:218 verbatim (a sibling after the example's solution, not inside it). F4.1-c `title="The induction display, read again"`: 01:165 verbatim.

**Cut outright:** the pointers in 01:39, 01:41, 01:101, 01:184 and 01:246; the remark 01:53-55 (replaced by the table); 01:221 and 01:223-224 (replaced by the bullets, table and remark); 01:250-252 (replaced).

**Quick checks:** \( \exists x\, (x + x = x) \) over three domains (kept), world W (new), the swapped prime sentence (kept), keys and locks (new): four in ~5,000 words.

**Exercises.** A1, B1, B2, C1 (its solution's pointer 01:352 kept), C2 kept. New:
- **A2: Drill** (`exr-predicates-and-quantifiers-a2`), parts (a)–(d) about world W of the text, (e)–(i) about the building, (j)–(l) over the numbers:
  (a) In W, is \( \forall x\, (P(x) \to \exists y\, R(x, y)) \) true? — Yes: \( P \) holds of \( a \) and \( b \), and \( a \to b \), \( b \to c \).
  (b) In W, is \( \exists x\, (Q(x) \wedge \neg P(x)) \) true? — Yes, at \( c \).
  (c) In W, is \( \forall x\, \exists y\, R(y, x) \) true? — No: no arrow ends at \( d \).
  (d) In W, is \( \exists x\, R(x, x) \) true? — Yes: the loop at \( c \).
  (e) Translate "every key opens some lock". — \( \forall x\, (\mathrm{Key}(x) \to \exists y\, (\mathrm{Lock}(y) \wedge \mathrm{Opens}(x, y))) \).
  (f) Translate "no lock is a key". — \( \forall x\, (\mathrm{Lock}(x) \to \neg\mathrm{Key}(x)) \), or \( \neg\exists x\, (\mathrm{Lock}(x) \wedge \mathrm{Key}(x)) \).
  (g) Translate "only keys open locks". — \( \forall x\, \forall y\, ((\mathrm{Lock}(y) \wedge \mathrm{Opens}(x, y)) \to \mathrm{Key}(x)) \).
  (h) Translate "some lock is opened by every key". — \( \exists y\, (\mathrm{Lock}(y) \wedge \forall x\, (\mathrm{Key}(x) \to \mathrm{Opens}(x, y))) \).
  (i) Is (h) true in the building of Figure K? — No: \( \ell_1 \) is not opened by \( k_2 \), and \( \ell_2 \) not by \( k_1 \).
  (j) Over \( \nZ \), translate "every integer has a larger one", and say whether it is true. — \( \forall x\, \exists y\, (y > x) \); true, with \( y = x + 1 \).
  (k) Swap the quantifiers of (j) and read the result. — \( \exists y\, \forall x\, (y > x) \), "some integer is larger than every integer"; false: \( x = y \) defeats every \( y \).
  (l) Over \( \nR \), translate with bounded quantifiers "some positive number is smaller than every positive number", and say whether it is true. — \( \exists x > 0\; \forall y > 0\; (x < y) \); false: for any proposed \( x > 0 \), \( y = x \) gives \( x < x \).

**Sidecars:** `exr-predicates-and-quantifiers-a2.py` (world W and Figure K as finite structures: the six readings of item 5, its Quick check, drill (a)–(d), (i), the Quick check of item 11); school arithmetic for (j)–(l). Ledger: the readings of W and K (informal truth in a finite world, checked by the sidecar).

### 4.2 Section 4.2: Terms, Formulas, Free Variables and Substitution (`02-terms-formulas-substitution.md`)

**Budget:** main line ≤ 3,900 words (now 6,420; about 2,600 folded or cut, about 320 new); folds ≤ 2,400. No Looking-ahead box.

*Recorded deviation from the plan (§3, 4.2: "a core of about 2,500 words; Tm/Fm recursive clauses with the closure clauses folded").* The two definitions `def-term` and `def-first-order-formula` are blocks whose clauses include the closure clauses (Tm3), (Fm5); `def-first-order-formula` is cited by fd3 four times, and both are used on the main line by `def-substitution` and every rule. STYLE §12.0 forbids folding a cited statement or a definition the main line uses, so both blocks stay on the main line verbatim, as do `def-free-variable`, "appear", `def-sentence`, `def-substitution`, `def-free-for` with its four special cases (later sections cite them as "the special cases after @def-free-for"), and the statement of the claim "if \( x \) is not free in \( \varphi \), then \( \varphi[t/x] = \varphi \)" (cited by 4.3, 4.9 and 4.12). What folds is everything around them: their clause-by-clause commentary, the symbol list, the recursive descriptions, the claim's proof, well-definedness, and the status of renaming. The main line comes to about 3,900 words, not 2,500.

**New order of material.**
1. Opening (02:3) cut to ~90 words: Section 4.1 read quantified sentences by eye; every rule of Sections 4.3–4.7 has the form "put the term \( t \) in for the variable \( x \) in \( \varphi \)", written \( \varphi[t/x] \); this section says exactly what that does, and the one way it goes wrong, **capture**. The meta-remark 02:27 is **cut**.
2. `## Which letters are holes`: 02:7-25 kept.
3. `## Terms and formulas` (02:29-138, compressed). 02:31-41 (the symbol list) → fold F4.2-a, its variable list without "for primes and other natural numbers \( p, q \)". Main line: 02:43-45 and `def-term` verbatim; 02:59 cut and replaced by one sentence: "In words: variables and constants are terms, a function symbol applied to as many terms as it has places is a term, and nothing else is." 02:61 kept. 02:63 (shorthand) cut to two sentences: "We write terms in the familiar way: \( x + y \) for \( +(x, y) \), \( x^2 \), \( \abs{x} \), \( a_n \) for \( a(n) \) (a sequence is a function symbol, as Section 4.1 said). School conventions about grouping say which term is meant." 02:65-70 kept (four examples). 02:72-75 (non-terms) and 02:77 (term trees and unique readability) → fold F4.2-a. Then 02:81-83 and `def-first-order-formula` verbatim; 02:99-104 **replaced** by three bullets (~60 words): (Fm1) atomic formulas, a predicate symbol with its terms, or an equation, or \( \bot \), take the place of Chapter 3's atoms; (Fm2), (Fm3) are the connectives as before; (Fm4) puts \( \forall x \) or \( \exists x \), with a **variable** \( x \), in front of a formula, without parentheses, as \( \neg \) is. 02:106 (structural induction and recursion carry over) → fold F4.2-b; its first sentence stays on the main line: "Structural induction and recursion carry over to terms and first-order formulas, with the atomic formulas as base case and one new building step for each quantifier (the fold below says how)." Shorthand 02:108-114: rule 2 (a quantifier binds as tightly as \( \neg \)) and 02:114 kept; rules 1 and 3 one sentence each (02:110's parenthesis about *Sets, Relations, and Cardinality* cut). Parse tree 02:116-130 and its Quick check 02:132-138 kept.
4. `## Free and bound: drawing the arrows` (replaces the heading 02:140). **Figure B (new TikZ; binding arrows; the plan's "free vs bound by arrows from each quantifier").** The formula \( P(x) \wedge \forall x\, (Q(x) \to \exists y\, R(x, y)) \), typeset on one line; above it, an arc from each bound occurrence back to the quantifier that binds it: the \( x \) of \( Q(x) \) and the \( x \) of \( R(x, y) \) to \( \forall x \); the \( y \) of \( R(x, y) \) to \( \exists y \). The \( x \) of \( P(x) \) has no arc and is underlined, labeled "free". Caption: "Each bound occurrence points to its quantifier. The first \( x \) points nowhere: it is free." Lead sentence (~40 words): "Draw an arrow from each occurrence of a variable to the nearest quantifier on that variable above it in the parse tree. An occurrence with an arrow is bound; one with none is a hole still open." Then 02:144 and `def-free-variable` verbatim; 02:157 kept. 02:159 cut to its definition (main line, ~45 words): "A variable **appears in** \( \varphi \) if it is written anywhere in \( \varphi \): inside a term, or just after a quantifier symbol. Every freshness condition of this chapter is stated with 'appear'; in practice, a fresh letter is one written nowhere yet." The rest of 02:159 (the example \( \forall y\, P(x) \) and why 'appear' is used) → fold F4.2-c. `def-sentence` and 02:167 kept. Examples 02:169-176: keep the bullets for \( \forall x\, (x \ge y) \), \( P(x) \wedge \forall x\, Q(x) \) and \( \forall x\, \exists x\, P(x) \); the degenerate bullet 02:171 and the bullets 02:172, 02:174 → fold F4.2-c. The recursive description 02:178-185 → fold F4.2-c. `exm-free-and-bound-limit` (02:187-216) → fold F4.2-d verbatim (the analysis payoff; it relies on 4.1's two sentences on mixing kinds, §4.1 item 8). Warning 02:218-220 and Quick check 02:222-228 kept.
5. `## Substitution, by example first`: 02:232 and the slogan 02:234 kept. Then `exm-computing-substitutions` **moved up**, before the definition, with (b) written \( \bigl( x < y \wedge \forall x\, (x \ge 0) \bigr)[(y + 1)/x] \) and its solution unchanged in substance (each part says in words what was replaced; the "@def-substitution" in its lead becomes "the rule in the slogan above"; the solution's references to clauses stay valid once the definition follows). Then one sentence "Here are the clauses those computations followed." and `def-substitution` verbatim. 02:260 kept. 02:262 **replaced** by one sentence: "A compound term is written in parentheses: \( \varphi[(y + 1)/x] \) puts \( y + 1 \) in for \( x \)." 02:264 (well defined) and 02:266 (not the \( \sigma \) of Section 3.4) → fold F4.2-e. 02:295-297 kept. 02:299 kept, its last sentence → "Sections 4.3, 4.9 and 4.12 use it; its proof, a structural induction, is in the fold below." The `.claim` block, its Idea and proof (02:301-319) → fold F4.2-e verbatim (the statement is on the main line in 02:299).
6. `## Capture, and the practical rule`: 02:323-329 (the first capture) and 02:337-343 (the safe substitution, written \( [(y + 1)/x] \)) kept; 02:331-335 (the second capture, with \( y + 1 \)) → fold F4.2-f. 02:345 and `def-free-for` verbatim; 02:353 kept; the four special cases 02:355-360 kept; 02:362 kept. The recursive description 02:364-370 → fold F4.2-f. 02:372: its first two sentences kept ("'Free for' is the precise condition under which \( \varphi[t/x] \) says about \( t \) what \( \varphi \) says about \( x \). Each rule of Sections 4.3, 4.5 and 4.7 carries it as a side condition."); the rest → fold F4.2-f. Then **the practical rule (new, bold lead-in, ~70 words):** "**Before you substitute.** Look at each free occurrence of \( x \) and at the quantifiers above it. If none of them is on a letter of \( t \), go ahead. If one is, rename that quantifier's letter to a brand-new letter first (next subsection), and then substitute. Nothing else can go wrong." Warning 02:374-376 kept (with \( [(y + 1)/x] \)); Quick check 02:378-386 kept.
7. `## Renaming bound variables`: 02:390, the renaming definition 02:392 and 02:394 kept (fd3 ch01 01:48 relies on "a letter that appears nowhere"). 02:396 ("Its status") → fold F4.2-g, its `@lem-term-substitution` and `@lem-free-coincidence` replaced by words: "… follows from the substitution lemma of the optional Section 4.12, with the coincidence lemma of Section 4.11 and an induction on the surrounding formula, which we do not carry out." Main line keeps one sentence in its place: "Renaming a bound letter never changes what a formula says; Sections 4.4 and 4.6 derive it at the front of a formula, and the fold says where the rest stands." The recipe 02:398-403 kept (examples written \( [y/x] \), \( [(y + 1)/x] \)).
8. `## How substitution looks in a mathematical proof`: 02:407-429 kept ("apply the hypothesis with \( \varepsilon/2 \)", written \( \varphi[t/\varepsilon] \) with \( t = \varepsilon/2 \) as now; "take \( N = n \)"). The induction formula 02:431-436 → fold F4.2-h, written \( \varphi[(n + 1)/n] \).

**Folds** (each a sibling at the place named; folds do not nest): F4.2-a `title="The symbols of the language, and strings that are not terms"`: 02:31-41, 02:72-75, 02:77. F4.2-b `title="Induction and recursion on formulas"`: 02:106 from its second sentence. F4.2-c `title="Occurrences, 'appear', and the recursive description of 'free'"`: 02:159 (rest), 02:171, 02:172, 02:174, 02:178-185; placed after the examples of item 4. F4.2-d `title="The free variables of a limit statement"`: `exm-free-and-bound-limit` verbatim. F4.2-e `title="Why the definition defines, and the claim proved"`: 02:264, 02:266, 02:301-319. F4.2-f `title="A second capture, the recursive description of 'free for', and why it asks no more than it needs"`: 02:331-335, 02:364-370, 02:372 from its third sentence; placed after 02:362. F4.2-g `title="The status of renaming"`: 02:396 as reworded. F4.2-h `title="Induction, as a formula"`: 02:431-436.

**Cut outright:** 02:27; 02:59; 02:99-104 (replaced by bullets); 02:262 (replaced); the pointer in 02:110.

**Quick checks:** parse tree (kept), a free \( x \) (kept), free for (kept): three in ~3,900 words, plus Figure B.

**Exercises.** A1 kept; B1 kept with (c) \( \bigl( \forall y\, (x < y) \bigr)[(y + 1)/x] \) and (e) \( \bigl( \exists y\, (y > x) \wedge Q(y) \bigr)[(x + 1)/y] \) (solutions likewise); B2 kept (its (a) asks for the clauses the fold F4.2-c shows for "free"; the solution says so, and the item is doable from `def-free-variable` and the parse tree with the fold closed); C2 kept, the section's core C. New and changed:
- **A2: Drill** (`exr-terms-formulas-substitution-a2`):
  (a) In \( \forall y\, (x < y) \wedge \exists x\, (x = y) \), which occurrences are free, and what are the free variables? — The \( x \) of \( x < y \) and the \( y \) of \( x = y \) are free; the \( y \) of \( x < y \) is bound by \( \forall y \) and the \( x \) of \( x = y \) by \( \exists x \). Free variables: \( x \), \( y \).
  (b) Is \( \forall x\, \exists y\, (x + y = 0) \) a sentence? — Yes: every occurrence is bound.
  (c) Compute \( \bigl( x \le y \wedge \exists y\, (y < x) \bigr)[3/x] \). — \( 3 \le y \wedge \exists y\, (y < 3) \).
  (d) Compute \( \bigl( \forall x\, (x \ge y) \bigr)[0/y] \). — \( \forall x\, (x \ge 0) \).
  (e) Compute \( \bigl( \forall x\, P(x) \to P(x) \bigr)[c/x] \). — \( \forall x\, P(x) \to P(c) \) (shorthand rule 2: the \( \forall x \) governs only \( P(x) \)).
  (f) Is \( x \) free for \( y \) in \( \exists x\, (x > y) \)? — No: the free \( y \) lies in the scope of \( \exists x \), and \( x \) is the variable of the term.
  (g) Is \( z + 1 \) free for \( y \) in \( \exists x\, (x > y) \)? Compute. — Yes: \( \exists x\, (x > z + 1) \).
  (h) Put \( x \) in for \( y \) in \( \exists x\, (x > y) \), renaming first. — Rename \( x \) to \( z \): \( \exists z\, (z > y) \); then \( \exists z\, (z > x) \).
- **C1** (`exr-terms-formulas-substitution-c1`, changed: guided, a Challenge), `[C1: Challenge: What substitution does to the free variables]`. Statement: as 02:538-546, with (a) now reading: "(a) Prove (a) in the following form, by structural induction on \( \varphi \): for every \( \varphi \) in which \( t \) is free for \( x \), *if \( x \in \mathrm{FV}(\varphi) \), then \( \mathrm{FV}(\varphi[t/x]) = (\mathrm{FV}(\varphi) \setminus \{x\}) \cup \mathrm{Var}(t) \); if \( x \notin \mathrm{FV}(\varphi) \), then \( \varphi[t/x] = \varphi \).* The term version, the atomic case and the connective cases are done below; prove the case of \( \forall y\, \varphi \) (the case of \( \exists y\, \varphi \) is the same)." Then the given text, taken from the current solution: the term paragraph (02:563), the setup and \( E(\chi) \) (02:565), the atomic, negation and binary-connective cases (02:567-571). The solution keeps the quantifier case (02:573-585) and (b) (02:587-589). Hints: Hint 1 → "When \( x \) is free in \( \forall y\, \varphi \), what does 'free for' tell you about \( y \) and \( t \)?"; Hint 2 → "The recursive description of 'free for' (in the fold F4.2-f) gives \( y \notin \mathrm{Var}(t) \). Where does the computation of \( \mathrm{FV}((\forall y\, \varphi)[t/x]) \) need it?". Marking scheme (10 points): 3 the quantifier case reduced to \( \mathrm{FV}(\varphi[t/x]) \setminus \{y\} \) by the definitions; 3 the use of "free for" to get \( y \notin \mathrm{Var}(t) \) and \( t \) free for \( x \) in \( \varphi \), naming where it is used; 1 the case "\( x \) not free in \( \forall y\, \varphi \)" handled by the claim of the text; 3 both counterexamples of (b), each checked by computing both sides. Fatal errors kept (02:597).

**Sidecars:** none new; `exr-terms-formulas-substitution-b1.py` follows the parenthesized notation if it prints formulas.

### 4.3 Section 4.3: Using "For Every": Instantiation (`03-universal-elimination.md`)

**Budget:** main line ≤ 3,100 words (now 3,023); folds ≤ 200. No Looking-ahead box (the in-chapter pointer to 4.11 sits in item 9).

**Changes, in the file's order.**
1. 03:3-17 kept (03:9 already reads as Chapter 1's §6 asks; 03:10 `@exm-raa-zero` stays, Chapter 2 keeps it in 2.5).
2. The rule: slogan 03:21 and `def-rule-universal-elimination` verbatim. 03:39 kept. "Read the definition clause by clause" and clauses 1–5 (03:41-47) are **replaced** by three bullets (convention 3):
   - **Schema:** the block above: one cited line, no box.
   - **Reading:** drop the \( \forall x \), put one term in for every free \( x \), and check that no letter of the term gets caught by a quantifier inside.
   - **Example:** from \( \forall x\, (P(x) \to S(x)) \), "\( \rulename{\forall E} \) 1" at the term \( 2 \) writes \( P(2) \to S(2) \).

   Then two sentences of prose (from clauses 1 and 2): "The cited line must **begin** with \( \forall x \); a \( \forall \) buried inside another connective is dug out first by that connective's rule. Any term will do, a constant, a variable or a compound term, and nothing about it needs to be established first, since every term names an object of the domain." And one sentence on bounds (new): "When the universal statement has a bound, \( \forall x \in A\; \varphi \), using it at \( t \) also needs the line \( t \in A \); Section 4.8 makes the two steps one."
3. **Quick check (new)**, after the bullets: "Line 1 is \( \forall x\, (x + 0 = x) \). Which of \( 3 + 0 = 3 \), \( y + 0 = y \), \( 3 + 0 = x \) may line 2 be, by \( \rulename{\forall E} \)?" Solution: the first two (at the terms \( 3 \) and \( y \); \( y \) is free for \( x \), since the formula has no quantifier). The third is not an instance: \( \varphi[t/x] \) puts the **same** term in for every free \( x \), and \( 3 + 0 = x \) replaced one \( x \) and left the other.
4. 03:49 (the degenerate case) → fold F4.3-a. 03:51 and 03:53 kept. 03:55: its last sentence ("Section 4.11 states that the rule … proves it.") cut; item 9 says it once. Quick check 03:57-63 kept.
5. Four derivations (03:65-150), checking (03:152-161): kept. (No snapshots: STYLE §12.4 scopes them to 4.4–4.6.)
6. How this rule looks (03:163-193): kept, except 03:187-191 → main line keeps "A line justified 'arith' records a fact of school arithmetic or algebra, used on the lines it cites; here the fact is that \( (u - 1)^2 \) and \( u^2 - 2u + 1 \) are the same number for every real \( u \). It is **not a new rule**, and the facts of school algebra are used as facts." The rest (from "Written out in full" through "keeps every term free for them") → fold F4.3-b (4.12 recalls the convention; it is unchanged, only folded). 03:193 kept.
7. `## Common errors`: 03:197 and the three errors (03:199-219) kept. **Figure C3 (new TikZ; three tiny counter-worlds, side by side, each under a title):**
   - *Capture.* Two dots \( 0 \), \( 1 \), joined by a two-headed arrow labeled "differ". Caption line: premise \( \forall x\, \exists y\, (y \ne x) \) true (each dot has the other); line 2, \( \exists y\, (y \ne y) \), false (no dot differs from itself).
   - *A buried quantifier.* Two dots \( 0 \), \( 1 \); the label \( P \) at \( 1 \), the label \( Q \) at \( 0 \); the constant \( c \) names \( 1 \). Caption line: \( \forall x\, P(x) \to Q(c) \) true, since \( \forall x\, P(x) \) fails at \( 0 \); \( P(c) \to Q(c) \) false, since \( 1 \) has \( P \) and not \( Q \).
   - *Some occurrences only.* Two dots \( 1 \), \( 2 \), the numbers themselves, with \( x \) pointing at \( 1 \). Caption line: \( \forall x\, (x \le x^2 \vee x < 1) \) true at both; the half-replaced \( 2 \le x^2 \vee x < 1 \) false when \( x \) names \( 1 \).

   Figure caption: "Three tiny worlds. In each, the premise is true and the faulty line false." Lead sentence before it: "Each error has a reading, a small one, in which the premise is true and the faulty line false." (The worlds are the readings of 03:199-219, made finite; the text's \( \nN \) and \( \nR \) readings stay.) The warning 03:213-215 kept.
8. `## A stall`: 03:223-229 kept.
9. **Counter-readings (new paragraph, bold lead-in, ~130 words; at the end of "A stall"; the chapter's one explanation, convention 11).** "**Counter-readings.** Each error above was shown wrong by a reading, a domain with a meaning for every symbol, in which the premises are true and the line is false. Call such a reading a **counter-reading**. A counter-reading shows that a step is unsafe. It is also how this book shows that a sequent has no derivation at all: a search that stalls proves nothing, since a cleverer derivation might exist. Section 4.11 makes readings exact, under the name of models, and states that a counter-reading rules out every derivation. Until then, when this chapter says that something does not follow, it gives a counter-reading, and it never treats a stalled search as a proof."
10. Rule card (replaces 03:231-239): lead sentence (convention 6), the row ∀E, 03:239's sentence kept.
11. Search method (03:241-247): kept, and one sentence added (STYLE §12.5): "In the Givens/Goal table, \( \rulename{\forall E} \) adds an instance \( \varphi[t/x] \) to the Givens, with \( t \) read off the goal."

**Folds.** F4.3-a `title="A quantifier that binds nothing"`: 03:49. F4.3-b `title="What an arith line stands for"`: 03:187 from "Written out in full" and 03:191.

**Cut outright:** clauses 1–5 (03:41-47; replaced by bullets and two sentences); 03:55's last sentence.

**Quick checks:** instances of \( x + 0 = x \) (new), terms for \( \forall x\, \exists z\, (z > x + y) \) (kept): two in ~3,000 words, plus Figure C3 and the checking routine.

**Exercises.** A1, B1, B2, B3, C1 kept. **C2** (`exr-universal-elimination-c2`) keeps (a) and (b); (c) moves to 4.4 (`exr-universal-introduction-b4`), and with it the third and fourth marking lines and the second fatal error. New marking scheme (10 points): 6 for (a), the derivation with each of the five conditions checked (the four of the bullets and availability), including that \( x \) is free for \( x \); 4 for (b), a reading with \( P(x) \) true and \( \forall x\, P(x) \) false, with the value of \( x \) stated. Fatal error kept: treating \( P(x) \) and \( P(x_0) \) as the same line. The solution's (c) paragraph (03:464-466) moves with the part. New:
- **A2: Drill** (`exr-universal-elimination-a2`):
  (a) Line 1 is \( \forall x\, (x^2 \ge 0) \). Write its instance at \( a + 1 \). — \( (a + 1)^2 \ge 0 \).
  (b) Line 1 is \( \forall x\, \forall y\, (x + y = y + x) \). What does one \( \rulename{\forall E} \) at \( 2 \) give? — \( \forall y\, (2 + y = y + 2) \): the outer quantifier only.
  (c) Line 1 is \( \forall x\, P(x) \wedge Q(c) \). May \( \rulename{\forall E} \) cite it? — No: its main connective is \( \wedge \); \( \rulename{\wedge E} \) first gives \( \forall x\, P(x) \).
  (d) Line 1 is \( \forall x\, R(x, x) \). Is \( R(c, d) \) an instance? — No: every free \( x \) gets the same term, so the instances are \( R(t, t) \).
  (e) Line 1 is \( \forall x\, \exists y\, (y > x) \). Is \( \rulename{\forall E} \) at the term \( y \) legal? — No: \( y \) would be captured by \( \exists y \); rename first, and get \( \exists z\, (z > y) \).
  (f) Same line: is \( \rulename{\forall E} \) at \( x + 1 \) legal, and what does it give? — Yes: \( \exists y\, (y > x + 1) \); the only quantifier inside is on \( y \), which is not in \( x + 1 \).
  (g) Line 1 is \( \forall x\, (P(x) \to Q(f(x))) \). Its instance at \( f(c) \)? — \( P(f(c)) \to Q(f(f(c))) \).
  (h) Derive \( \forall x\, (P(x) \wedge Q(x)) \vdash Q(a) \). — 2 \( P(a) \wedge Q(a) \) ∀E 1; 3 \( Q(a) \) ∧E 2.
  (i) Derive \( \forall x\, (P(x) \to Q(x)), \ \forall x\, P(x) \vdash Q(c) \). — 3 \( P(c) \to Q(c) \) ∀E 1; 4 \( P(c) \) ∀E 2; 5 \( Q(c) \) →E 3, 4.
  (j) Derive \( \forall x\, \forall y\, R(x, y) \vdash R(a, b) \wedge R(b, a) \). — 2 \( \forall y\, R(a, y) \) ∀E 1; 3 \( R(a, b) \) ∀E 2; 4 \( \forall y\, R(b, y) \) ∀E 1; 5 \( R(b, a) \) ∀E 4; 6 ∧I 3, 5.
- **B4** (`exr-universal-elimination-b4`, new, scaffolded), `[B4: Read the terms off the goal]`: "A search for \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to R(x)), \ \forall x\, P(x) \vdash R(c) \wedge Q(c) \) has reached the stage below. *Name the move, then complete it.*" Shown: lines 1–3 premises, a gap, line 9 \( R(c) \wedge Q(c) \) with "?". Answer: the move is *instantiate at the term you need*: the goal names \( c \), so every \( \rulename{\forall E} \) is at \( c \); \( \rulename{\wedge I} \) splits the goal into \( R(c) \) and \( Q(c) \), and each is the end of a chain of →E: 4 \( P(c) \) ∀E 3; 5 \( P(c) \to Q(c) \) ∀E 1; 6 \( Q(c) \) →E 5, 4; 7 \( Q(c) \to R(c) \) ∀E 2; 8 \( R(c) \) →E 7, 6; 9 ∧I 8, 6.

**Sidecars:** `def-rule-universal-elimination.py` gains the three worlds of Figure C3 (finite checks). Drills: school arithmetic only.

### 4.4 Section 4.4: Proving "For Every": Let x Be Arbitrary (`04-universal-introduction.md`)

**Budget:** main line ≤ 3,800 words (now 3,861); folds ≤ 700. Looking ahead: "Chapter 5 collects the errors of this section, with others, in a catalogue of steps a proof may not take." (04:369's pointer, moved; STATUS row F1.4 §04, (N1).)

**New order of material.**
1. Opening (04:3) and `## One number we know nothing about` (04:5-17): kept (04:13 relies on Chapter 1's Looking-ahead box, which is delivered).
2. `## The flagged box`: slogan 04:21, 04:23, `def-rules-universal` verbatim, 04:55 ("In words …") kept.
3. `### A first flagged box: how the rule looks in a mathematical proof` **(moved up; the plan's "first concrete flagged box right after the schema")**: the derivation of 04:341-354 (lead "Here is the opening proof as a derivation, …"), its table 04:356-361 and 04:363 (kept: ch05 04:179 relies on "the prose uses the same letter for the flag and the bound variable"), with **two snapshots** before it (the first flagged box the reader sees; not exempted under (ii)): S1: line 1; the box flagged \( x_0 \) opened, a gap; line 3 \( x_0^2 - 2 \cdot x_0 + 1 \ge 0 \) unjustified as the box's last line; line 4 \( \forall x\, (x^2 - 2 \cdot x + 1 \ge 0) \) unjustified. S2: line 2 \( (x_0 - 1)^2 \ge 0 \) written (∀E 1), a gap, line 3 still unjustified, line 4. One sentence between them: "The goal is universal, so the box opens first, with the goal's instance at \( x_0 \) as its last line; then the premise is instantiated at the term that last line needs, \( x_0 - 1 \)." 04:365 ("let \( \varepsilon > 0 \)" asks something; Section 4.8's bounded rule) kept here. The old heading "How this rule looks in a mathematical proof" (04:339) is replaced by this subsection's title; at its old place nothing remains.
4. 04:59-81 (the two boxes side by side) kept; 04:83 kept up to "… whatever the box's first line is."; its last sentence (the range convention) → item 8.
5. *"This rule has conditions that matter; read each one."*, then 04:85-90 (the flag, the two clauses, the conclusion clause, the last line) and 04:92 ("appear") kept. 04:94 ("Fresh is not the same as new") → fold F4.4-a. In its place **the practical rule (new, ~60 words):** "**In practice:** choose as flag a letter written nowhere in the derivation so far, and when the box closes, put \( x \) in place of **every** occurrence of the flag in its last line. Then all three clauses hold at once: no premise or open assumption can contain a letter written nowhere, and the conclusion no longer contains the flag. The clauses are what a checker tests, and they allow a little more than this habit does (the fold below)." **Quick check (new):** "A derivation has used the letters \( x_0 \), \( y_0 \) and \( u_0 \) so far, and \( u_0 \) appears in an open assumption. Which flag can a new \( \rulename{\forall I} \) box take without checking anything?" Solution: any letter written nowhere yet, for example \( z_0 \). (\( x_0 \) or \( y_0 \) may also be allowed, but only after checking the three clauses; \( u_0 \) is not, while its assumption is open.)
6. `### Why each clause` (04:96-155): "A name in a premise" (04:98-113) kept. "A name in an open assumption" (04:115-136) **replaced** by the minimal derivation (~90 words of prose):
   ```
   1 | x0 > 0                   assumption
     | [x0]
   2 | | x0 > 0                 R 1
   3 | ∀x (x > 0)               ∀I 2–2      ← rejected
   4 x0 > 0 → ∀x (x > 0)        →I 1–3
   ```
   (an `nd` block marked `% expect-invalid: line 3 generalizes over x_0 while the assumption x_0 > 0 on line 1 is open`; `check_fitch.py` rejects exactly line 3, run when this file was written). Prose: line 3 breaks the second clause, since \( x_0 \) appears in the assumption of line 1, whose box is still open at line 3. Read over \( \nZ \) with \( x_0 \) naming \( 1 \): line 4 says "if \( 1 > 0 \), then every integer is positive", false at \( 0 \), and it rests on no premise at all. "This is the 'let \( x \) be a real number with \( x > 0 \) … since \( x \) was arbitrary' of the opening, made into lines. One more legal flagged box around everything turns line 4 into a false sentence; the fold shows it." The old derivation and its paragraph (04:115-136) → fold F4.4-b verbatim. "A name in the conclusion" (04:138-153) and 04:155 kept.
7. `## Derivations with flagged boxes`: 04:159 kept. `exm-universal-introduction-derivations` with **part (b) replaced** (S2a 1): "(b) \( \forall x\, (P(x) \to Q(x)), \ \forall x\, P(x) \vdash \forall x\, Q(x) \)." The statement's lead becomes "Give a derivation of each sequent." Solutions:
   - (a): 04:174-189 kept, with **two snapshots** in its Idea: S1: line 1, the box flagged \( x_0 \) opened, a gap, line 3 \( R(x_0, x_0) \) unjustified, line 4 \( \forall x\, R(x, x) \) unjustified. S2: line 2 \( \forall y\, R(x_0, y) \) written (∀E 1), line 3 still unjustified, line 4.
   - (b) **new**: *Idea.* The goal is universal: a box flagged \( x_0 \), whose last line must be \( Q(x_0) \). Both premises are universal; instantiate each at the term the box's goal names, \( x_0 \), and \( \rulename{{\to}E} \) finishes. Then a **Givens/Goal table** (the section's one table; convention 5):

     | Givens | Goal |
     |---|---|
     | \( \forall x\, (P(x) \to Q(x)) \), \( \forall x\, P(x) \) | \( \forall x\, Q(x) \) |
     | the same, and the fresh name \( x_0 \) (\( \rulename{\forall I} \) opens a box) | \( Q(x_0) \) |
     | + \( P(x_0) \to Q(x_0) \), \( P(x_0) \) (\( \rulename{\forall E} \) at \( x_0 \), twice) | \( Q(x_0) \) |
     | + \( Q(x_0) \) (\( \rulename{{\to}E} \)) | \( Q(x_0) \) ✓ |

     Two snapshots: S1: lines 1–2, the box flagged \( x_0 \) opened, a gap, line 5 \( Q(x_0) \) unjustified, line 6 \( \forall x\, Q(x) \) unjustified. S2: lines 3 \( P(x_0) \to Q(x_0) \) (∀E 1) and 4 \( P(x_0) \) (∀E 2) written, line 5 unjustified, line 6. The derivation: 1 \( \forall x\, (P(x) \to Q(x)) \); 2 \( \forall x\, P(x) \); box \( x_0 \): 3 \( P(x_0) \to Q(x_0) \) ∀E 1; 4 \( P(x_0) \) ∀E 2; 5 \( Q(x_0) \) →E 3, 4; 6 \( \forall x\, Q(x) \) ∀I 3–5. Then one sentence: at line 6, \( x_0 \) appears in neither premise nor in \( \forall x\, Q(x) \), and no box is open.
   - (c): 04:216-236 kept, except 04:234's "following the convention after @def-rules-universal" → "following the convention for a flagged box that immediately contains another box (the fine print below)", since that convention moves after the examples (item 9); with **two snapshots** in its Idea: S1: line 1, the box flagged \( y_0 \) opened, inside it the box flagged \( x_0 \) opened, a gap, line 3 \( R(x_0, y_0) \) unjustified, line 4 \( \forall x\, R(x, y_0) \) unjustified, line 5 \( \forall y\, \forall x\, R(x, y) \) unjustified. S2: line 2 \( \forall y\, R(x_0, y) \) written (∀E 1), line 3 still unjustified, lines 4–5. 04:236 (any formula \( \psi \); two adjacent universals swap) kept on the main line (4.8 C2 and 4.10 cite it).
   - Old (b) (04:191-214, the front renaming, its schema blocks and paragraph) → fold F4.4-c, placed after the example, with its lead "(b) *Idea.* This is the renaming …" turned into "**The front renaming, derived.** Section 4.2 took renaming of a bound variable as a convention and promised to derive it at the front of a formula. For a formula \( \varphi \) and variables \( y \), \( z \) with \( z \) not appearing in \( \varphi \), \( \forall y\, \varphi \dashv\vdash \forall z\, \varphi[z/y] \):", then 04:193-214 verbatim.
8. `prp-forall-and` (04:239-298): statement, Idea and proof verbatim; the Idea gains **two snapshots for each derivation**. (⊢): S1: line 1; the box flagged \( x_0 \) with a gap and line 3 \( P(x_0) \) unjustified; line 4 \( \forall x\, P(x) \) unjustified; a second box flagged \( x_0 \) with a gap and line 6 \( Q(x_0) \) unjustified; line 7 \( \forall x\, Q(x) \) unjustified; line 8 the goal, ∧I 4, 7. S2: lines 2 and 5 (∀E 1 in each box) written, lines 3 and 6 still unjustified. (⊣): S1: line 1; lines 2–3 by ∧E written (the premise taken apart first); the box flagged \( x_0 \), a gap, line 6 \( P(x_0) \wedge Q(x_0) \) unjustified; line 7 unjustified. S2: lines 4 \( P(x_0) \) (∀E 2) and 5 \( Q(x_0) \) (∀E 3) written, line 6 still unjustified, line 7. 04:298 kept.
9. **Fine print (moved here; bold lead-in "**Fine print: flagged boxes in a derivation.**")**: 04:57 verbatim (the extension of @def-derivation to flagged boxes; a definition the main line uses, so it stays on the main line), then 04:83's last sentence (the range convention: a flagged box that immediately contains another box is cited from that inner box's first line), then one new sentence: "Derivation (c) above and Exercise B1 below use the convention."
10. `## Every element of the empty set` (04:300-337, id kept): 04:302-317 kept, with **two snapshots** for the first derivation: S1: line 1, the box flagged \( x_0 \), a gap, line 3 \( x_0 \in A \to x_0 > 5 \) unjustified, line 4 unjustified. S2: line 2 \( \neg(x_0 \in A) \) written (∀E 1), line 3 still unjustified, line 4. 04:319 **cut to two sentences** on the main line: "Line 3 uses VI (@prp-vacuous-implication) as one line, with the formulas \( x_0 \in A \) and \( x_0 > 5 \) for \( P \) and \( Q \); every derived rule of Chapter 2 may be used in this way on first-order formulas. Nothing in the derivation used \( x > 5 \): with any formula in place of \( x > 5 \) in which \( x_0 \) does not appear, the same four lines go through, so 'every element of an empty set has property \( \varphi \)' is derivable for every \( \varphi \), as Section 4.1 said." The justification of the VI step (04:319, from "This is allowed because" to "on first-order formulas.") → fold F4.4-d. Then 04:319's last sentence ("One more flagged box …"), the second derivation (exempt (iii): the first one's shape inside one more flagged box) and 04:337 kept (ch05 01:172 relies on it).
11. `## Common errors`: 04:369 without "The first of them opens Chapter 5's catalogue of steps that are not allowed." (→ Looking ahead); the three bullets 04:371-373 kept (the second points to the minimal derivation of item 6); warning 04:375-377 kept; Quick check 04:379-401 kept.
12. `## A foreshadowing` (04:403-409) kept.
13. Rule card (replaces 04:411-420): lead sentence, rows ∀E, ∀I; 04:420's sentence kept. One sentence (STYLE §12.5): "In the Givens/Goal table, \( \rulename{\forall I} \) puts a fresh name among the Givens and makes \( \varphi[x_0/x] \) the goal."
14. Search method (04:422-426) kept.
15. Looking ahead (as above).

**Folds.** F4.4-a `title="Fresh is not the same as new"`: 04:94 verbatim. F4.4-b `title="The same error, as a false sentence"`: 04:115-136 verbatim (lead changed to "With one more flagged box, the error of the minimal derivation becomes a false **sentence**:"). F4.4-c `title="The front renaming, derived"`: old (b), as in item 7. F4.4-d `title="Why a derived rule may stand in a flagged box"`: the middle of 04:319 as in item 10.

**Cut outright:** 04:369's pointer. (Everything else moves or stays.)

**Quick checks:** the free flag (new), the \( y_0 \) premise (kept): two in ~3,800 words, plus a Givens/Goal table and eleven snapshots' worth of partial derivations.

**Exercises.** A1 kept except **D3**, which duplicated the main line's new minimal derivation; D3 becomes (`% expect-invalid`):
   ```
   1 | R(x0, c)                    assumption
     | [x0]
   2 | | R(x0, c)                  R 1
   3 | ∀x R(x, c)                  ∀I 2–2
   4 R(x0, c) → ∀x R(x, c)         →I 1–3
   ```
   and its answer in (b): "*D3:* not legal. At line 3 the assumption \( R(x_0, c) \) on line 1 is still open, and \( x_0 \) appears in it (the second clause). Line 4, which closes the box legally, then says 'if \( x_0 \) is below \( c \), everything is below \( c \)': false over \( \nZ \) with \( R \) read as \( < \), \( c \) as \( 5 \) and \( x_0 \) as \( 1 \)." (`check_fitch.py` rejects exactly line 3.) B2 frozen; B3, C1, C2 kept (C2(c)'s parenthesis "(Section 4.11 states, and the optional Section 4.12 proves, …)" → "(A legal step never leads from true premises to a false conclusion; Section 4.11 states this.)"). Changed and new:
- **B1** (`exr-universal-introduction-b1`), recast as the section's scaffolded item, `[B1: A chain, for every x]`: "A search for \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to R(x)) \vdash \forall x\, (P(x) \to R(x)) \) has reached the stage below. *Name the move, then complete it, and check the side condition at line 9.*" Shown: lines 1–2; the box flagged \( x_0 \); inside it the box of line 3 \( P(x_0) \); a gap; line 8 \( P(x_0) \to R(x_0) \) with "?"; line 9 \( \forall x\, (P(x) \to R(x)) \) with "?". Answer: the moves are *let \( x \) be arbitrary* and then the →I box; inside, instantiate both premises at \( x_0 \) and fire twice. The derivation and the paragraph of 04:522-544, unchanged.
- **A2: Drill** (`exr-universal-introduction-a2`):
  (a) What does opening a flagged box say, in the words of a proof? — "Let \( x_0 \) be arbitrary."
  (b) A box flagged \( x_0 \) ends in \( P(x_0) \wedge Q(x_0) \), and \( x_0 \) is in no premise and no open assumption. Which line may \( \rulename{\forall I} \) write? — \( \forall x\, (P(x) \wedge Q(x)) \).
  (c) The premise is \( R(x_0) \). May a box flagged \( x_0 \) that ends in \( R(x_0) \) be closed with \( \forall x\, R(x) \)? — No: \( x_0 \) appears in a premise.
  (d) May a flag be the constant \( c \)? — No: a flag is always a variable.
  (e) A box flagged \( y_0 \) ends in \( y_0 \le y_0 \). Is \( \forall x\, (x \le y_0) \) a legal \( \rulename{\forall I} \) line? — No: \( y_0 \) appears in the conclusion.
  (f) Inside the box of an assumption \( Q(x_0) \), a box flagged \( x_0 \) ends in \( Q(x_0) \). May \( \rulename{\forall I} \) close it? — No: \( x_0 \) appears in an open assumption.
  (g) Derive \( \forall x\, P(x) \vdash \forall y\, P(y) \). — box \( y_0 \): 2 \( P(y_0) \) ∀E 1; 3 \( \forall y\, P(y) \) ∀I 2–2.
  (h) Derive \( \forall x\, (P(x) \wedge Q(x)) \vdash \forall x\, Q(x) \). — box \( x_0 \): 2 \( P(x_0) \wedge Q(x_0) \) ∀E 1; 3 \( Q(x_0) \) ∧E 2; 4 ∀I 2–3.
  (i) Derive \( \forall x\, P(x), \ \forall x\, Q(x) \vdash \forall x\, (Q(x) \wedge P(x)) \). — box \( x_0 \): 3 \( Q(x_0) \) ∀E 2; 4 \( P(x_0) \) ∀E 1; 5 ∧I 3, 4; 6 ∀I 3–5.
  (j) Derive \( \vdash \forall x\, (P(x) \to P(x)) \). — box \( x_0 \), inside it the box of 1 \( P(x_0) \); 2 \( P(x_0) \to P(x_0) \) →I 1–1; 3 \( \forall x\, (P(x) \to P(x)) \) ∀I 1–2 (the flagged box immediately contains the →I box, so it is cited from line 1).
- **B4** (`exr-universal-introduction-b4`, new; old 4.3 C2(c), now that ∀I is known), `[B4: Back to the stall of Section 4.3]`: "(a) Derive \( \forall x\, P(x) \vdash \forall x\, P(x) \) with \( \rulename{\forall E} \) and \( \rulename{\forall I} \), not \( \rulename{R} \). Why can the flagged box not be flagged \( x \)? (b) Explain why no flag at all gives a derivation of \( P(x) \vdash \forall x\, P(x) \) by this route, and give a counter-reading to the sequent." Answer: (a) box \( x_0 \): 2 \( P(x_0) \) ∀E 1; 3 \( \forall x\, P(x) \) ∀I 2–2; with the flag \( x \), the conclusion \( \forall x\, P(x) \) contains \( x \) (the letter after the quantifier counts: that is what "appear" means), so the third clause fails whatever else holds. (b) The text of 03:466 adapted: with the flag \( x \), \( x \) appears in the premise and in the conclusion; with any other flag \( x_0 \), the box needs the line \( P(x_0) \), and nothing gives it, since the premise is about \( x \). A stalled search proves nothing by itself; the counter-reading settles it: over \( \nZ \), \( P \) read as "even" and \( x \) naming \( 2 \), the premise is true and \( \forall x\, P(x) \) false (Section 4.11 makes this a counter-model). Marking scheme (10 points): 3 the derivation of (a); 3 the flag \( x \) fails "not in the conclusion", with the reason; 2 (b) both cases of the flag; 2 the counter-reading with the value of \( x \). Fatal errors: claiming the flag \( x \) is fine because \( x \) is bound in the conclusion; treating \( P(x) \) and \( P(x_0) \) as the same line.

**Sidecars:** `def-rules-universal.py` gains the minimal derivation's reading (\( 1 > 0 \), \( 0 > 0 \) fails) and D3's (\( 1 < 5 \), \( 6 < 5 \) fails).

### 4.5 Section 4.5: Proving "There Exists": Exhibit a Witness (`05-existential-introduction.md`)

**Budget:** main line ≤ 3,100 words (now 3,090); folds ≤ 200. No Looking-ahead box.

**Changes, in the file's order.**
1. 05:3-17 kept.
2. The rule: slogan 05:21 and `def-rule-existential-introduction` verbatim. "In words, clause by clause" and clauses 1–5 (05:39-45) **replaced** by three bullets (convention 3):
   - **Schema:** the block above: one cited line, no box, no fresh name.
   - **Reading:** from a line that says something about the term \( t \), write "something has that property": mark some occurrences of \( t \) with a variable \( x \) to get \( \varphi \), and write \( \exists x\, \varphi \).
   - **Example:** from \( 6 = 2 \cdot 3 \), marking the \( 3 \) gives \( \exists k\, (6 = 2 \cdot k) \).

   Then one paragraph (~100 words; clauses 3, 4 and 5 compressed): "**Which occurrences?** Any you like, as the table below shows; the term \( t \) is the **witness**, and it may be a constant, a compound term or a variable, a flag such as \( x_0 \) included. Check two things: \( \varphi[t/x] \) must be **exactly** the cited line (choose a variable \( x \) that does not appear in the line, and the marking recipe guarantees it), and \( t \) must be free for \( x \) in \( \varphi \), the condition of @def-free-for that \( \rulename{\forall E} \) also carries." One sentence on bounds (new): "With a bound, \( \exists x \in A\; \varphi \), the witness needs the line \( t \in A \) too; 'A bounded witness' below shows the two steps, and Section 4.8 makes them one."
3. The table 05:47-54 kept without its last row; 05:56 kept up to "Each is a true and weaker statement." The last row and the rest of 05:56 (the degenerate choice) → fold F4.5-a. 05:58 kept without its last sentence ("Section 4.12 turns this sentence into a proof."). 05:60 kept. Capture nonexample 05:62-74, warning 05:76-78, Quick check 05:80-90 kept.
4. `## From "for every" to "there exists"`: kept (05:94-122). 05:124 (the bounded empty-set case) → fold F4.5-b.
5. `## An existential goal: postpone the witness`: 05:128-134 kept. **Quick check (new)**, after the slogan 05:132: "Premises: \( \forall x\, (P(x) \to Q(x + 1)) \) and \( P(2) \). The goal is \( \exists y\, Q(y) \). Which witness will the search find, and after which steps?" Solution: the term \( 2 + 1 \): \( \rulename{\forall E} \) at \( 2 \) gives \( P(2) \to Q(2 + 1) \), \( \rulename{{\to}E} \) gives \( Q(2 + 1) \), and only then does \( \rulename{\exists I} \) have an instance to cite. (The witness is the term \( 2 + 1 \); a proof may also write it as \( 3 \) by an arith line.)
6. `exm-existential-introduction-derivations`: statement and solutions verbatim, with snapshots (convention 4): (a) is exempt (i) (two lines). (b): S1: line 1, a gap, line 4 \( \exists x\, R(x, c) \wedge \exists x\, R(x, x) \) unjustified. S2: lines 2 and 3 unjustified as the two subgoals (∧I splits the goal), line 4 ∧I 2, 3. (c): S1: line 1, the box flagged \( x_0 \), a gap, line 3 \( \exists y\, R(x_0, y) \) unjustified (the postponed goal), line 4 unjustified. S2: line 2 \( R(x_0, x_0) \) written (∀E 1), line 3 still unjustified (its instance now stands on line 2, with the witness \( x_0 \)), line 4. (d): S1: lines 1–2, a gap, line 5 \( \exists y\, Q(y) \) unjustified (postponed). S2: lines 3 \( P(c) \to Q(f(c)) \) (∀E 1) and 4 \( Q(f(c)) \) (→E 3, 2) written, line 5 unjustified, the witness now visible. And the section's **Givens/Goal table**, in (d)'s Idea (convention 5):

   | Givens | Goal |
   |---|---|
   | \( \forall x\, (P(x) \to Q(f(x))) \), \( P(c) \) | \( \exists y\, Q(y) \): postponed, no instance yet |
   | + \( P(c) \to Q(f(c)) \) (\( \rulename{\forall E} \) at \( c \)) | \( \exists y\, Q(y) \) |
   | + \( Q(f(c)) \) (\( \rulename{{\to}E} \)) | \( \exists y\, Q(y) \) ✓ by \( \rulename{\exists I} \), witness \( f(c) \) |

   05:214 kept.
7. How this rule looks (05:216-250): kept; both derivations exempt (ii) (each writes out the sentence above it).
8. Rule card (replaces 05:252-260): lead sentence, rows ∀E, ∀I, ∃I; 05:254's "nothing later depends on the last column" and 05:260 kept. One sentence (STYLE §12.5): "In the Givens/Goal table, \( \rulename{\exists I} \) ticks off the goal \( \exists x\, \varphi \) once a Given is an instance \( \varphi[t/x] \); until then the goal row waits."
9. Search method (05:262-264): kept.

**Folds.** F4.5-a `title="A witness that is not marked"`: the last table row and 05:56 from "The last row is the **degenerate** choice". F4.5-b `title="The empty set, again"`: 05:124 verbatim.

**Cut outright:** clauses 1–5 (05:39-45; replaced); 05:58's last sentence.

**Quick checks:** three readings of \( 2 + 2 = 4 \) (kept), the witness \( 2 + 1 \) (new): two in ~3,100 words, plus the table and a Givens/Goal table.

**Exercises.** A1, B2, B3 kept; C1, C2 frozen. Changed and new:
- **B1** (`exr-existential-introduction-b1`), recast as the scaffolded item, `[B1: Postpone, then choose]`: "A search for \( \forall x\, (P(x) \to Q(x)), \ P(a) \vdash \exists x\, (P(x) \wedge Q(x)) \) has reached the stage below. *Name the move, then complete it, saying for each line whether the goal or a premise chose it.*" Shown: lines 1–2, a gap, line 6 \( \exists x\, (P(x) \wedge Q(x)) \) with "?". Answer: the move is *postpone the witness*; the solution 05:304-319 unchanged.
- **A2: Drill** (`exr-existential-introduction-a2`):
  (a) Line 1 is \( 3 + 4 = 7 \). Name \( \varphi \) and \( t \) so that \( \rulename{\exists I} \) gives \( \exists x\, (x + 4 = 7) \). — \( \varphi = (x + 4 = 7) \), \( t = 3 \).
  (b) Line 1 is \( R(c, c) \). Which of \( \exists x\, R(x, c) \), \( \exists x\, R(c, x) \), \( \exists x\, R(x, y) \) can one \( \rulename{\exists I} \) **not** give? — \( \exists x\, R(x, y) \): its instances \( R(t, y) \) have \( y \) in the second place, and line 1 has \( c \).
  (c) Line 1 is \( P(f(c)) \). Give two different \( \rulename{\exists I} \) conclusions. — \( \exists x\, P(x) \) (witness \( f(c) \)) and \( \exists x\, P(f(x)) \) (witness \( c \)).
  (d) Line 1 is \( \forall y\, (y = y) \). Is \( \exists x\, \forall y\, (x = y) \) a legal \( \rulename{\exists I} \) line? — No: the witness would be \( y \), which \( \forall y \) captures. Over \( \nZ \) line 1 is true and the other line, "some integer equals every integer", false.
  (e) True or false: \( \rulename{\exists I} \) may cite \( \exists x\, P(x) \) and write \( P(c) \). — False: it goes from an instance to an existential, never back.
  (f) Premises \( P(a) \), \( Q(b) \); goal \( \exists x\, (P(x) \wedge Q(x)) \). Should a witness be chosen now? — No: neither \( a \) nor \( b \) has both properties on a line; in fact a counter-reading exists (\( D = \{a, b\} \), \( P \) true of \( a \) only, \( Q \) of \( b \) only).
  (g) Derive \( P(c) \vdash \exists x\, (P(x) \vee Q(x)) \). — 2 \( P(c) \vee Q(c) \) ∨I 1; 3 ∃I 2.
  (h) Derive \( \forall x\, P(x) \vdash \exists x\, P(f(x)) \). — 2 \( P(f(x)) \) ∀E 1 (at the term \( f(x) \)); 3 \( \exists x\, P(f(x)) \) ∃I 2 (with \( \varphi = P(f(x)) \) and the witness \( x \)).

**Sidecars:** none new (drills: school arithmetic; (d) and (f) are finite or school readings).

### 4.6 Section 4.6: Using "There Exists": Name a Witness (`06-existential-elimination.md`)

**Budget:** main line ≤ 4,950 words (now 4,847; about 520 folded or cut, about 600 new); folds ≤ 650. No Looking-ahead box.

**New order of material.**
1. Opening (06:3) kept.
2. `## Using a witness whose identity is unknown`: 06:7-20 kept.
3. `## The rule of existential elimination`: slogan 06:24, `def-rules-existential` verbatim, 06:59 kept. Then **the core wording (new, ~70 words; bold lead-in):** "**In practice**, two habits make every clause of the side condition hold: name the witness with a brand-new letter, written nowhere in the derivation so far, and make sure the box's last line does not mention it. The four clauses below are the official test, the one a checker runs." Then *"This rule has conditions that matter; read each one."* (replacing 06:61's "Read the rule clause by clause.") and clauses 1–6 (06:63-68) kept; in clause 3, "The derivation after this list shows the damage." → "The subsection 'Three ways to break the rule' below shows the damage." 06:70 moves with the counterexamples (item 6).
4. `### A first witness: \( n + 2 \) is even` **(new, ~150 words of prose and a table; the plan's "the n + 2 derivation with a prose table")**. Lead: "Here is the proof of 06:9 as a derivation, over \( \nZ \), with '\( n \) is even' written \( \exists k\, (n = 2 \cdot k) \) and the computation as one line justified 'arith' (Section 4.3)." Two snapshots (the first \( \rulename{\exists E} \) box the reader sees; not exempted under (ii)): S1: line 1; the box flagged \( k_0 \) opened with its assumption, line 2 \( n = 2 \cdot k_0 \); a gap; line 4 \( \exists k\, (n + 2 = 2 \cdot k) \) unjustified as the box's last line; line 5 \( \exists k\, (n + 2 = 2 \cdot k) \) unjustified. S2: line 3 \( n + 2 = 2 \cdot (k_0 + 1) \) written (arith 2), line 4 still unjustified, line 5. One sentence between them: "The premise is an existential, so its box opens first, aimed at the goal; the goal is postponed until a line shows its witness." The derivation (`check_fitch.py` accepts it):
   ```
   1 ∃k (n = 2·k)                  premise
     | [k0]
   2 | n = 2·k0                    assumption
   3 | n + 2 = 2·(k0 + 1)          arith 2
   4 | ∃k (n + 2 = 2·k)            ∃I 3
   5 ∃k (n + 2 = 2·k)              ∃E 1, 2–4
   ```
   Then the side condition at line 5 in one sentence (\( k_0 \) is not in line 4, not in the existential of line 1, which is also the only premise, and no box is open), and the prose table:

   | Line | Sentence |
   |---|---|
   | 1 | "Since \( n \) is even, …" |
   | box \( k_0 \), 2 | "… choose an integer \( k \) with \( n = 2k \)." |
   | 3 | "Then \( n + 2 = 2k + 2 = 2(k + 1) \), …" (arith) |
   | 4 | "… so \( n + 2 \) is even." (\( \rulename{\exists I} \), the witness \( k + 1 \)) |
   | 5 | (unwritten: the conclusion does not mention \( k \), so the box closes) |

   **Quick check (new):** "Could line 5 have been \( n + 2 = 2 \cdot (k_0 + 1) \), closing the box one line earlier?" Solution: no: that line mentions the witness \( k_0 \), which breaks clause 3. Outside the box \( k_0 \) names nothing; \( \rulename{\exists I} \) must forget it first, as line 4 does.
5. `## Using an existential: open the box early`: 06:158 and the slogan 06:160 kept. 06:162 ("Why early?") cut to two sentences on the main line: "Opening early keeps every resource, since every line available before the box is available inside it; and a box aimed at the current goal can always be closed once the goal is reached, since its name was chosen fresh. What the early box gives is the witness's name, often exactly the term a postponed \( \exists \) goal is waiting for." (The wording keeps the S3 deviation of `ch04.md`: no claim that opening early 'loses nothing'.) The rest of 06:162 (the safety argument and the caution about \( \rulename{\forall I} \) flags) → fold F4.6-b. 06:164 and `prp-exists-and` (statement, Idea, proof verbatim), with **two snapshots** in its Idea: S1: line 1; the box flagged \( x_0 \) with line 2 \( P(x_0) \wedge Q(x_0) \); a gap; line 7 \( \exists x\, P(x) \wedge \exists x\, Q(x) \) unjustified; line 8 unjustified. S2: lines 3 \( P(x_0) \) and 5 \( Q(x_0) \) written (∧E 2), lines 4 \( \exists x\, P(x) \) and 6 \( \exists x\, Q(x) \) unjustified (the two subgoals ∧I asks for), line 7 ∧I 4, 6, line 8. 06:199 kept. Quick check 06:201-207 kept, its last sentence → "It must: over \( \nZ \), with \( P \) as 'even' and \( Q \) as 'odd', the premise is true and the conclusion, 'some integer is both even and odd', is false. That is a counter-reading, and Section 4.11 shows that a counter-reading rules out every derivation."
6. `## Three ways to break the rule` **(moved here; 06:70-131)**: 06:70 (lead) and the three counterexamples for clauses 3, 4 and 5, verbatim, each followed by its panel of **Figure C6 (new TikZ; three counter-worlds, side by side)**:
   - *Clause 3.* Two dots \( 0 \) and \( 6 \); the label "\( > 5 \)" at \( 6 \). Caption line: the premise \( \exists x\, (x > 5) \) is true (at \( 6 \)); the line \( \forall x\, (x > 5) \) is false (at \( 0 \)).
   - *Clause 4.* Two dots \( 1 \) and \( 2 \); the label \( P \) ("even") at \( 2 \); the variable \( x_0 \) points at \( 1 \). Caption line: both premises, \( \exists x\, P(x) \) and \( \neg P(x_0) \), are true; the line \( \bot \) is false, as always.
   - *Clause 5.* Three dots \( a \), \( b \), \( c \) in a triangle, with arrows \( a \to b \), \( b \to c \), \( c \to a \) (an arrow from \( u \) to \( v \) means \( R(u, v) \)). Caption line: the premise \( \forall y\, \exists x\, R(x, y) \) is true (every dot has an arrow into it); the line \( \exists z\, R(z, z) \) is false (no loops).

   Figure caption: "Three small worlds, one per clause: in each, the premises are true and the line that breaks the clause is false." (The text's readings over \( \nN \) and \( \nZ \) stay; the worlds are finite versions of them.) 06:131 and the warning 06:133-154 kept.
7. `exm-existential-elimination-derivations` (06:209-307): statement and solutions verbatim, with snapshots: (a) \( (\vdash) \): S1: line 1; the box flagged \( x_0 \) with line 2; a gap; line 9 \( \exists x\, P(x) \vee \exists x\, Q(x) \) unjustified; line 10 unjustified. S2: inside, the two case boxes opened (line 3 \( P(x_0) \), a gap, line 5 the goal unjustified; line 6 \( Q(x_0) \), a gap, line 8 the goal unjustified), line 9 ∨E 2, 3–5, 6–8, line 10. (a) \( (\dashv) \): S1: line 1; the case box of line 2 \( \exists x\, P(x) \) with a gap and line 6 the goal unjustified; the case box of line 7 with a gap and line 11 unjustified; line 12 ∨E 1, 2–6, 7–11. S2: inside each case box its \( \rulename{\exists E} \) box opened (lines 3, 8 the assumptions; lines 5, 10 the goal unjustified; lines 6, 11 ∃E). (b): S1: lines 1–2; the ¬I box of line 3 \( \forall x\, Q(x) \); a gap; line 9 \( \bot \) unjustified; line 10 ¬I 3–9. S2: inside, the box flagged \( x_0 \) with line 4 \( P(x_0) \), a gap, line 8 \( \bot \) unjustified, line 9 ∃E 1, 4–8.
8. `## Moving one quantifier past another`: 06:311 and `prp-exists-forall-swap` (key proof): statement and proof verbatim. Its Idea keeps ①②③ and the *Before reading on* prompt, and gains (between ③ and the prompt) a **Givens/Goal table** (the section's one table; convention 5):

   | Givens | Goal |
   |---|---|
   | \( \exists x\, \forall y\, R(x, y) \) | \( \forall y\, \exists x\, R(x, y) \) |
   | + the fresh name \( y_0 \) (fix: \( \rulename{\forall I} \) opens a box) | \( \exists x\, R(x, y_0) \): postponed |
   | + the witness \( x_0 \) and \( \forall y\, R(x_0, y) \) (obtain: \( \rulename{\exists E} \) opens a box) | \( \exists x\, R(x, y_0) \) |
   | + \( R(x_0, y_0) \) (\( \rulename{\forall E} \) at \( y_0 \)) | \( \exists x\, R(x, y_0) \) ✓ by \( \rulename{\exists I} \), the witness \( x_0 \) (choose) |

   and **two snapshots**: S1: line 1; the box flagged \( y_0 \) opened; a gap; line 5 \( \exists x\, R(x, y_0) \) unjustified; line 6 \( \forall y\, \exists x\, R(x, y) \) unjustified. S2: inside the box of \( y_0 \), the box flagged \( x_0 \) with line 2 \( \forall y\, R(x_0, y) \), a gap, line 4 \( \exists x\, R(x, y_0) \) unjustified, line 5 ∃E 1, 2–4, line 6. 06:358-360 kept. 06:362 → one sentence on the main line ("Nothing in the proof used that the formula is \( R(x, y) \): the same six lines derive \( \exists x\, \forall y\, \varphi \vdash \forall y\, \exists x\, \varphi \) for any formula \( \varphi \), which is the derivation promised in Section 4.1; the fold checks the substitutions.") and the rest verbatim → fold F4.6-c. "Either nesting works" (06:364-383) kept (exempt (iii); A1(b) asks about it). The converse (06:385-430) kept; 06:432's last two sentences → "A stalled search is not a proof that no derivation exists; a counter-reading is. Section 4.11 gives one on \( \nZ \)."
9. `## Renaming the bound variable of an existential` (06:434-467) → fold F4.6-a, verbatim, its heading a bold lead-in and its id on the fold (§1 item 1), placed after the converse; 06:436's "(@exm-universal-introduction-derivations (b))" → "(the fold after @exm-universal-introduction-derivations)", because part (b) of that example is replaced (§4.4 item 7).
10. `## Two witnesses`: 06:471 and `exm-sum-of-evens` verbatim (cited by ch05 06:37), with **two snapshots** in its Idea: S1: lines 1–2; the box flagged \( k_0 \) with line 3; a gap; line 7 \( \exists k\, (n + m = 2 \cdot k) \) unjustified; line 8 unjustified. S2: inside, the box flagged \( l_0 \) with line 4, a gap, line 6 unjustified, line 7 ∃E 2, 4–6, line 8. Quick check 06:509-515 kept.
11. `## How this rule looks in a mathematical proof` (06:517-576): kept (the bounded-sequence derivation is exempt (ii): "The sentences match the boxes"; ch05 05:444 relies on the definition of "bounded" here). The warning "Two witnesses, one name" kept.
12. **The Chapter 4 rule card (replaces 06:578-586; the plan's "Ch4 rule card after 4.6").** Heading `## The four quantifier rules on one card`. Lead: "Chapters 1 and 2's thirteen rules are on the card at the end of Section 2.6. Here are the four quantifier rules, with their side conditions." The card: rows ∀E, ∀I, ∃I, ∃E (convention 6). 06:586 ("The phrase 'choose' is apt and slightly misleading …") kept after it. Then **the decision chart, quantifier rows (new; the chart of 1.6 and 2.6 grown):**

    | Main symbol | As the goal (goal-directed) | As an available line (premise-directed) |
    |---|---|---|
    | \( \forall x\, \varphi \) | open a flagged box with a brand-new name \( x_0 \); its last line is \( \varphi[x_0/x] \); close with \( \rulename{\forall I} \) | instantiate at the term the goal, or another line, names (\( \rulename{\forall E} \)) |
    | \( \exists x\, \varphi \) | postpone; use \( \rulename{\exists I} \) once a line shows an instance \( \varphi[t/x] \) | open the \( \rulename{\exists E} \) box at once, with a brand-new witness name, aimed at the current goal |

    One sentence: "The connective rows are the table of moves in Section 2.6; Section 4.8 puts all of them into one method."
13. Search method (06:588-590): kept, and one sentence (STYLE §12.5): "In the Givens/Goal table, \( \rulename{\exists E} \) puts a witness among the Givens, its name and its assumption \( \varphi[x_0/x] \), and leaves the goal as it was."

**Folds.** F4.6-a (id `existential-renaming`) `title="Renaming the bound variable of an existential"`: 06:436-467 as in item 9. F4.6-b `title="Why opening early is safe"`: 06:162 from its third sentence ("And a box aimed at the current goal …") to its end. F4.6-c `title="The swap for any formula"`: 06:362 from its second sentence.

**Cut outright:** the first two sentences of 06:162 (replaced by the two new ones); 06:206's and 06:432's soundness clauses (reworded).

**Quick checks:** line 5 of the \( n + 2 \) derivation (new), the converse of `prp-exists-and` (kept), the second witness's name (kept): three in ~4,950 words, plus a Givens/Goal table, the decision chart and nine snapshots' worth of partial derivations.

**Exercises.** A1 (key proof), B1, B2 (faded, scaffolded; the faded triple's middle), B3, C1 kept; C2 frozen. New:
- **A2: Drill** (`exr-existential-elimination-a2`):
  (a) A line \( h \) is \( \exists x\, P(x) \). Write the first line of its \( \rulename{\exists E} \) box, with the name \( u_0 \). — The box flagged \( u_0 \), opening with the assumption \( P(u_0) \).
  (b) An \( \rulename{\exists E} \) box for \( \exists k\, (m = 2 \cdot k) \), named \( k_0 \), ends in \( m^2 = 4 \cdot k_0^2 \). May it close with that line? — No: the last line mentions \( k_0 \) (clause 3).
  (c) The premise is \( Q(x_0) \). May the box of \( \exists x\, P(x) \) be named \( x_0 \)? — No: \( x_0 \) appears in a premise (clause 4).
  (d) Premises \( \exists x\, P(x) \), \( \exists x\, Q(x) \). May both boxes be named \( x_0 \) if one is inside the other? — No: the inner box's name appears in the open assumption \( P(x_0) \) of the outer one.
  (e) May two boxes share a name if the first has closed before the second opens? — Yes, as in @exm-existential-elimination-derivations (a), \( (\dashv) \).
  (f) Inside an \( \rulename{\exists E} \) box with assumption \( P(x_0) \), may \( \rulename{\forall I} \) generalize over \( x_0 \)? — No: \( x_0 \) is in an open assumption; the witness is not arbitrary.
  (g) Derive \( \exists x\, (P(x) \wedge Q(x)) \vdash \exists x\, Q(x) \). — box \( x_0 \): 2 \( P(x_0) \wedge Q(x_0) \); 3 \( Q(x_0) \) ∧E 2; 4 \( \exists x\, Q(x) \) ∃I 3; 5 ∃E 1, 2–4.
  (h) Derive \( \exists x\, P(x), \ \forall x\, (P(x) \to Q(x)) \vdash \exists x\, Q(x) \). — box \( x_0 \): 3 \( P(x_0) \); 4 \( P(x_0) \to Q(x_0) \) ∀E 2; 5 \( Q(x_0) \) →E 4, 3; 6 \( \exists x\, Q(x) \) ∃I 5; 7 ∃E 1, 3–6.
  (i) Derive \( \exists x\, \exists y\, R(x, y) \vdash \exists y\, \exists x\, R(x, y) \). — box \( x_0 \): 2 \( \exists y\, R(x_0, y) \); box \( y_0 \): 3 \( R(x_0, y_0) \); 4 \( \exists x\, R(x, y_0) \) ∃I 3; 5 \( \exists y\, \exists x\, R(x, y) \) ∃I 4; 6 ∃E 2, 3–5; 7 ∃E 1, 2–6.
  (j) Find the illegal line: 1 \( \exists x\, P(x) \) premise; box \( x_0 \): 2 \( P(x_0) \) assumption; 3 \( P(x_0) \) ∃E 1, 2–2; 4 \( \exists y\, P(y) \) ∃I 3. — Line 3: its box's last line mentions \( x_0 \) (clause 3). (Line 4 would be legal; the conclusion is even true, but this derivation does not prove it.)

**Sidecars:** `def-rules-existential.py` gains the \( n + 2 \) arith line (\( 2k + 2 = 2(k + 1) \)) and the three worlds of Figure C6 (finite checks).

### 4.7 Section 4.7: Equality and Unique Existence (`07-equality-and-uniqueness.md`)

**Budget:** main line ≤ 3,900 words (now 5,011; about 1,350 folded or cut, about 250 new); folds ≤ 1,300. Looking ahead: "Chapter 5 turns the 'You write' column of this table into a full dictionary of proof phrases." (07:419's pointer, moved; STATUS row F1.4 §07.)

**Changes, in the file's order.**
1. 07:3-18 kept.
2. The rules: slogan 07:22, `def-rules-equality` verbatim, 07:45 kept. Then **mark the holes (new, ~120 words, bold lead-in; the plan's "=E introduced by boxing the occurrences to replace"):** "**Mark the holes first.** To use \( \rulename{{=}E} \) with \( t_1 = t_2 \), write down the line you have and draw a box round each occurrence of \( t_1 \) you want to replace. The boxes are the holes: \( \varphi \) is the line with a variable in each box, and the new line puts \( t_2 \) in every box. With \( a = b \):
   \[ \boxed{a} + \boxed{a} = 2 \cdot \boxed{a} \ \text{ gives } \ b + b = 2 \cdot b, \qquad \boxed{a} + a = 2 \cdot a \ \text{ gives } \ b + a = 2 \cdot a . \]
   Occurrences without a box stay as they are." Then "Read the definition clause by clause." with clause 1 (07:49) **replaced** by three bullets for \( \rulename{{=}I} \) (convention 3): *Schema:* the left block, \( t = t \), citing nothing. *Reading:* every term equals itself, so the line may stand anywhere, even first in a derivation with no premises. *Example:* "\( a + b = a + b \) — \( \rulename{{=}I} \)", the first line of every chain below. Clauses 2–4 (07:50-52) kept, clause 3 gaining "(the boxes above)". The table 07:54-63 kept without its last row; 07:64 kept up to "The fourth row is the step of the opening calculation."; the last row and the rest of 07:64 (the degenerate choices) → fold F4.7-a. Quick check 07:66-72 kept. **Quick check (new)**, after it: "From \( a = b \) and the line \( a \cdot a = a + 1 \), which occurrences do you box to get \( a \cdot b = b + 1 \)?" Solution: the second and the third \( a \); \( \varphi = (a \cdot z = z + 1) \), and \( \varphi[a/z] \) is the given line, \( \varphi[b/z] \) the new one.
3. Capture nonexample 07:74-87 kept. "Why these two rules" 07:89 kept. The warning 07:91-93 **cut to its reading example** (~55 words): "**A bound variable is not a place to substitute.** From \( x = 0 \) and \( \forall x\, (x = x) \), the line \( \forall x\, (0 = x) \) does **not** follow: the \( x \)'s of \( \forall x\, (x = x) \) are bound, and \( \rulename{{=}E} \) replaces only free occurrences. Over \( \nZ \), with \( x \) naming \( 0 \), the premises are true and \( \forall x\, (0 = x) \) is false." The case analysis (07:92 from "To write \( \forall x\, (x = x) \) as \( \varphi[x/z] \)") → fold F4.7-b.
4. `## Symmetry, transitivity and congruence`: 07:97-160 kept (`prp-equality-symmetric-transitive` verbatim, 07:144, the (sym)/(trans) license 07:146, congruence 07:148-160). The claim "equals share every property" (07:162-192: the bold **Claim**, *Finding it*, the 7-line derivation, 07:190 and 07:192) → fold F4.7-c verbatim.
5. `## Calculations are chains of substitutions`: 07:196-226 kept. 07:228 (mixed chains) kept up to "Those are facts about order, not about equality."; its last sentence → "They enter derivations as 'arith' lines, one per link." Quick check 07:230-236 kept.
6. `## What equality sounds like in a proof`: 07:240-248 kept, 07:248's last clause → "… the facts it uses are the field axioms, here school algebra."
7. `## Unique existence`: 07:252-254 and `def-unique-existence` verbatim; 07:266 kept. 07:268 ("Well-definedness") → main line keeps (~60 words): "**Well-definedness.** The abbreviation does not depend on the choice of \( y \), up to renaming a bound variable. The argument, in the fold below, rests on one fact about substitution that the proof of @prp-unique-existence-use uses again: *if \( y \) does not appear in \( \varphi \), then \( (\varphi[y/x])[t/y] \) is \( \varphi[t/x] \).*" The rest of 07:268 (from "This is a structural induction") → fold F4.7-d verbatim. 07:270-274 ("Why \( y \) must not appear") → fold F4.7-e verbatim. Examples 07:276-280 kept; example 4 (07:281) and the derivation of \( \exists! x\, (x = c) \) with 07:285 and 07:304 → fold F4.7-e (after 07:274's text). Nonexample 07:283 kept. Warning 07:306-308 kept.
8. `## How uniqueness is used and proved`: 07:312, `prp-unique-existence-use` (statement), 07:323 and its Idea (07:325-327) kept on the main line; one sentence added after the Idea: "The two derivations that carry this out are in the fold below." The proof (07:329-403, both derivations and their paragraphs) → fold F4.7-f verbatim (a sibling after the Idea; the fold holds the whole `.proof` div). 07:405 and "the maximum" 07:407 kept (fd2 ch02 01:150 names it).
9. Search method 07:409-415 kept, and one sentence (STYLE §12.5): "In the Givens/Goal table, \( \rulename{{=}E} \) turns a Given into a new Given with some holes refilled, and \( \rulename{{=}I} \) adds \( t = t \) to the Givens at no cost."
10. `## The rule, phrase and Lean table, completed` (07:417-443, id kept; the section's rule card and the volume's one-page reference). 07:419 kept without its last sentence ("Nothing later depends … proof phrases.", → Looking ahead) and with "the Lean code" kept (the box below). The table: columns `Rule | Shape | You write`, nineteen rows in the order of 07:421-441, the You-write entries as now, the Shape entries from Chapter 1's card (1.6), Chapter 2's card (`ch02-revision.md` §1 item 7) and convention 6 above, and for equality "nothing \( \Longrightarrow \) \( t = t \)" (\( \rulename{{=}I} \)) and "\( t_1 = t_2 \), \( \varphi[t_1/x] \) \( \Longrightarrow \) \( \varphi[t_2/x] \)" (\( \rulename{{=}E} \)). Then **the Lean box (new; the collapsed column):** `::: {.remark}` with the title line `[For Lean users]` and one paragraph: "∧I `constructor`; ∧E `h.1`, `h.2`; →E `exact h hp`; →I `intro hp`; R `exact hp`; ∨I `left`, `right` (or `Or.inl hp`); ∨E `Or.elim h` (or `cases h`); ¬E `exact hn hp` (goal `False`); ⊥E `exfalso`; ¬I `intro hp` (goal `False`); ↔I `constructor`; ↔E `h.mp hp`, `h.mpr hq`; RAA `by_contra h`; ∀E `h t` (or `specialize h t`); ∀I `intro x`; ∃I `use t` (or `Exists.intro t h`); ∃E `obtain` (or `Exists.elim h`); =I `rfl`; =E `rw [h]`, chains `calc`. Nothing later depends on these." (ch05 01:70, "the Lean command for each primitive rule in the rule, phrase and Lean table that ends Section 4.7", stays true.) 07:443 kept.
11. Looking ahead (as above).

**Folds.** F4.7-a `title="Degenerate choices"`: the table's last row and 07:64 from "The last row is the **degenerate** choice". F4.7-b `title="Why no choice of the hole works"`: 07:92 from its third sentence. F4.7-c `title="Equals share every property"`: 07:162-192. F4.7-d `title="Well-definedness, proved"`: 07:268 from "This is a structural induction". F4.7-e `title="Why y must not appear, and a degenerate case"`: 07:270-274, 07:281, 07:285-304. F4.7-f `title="The proof of the two halves"`: 07:329-403.

**Cut outright:** clause 1 (07:49; replaced by the bullets); 07:92's first two sentences (reworded); the pointers in 07:228, 07:248 and 07:419.

**Quick checks:** the hole \( z \) for \( x_0 = 3 \) (kept), the boxes for \( a \cdot b = b + 1 \) (new), the one-\( b \) chain step (kept): three in ~3,900 words.

**Exercises.** A1, B1 (its "To use it in @prp-unique-existence-use …" paragraph kept: it cites the statement, which is on the main line), B2, B3, C1, C2 kept. New:
- **A2: Drill** (`exr-equality-and-uniqueness-a2`):
  (a) What does \( \rulename{{=}I} \) cite? — Nothing.
  (b) From \( a = b \) and \( P(a, a) \), box the holes to get \( P(a, b) \). — Box the second \( a \) only: \( \varphi = P(a, z) \).
  (c) From \( a = b \) and \( P(b) \), does one \( \rulename{{=}E} \) give \( P(a) \)? — No: the equation rewrites \( a \) into \( b \); turn it round first (sym), then \( \rulename{{=}E} \).
  (d) From \( x_0 = 2 \) and \( x_0 + x_0 = 4 \), which \( \varphi \) gives \( 2 + x_0 = 4 \)? — \( \varphi = (z + x_0 = 4) \).
  (e) From \( a = y \) and \( \exists y\, (y < a) \), is \( \exists y\, (y < y) \) a legal \( \rulename{{=}E} \) line? — No: the \( y \) put in would be captured by \( \exists y \).
  (f) Write \( \exists! x\, (x + 1 = 3) \) without \( \exists! \). — \( \exists x\, (x + 1 = 3 \wedge \forall y\, (y + 1 = 3 \to y = x)) \).
  (g) Derive \( a = b \vdash f(b) = f(a) \). — 2 \( f(a) = f(a) \) =I; 3 \( f(b) = f(a) \) =E 1, 2, with \( \varphi = (f(z) = f(a)) \).
  (h) Derive \( a = b, \ b = c \vdash a = c \) in one step. — 3 \( a = c \) =E 2, 1, with \( \varphi = (a = z) \).
- **B4** (`exr-equality-and-uniqueness-b4`, new, scaffolded), `[B4: Rewrite, and turn round]`: "A search for \( a = b, \ b = c, \ P(a) \vdash P(c) \wedge c = a \) has reached the stage below. *Name the move, then complete it, giving for each \( \rulename{{=}E} \) line its holes.*" Shown: lines 1–3 premises, a gap, line 9 \( P(c) \wedge c = a \) with "?". Answer: the move is *substitute equals, holes marked*, with an \( \rulename{{=}I} \) line to turn an equation round: 4 \( P(b) \) =E 1, 3 (\( \varphi = P(z) \)); 5 \( P(c) \) =E 2, 4 (\( \varphi = P(z) \)); 6 \( a = c \) =E 2, 1 (\( \varphi = (a = z) \)); 7 \( a = a \) =I; 8 \( c = a \) =E 6, 7 (\( \varphi = (z = a) \): line 7 is \( \varphi[a/z] \), and the equation \( a = c \) refills the box with \( c \)); 9 ∧I 5, 8. (Lines 7–8 are (sym) written out; with the abbreviation of the text, line 8 is "\( c = a \) (sym) 6".)

**Sidecars:** none new beyond the drills (no arithmetic).

### 4.8 Section 4.8: Translating Mathematics: Nested and Bounded Quantifiers (`08-translation.md`)

**Budget:** main line ≤ 3,300 words (now 3,753; about 800 folded or cut, about 330 new or moved in); folds ≤ 850. No Looking-ahead box.

**Changes, in the file's order.**
1. 08:3-13 kept.
2. `## Translation from the outside in`: 08:17-19 kept. Step 1 (08:21) **replaced** by the paragraph moved from 4.1 (01:178-182), verbatim, as step 1's body, with its display, after the lead "**Fix the domain.** State what the variables range over. A sentence of analysis often mixes kinds of objects:" — so step 1 reads "… **One domain per formula.** The logic of this book has a single domain …" through "… every translation in this chapter follows it." Steps 2–3 (08:22-23) kept, with 08:23's "\( \mathrm{Prime}(p) \)" → "\( \mathrm{Prime}(m) \)". 08:25 kept.
3. `exm-translate-limit`: statement and solutions (a)–(c) verbatim; (d) and (e) with the bound letters renamed (S2a 3): (d) "Section 4.1 read the sentence as \( \neg\exists m\, \bigl( \mathrm{Prime}(m) \wedge \forall n\, (\mathrm{Prime}(n) \to n \le m) \bigr) \)", the positive form \( \forall m\, \bigl( \mathrm{Prime}(m) \to \exists n\, (\mathrm{Prime}(n) \wedge m < n) \bigr) \), the pushed form \( \forall m\, \bigl( \mathrm{Prime}(m) \to \exists n\, (\mathrm{Prime}(n) \wedge \neg(n \le m)) \bigr) \), "the order fact that \( \neg(n \le m) \) is the same as \( m < n \)"; (e) \( \forall n > 1\; \exists m\, \bigl( \mathrm{Prime}(m) \wedge \exists k\, (n = m \cdot k) \bigr) \), with "some \( m \) is prime and divides \( n \)", "\( m \mid n \) means \( n = m \cdot k \)". 08:73 and Quick check 08:75-81, warning 08:83-85 kept.
4. `## Rules for bounded quantifiers`: 08:89-91 and `prp-bounded-quantifier-rules` (statement) verbatim; 08:145 and 08:147 kept. 08:149 ("Why is this a proposition and not simply a definition?") → fold F4.8-a. The Idea 08:151-153 kept on the main line (the one-sentence meaning: each bounded rule is an unbounded rule on the unfolded formula, plus the connective rule for \( \to \) or \( \wedge \)). The proof (08:155-235) → fold F4.8-b verbatim, a sibling after the Idea, lead sentence on the main line: "The proof writes out, for each bounded rule, the block of unbounded steps it abbreviates, and checks that the side conditions match; it is in the fold below." 08:237 and Quick check 08:239-245 kept.
5. `## A limit derivation with bounds`: 08:249-259 kept (the claim and the Idea).
6. **The skeleton (new, ~140 words and a partial derivation; the plan's named matrices).** After the Idea, before the derivation: "Two abbreviations show the shape. Write \( G(N, \varepsilon) \) for \( \forall n \in \nN\; (n \ge N \to \abs{a_n - L} < \varepsilon) \), 'from \( N \) on, every term is within \( \varepsilon \) of \( L \)', and \( G_2(N, \varepsilon) \) for the same formula with \( 2 \cdot a_n \) and \( 2 \cdot L \). The premise is \( \forall \varepsilon > 0\; \exists N \in \nN\; G(N, \varepsilon) \), and the goal is the same with \( G_2 \). With the lines that look inside \( G \) left as a gap, the derivation is:" Then a partial derivation (`% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)`, every line carrying the number it has in the full derivation):
   ```
   1 ∀ε>0 ∃N∈ℕ G(N, ε)                      premise
     | [ε0]
   2 | ε0 > 0                               assumption
   3 | ε0/2 > 0                             arith 2
   4 | ∃N∈ℕ G(N, ε0/2)                      ∀E 1, 3
   5 | | [N0] N0 ∈ ℕ                        assumption
   6 | | G(N0, ε0/2)                        assumption
     | | ⋮
   13| | G₂(N0, ε0)
   14| | ∃N∈ℕ G₂(N, ε0)                     ∃I 5, 13
   15| ∃N∈ℕ G₂(N, ε0)                       ∃E 4, 5–14
   16 ∀ε>0 ∃N∈ℕ G₂(N, ε)                    ∀I 2–15
   ```
   Then two sentences: "Lines 7–12 are the only lines that look inside \( G \) and \( G_2 \): they unfold \( G(N_0, \varepsilon_0/2) \), use it at a fresh \( n_0 \), and fold the result back into \( G_2(N_0, \varepsilon_0) \). Here is the derivation in full; its lines 1–6 and 13–16 are the lines above, written out." Then the full derivation (08:261-290) **verbatim** (ch05 02:7, 02:13 and 02:57 cite its line numbers; `check_fitch.py` checks only written-out formulas, so the abbreviations stay in the skeleton). **Quick check (new):** "In the skeleton, line 4 instantiates the premise at \( \varepsilon_0/2 \). Why that term, and not \( \varepsilon_0 \)?" Solution: the goal needs \( \abs{2a_n - 2L} < \varepsilon_0 \), which is \( 2\abs{a_n - L} < \varepsilon_0 \), so it is enough to have \( \abs{a_n - L} < \varepsilon_0/2 \); the term is read off the goal (Section 4.3's step), not off the premise.
7. 08:292-303 kept. 08:305 kept up to "… costs one line more."; its last sentence → "The claim '\( \frac1n \to 0 \)' (for \( n \ge 1 \)) is not derived here: its proof needs the Archimedean property, a fact about \( \nN \) inside \( \nR \), not a law of logic."
8. `## The search method, extended` (08:307-333): kept.

**Folds.** F4.8-a `title="Why a proposition, not a definition"`: 08:149. F4.8-b `title="The proof: each bounded rule as a block of unbounded steps"`: 08:155-235 (the `.proof` div).

**Cut outright:** 08:21 (replaced by the moved paragraph); 08:305's pointer.

**Quick checks:** a maximum (kept), the bounded \( \rulename{\exists E} \) box (kept), the term \( \varepsilon_0/2 \) (new): three in ~3,300 words.

**Exercises.** A1, B1, B2, C1 (frozen), C2 kept. New:
- **A2: Drill** (`exr-translation-a2`):
  (a) Over \( \nR \), translate "\( f \) is bounded above on \( A \)". — \( \exists M\; \forall x \in A\; (f(x) \le M) \).
  (b) Translate "every element of \( A \) is less than some element of \( B \)". — \( \forall x \in A\; \exists y \in B\; (x < y) \).
  (c) Translate "some element of \( A \) is less than every element of \( B \)". — \( \exists x \in A\; \forall y \in B\; (x < y) \).
  (d) Unfold the bounds of (c). — \( \exists x\, (x \in A \wedge \forall y\, (y \in B \to x < y)) \).
  (e) Translate "\( a_n > 0 \) for all large \( n \)". — \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0) \).
  (f) Lines 1 \( \forall \varepsilon > 0\; \varphi \) and 2 \( 1 > 0 \). What does the bounded \( \rulename{\forall E} \) 1, 2 give? — \( \varphi[1/\varepsilon] \).
  (g) Lines 1 \( 3 \in \nN \) and 2 \( 3 + 3 = 6 \). What does the bounded \( \rulename{\exists I} \) 1, 2 give, with \( \varphi = (n + n = 6) \)? — \( \exists n \in \nN\; (n + n = 6) \).
  (h) How many lines does a bounded \( \rulename{\exists E} \) save over the unbounded rule? — One: two assumptions in place of one assumption and two \( \rulename{\wedge E} \) lines.

**Sidecars:** none new. Ledger: the moved one-domain paragraph's line (`file:` → `08-translation.md`).

### 4.9 Section 4.9: Negating and Moving Quantifiers (`09-quantifier-laws.md`)

**Budget:** main line ≤ 4,100 words (now 4,496); folds ≤ 400. Looking ahead: "Chapter 5 says what is at stake when 'not every' becomes 'some not' by RAA, and catalogues the wrong negations of this section among the steps a proof may not take." (09:118's, 09:290's and 09:695's pointers, merged into one box with one destination; STATUS row F1.4 §09.)

*Recorded deviation from the plan (§3, 4.9: "Order: negation laws, negating an implication, negating a definition mechanically (moved up), how it looks in proofs, then bounded laws, then passage and distribution").* The bounded laws stay **before** the negation procedure: the procedure (09:597) and every solution of `exm-negating-definitions` cite `prp-bounded-quantifier-negation`, and a citation of a result placed later in the section would be a forward dependency. The plan's purpose, that the practical recipe comes before 300 lines of passage and distribution laws (the novice report's point), is kept: those laws move to the end.

**New order of material.**
1. Opening (09:3) kept, its last sentence → "It then shows the laws at work, in an analysis proof in which a negation and a well-chosen \( \varepsilon \) do the work, and ends with the laws that move a quantifier across a connective, which a first reading may leave for later."
2. `## Not every, and some not` (09:5-128): kept (key proof, *Try it first*, the Quick check, "The laws as one line"). 09:118: its first three sentences kept ("So … interderivable. The direction that cost two RAA boxes … no derivation of (a) avoids RAA. This is a claim about all derivations, … (Chapter 3's optional @thm-raa-independent proves the propositional analogue for \( \neg\neg P \vdash P \))."); the sentence "Chapter 5 returns to what is at stake: …" → the Looking-ahead box; the sentence "This is the law that *Analysis on the Real Line*, Chapter 1 uses …" → the index's "Where this goes" (§4.0 item 7).
3. `## The negation of an implication` (09:130-191): kept.
4. `## Bounded quantifiers keep their bounds` (09:193-291): kept; the warning's parenthesis 09:290 "(Chapter 5 lists this among the wrong negations it catalogues)" cut.
5. `## Negating a definition, mechanically` **(moved up; 09:588-696; heading kept, fd2 ch03 07:94 names it)**: the algorithm 09:590-604 kept. 09:606 **replaced** on the main line by two sentences: "Why may a step act on a part buried inside the formula? Because provable equivalence passes through every connective and every quantifier, so a part may be replaced by a part provably equivalent to it; the fold below gives the argument." The paragraph 09:606 → fold F4.9-a (verbatim except the sentences about passage laws, which go to F4.9-c after the passage laws, item 7, and one bridging sentence): F4.9-a runs from "If \( \alpha \dashv\vdash \beta \), then \( \neg\alpha \dashv\vdash \neg\beta \)" through "… for the same reason.", with that sentence reworded "The laws this book applies to parts have conditions of two kinds, and both survive, for the same reason; the passage laws at the end of this section have one kind, checked in the fold after them, and the bounded negation laws the other.", then the sentences on `prp-bounded-quantifier-negation` ("A law of @prp-bounded-quantifier-negation with a bound such as \( z > a \) …" through "… so \( z \) does not occur in it."), then "So the pair \( \alpha[x_0/x] \), \( \beta[x_0/x] \) is again an instance of the same law, with its condition met. A part sitting under several symbols is reached one symbol at a time." `exm-negating-definitions` (09:608-667) verbatim. 09:669-680 kept with the bound letters \( m, n \) for \( p, q \) (§1 item 10). Quick check 09:682-692 kept. Warning 09:694-696 kept without its last sentence ("Chapter 5 catalogues this slip among the wrong negations.").
6. `## How the laws look in a mathematical proof` (09:698-720): 09:700 reworded per ch02-revision §6: "Chapter 2 proved, in @exm-raa-zero, that a number \( x \ge 0 \) below every positive number is \( 0 \). Its key step chose \( \varepsilon \coloneqq x/2 \), and the reading after it called 'the hypothesis applies to it' a step about 'every', used as ordinary reasoning until Chapter 4. The rule is \( \rulename{\forall E} \), in its bounded form (@prp-bounded-quantifier-rules), at a term built from the data. …" `prp-arbitrarily-close-equal` verbatim; 09:718's last sentence ("The facts about \( \abs{\cdot} \) used here are school algebra; *Analysis on the Real Line*, Chapter 1 proves them …") → "The facts about \( \abs{\cdot} \) used here are school algebra." 09:720 kept.
7. `## Moving a quantifier across a connective` **(moved to the end; 09:293-586)**, with one new lead sentence: "The laws of this subsection are reference material for a first reading; Section 4.11 returns to two of them." 09:295, `prp-quantifier-distribution` and its proof, 09:312, 09:348 (its last sentence → "These are counter-readings; Section 4.11 draws them as counter-models."), 09:350, `prp-quantifier-passage` with its proof, 09:368, "Why the condition on \( \psi \)" 09:578 kept. Then fold F4.9-c (the passage-law sentences of 09:606). Quick check 09:580-586 kept, its parenthesis "(a law may be used on a part under a quantifier; the next subsection says why)" → "(a law may be used on a part under a quantifier: the paragraph after the negation procedure, and the fold above for the passage laws)".

**Folds.** F4.9-a `title="Why a step may act on a part"`: 09:606 as described in item 5. F4.9-c `title="Passage laws on a part"`: the two sentences of 09:606 beginning "A passage law of @prp-quantifier-passage asks that its moving variable \( y \) not be free in \( \psi \)" through "… and \( y \) is not free in it either.", followed by "So the pair is again an instance of the law, with its condition met." (There is no F4.9-b.)

**Cut outright:** the pointers in 09:118, 09:290, 09:695, 09:718.

**Quick checks:** \( \neg\forall x\, P(x) \) and \( \neg P(c) \) (kept), the supremum statement negated (kept), the passage law with \( y \) (kept): three in ~4,100 words.

**Exercises.** A1 (key proof), B1, B2, B3, C1, C2 (exit check) kept (B2's and C1's solutions cite "the paragraph after the negation procedure", which stays true). New:
- **A2: Drill** (`exr-quantifier-laws-a2`), each part to be negated into positive form:
  (a) \( \forall x\, P(x) \). — \( \exists x\, \neg P(x) \).
  (b) \( \exists x\, (P(x) \wedge Q(x)) \). — \( \forall x\, (\neg P(x) \vee \neg Q(x)) \), equivalently \( \forall x\, (P(x) \to \neg Q(x)) \).
  (c) \( \forall x > 0\; (x^2 > 0) \), over \( \nR \). — \( \exists x > 0\; (x^2 \le 0) \): the bound stays, and the order fact turns \( \neg(x^2 > 0) \) into \( x^2 \le 0 \).
  (d) "If \( n \) is even, then \( n^2 \) is even", for one integer \( n \). — "\( n \) is even and \( n^2 \) is not even" (@prp-negated-implication).
  (e) \( \forall \varepsilon > 0\; \exists \delta > 0\; (\delta < \varepsilon) \). — \( \exists \varepsilon > 0\; \forall \delta > 0\; (\delta \ge \varepsilon) \).
  (f) \( \forall x \in A\; (x \le s) \). — \( \exists x \in A\; (x > s) \).
  (g) Which is the negation of \( \forall x \in A\; \exists y \in B\; (x < y) \): (i) \( \exists x \in A\; \forall y \in B\; (x \ge y) \); (ii) \( \exists x \notin A\; \forall y \notin B\; (x \ge y) \); (iii) \( \forall x \in A\; \exists y \in B\; (x \ge y) \)? — (i): flip each quantifier, keep each bound.
  (h) "\( (a_n) \) is bounded below": \( \exists m\; \forall n \in \nN\; (m \le a_n) \). — \( \forall m\; \exists n \in \nN\; (a_n < m) \).

**Sidecars:** none new.

### 4.10 Section 4.10: Uniformly Continuous Implies Continuous, Rule by Rule (`10-uniform-continuity-rule-by-rule.md`)

**Budget:** main line ≤ 2,700 words (now 2,429); folds ≤ 150. Looking ahead: "Chapter 5 shows how the eleven lines of this derivation become the three sentences of a written proof, at several levels of detail." (10:83's pointer, moved; STATUS row F1.4 §10, levels of proof.)

**Changes, in the file's order.**
1. 10:3 kept.
2. `## Two definitions that differ in one place`: 10:7 without its sentence "*Analysis on the Real Line*, Chapters 5 and 6 define continuity and uniform continuity properly and develop them." (→ the index's "Where this goes"); the rest, the two displays, 10:18 and the Quick check 10:20-26 kept.
3. `## The skeleton first` **(new, ~280 words and a 6-line derivation; the plan's "bare skeleton first, then unfold K")**: "Hold \( \varepsilon \) fixed, and write \( K(x, \delta) \) for '\( \delta \) works at \( x \)', the formula \( \forall y \in A\; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon) \). Drop the bounds on \( \delta \) and \( x \) for a moment. Then UC at this \( \varepsilon \) says \( \exists \delta\, \forall x\, K(x, \delta) \), one \( \delta \) for every point, and C at this \( \varepsilon \) says \( \forall x\, \exists \delta\, K(x, \delta) \), a \( \delta \) for each point. The step from the first to the second is @prp-exists-forall-swap with other letters:" The derivation (an ordinary `nd` block; `check_fitch.py` accepts it):
   ```
   1 ∃δ ∀x K(x, δ)                 premise
     | [x0]
     | | [δ0]
   2 | | ∀x K(x, δ0)               assumption
   3 | | K(x0, δ0)                 ∀E 2
   4 | | ∃δ K(x0, δ)               ∃I 3
   5 | ∃δ K(x0, δ)                 ∃E 1, 2–4
   6 ∀x ∃δ K(x, δ)                 ∀I 2–5
   ```
   Then: "Fix a point, obtain the one \( \delta \) that works everywhere, choose it for this point. The converse, from \( \forall x\, \exists \delta\, K \) to \( \exists \delta\, \forall x\, K \), is the swap whose search stalled in Section 4.6. The rest of this section puts \( \varepsilon \) and the bounds back and writes \( K \) out. That costs five lines: the assumptions \( x_0 \in A \), \( \varepsilon_0 > 0 \) and \( \delta_0 > 0 \), the step that applies UC at \( \varepsilon_0 \), and the line that closes the box of \( \varepsilon_0 \). The skeleton's line 1 becomes line 4 of the derivation below (UC at \( \varepsilon_0 \)), its lines 2–5 become lines 6–9, and its line 6 becomes lines 10 and 11, which close the boxes of \( \varepsilon_0 \) and \( x_0 \)." (The skeleton is exempt from snapshots: 4.10 is outside 4.4–4.6.)
4. `## The derivation`: `exm-uniform-implies-continuous` (10:30-77) verbatim (key proof; ch05 03:214 copies it with its line numbers), 10:79-81 kept; 10:83 kept without its last sentence ("Chapter 5 studies this passage …", → Looking ahead).
5. `## Reading dependence off the boxes`: 10:89-97 kept. 10:99 kept up to "… line 4 mentions \( \varepsilon_0 \) alone."; the rest (from "So \( \delta_0 \) could have been obtained before \( x_0 \) entered at all" to the end of the paragraph) → fold F4.10-a (B2's solution, which describes the same variants, stays as it is). 10:101 kept.
6. `## The converse breaks at a side condition`: 10:105-154 kept (`exm-converse-fails` verbatim). 10:156 → "A failed search proves nothing about all derivations; a counter-reading does, and the next subsection gives one: a function for which C is true and UC false. Section 4.11 explains why that settles the question."
7. `## A function that is continuous and not uniformly continuous`: before `exm-square-not-uniform`, the lead "Here is the picture first; the example proves it." and **Figure D (new TikZ; the plan's \( \delta \)-windows):** the graph of \( y = x^2 \) for \( 0 \le x \le 3.2 \) (vertical scale compressed); at each of \( x_0 = 0, 1, 2, 3 \), a dot on the graph, two short dashed horizontal lines at heights \( x_0^2 - 1 \) and \( x_0^2 + 1 \) (the band of \( \varepsilon = 1 \)), and on the horizontal axis a thick bar from \( x_0 - \delta \) to \( x_0 + \delta \) with \( \delta = \sqrt{x_0^2 + 1} - x_0 \), labeled \( \delta = 1 \), \( 0.41 \), \( 0.24 \), \( 0.16 \). Caption: "With \( \varepsilon = 1 \), the largest \( \delta \) that works at \( x \ge 0 \) is \( \sqrt{x^2 + 1} - x \): \( 1 \) at \( 0 \), about \( 0.41 \) at \( 1 \), \( 0.24 \) at \( 2 \), \( 0.16 \) at \( 3 \). It shrinks as \( x \) grows, and no single positive \( \delta \) works at every \( x \)." (No prose argument for "largest" on the main line; the sidecar checks it, §8 item 27.) Then `exm-square-not-uniform` verbatim; 10:188 → "The \( \delta \) for C grows smaller as \( \abs{x} \) grows, and no single \( \delta \) serves the whole line. The proof of failure says why: however small \( \delta \) is, far enough out (at \( x = 1/\delta \)) the graph is so steep that two points \( \delta/2 \) apart have values more than \( 1 \) apart. Read in the real numbers, with \( f \) as squaring, the premise C is true and the conclusion UC is false: a counter-reading, and by Section 4.11 no derivation of UC from C exists." The warning 10:190-192 kept.
8. Looking ahead (as above).

**Folds.** F4.10-a `title="Choosing \( \delta \) before the point"`: 10:99 from "So \( \delta_0 \) could have been obtained before \( x_0 \) entered at all".

**Cut outright:** the pointers in 10:7 and 10:83.

**Quick checks:** the swapped \( \exists \delta\, \forall \varepsilon \) (kept), the boxes around \( \delta_0 \) (kept): two in ~2,700 words, plus the skeleton and Figure D.

**Exercises.** A1 (key proof), B1, B2 (proof ordering), B3, C1 (faded, scaffolded), C2, C3 (exit check) kept. No drill bank (§1 item 8).

**Sidecars:** `exm-square-not-uniform.py` gains Figure D's values: \( \sqrt{x^2 + 1} - x \) at \( 0, 1, 2, 3 \) (\( 1 \), \( 0.4142 \), \( 0.2361 \), \( 0.1623 \)), and a check on a grid that for \( x \ge 0 \) this \( \delta \) works (\( \abs{y^2 - x^2} < 1 \) whenever \( \abs{y - x} < \delta \)) and that every larger \( \delta \) fails.

### 4.11 Section 4.11: Models and Counter-models (`11-models.md`)

**Budget:** main line ≤ 4,950 words (now 5,616; about 1,100 folded or cut, about 450 new); folds ≤ 1,100. No Looking-ahead box (11:42's pointer goes to the index).

**New order of material.**
1. Opening (11:3) kept, its last two sentences shortened: "This section builds the meaning of a quantified formula: a **model**, a domain with a meaning for every symbol. A model that makes the premises true and the conclusion false is a **counter-model**, the exact form of the counter-readings used since Section 4.3, and it settles the stalled searches."
2. `## Three pictures` **(new, ~420 words; the plan's "2–3 pictured counter-models first")**. Lead: "Section 4.3 called a reading in which the premises are true and the conclusion false a counter-reading. Here are three, drawn as in Section 4.1: dots for the objects, labels for one-place predicates, arrows for a two-place one." **Figure M (new TikZ; three panels):**
   - *(A)* Two dots \( a \), \( b \); the label \( P \) at \( a \), the label \( Q \) at \( b \). Text: \( \exists x\, P(x) \wedge \exists x\, Q(x) \) is true (the witnesses \( a \) and \( b \)), and \( \exists x\, (P(x) \wedge Q(x)) \) is false (no dot has both labels). So the converse of @prp-exists-and does not follow (Section 4.6 asked).
   - *(B)* The integers, as dots \( \dots, -1, 0, 1, 2, 3, \dots \) on a line, with an arrow from each \( n + 1 \) to \( n \), labeled "is above"; \( R(x, y) \) means \( x > y \). Text: \( \forall y\, \exists x\, R(x, y) \) is true (every integer has one above it, \( y + 1 \)), and \( \exists x\, \forall y\, R(x, y) \) is false (an integer above every integer would be above itself). So the converse of @prp-exists-forall-swap does not follow.
   - *(C)* Two dots \( a \), \( b \); the label \( P \) at \( b \); the constant \( c \) names \( a \). Text: \( \exists x\, P(x) \) is true (at \( b \)), and \( P(c) \) is false. So \( \exists x\, P(x) \vdash P(c) \) has no derivation (@exr-existential-introduction-c2 asked why).

   Closing (~50 words): "Each picture is a domain with a meaning for every symbol. The rest of this section says exactly what that is (a **structure**), exactly when it makes a formula true (**satisfaction**), and why one picture like these rules out every derivation (the last subsection)." **Quick check (new):** "Draw two dots that make \( \forall x\, (P(x) \vee Q(x)) \) true and \( \forall x\, P(x) \vee \forall x\, Q(x) \) false." Solution: picture (A) again: each dot has \( P \) or \( Q \); \( \forall x\, P(x) \) fails at \( b \), \( \forall x\, Q(x) \) at \( a \).
3. `## Why a row is not enough` (11:5-19): kept.
4. `## Structures` (11:21-63): 11:23-25 and `def-structure` verbatim; 11:42 kept without "*Sets, Relations, and Cardinality*, Chapter 1 develops sets, pairs and functions properly, and" (→ index), ending "… this section uses only their everyday meaning." 11:44 and the examples 11:46-51 kept. The non-example by minimal change 11:53 → fold F4.11-a. "Why this definition" 11:55-59 → fold F4.11-b, except its first bullet's sentence kept on the main line: "The domain is non-empty because of @prp-forall-implies-exists; a later subsection explains why." The warning 11:61-63 kept.
5. `## Assignments and the value of a term` (11:65-98): kept.
6. `## Satisfaction` (11:100-150): `def-satisfaction` verbatim, 11:102-104 and 11:124-130 kept. 11:132 ("Well defined") → fold F4.11-c. The trace 11:134-138 and 11:140 kept. 11:142 (degenerate cases) → fold F4.11-c. The Quick check 11:144-150 kept (fd4 ch01 04:3 and 04:74 name it).
7. `## Only the free variables matter` (11:152-199): 11:154 and 11:156 kept; `lem-free-coincidence` (statement) verbatim, followed by its meaning in one sentence (STYLE §12.12): "*In words: to decide a formula, only the values of its free variables matter.*" Its Idea and proof (11:167-189) → fold F4.11-d verbatim, a sibling after the statement. 11:191-195 (sentences true or false in \( \fM \); finitely many values) and the warning 11:197-199 kept on the main line (\( \fM \models \varphi \) is defined there).
8. `## Semantic entailment` (11:201-225): kept.
9. `## Why domains are non-empty` (11:227-237, id kept): kept.
10. `## Counter-models` (11:239-301): 11:241 and `exm-counter-model-swap` verbatim, 11:263 kept. 11:265-277 shortened to one paragraph (~120 words) that checks pictures (A) and (C) by the clauses: "Picture (A), checked by the clauses: with \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \), the premise of the converse of @prp-exists-and holds by (S5) and (S7), with witnesses \( a \) and \( b \), and the conclusion fails, since \( a \notin Q^{\fM} \) and \( b \notin P^{\fM} \). The same structure refutes the converse of the \( \forall \)/\( \vee \) law of @prp-quantifier-distribution: each element is in \( P^{\fM} \) or in \( Q^{\fM} \), and neither set is all of \( D \). Picture (C): with \( c^{\fM} = a \) and \( P^{\fM} = \{ b \} \), \( \exists x\, P(x) \) holds with the witness \( b \) and \( P(c) \) fails, since \( a \notin P^{\fM} \)." (The displayed non-entailments of 11:267, 11:273 and the sentence "So \( \exists x\, P(x) \not\models P(c) \)." stay in the paragraph.) 11:279 (the assignment is part of a counter-model), the warning 11:281-283, the model of a list 11:285-293 (C2 refers to "the three sentences of the text") and the Quick check 11:295-301 kept.
11. `## From counter-models to non-derivability` (11:303-315, id kept): kept; 11:311 gains "and the three pictures at the start of this section" after "With the statement, the examples above become non-derivability results."

**Folds.** F4.11-a `title="A non-example, and the repair used for \( 1/n \)"`: 11:53. F4.11-b `title="Why total functions, and why identity"`: 11:55-59 minus the kept sentence. F4.11-c `title="Satisfaction is well defined; degenerate cases"`: 11:132 and 11:142 (one fold after the trace, 11:140). F4.11-d `title="The proof: an induction for all assignments at once"`: 11:167-189.

**Cut outright:** 11:42's pointer; 11:265-277 reworded as in item 10 (no claim lost: every non-entailment there stays).

**Quick checks:** the two dots for the \( \forall \)/\( \vee \) converse (new), square roots in \( \nR \), \( [0, \infty) \), \( \nC \) (kept), the counter-model with a universal hypothesis (kept): three in ~4,950 words, plus Figure M.

**Exercises.** A1, B2, R1, R3, R4 kept; B1, B3, C3, R2 frozen (cited inside the chapter); C1, C2 frozen (fd2). New:
- **A2: Drill** (`exr-models-a2`):
  (a) \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \). Is \( \forall x\, P(x) \) true in \( \fM \)? — No: it fails at \( b \).
  (b) The same structure: is \( \exists x\, \neg P(x) \) true? — Yes, at \( b \).
  (c) Give a counter-model to \( \exists x\, P(x) \models \forall x\, P(x) \). — The structure of (a): the premise holds at \( a \), the conclusion fails at \( b \).
  (d) Is \( D = \{ a \} \), \( P^{\fM} = \{ a \} \) a counter-model to \( \forall x\, P(x) \models \exists x\, P(x) \)? — No: both are true there; and no structure is one, since domains are non-empty.
  (e) In \( (\{ 0, 1, 2 \}, \le) \), is \( \exists x\, \forall y\, (x \le y) \) true? — Yes, with \( x = 0 \).
  (f) In \( (\nN, <) \), under an assignment with \( \ell(x) = 3 \), is \( \exists y\, (y < x) \) satisfied? — Yes: \( y = 0 \) gives \( 0 < 3 \).
  (g) Give a counter-model to \( \forall x\, (P(x) \to Q(x)) \models \forall x\, (Q(x) \to P(x)) \). — \( D = \{ a \} \), \( P^{\fM} = \emptyset \), \( Q^{\fM} = \{ a \} \): the premise holds (its hypothesis fails at \( a \)), the conclusion fails at \( a \).
  (h) Why is \( (\nN, <) \), with \( R(x, y) \) read as \( x < y \), not a counter-model to \( \forall y\, \exists x\, R(x, y) \models \exists x\, \forall y\, R(x, y) \)? — Its premise is false: nothing in \( \nN \) is below \( 0 \).

**Sidecars:** `exm-counter-model-swap.py` (or `def-satisfaction.py`) gains the three pictures of Figure M (finite checks; picture (B) on a window of \( \nZ \) and by the argument given); `exr-models-a2.py` checks (a)–(h).

### 4.12 Section 4.12: Soundness for Predicate Logic (`12-first-order-soundness.md`)

**Kept.** The section is already optional (12:3), and the index's reading path now names it as second reading (§4.0 item 4). No text change: its statements and proofs, `thm-first-order-soundness` (cited by fd3 ch06 05) and `cor-counter-model`, stay as they are. The pointers it makes into earlier sections stay true after this revision: 12:13 ("Section 4.8 expanded into a displayed block" — the block is now in fold F4.8-b, still in Section 4.8), 12:15 (Section 4.2's renaming convention, now with its status in fold F4.2-g), 12:21 ("Section 4.4 extended @def-derivation" — now the fine print of 4.4, item 9), 12:268-274 (the counterexamples of Sections 4.4, 4.6, 4.3, 4.5, 4.7, all kept on their main lines or, for 4.4's nested one, in fold F4.4-b; the list's second item, "from \( x_0 > 0 \), \( \forall x\, (x > 0) \)", is exactly the new minimal derivation of 4.4). Exercises unchanged.

**Budget:** unchanged, 5,178 main-line words, not on the core track.

---

## 5. Budgets and the Time line

| Section | Main line now (before Exercises) | Main-line budget | Estimate after revision | Folds budget |
|---|---|---|---|---|
| index | 916 | ≤ 1,100 | ~1,050 | — |
| 4.1 | 4,670 | ≤ 5,000 | ~4,900 | ≤ 300 |
| 4.2 | 6,420 | ≤ 3,900 | ~3,900 | ≤ 2,400 |
| 4.3 | 3,023 | ≤ 3,100 | ~3,050 | ≤ 200 |
| 4.4 | 3,861 | ≤ 3,800 | ~3,700 | ≤ 700 |
| 4.5 | 3,090 | ≤ 3,100 | ~3,030 | ≤ 200 |
| 4.6 | 4,847 | ≤ 4,950 | ~4,900 | ≤ 650 |
| 4.7 | 5,011 | ≤ 3,900 | ~3,720 | ≤ 1,300 |
| 4.8 | 3,753 | ≤ 3,300 | ~3,290 | ≤ 850 |
| 4.9 | 4,496 | ≤ 4,100 | ~4,060 | ≤ 400 |
| 4.10 | 2,429 | ≤ 2,700 | ~2,650 | ≤ 150 |
| 4.11 | 5,616 | ≤ 4,950 | ~4,950 | ≤ 1,100 |
| total, index and 4.1–4.11 | 48,132 | ≤ 44,900 | ~43,200 | ≤ 8,250 (estimate ~7,150) |
| 4.12 (second pass, optional) | 5,178 | unchanged | 5,178 | — |

Every section stays under STYLE's 5,000 main-line words. With exercises included, the whole-file advisory count of `check_structure.py` exceeds 5,000 in most sections, as now; that count is advisory and the binding budget is the main line.

**Exercises after the revision:** 12 A1; 10 A2 drill banks (90 parts: 4.1 12, 4.2 8, 4.3 10, 4.4 10, 4.5 8, 4.6 10, 4.7 8, 4.8 8, 4.9 8, 4.11 8), counted for Time as 22.5 exercises at one per four parts (STYLE §12.8); 35 B (3 new: 4.3 B4, 4.4 B4, 4.7 B4; scaffolded: 4.3 B4, 4.4 B1, 4.5 B1, 4.6 B2, 4.7 B4); 26 C (exit checks 4.9 C2, 4.10 C3, 4.11 C3; one Challenge, 4.2 C1; faded: 4.10 C1); 4 R (4.11). 

**Time (B1 formula: 15 min per 400 main-line words; 20–45 min per exercise; a drill bank counts as one exercise per four parts).** Core track = main line of the index and 4.1–4.11, all of A, one B and one non-Challenge C per section 4.1–4.11 (in 4.9, 4.10 and 4.11 the exit check is that C); 4.12 is optional and off the core track. Reading 43,200 words ≈ 27.0 h; A1 11 × 25 min, A2 22.5 × 30 min, one B 11 × 30 min, one C 11 × 40 min ≈ 28.7 h; **≈ 55.7 h, so "About 56 hours on the core track"** (at the budget ceilings, about 57). Full track: main line plus folds plus 4.12 ≈ 55,500 words ≈ 34.7 h; exercises A1 12 × 25, A2 22.5 × 30, 35 B × 30, 26 C × 40, 4 R × 40 ≈ 53.8 h; **≈ 88.5 h, so "about 90 hours for everything"** (unchanged).

Two honest notes. The current index says "About 70 hours on the core track", but the same formula applied to the current text gives about 47.5 h (reading 48,132 words ≈ 30.1 h; A1, one B, one C per section ≈ 17.4 h); the 70 is not reproducible. The revised figure is higher than 47.5 because the ten drill banks add about 11 hours of core exercises while the folds take about 3 hours of reading off it. The plan's 45-hour target is not reached: the drills cost what the folds save. The drafter recomputes from the delivered text by the same rule (`check_structure.py --words`) and does not shade the number down (STYLE §11.9); §4.0 fixes no figure in advance.

---

## 6. Edits needed outside Chapter 4

No label moves, no section number changes, and no "Section 4.x" mention becomes false by number. These are the edits this revision forces elsewhere, for step R6 (fd1) or the coordinator:

| Where | Now says | Should say |
|---|---|---|
| `authoring/NOTATION.md` row 162 | `\mathrm{Prime}(p)` among the examples of predicate symbols | `\mathrm{Prime}(m)` (Chapter 4 no longer writes primes as \( p \)) |
| `authoring/NOTATION.md` row 163 | variables "(F1.4 §02, with \( \varepsilon, \delta, N, n, k, L \) and \( p, q \) in analysis)" | "(F1.4 §02, with \( \varepsilon, \delta, N, n, k, L \) in analysis)" |
| `authoring/NOTATION.md` row 165 | `\varphi[t/x]` … "the slash is a separator, n[ot division] …" | add: "a term built with an infix operation symbol is written in parentheses, \( \varphi[(y + 1)/x] \) (F1.4 §02); a variable, a constant or \( f(t) \) is written bare" |
| `authoring/STATUS.md` promise row "F1.4 §01, §04, §07, §09, §10 \| … \| F1.5" | the pointers in the running text of §01 (01:246), §04 (04:369), §07 (07:419), §09 (09:118, 09:290, 09:695), §10 (10:83) | the same promises, now carried by the Looking-ahead boxes of §01, §04, §07, §09 and §10 (texts in §4.1, §4.4, §4.7, §4.9, §4.10); content unchanged |
| `authoring/STATUS.md` row "F1.4 §01, §02, §11 \| sets, membership … \| F2.1" | sources §01, §02, §11 | source "F1.4 index (Where this goes)"; the notions are still used informally in §01, §02, §11 |
| `authoring/STATUS.md` row "F1.4 §01, §07, §08, §09 \| school facts about ℝ … \| AN1.1" | sources in the running text | source "F1.4 index (Where this goes)" |
| `authoring/STATUS.md` row "F1.4 §10 \| continuity and uniform continuity … \| AN1.5, AN1.6" | source §10 (10:7) | source "F1.4 index (Where this goes)" |
| fd4 `ch01-complex-numbers/04-square-roots-and-order.md:326` (dependency-ledger comment) | "(fd1 11-models.md ledger line 698)" | "(fd1 11-models.md ledger, the line for `def-satisfaction (solution)`)": the revision shifts line numbers in `11-models.md`; the fd4 text at 04:3 and 04:74 ("Section 4.11 … in one of its checks") stays true, since the Quick check on \( \nC \) stays in 4.11 |

**Mentions checked and left as they are** (each still true of the revised text):
- fd1 Chapter 5: 01:70 (the rule, phrase and Lean table ends Section 4.7: the table and the Lean box are its last subsection); 01:172, 01:189 (the empty-set derivations of Section 4.4, kept on the main line); 02:7, 02:13, 02:57 (the 16-line limit derivation of Section 4.8 and its lines 2–16, 4, 5: verbatim); 02:68, 02:88 (the limit definition, "for all large \( n \)", Section 4.8); 02:102 (mixed chains, Section 4.7: kept); 02:174, 02:178 (the hidden "for every" and "any", Section 4.1: kept); 02:53, 02:187, 03:7, 03:26, 03:214, 03:269, 03:275, 05:25, 05:430, index:7 (Section 4.10's 11-line derivation, line 4, the renamed bound variables: verbatim); 03:462 (the RAA box of `prp-arbitrarily-close-equal`, Section 4.9: verbatim); 04:179 (Section 4.4's prose uses one letter for flag and bound variable: 04:363 kept); 05:12, 05:14, 05:126, 05:335, index:11 (translation and the search method of Section 4.8: kept); 05:444 (bounded sequences, Section 4.6: kept); 06:14, 07:18, 07:77, 07:258 (the soundness statement of Section 4.11: kept); 06:34-37 (Sections 4.4, 4.10, 4.6 and `exm-sum-of-evens`); 06:44, 07:454 (Section 4.9's laws and procedure); 06:248, 06:378.
- fd2: ch01 05:212, 06:51, 06:315, 06:334, 06:556 (Section 4.6's fresh-name condition: verbatim); ch02 01:150 (the maximum of Section 4.7: kept on the main line); ch03 06:281 and 07:94, 07:363-365 (the subsection names and labels of 4.1, 4.6, 4.9, 4.10, 4.11: kept); the ledger lines that name `from-counter-models-to-non-derivability` (ch03 06:333; fd1 ch05 06:393): the id is kept.
- fd3: ch01 01:48 (renaming in Section 4.2, "a letter that appears nowhere": the main line keeps 02:392-394); ch01 01:245 (Section 4.11, domains non-empty: kept); ch04 index:7 and 03 (the negation laws, `exm-translate-limit` (a), the bounded rules, `prp-arbitrarily-close-equal`: verbatim); ch06 05 (`thm-first-order-soundness`: unchanged).
- fd1 Chapters 1–3: ch01's Looking-ahead box ("Chapter 4 gives 'for every' its rules …"), ch02's index note ("Chapter 4 gives them rules"), ch03's 3.3 box and "Where this goes" ("Chapter 4 looks inside atoms"): all still true.
- The about 60 hand-written mentions "*Logic and Proof*, Chapter 4 / Section 4.x" in fd2, fd3, fd4 and an1: the numbers are unchanged; the R7 seam referee reads each against the new text, as the plan says.

**Edits that other blueprints asked of this chapter, made here:** ch03-revision §6 row "fd1 ch04 01:25" (§4.1 item 2); ch02-revision §6 row "ch04 09:700" (§4.9 item 6). Chapter 1's §6 rows for this chapter are already in the current text.

---

## 7. What stays exactly as it is

The square-root argument that truth tables reject (01:5-21) and its four-line derivation (03:85-96); the \( A = \{1, 2\} \) demonstration of \( \to \) under \( \forall \) and \( \wedge \) under \( \exists \) (01:167-172) and its warning; the \( x + y = 0 \) order example and "read the dependency off the order" (01:199-226); \( \exists \) as a long "or" (05:13-17, 06:20); the marking tables for \( \rulename{\exists I} \) and \( \rulename{{=}E} \) (05:47-54, 07:54-63, each without its degenerate last row); the \( 2^3 \) count; every illegal step paired with a reading in which the premises are true and the line false (now also drawn, in 4.3 and 4.6); "Why each clause" with one failure per clause; the three ways to break the limit definition (08:9-11); the prose versions of the long derivations with line references (08:303, 10:81); the search method (08:311-331) and the negation procedure (09:592-604) as reference cards; 4.10 as the centerpiece, its derivation verbatim; the key proofs `prp-exists-forall-swap`, `prp-quantifier-negation`, `exm-uniform-implies-continuous` with their *Before reading on* and *Try it first* prompts; the faded triple (`prp-exists-forall-swap`, 4.6 B2, 4.10 C1); the proof-ordering item (4.10 B2); the exit checks (4.9 C2, 4.10 C3, 4.11 C3) with their marking schemes; the find-the-error items (4.4 C2, 4.6 C2); the R group of 4.11; Section 4.12 entire; every statement and proof of every label in §3.1 marked "kept", "kept verbatim" or "frozen".

---

## 8. S2a: every new or changed claim that needs blueprint verification

**Changed wording in labelled blocks (check that every citation still holds):**
1. `exm-universal-introduction-derivations` (b) replaced by \( \forall x\, (P(x) \to Q(x)), \forall x\, P(x) \vdash \forall x\, Q(x) \) (6 lines; `check_fitch.py` accepts it). The old (b), the front renaming for \( \forall \), is verbatim in fold F4.4-c. Also part (c)'s pointer at 04:234, reworded because the range convention moves after the examples (§4.4 item 9). Check the in-chapter citations: 06:436 (reworded to "the fold after @exm-universal-introduction-derivations"), 08:461, 08:477, 10:99, 10:300 (all about (c), unchanged), 02:396's status paragraph ("that section does it", now in fold F4.2-g: still true).
2. `exr-universal-introduction-a1`'s D3 (\( R(x_0, c) \) in place of \( P(x_0) \)): `check_fitch.py` rejects exactly line 3; the reading over \( \nZ \) (\( R \) as \( < \), \( c = 5 \), \( x_0 = 1 \)) makes line 4 false (\( 6 < 5 \) fails).
3. Bound-letter renamings (\( p, q \) → \( m, n \)): `exm-reading-quantified-sentences` (c) and its solution; the Quick check 01:230-236; `exm-translate-limit` (d), (e) and 08:23; 09:669-680. Each is a renaming of bound variables to letters that appear nowhere in the formula (in (e), \( m \) is new and \( k \) stays), so each sentence is the same up to renaming (Section 4.2); check that no free letter is captured and that the prose names the same objects.
4. `exm-computing-substitutions` (b) written \( [(y + 1)/x] \), and the example moved before `def-substitution`: its solution must read correctly with only the slogan 02:234 before it (it describes which occurrences change and why), and the definition that follows must match each computation.
5. 4.2's main-line statements kept from folded passages: the claim "if \( x \) is not free in \( \varphi \), then \( \varphi[t/x] = \varphi \)" (02:299, its proof in F4.2-e); the shortened definition of "appear" (equivalent to 02:159's first sentence) with "in practice, a fresh letter is one written nowhere yet" (a sufficient condition); the one-sentence statement that induction and recursion carry over (02:106's first sentence).
6. 4.9's split of 09:606 into folds F4.9-a and F4.9-c, with the bridging sentence: together they are the whole argument (both kinds of condition covered), and F4.9-c sits after `prp-quantifier-passage`, so no fold cites a later result.
7. 4.7's main-line statement of the substitution fact \( (\varphi[y/x])[t/y] = \varphi[t/x] \) for \( y \) not appearing in \( \varphi \) (its proof in F4.7-d), which the folded proof of `prp-unique-existence-use` cites; and 4.11's one-sentence meaning of `lem-free-coincidence`.

**New claims and examples in the main text:**
8. The index: the keys-and-locks hook (the second sentence says more than the first; a swap of "every lock" and "some key" turns one into the other); the reading path; "Where this goes" (each pointer: SRC Ch1 sets, membership, \( \emptyset \), pairs, functions; AN Ch1 \( \sqrt 2 \) (`thm-nth-root`), ordered-field facts, the Archimedean property, absolute value; AN Ch5–6 continuity and uniform continuity) against STATUS's rows.
9. 4.1: the letter table (true of the revised chapter: \( p, q, r \) occur only as atoms read by a truth table); world W's six readings and its Quick check; the move table's numbers (\( 5 + (-5) = 0 \); \( -2 + 3 = 1 \)); the two sentences on mixing kinds (consistent with the moved paragraph in 4.8); the translation table (six rows, including "only" and the two "no" forms); Figure K's two verdicts; "the sixth sentence implies the fifth"; the \( \exists x\, (\mathrm{Key}(x) \to \dots) \) slip (true in every building because no lock is a key); the keys-and-locks Quick check.
10. 4.1's game bullets and the caveat remark (same content as 01:221).
11. 4.2: Figure B's arcs (each bound occurrence to the right quantifier; the \( x \) of \( P(x) \) free); the bullets replacing 02:99-104; the practical rule ("if no quantifier above a free \( x \) is on a letter of \( t \), the substitution is safe", which is @def-free-for).
12. 4.3: the three bullets and two sentences (equivalent to clauses 1–5 with 03:47's availability); the bound sentence; the Quick check on \( x + 0 = x \); Figure C3's three worlds (each premise true, each faulty line false); the counter-readings paragraph (no claim that counter-readings are the only route to non-derivability; the soundness statement is in 4.11).
13. 4.4: the minimal derivation (rejected at exactly line 3; the reading at \( x_0 = 1 \)); the practical rule (a never-written flag plus generalizing every occurrence of it makes all three clauses hold); its Quick check; the new (b) with its Givens/Goal table; the two-sentence replacement of 04:319 (VI usable on first-order formulas; the folded justification unchanged); the fine print moved after the examples (04:57 verbatim).
14. 4.5: the three bullets and "Which occurrences?" (equivalent to clauses 1–5; the recipe as in the ledger line for clause 3); the bound sentence; the Quick check (the witness \( 2 + 1 \)); the Givens/Goal table for (d).
15. 4.6: the core wording (two habits make all four clauses hold); the \( n + 2 \) derivation (`check_fitch.py` accepts it; arith \( 2k_0 + 2 = 2(k_0 + 1) \)), its prose table and Quick check; the two sentences replacing "Why early?" (no "loses nothing"); Figure C6's three worlds (clause 3: \( \{0, 6\} \); clause 4: \( \{1, 2\} \) with \( x_0 = 1 \); clause 5: the 3-cycle, every dot with an arrow in, no loop); the Givens/Goal table for `prp-exists-forall-swap`; the decision-chart rows; the reworded 06:206 and 06:432.
16. 4.7: the "mark the holes" display (\( b + b = 2 \cdot b \); \( b + a = 2 \cdot a \)); the =I bullets; the boxes Quick check (\( \varphi = (a \cdot z = z + 1) \)); the warning cut to its reading; the 19-row table's Shape column (consistent with 1.6's and 2.6's cards) and the Lean box (the same commands as 07:421-441).
17. 4.8: the skeleton (every abbreviated line is the written-out line of the full derivation with \( G \), \( G_2 \) folded in; lines 7–12 are the only ones that look inside \( G \) and \( G_2 \)); its Quick check (\( \varepsilon_0/2 \)); step 1 with the moved paragraph.
18. 4.9: the reorder creates no forward citation (the procedure, `exm-negating-definitions`, 09:669-680 and `prp-arbitrarily-close-equal` cite only QN, NIm, the bounded laws, De Morgan, double negation, `prp-iff-two-implications`, `prp-implication-as-disjunction` and the bounded rules, all earlier); 09:700 as worded by ch02-revision; the reworded 09:348 and 09:580.
19. 4.10: the skeleton derivation (`check_fitch.py` accepts it) and the claim that it is `prp-exists-forall-swap` with other letters, same nesting; the five-line count and the line map (skeleton 1 ↔ 4, 2–5 ↔ 6–9, 6 ↔ 10–11); Figure D: \( \delta = \sqrt{x^2 + 1} - x \) is the largest \( \delta \) with \( \abs{y^2 - x^2} < 1 \) for all \( \abs{y - x} < \delta \), at \( x \ge 0 \), and its values \( 1, 0.41, 0.24, 0.16 \) at \( 0, 1, 2, 3 \); the reworded 10:156 and 10:188.
20. 4.11: Figure M's three pictures (each premise true, each conclusion false; (B) with \( R \) as \( > \) on \( \nZ \)); its Quick check; the shortened paragraph replacing 11:265-277 keeps every non-entailment; the kept sentence on non-empty domains; 11:311's addition.
21. The Looking-ahead texts: 4.1 (F1.5 §02 names the hidden "for every" convention, `what-the-sentence-does-not-say`); 4.4 (`exm-not-allowed-catalogue` (N1)); 4.7 (F1.5's phrase dictionary); 4.9 (F1.5 §07's discussion of QN (a) and (N11) of the catalogue); 4.10 (`def-levels-of-proof`, `exm-uniform-four-levels`).
22. The counter-reading convention: every main-line hit listed in §1 item 11 is reworded so that no stalled search is called a proof and no non-derivability claim rests on anything but a counter-reading with the statement of 4.11.

**New and changed exercise answers:**
23. 4.1 A2 (a)–(l).
24. 4.2 A2 (a)–(h); B1 (c), (e) in the parenthesized notation; C1 guided (the given text is the current solution's term, atomic and connective cases, unchanged; the asked part is the quantifier case and (b); the new marking scheme).
25. 4.3 A2 (a)–(j); B4 (9 lines); C2's rebalanced marking scheme after (c) leaves.
26. 4.4 A2 (a)–(j) (each derivation checked by `check_fitch.py`); B1 recast (answer unchanged); B4 (old C2(c) with ∀I now known; the counter-reading at \( x = 2 \)); A1 D3 (item 2); C2(c)'s reworded parenthesis.
27. 4.5 A2 (a)–(h) ((d): \( y \) not free for \( x \) in \( \forall y\, (x = y) \); (h): \( \rulename{\forall E} \) at \( f(x) \), then \( \rulename{\exists I} \) with the witness \( x \)); B1 recast.
28. 4.6 A2 (a)–(j) ((i): the side conditions at lines 6 and 7; (j): line 3 breaks clause 3).
29. 4.7 A2 (a)–(h) ((g), (h) checked by `check_fitch.py`); B4 (9 lines; line 6 is =E 2, 1 with \( \varphi = (a = z) \); line 8 is =E 6, 7 with \( \varphi = (z = a) \)).
30. 4.8 A2 (a)–(h).
31. 4.9 A2 (a)–(h) ((b): both positive forms equivalent; (c), (e), (h): the order facts named).
32. 4.11 A2 (a)–(h) ((g): \( P^{\fM} = \emptyset \) is allowed by (M4)).

**Routes to confirm do not rest on folded or removed material:** every statement a later proof cites stays on the main line (§3.1; items 5, 7); every A and B exercise is doable with the folds closed (4.2 B2 from `def-free-variable` and the parse tree; 4.6 A1(b) by trying the other nesting, which stays on the main line; 4.7 B1 from the statement of `prp-unique-existence-use`); no fold holds a section's only Quick check or only warning.

---

## 9. Decisions recorded in this file

- **D1 (4.2's core is ~3,900 words, not 2,500).** STYLE §12.0 forbids folding a cited statement or a definition the main line uses; the six definitions and the claim stay, with only their commentary folded (§4.2, recorded deviation).
- **D2 (4.9 keeps the bounded laws before the negation procedure).** The procedure cites them; the passage and distribution laws move to the end instead (§4.9, recorded deviation).
- **D3 (abbreviations live in skeletons).** The 16-line limit derivation (4.8) and the 11-line centerpiece (4.10) stay verbatim: Chapter 5 cites and copies them by line number, and `check_fitch.py` checks only written-out formulas. The plan's named matrices \( G \), \( G_2 \) and \( K \) appear in a skeleton display beside each.
- **D4 (the one-domain convention).** Its full paragraph moves to 4.8 (step 1 of the translation procedure); 4.1 keeps two sentences, because 4.2's limit example, its shorthand for \( a_n \), and 10:7 use the convention before 4.8.
- **D5 (the minimal open-assumption counterexample).** `check_fitch.py` rejects exactly the intended line in the minimal form (checked; the form is already exercise A1's D3), so `ch04.md`'s S3 reason for the nested form no longer holds. The nested derivation is kept verbatim in a fold, and D3 gets a new formula so that it does not repeat the main line.
- **D6 (cards).** Chapter 4's cards carry a Side condition column; the card after 4.6 is the cumulative quantifier card with the decision chart's quantifier rows; 4.7's table of the whole calculus is the volume's one-page reference, with the Lean column collapsed into a box.
- **D7 (drill banks)** in 4.1–4.9 and 4.11; none in 4.10 (the centerpiece) or 4.12 (second pass).
- **D8 (letters).** \( p, q \) leave the chapter as variables by renaming bound variables, which changes no content; compound terms are parenthesized in substitutions only when built with an infix symbol.
- **D9 (counter-readings).** The disclaimer about stalled searches is made once, in 4.3, with a name; Section 4.11's opening and its last subsection remain the place where the statement is given.
- **D10 (snapshots on two (ii)-exempt derivations).** The first flagged box (4.4, the \( x^2 - 2x + 1 \) derivation) and the first \( \rulename{\exists E} \) box (4.6, \( n + 2 \)) get snapshots although each translates prose above it, because each is the reader's first sight of its box.
- **D11 (4.7's second half).** The proof of `prp-unique-existence-use` (two long derivations) is folded verbatim; its statement, meaning and Idea stay. The reading path marks unique existence as second reading; fd2 cites the statement, which stays on the main line.
- **D12 (Time).** About 56 hours on the core track by the B1 formula (§5); the plan's 45 is not reached, and the printed 70 is not reproducible from the current text.
