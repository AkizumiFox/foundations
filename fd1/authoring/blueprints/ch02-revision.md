<!-- hand-written -->
# Revision blueprint: F1.2 Negation, Classical Logic and Finding Derivations (fd1 Chapter 2), R3

**What this is.** A **delta** blueprint (stage S1) for revising the released Chapter 2 of *Logic and Proof* so that a first-year reader gets in more easily, in the register of the approved Chapter 1 pilot (`ch01-revision.md`, delivered in `fd1/src/ch01-connectives-and-derivations/`). It is complete on its own: a drafter executes it with this file, the current `fd1/src/ch02-negation-and-classical-logic/`, the original blueprint `fd1/authoring/blueprints/ch02.md` (for anything this file does not change), `authoring/STYLE.md` (§12 above all), `DRAFTING.md` and `NOTATION.md`. All line numbers below are of the **current** files (HEAD `70e64bc`; the chapter last changed in `086a23a`), written `05:79` for `05-reductio-and-classical-rules.md` line 79, and so on.

**Inputs.** The novice-reader report on Chapter 2 (journal `wf_d5bd0807-139`, result `novice:ch02`), the fd1 revision plan (§2 Chapter 2 rows, §3 volume-wide conventions and Chapter 2 changes, §4–§6), the delivered Chapter 1 and its revision blueprint with its S3/S7 deviation notes, and greps of fd1, fd2, fd3 and an1 (2026-10-12). Reference books were used for teaching technique only. **Every example, drill and exercise below is the book's own.** The review rule of `ch02.md` still binds: no example, sequent list or exercise of Huth & Ryan §1.2 comes back (S2 checks every new drill sequent against it and replaces any match).

**Binding rules for this revision.**
1. **No label is lost.** Every label now in the chapter survives, in this chapter and in the same section. The only label whose item changes is the uncited `exr-reductio-and-classical-rules-b4`, reused for a new item (§3). No label is renamed or retired.
2. **Reviewed content of cited results does not change**, except where this file says so and lists the item for S2a (§8). Moving a passage into a Second-reading fold verbatim is not a change. Every statement and proof of a label cited outside Chapter 2 (§3) keeps its content; where its proof is folded (`prp-provable-equivalence-basics`, `prp-peirce`, `thm-classical-rules-interderivable`) it moves verbatim.
3. **Forward references.** No `@ref` to a later chapter survives anywhere in the chapter's main line, folds or solutions (list in §1.8). Each section's main line and folds carry **at most one** forward pointer, in its Looking-ahead box; every other plain pointer to a later chapter or volume in them is cut or reworded as a non-promise (the section plans name each). Plain pointers inside exercise solutions stay only where this file keeps them. No forward pointer is ever used as a **reason**: where the text now argues "the rules never lead from true premises to a false conclusion (Chapter 3 proves this)", it argues instead with Section 1.1's move *try to break it* (a row that makes the premises true and the line false), and claims only that the step can be broken, never that no derivation exists.
4. **Chapter 2's section numbers and section files do not change.** Every hand-written "Section 2.x" in Chapters 3–5, fd2, fd3 and an1 stays true; §6 lists the sentences around them that need a word changed.
5. **Depends on R0 and R1**, as Chapter 1 did: the fold, drill-bank, Challenge and Looking-ahead markup is STYLE §12's, as Chapter 1 delivered it (`::: {.second-reading title="…"}`; `::: {.remark}` opening `[Looking ahead]`; `[A2: Drill]`).

---

## 1. The volume-wide conventions, as applied to Chapter 2

Chapter 1's §1 (conventions 1–14 of `ch01-revision.md`) applies unchanged, with these Chapter 2 specifics.

1. **Second-reading folds.** Every fold is listed by current file:line in its section's plan; nothing else goes into a fold. No fold holds a statement a later proof cites, a definition the main line uses, or a section's only Quick check or warning. Folded proofs of cited results move **verbatim**.
2. **Looking ahead.** At most one per section, the last thing before `## Exercises`, `::: {.remark}` opening `[Looking ahead]`, one or two sentences, no `@ref`. The texts are given per section. After drafting, the drafter greps each section's main line and folds for `Chapter [3-9]`, `Section [3-9]\.`, `Sets, Relations`, `Analysis on the Real Line` and `@(thm|cor|lem|def)-` labels of Chapters 3–5, and cuts or rewords every hit other than the box.
3. **The global quantifier note** (STYLE §12.1) goes in `index.md` (§4.0) and replaces the per-proof caveats "this is a step about 'there exists'/'every'; Chapter 4 gives its rules" at 01:281, 01:345, 02:275, 04:359, 05:23, 05:619, 06:487, A1(b)'s solution in 2.6 (06:713). Where a sentence must still say that a step is about "every" or "some" (01:345, 02:275, 05:619), it ends "used as ordinary reasoning (the note at the start of this chapter)", with no chapter named.
4. **Effort in proportion to difficulty** (STYLE §12.2). ¬I and RAA keep the full clause-by-clause reading and are introduced by *"This rule has conditions that matter; read each one."* ¬E gets **four bullets**, as →E did in 1.3 (the given lines, exactness, the citation order, the new line); ⊥E gets **three bullets** (schema, reading, example). ↔I/↔E keep their four short numbered clauses (04:50-53), which already are one line each. A derived rule (MT, CP, DS, ¬¬I, ¬¬E, LEM) gets its schema and one line, as now.
5. **Snapshots** (STYLE §12.4). Chapter 1's convention 4 applies with its exemption classes (i)–(vi), quoted here by number. Every other main-line derivation of four or more lines gets **two snapshots** in its Idea, listed per section, in the markup Chapter 1 delivered (`% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)`, gap rows `\have[\ ][0] {} {\vdots}`, every written line carrying its final number). A snapshot below is written `S1`/`S2`, listing what stands on the page; "unjustified" means the line is written as a goal with no justification yet.
6. **Givens/Goal table** (STYLE §12.5). Each rule section says in one line what its rule does to the table (texts per section); full tables are drawn in 2.6 (two) and nowhere else in this chapter.
7. **Rule card** (STYLE §12.6). The run of rule sections is Chapter 2. Each section 2.1–2.5 replaces its "What the rule(s) sound like" table by a card, columns `Rule | Shape | You write | Lean`, with one row per rule **of Chapter 2 so far**, under the lead sentence "Chapter 1's seven rules are on the card at the end of Section 1.6; here are this chapter's so far." The full cumulative card, all thirteen primitive rules, is 2.6's one-page reference (§4.6). Derived rules are marked "(derived)" in the Shape column. The Lean entries are the current ones (01:413-414, 02:287, 03:354-356, 04:465-466, 05:640-642), and each section keeps its Lean sentence (01:416, 02:289, 04:461's last sentence).
   The rows, used cumulatively:
   | Rule | Shape | You write | Lean |
   |---|---|---|---|
   | ¬E | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
   | ⊥E | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
   | ¬I | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
   | MT (derived) | \( \varphi \to \psi \), \( \neg\psi \) \( \Longrightarrow \) \( \neg\varphi \) | "Since \( Q \) fails, so does \( P \)." | `mt h hnq` |
   | CP (derived) | \( \varphi \to \psi \) \( \Longrightarrow \) \( \neg\psi \to \neg\varphi \) | "We prove the contrapositive: suppose not \( Q \); … so not \( P \)." | `mt` |
   | DS (derived) | \( \varphi \vee \psi \), \( \neg\varphi \) \( \Longrightarrow \) \( \psi \) | "\( P \) is impossible, so \( Q \)." | `h.resolve_left hnp` |
   | ↔I | box \( \varphi \) … \( \psi \), box \( \psi \) … \( \varphi \) \( \Longrightarrow \) \( \varphi \leftrightarrow \psi \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." | `constructor` |
   | ↔E | \( \varphi \leftrightarrow \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) (or with \( \psi \), \( \varphi \)) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." | `h.mp hp` / `h.mpr hq` |
   | RAA | box \( \neg\varphi \) … \( \bot \) \( \Longrightarrow \) \( \varphi \) | "Suppose, for a contradiction, that \( P \) fails. … This is impossible. Hence \( P \)." | `by_contra h` |
   | ¬¬E (derived) | \( \neg\neg\varphi \) \( \Longrightarrow \) \( \varphi \) | "It cannot be that \( P \) fails; so \( P \)." | `not_not.mp h` |
   | LEM (derived) | nothing \( \Longrightarrow \) \( \varphi \vee \neg\varphi \) | "Either \( P \) or not. If \( P \), … If not, … In either case, …" | `by_cases h : P` |
8. **Forward `@ref`s removed** (each replaced as the section plan says): index.md:5 `cor-refuting-row`; 01:60 `thm-soundness`; 01:401 `def-truth-value`; 02:45, 02:66 `thm-soundness`; 04:227 `thm-raa-independent`; 04:273 `thm-soundness`; 05:37 `thm-raa-independent`; 05:309 (in prose) the remark after `thm-raa-independent`; 06:76, 06:286, 06:466 `cor-refuting-row`; and in solutions 05:671 (A1(e)) and 05:924 (C2(c)) `thm-soundness`, 06:1019 (C2(b)) and 06:1234 (R3) `cor-refuting-row`.
9. **Quick-check density** (STYLE §12.7): about one per 800–1,000 main-line words; the new checks are written out per section.
10. **Drill bank** `exr-<slug>-a2`, `[A2: Drill]`, 10–11 lettered parts, recall and judgement first, then the illegal line, then 2–6-line derivations, one folded solution answering every part in one or two lines. **Scaffolded B** items as Chapter 1's: premises and the last line shown, the gap marked, lines numbered as at the end, "*Name the move, then complete it.*".
11. **Conventions on order and equality** (new box in 2.1, §4.1 item 3) sit beside Chapter 1's ≤/≥ box (1.5) and are reused through the chapter: a derivation writes \( \neg(a < b) \) where ¬E or ¬I must see the negation, and prose keeps \( a \ge b \).

---

## 2. Section map

| Sec | Title (the `#` line) | File | Kind | Notes |
|---|---|---|---|---|
| index | Negation, Classical Logic and Finding Derivations | `index.md` | rewritten | three questions first; the quantifier note; terms move to the Roadmap; named moves with sections |
| 2.1 | Contradiction: Using a Negation | `01-contradiction-and-vacuous-truth.md` | rewritten | ⊥E intuition right after the schema; ¬E in four bullets, ⊥E in three; the order/equality convention box; "two more observations" folded; the x < 1 / x > 1 encoding becomes a drill |
| 2.2 | Proving a Negation | `02-negation-and-contradiction.md` | rewritten | `exm-square-plus-one` first, with a new 5-line derivation; then \( P \vdash \neg\neg P \); triple negation after; the two ¬¬(x > 0) warnings become one sentence |
| 2.3 | Derived Rules: Proved Sequents as New Rules | `03-derived-rules.md` | edited | side-by-side MT / expansion figure; "convenience, not power" folded; the four cards as a table; prose payoff before the kept 13-line derivation; the x³ warning moves to 2.5 |
| 2.4 | Iff, Equivalence, and What a Definition Says | `04-biconditional-and-definitions.md` | edited | ⊣⊢: definition, meaning, the \( P \wedge Q \) / \( Q \wedge P \) instance, proof folded; school-level converse warning; B3 split, new scaffolded B4 |
| 2.5 | Proof by Contradiction and the Classical Rules | `05-reductio-and-classical-rules.md` | rewritten | opens with the quantifier-free \( x^2 \le x \Rightarrow x \le 1 \); the single home of ¬I vs RAA, with the x³ proof both ways; Peirce's derivation folded; the cycle diagram and ②, ③ on the opening example, the schematic proof folded; C1(b) cut |
| 2.6 | How to Find a Derivation | `06-finding-derivations.md` | edited | gaps met on a snapshot before the definition; the check moved after its example; step 2 without the forward exception; three bullets plus a fold for the order; Peirce's search as two snapshots; the failed search as a table; the cumulative rule card, decision chart and named moves |

No file is added, deleted or renamed. The atlas entry F1.2, the chapter title and every section title stay.

---

## 3. Labels

### 3.1 Every label now in the chapter

Citation counts are `@label` / `@fd1:label` hits outside Chapter 2, as fd1 Ch1+Ch3–5 / fd2 / fd3 / an1 (grep of 2026-10-12; no fd1 Ch1 hit exists). "In ch02" lists the citing places inside the chapter for labels with none outside. Status: **kept** = label and content unchanged; **kept (moved)** = unchanged, moved within its section; **kept (folded)** = statement on the main line, named part moved verbatim into a fold; **edited** = content changed, listed in §8.

| Label | Now | fd1/fd2/fd3/an1 | In ch02 | Status |
|---|---|---|---|---|
| `def-rules-contradiction` | 01:24 | 3/1/0/0 | 02:38, 05:3, 06:575 | kept |
| `exm-first-contradictions` | 01:84 | — | — | kept; snapshots for (b) |
| `prp-ex-falso` | 01:125 | 7/0/0/0 | 06:667 | kept |
| `prp-vacuous-implication` | 01:154 | 13/6/0/1 | 03:124, 05:469, 06:668, 06:759, 06:1198 | kept; snapshots in Idea |
| `exm-manufactured-clash` | 01:188 | 2/0/0/0 | 02:140, 02:160, 05:232 | kept; snapshots |
| `exm-impossible-case` | 01:221 | — | 03:3, 03:158, 03:185, 04:289, 05:602 | kept; snapshots |
| `thm-square-even-implies-even` | 01:283 | 16/3/2/0 | 02:221–489 (16), 03:288, 03:330, 04:564–591 (3) | kept (statement, proof, derivation, table verbatim) |
| `exm-vacuous-square` | 01:365 | — | 03:124 | kept |
| `exr-contradiction-and-vacuous-truth-a1` … `-b3` | 01:422–512 | — | — | kept |
| `exr-contradiction-and-vacuous-truth-c1`, `-c2` | 01:542, 01:576 | — | — | kept |
| `def-rules-negation` | 02:15 | 4/1/7/2 | 03:13, 03:463, 05:3, 05:9, 05:146, 06:575 | edited: block verbatim; clause 3's last sentence (02:45) and 02:66's last sentence cut (pointers), §8 item 2 |
| `exm-double-negation-introduction` | 02:91 | 2/0/0/0 | 03:144, 03:265, 04:227, 05:79, 05:146, 06:677 | kept; snapshots |
| `exm-triple-negation` | 02:165 | 1/0/0/0 | — | **kept (moved)** after `exm-square-plus-one`; ch05 07:433 uses its derivation without RAA and ch05 07:417's hint looks for it in Section 2.2, so it stays on 2.2's main line (the plan's "B exercise" is not taken, §9 D1) |
| `exm-square-plus-one` | 02:205 | 0/0/0/1 | — | **edited, moved** to right after the rule: statement unchanged, prose solution unchanged, a 5-line derivation added (§8 item 6); an1 01:117 cites it for \( x^2 \ge 0 \) as school algebra, still true |
| `thm-sqrt2-irrational` | 02:227 | 20/4/4/20 | 05:9, 05:624, 05:631 | kept (key proof; statement, Idea, proof, derivation verbatim) |
| `exr-negation-and-contradiction-a1` | 02:295 | — | — | kept (key-proof comprehension) |
| `exr-negation-and-contradiction-b1` | 02:321 | — | — | edited: recast as the section's scaffolded B, same sequent and answer |
| `exr-negation-and-contradiction-b2`, `-b4`, `-c2` | 02:351, 02:405, 02:470 | — | — | kept |
| `exr-negation-and-contradiction-b3` | 02:371 | — | 04:564, 04:584, 04:591 | **frozen** |
| `exr-negation-and-contradiction-c1` | 02:435 | 0/0/0/2 | — | **frozen** (an1 07:457, 07:459) |
| `prp-modus-tollens` | 03:21 | 1/0/0/0 | 04:107, 06:669 | kept; snapshots |
| `prp-contrapositive` | 03:56 | 19/4/4/3 | 04:227, 04:346, 05:185, 06:479, 06:483, 06:670, 06:679 | kept |
| `def-derived-rule` | 03:100 | 20/4/0/0 | 04:258, 04:548, 05:183, 06:657 | kept, block verbatim; clause 2's last sentence (03:120) moves to the Looking-ahead box |
| `prp-disjunctive-syllogism` | 03:151 | 4/0/0/0 | 04:452, 05:617, 06:313, 06:483, 06:671 | kept (left disjunct, as stated; §9 D2) |
| `exm-derived-rules-in-use` | 03:189 | — | — | kept; snapshots for (a), (b) |
| `exm-modus-tollens-instance` | 03:272 | — | — | kept |
| `exm-square-even-via-contrapositive` | 03:290 | 2/1/0/0 | — | kept verbatim, including line 11 "or commutes" (ch05 01:7 reprints this derivation; ch05's ledger reads its line 11) |
| `exr-derived-rules-a1`, `-b2`, `-c2`, `-c3` | 03:362–606 | — | — | kept (C3 is an exit check) |
| `exr-derived-rules-b1` | 03:409 | — | 06:672 | **frozen** |
| `exr-derived-rules-b3` | 03:466 | — | — | edited: recast as the section's scaffolded B, same sequent and answer |
| `exr-derived-rules-c1` | 03:503 | — | 05:32 | **frozen** |
| `def-rules-biconditional` | 04:11 | 1/1/0/0 | 05:749, 06:602 | kept |
| `exm-iff-symmetric` | 04:59 | — | 06:673 | kept; snapshots for (a) |
| `prp-iff-two-implications` | 04:112 | 2/7/0/0 | 06:674 | kept; snapshots in Idea |
| `exm-iff-negations` | 04:170 | 0/3/0/0 | 05:33, 05:778, 06:675 | kept; snapshots |
| `def-provable-equivalence` | 04:217 | 1/0/0/0 | — | kept |
| `prp-provable-equivalence-basics` | 04:231 | — | — | **kept (folded)**: statement + one-sentence meaning on the main line; Idea and proof verbatim into fold F2.4-b |
| `thm-odd-iff-square-odd` | 04:282 | — | — | kept |
| `thm-squares-order` | 04:304 | 1/7/0/0 | — | kept (statement, Idea, proof, remark verbatim) |
| `exm-strictly-increasing-both-ways` | 04:361 | 1/0/0/0 | — | kept |
| `prp-equivalence-cycle` | 04:393 | 0/0/0/2 | 06:676 | kept; snapshots |
| `exm-unit-interval-tfae` | 04:435 | — | — | kept |
| `exr-biconditional-and-definitions-a1`, `-b1`, `-b2`, `-c1`, `-c2` | 04:472–598 | — | — | kept |
| `exr-biconditional-and-definitions-b3` | 04:541 | — | — | edited: split into scaffolded parts, same content and answer |
| `exm-raa-zero` | 05:13 | 2/0/0/0 | 05:614 | **kept (moved)** to "How reductio looks in a mathematical proof"; statement and solution verbatim; 05:23 cut (ch04 03:10, 09:700 cite it; §6) |
| `def-rule-raa` | 05:43 | 6/3/11/1 | 06:635 | kept, block verbatim |
| `prp-double-negation` | 05:128 | 7/1/0/0 | 06:677, 06:678 | kept |
| `prp-contrapositive-converse` | 05:187 | 10/2/0/0 | 06:679 | kept; snapshots; 05:221's last sentence moves to fold F2.5-c |
| `prp-excluded-middle` | 05:225 | 15/9/0/0 | 06:680 | kept; Idea's "(… Chapter 3 makes this exact)" reworded (§8 item 20); snapshots |
| `prp-peirce` | 05:266 | 3/0/0/0 | 06:439, 06:681 | **kept (folded)**: statement + one-sentence meaning on the main line; Try-it-first, Idea, proof and 05:309 verbatim into fold F2.5-b, 05:309's last parenthetical to the Looking-ahead box |
| `prp-de-morgan` | 05:315 | 15/8/7/0 | 06:682, 06:688, 06:1198 | kept (key proof); statement and proofs verbatim; the Idea's soundness clause reworded (§8 item 21); snapshots |
| `prp-implication-as-disjunction` | 05:457 | 4/0/0/0 | 06:683 | kept; snapshots |
| `thm-classical-rules-interderivable` | 05:537 | 4/0/0/0 | — | **kept (folded)**: 05:533-535 (the rule forms and "X derives Y"), statement, one-sentence meaning on the main line; Idea and proof verbatim into fold F2.5-d (key proof: comprehension moves to the main-line instance, §4.5) |
| `exr-reductio-and-classical-rules-a1` | 05:648 | — | — | edited: (e)'s solution without `@thm-soundness`; (g) reworded to the main-line instance of ② |
| `exr-reductio-and-classical-rules-b1` | 05:680 | 2/0/0/0 | — | **frozen** (ch05 07:400, 07:425 use (a)'s printed solution) |
| `exr-reductio-and-classical-rules-b2` | 05:742 | — | 06:675 | **frozen** |
| `exr-reductio-and-classical-rules-b3` | 05:781 | — | — | kept |
| `exr-reductio-and-classical-rules-b4` | 05:806 | — | — | **old item promoted to the main line** (it becomes the opening example and the instance of ②); the uncited label now carries a new scaffolded item (§4.5) |
| `exr-reductio-and-classical-rules-c1` | 05:835 | — | — | edited: part (b) cut; titled `[C1: Challenge: Excluded middle does the work of reductio directly]` |
| `exr-reductio-and-classical-rules-c2` | 05:885 | — | 06:962 | **frozen** except (c)'s solution, which loses `@thm-soundness` (§8 item 33; the label's content, the find-the-error item, is unchanged) |
| `exr-reductio-and-classical-rules-c3` | 05:955 | — | — | kept (exit check) |
| `def-partial-derivation` | 06:29 | — | — | kept, block verbatim (moved after the first snapshot) |
| `exm-search-distribute` | 06:99 | — | 06:42 | kept (faded triple, full) |
| `exm-search-cases` | 06:192 | 1/0/0/0 | — | kept; a first snapshot added |
| `exm-search-postpone-or` | 06:253 | 1/0/0/0 | — | kept; 06:286's `@cor-refuting-row` parenthetical cut |
| `exm-search-raa` | 06:355 | — | 06:1077 | kept |
| `exm-skeleton-odd-product` | 06:472 | — | — | kept; Givens/Goal table added; 06:487's last parenthetical cut |
| `exr-finding-derivations-a1`, `-b2`, `-b3`, `-c1`, `-c3`, `-c4`, `-r1`, `-r2` | 06:695–1161 | — | — | kept (C3's solution: one pointer reworded, §8 item 38) |
| `exr-finding-derivations-b1` | 06:726 | 2/0/0/0 | — | **frozen** |
| `exr-finding-derivations-c2` | 06:965 | 2/0/0/0 | — | **frozen** except (b)'s solution, which loses `@cor-refuting-row` (plain "Chapter 3" kept) |
| `exr-finding-derivations-r3` | 06:1201 | — | — | kept; solution loses `@cor-refuting-row` (plain "Chapter 3" kept) |

### 3.2 New labels

`exm-raa-at-most-one` (2.5); `exr-contradiction-and-vacuous-truth-a2`, `-b4`; `exr-negation-and-contradiction-a2`; `exr-derived-rules-a2`; `exr-biconditional-and-definitions-a2`, `-b4`; `exr-reductio-and-classical-rules-a2` (and the reused `-b4`); `exr-finding-derivations-a2`. No new `def-`, `prp-` or `thm-` label. Each was grepped absent from `fd1/src` on 2026-10-12; the drafter greps again before creating it.

### 3.3 Bookkeeping (coordinator, S4)

- `fd1/authoring/ledger/ch02.yaml`: no key changes except `exr-reductio-and-classical-rules-b4`, whose old entry is retired to `fd1/authoring/ledger/archive/ch02-r3-retired.yaml` (the label string now carries a different item: a new entry, no verdict carried) and a new entry `exm-raa-at-most-one`. Every touched block's hash changes; verdicts go stale and are re-earned (S5–S8). Recast items (`exr-negation-and-contradiction-b1`, `exr-derived-rules-b3`, `exr-biconditional-and-definitions-b3`, `exr-reductio-and-classical-rules-c1`) keep their keys with stale verdicts, as Chapter 1's deviation note did for `exr-disjunction-and-cases-b3`.
- `fd1/verify/ch02/`: `exr-reductio-and-classical-rules-b4.py` is rewritten for the new B4 (no numeric content; it may be deleted if the item quotes no values), and its old values (\( x > 1 \Rightarrow x > 0 \), \( x^2 > x \)) move to a new `exm-raa-at-most-one.py`. New sidecars are listed per section.
- Dependency ledgers: every line whose source is "F1.3 (promised; thm-soundness …)" for a sentence this file rewords as *try to break it* becomes "inline (a row that breaks the step; no claim about derivations)". Lines for passages moved into folds stay, with the same source.

---

## 4. Per-section plans

Budgets: **main line** = prose words by `tools/check_structure.py`'s `prose_words`, counted outside `.second-reading` folds and **before `## Exercises`**; current counts are of the same span. Exercises are budgeted separately. Totals and Time in §5.

### 4.0 `index.md` (rewritten)

1. **Opening** (replaces index:3-5; ~170 words). Three questions, each one sentence: Is there a rational number whose square is \( 2 \)? Is \( x^2 + 1 \) ever \( 0 \) for a real number \( x \)? Is "if \( x^2 < 0 \), then \( x = 7 \)" true? Then index:3's last two clauses kept in substance: Chapter 1 could prove that things are so, not that something is **not** so; it read the third sentence only informally, as a promise not broken, and no rule yet derives it. Then the promise, in plain words: "By the end of this chapter you will be able to prove that something is not so; you will know when 'suppose not' is a different kind of step from the others; and you will have a method for finding derivations. You will also meet a question the method cannot answer: we show that something is derivable by exhibiting a derivation, but how could we show that something is **not** derivable? Chapter 3 answers it." (No `@ref`.)
2. **Steps about "every" and "some"** (new, bold lead-in paragraph after the opening; the global note, STYLE §12.1): "Proofs in this chapter apply facts about every integer to one integer, pass from an arbitrary rational number to all of them, and name the \( k \) in '\( n = 2k + 1 \)'. These are steps about 'every' and 'some'. Here they are used as ordinary reasoning, as in school algebra; Chapter 4 gives them rules."
3. **What you need:** index:7 kept.
4. **Time:** recomputed from the delivered text (§5); the estimate is about 30 hours core, about 50 for everything.
5. **Roadmap:** six bullets, one or two sentences each, now carrying the terms index:5 named: 2.1 ¬E and ⊥E, clashes, the impossible case, vacuous truth; 2.2 ¬I and the irrationality of \( \sqrt2 \); 2.3 a proved **sequent used as a rule**, with modus tollens, the contrapositive and disjunctive syllogism; 2.4 the rules for ↔, provable equivalence, the "if" of a definition, chains of equivalences; 2.5 RAA, the classical laws (**double-negation elimination**, **excluded middle**, De Morgan, Peirce), and why three of them **stand or fall together**; 2.6 the search method, a search that fails, and every rule on one page.
6. **Named moves:** the seven of index:22-28, verbatim, each followed by its section: (2.1), (2.1), (2.2), (2.3), (2.4), (2.5), (Sections 1.2 and 2.6). Then: "The chapter's moves are collected again at the end of Section 2.6, beside the rules that make them."

### 4.1 Section 2.1: Contradiction: Using a Negation (`01-contradiction-and-vacuous-truth.md`)

**Budget:** main line ≤ 3,200 words (now 3,507); folds ≤ 450. Looking ahead: item 9.

**New order of material.**
1. 01:3 and `## A case that cannot occur` 01:5-16 kept.
2. `## The rules for a clash`: 01:20-22 and `def-rules-contradiction` verbatim. **Then at once (new, ~70 words), "Why may ⊥E write anything?":** "A line \( \bot \) can stand only in a box whose assumptions cannot all hold together: a box that reaches \( \bot \) describes a situation that never happens. Nothing said there can ever be caught false, just as a promise whose condition is never met is never broken; the subsection 'Vacuous truth' below makes this exact." Then the readings, replacing 01:46-56: one sentence for 01:46 ("As in every schema (@def-rule-schema), \( \varphi \) is one statement, the same wherever it occurs, and \( i, j, k \) are line numbers.") and
   - **¬E in four bullets.** *Two given lines,* both available (the scope rule of @def-derivation), in either order on the page. *Exactly* \( \varphi \) and \( \neg\varphi \): the second is the first with one \( \neg \) in front of the whole of it, symbol for symbol; "contradicts it in spirit" is not enough (\( x < 1 \) and \( x > 1 \): the box below). *The citation* lists the unnegated line first: "¬E \( i, j \)" says line \( i \) is \( \varphi \). *The new line* is \( \bot \) and nothing else; what to do with the clash is ⊥E's business.
   - **⊥E in three bullets.** *Schema:* the right one in the block above. *Reading:* one available line \( \bot \), cited alone; write **any** statement, related to nothing above, a negation or \( \bot \) itself included. *Example:* from line 4 \( \bot \), "⊥E 4" writes \( R \), or \( \neg R \), or \( x = 7 \).
   
   Then one line, *Why is this honest?*: "A line \( \bot \) stands only where the premises and open assumptions cannot all hold, so a line that ⊥E writes there can never be caught false." Then **fold F2.1-a**. Then the Givens/Goal sentence (convention 6): "In the Givens/Goal table, ¬E adds \( \bot \) to the Givens once \( \varphi \) and \( \neg\varphi \) are both there; and with \( \bot \) among the Givens, ⊥E ticks off any goal."
3. Quick check 01:62-68 kept. 01:70 **replaced by the convention box** (`::: {.remark}`, first words `**Convention: negations of order and equality.**`, ~120 words): "For real numbers \( a \) and \( b \), exactly one of \( a < b \) and \( a \ge b \) holds. So \( a \ge b \) says the same as \( \neg(a < b) \), and likewise \( a > b \) the same as \( \neg(a \le b) \), \( a \le b \) as \( \neg(a > b) \), and \( a < b \) as \( \neg(a \ge b) \); and \( a \ne b \) **means** \( \neg(a = b) \), by definition. A derivation writes the negation out whenever ¬E or ¬I must see it; otherwise, and in prose, the short forms stay. Together with the box of Section 1.5, which writes \( a \le b \) out as \( (a < b) \vee (a = b) \) when ∨I or ∨E must see the disjunction, this fixes how an inequality looks on a line." Then the last two sentences of 01:70 as prose (the parity fact \( \neg(E \wedge O) \) clashes only with \( E \wedge O \), built by ∧I). **Quick check (new):** "For a real number \( x \), which pairs are a clash as written, once the convention is used? (i) \( x^2 < 0 \) and \( x^2 \ge 0 \); (ii) \( x = 2 \) and \( x \ne 2 \); (iii) \( x < 1 \) and \( x > 1 \)." Solution: (i) yes, \( x^2 \ge 0 \) is \( \neg(x^2 < 0) \), cite \( x^2 < 0 \) first; (ii) yes, \( x \ne 2 \) is \( \neg(x = 2) \); (iii) no: \( x > 1 \) is \( \neg(x \le 1) \), and \( x < 1 \) is not \( x \le 1 \); the line \( x \le 1 \), written out, must first be built by ∨I (drill A2(f)).
4. Warning 01:72-74 **cut to** its first sentence and its last ("A clash must have the exact shape \( \varphi \), \( \neg\varphi \). … And some pairs that look opposed do not clash at all: \( x \ge 1 \) and \( x \le 1 \) both hold at \( x = 1 \)."); the construction in between becomes drill A2(f). Warning 01:76-78 kept.
5. `## First derivations with a clash`: 01:82 kept. `exm-first-contradictions` kept; (b)'s Idea gains **two snapshots**: S1 lines 1–2, gap, line 5 \( R \) unjustified; S2 lines 1–2, gap, line 4 \( \bot \) unjustified, line 5 \( R \) ⊥E 4 (the goal replaced by \( \bot \)). (a) is exempt (i). 01:120, 01:123 and `prp-ex-falso` kept (exempt (iii): "the pattern of (b) with nothing extra around it"). `prp-vacuous-implication`, statement and proof verbatim; its Idea gains **two snapshots**: S1 line 1, box opened with line 2 \( P \), gap, line 4 \( Q \) unjustified, line 5 \( P \to Q \) →I 2–4; S2 the same with line 3 \( \bot \) unjustified above line 4 \( Q \) ⊥E 3 (the clash named as the subgoal). 01:184, 01:186 kept. `exm-manufactured-clash`, its Idea gaining **two snapshots**: S1 line 1, box 2 \( P \), gap, line 5 \( R \), line 6 →I 2–5; S2 box 2 \( P \), gap, line 4 \( \bot \) unjustified, line 5 \( R \) ⊥E 4 (the premise now asks for \( P \vee Q \)). **Quick check (new)** after its solution: "Inside the box of \( P \), could ⊥E write \( R \) straight from line 2? Which lines must come first?" Solution: no; ⊥E needs a line \( \bot \), and \( \bot \) needs the pair \( P \vee Q \), \( \neg(P \vee Q) \): first \( P \vee Q \) by ∨I 2, then \( \bot \) by ¬E 3, 1. 01:219, `exm-impossible-case` with **two snapshots** (S1 lines 1–3, box 4 \( P \), gap, line 7 \( Q \) unjustified, box 8 \( Q \), line 9 ∨E 1, 4–7, 8–8; S2 the first box with a gap, line 6 \( \bot \) unjustified and line 7 \( Q \) ⊥E 6), 01:257, warning 01:259-261, the moves paragraph 01:263, all kept.
6. `## How the rules look in a mathematical proof`: 01:267-280 kept; 01:281's last sentence ("Taking 'an integer \( k \)' … here we use the step as school algebra.") **cut** (index note). `thm-square-even-implies-even`, Idea, proof, derivation (exempt (ii)), table 01:332-343 **verbatim** (ch05 01:7 relies on the table). 01:345: first sentence kept; the rest → "Two steps of the proof are not in the derivation: passing from the facts (E1)–(E3), about every integer, to their instances for this \( n \) and this \( n^2 \), and naming the \( k \) of (E3). Both are steps about 'every' and 'some', used as ordinary reasoning (the note at the start of this chapter)." Quick check 01:347-353 kept. 01:355 kept.
7. `## Vacuous truth`: 01:357-399 kept, `exm-vacuous-square` exempt (iii) (its Idea: "exactly the derivation of @prp-vacuous-implication"). 01:401: its first two sentences kept; "When Chapter 3 gives each connective a truth table (@def-truth-value) … force." **cut** (to the box); "Chapter 4 meets the same phenomenon … to test." **cut** (pointer budget; ch04 01:189 and 04:302 point back to 2.1 and need nothing here). Warning 01:403-405 kept.
8. **Rule card** (replaces 01:407-416): rows ¬E, ⊥E (§1.7) under the lead sentence, then 01:416's Lean sentence.
9. **Looking ahead:** "Chapter 3 gives each connective a truth table. The rows of \( \to \) with a false hypothesis are exactly the ones that →I and ⊥E force here."

**Folds.** F2.1-a `title="Where a line ⊥ comes from, and why ⊥E is honest"`: 01:58 verbatim; 01:60 with two edits (§8 item 3): "…that the rules which only pass a \( \bot \) along keep this property is part of what Chapter 3 checks in proving @thm-soundness." → "…that the rules which only pass a \( \bot \) along keep this property is part of what Section 1.2's Looking-ahead box promised for every rule."; its last sentence ("Chapter 3's soundness theorem turns this remark into a proof.") cut.

**Cut outright:** 01:46-56 (replaced by the bullets), the middle of warning 01:73 (to the drill), 01:281's last sentence, the pointers of 01:401.

**Quick checks:** pairs (kept), convention (new), manufactured clash (new), the ⊥E sentence (kept): four in ~3,200 words.

**Exercises.** A1, B1–B3, C1, C2 kept. New:
- **A2: Drill** (`exr-contradiction-and-vacuous-truth-a2`):
  (a) Lines 1 \( \neg(P \wedge Q) \), 2 \( P \wedge Q \). What does "¬E 2, 1" write? — \( \bot \).
  (b) Lines 1 \( \neg\neg P \), 2 \( \neg P \). Which line is \( \varphi \) for ¬E, and how is the step cited? — \( \varphi = \neg P \) (line 2), \( \neg\varphi = \neg\neg P \) (line 1): "¬E 2, 1".
  (c) Lines 1 \( \neg P \wedge Q \), 2 \( P \). Is "\( \bot \) — ¬E 2, 1" legal? — No: line 1's main connective is ∧, so it is not a negation; first \( \neg P \) by ∧E 1, then ¬E 2, 3.
  (d) Line 1 is \( \bot \). Which of \( P \), \( \neg P \), \( \bot \), \( x = 7 \) may "⊥E 1" write? — All four.
  (e) Line 1 is \( P \). May "\( \bot \) — ⊥E 1" be written? — No: ⊥E starts from a line \( \bot \); no rule writes \( \bot \) from a single line \( P \).
  (f) For one real number \( x \), lines 1 \( x < 1 \) and 2 \( x > 1 \) are given. Make them a clash, line by line. — Write line 2 as \( \neg((x < 1) \vee (x = 1)) \) (\( x > 1 \) says that \( x \le 1 \) fails, and \( x \le 1 \) is written out because ∨I must build it); 3 \( (x < 1) \vee (x = 1) \) ∨I 1; 4 \( \bot \) ¬E 3, 2.
  (g) Do the lines \( x \ge 1 \) and \( x \le 1 \) clash? — No: both hold at \( x = 1 \).
  (h) Find the illegal line: 1 \( P \to Q \); 2 \( \neg Q \); 3 | \( P \); 4 | \( Q \) →E 1, 3; 5 | \( \bot \) ¬E 2, 4; 6 | \( R \) ⊥E 5; 7 \( P \to R \) →I 3–6. — Line 5: the unnegated line comes first; with line 2 as \( \varphi \), line 4 would have to be \( \neg\neg Q \). Correct: "¬E 4, 2".
  (i) Derive \( P, \ \neg P \wedge Q \vdash R \). — 3 \( \neg P \) ∧E 2; 4 \( \bot \) ¬E 1, 3; 5 \( R \) ⊥E 4.
  (j) Derive \( \neg Q \vdash Q \to P \). — 2 | \( Q \); 3 | \( \bot \) ¬E 2, 1; 4 | \( P \) ⊥E 3; 5 \( Q \to P \) →I 2–4.
  (k) Derive \( P \to Q, \ \neg Q, \ P \vdash R \). — 4 \( Q \) →E 1, 3; 5 \( \bot \) ¬E 4, 2; 6 \( R \) ⊥E 5.
- **B4** (new, scaffolded), `[B4: An impossible case, scaffolded]`: "A search for \( P \vee Q, \ P \to R, \ Q \to S, \ \neg R \vdash S \) has reached the stage below. *Name the move, then complete it.*" Shown: lines 1–4 premises; a box opened by 5 \( P \), a gap, line 8 \( S \) unjustified; a box opened by 9 \( Q \), a gap, line 10 \( S \) unjustified; line 11 \( S \) ∨E 1, 5–8, 9–10. Answer: the move is *an impossible case closes itself*: the case \( P \) cannot reach \( S \) honestly, so it reaches a clash: 6 \( R \) →E 2, 5; 7 \( \bot \) ¬E 6, 4; 8 \( S \) ⊥E 7. The case \( Q \): 10 \( S \) →E 3, 9.

**Sidecars:** none new (A2(g) at \( x = 1 \) is arithmetic; the ledger records it).

### 4.2 Section 2.2: Proving a Negation (`02-negation-and-contradiction.md`)

**Budget:** main line ≤ 2,300 words (now 2,420); folds ≤ 300. Looking ahead: item 9.

**New order of material.**
1. 02:3 and `## How to prove that something is not so` 02:5-13 kept.
2. `def-rules-negation` verbatim. Then *"This rule has conditions that matter; read each one."* (replacing 02:41) and clauses 1–5 (02:43-47) kept, except clause 3's last sentence ("Chapter 3's soundness proof (@thm-soundness) relies on it.") **cut**. 02:49-64 (the one-line box, ⊢ ¬⊥, the noninstance by one change) → fold F2.2-a. "Why this rule" 02:66: kept to "That is exactly what \( \neg\varphi \) claims."; its last sentence cut. Table 02:68-73 kept. Remark 02:75-77 kept up to "Some presentations of logic take this as the definition of \( \neg \). This book keeps \( \neg \) as a connective with its own rules."; the clause "and Chapter 5 returns to the reading … provides" cut (ch05 07:97 points back to the table, which stays).
3. Warnings 02:79-85 → **one warning** (~70 words): 02:83-85 kept ("Do not open the box with what you want to prove. … the converse error that Section 1.4 found in Argument B."), with one sentence added before its last: "So a box opened with \( \neg(x > 0) \) and closed by ¬I gives \( \neg\neg(x > 0) \), not \( x > 0 \); Section 2.5 shows the other kind of 'suppose not'." (The rest of 02:79-81 is cut; 2.5 is the single home of ¬I vs RAA.)
4. Givens/Goal sentence: "In the Givens/Goal table, ¬I moves \( \varphi \) into the Givens and makes \( \bot \) the goal."
5. `## The first example: a number that is never zero` (new heading; ~30 words of lead: "The goal we could not reach at the start of the section comes first."). `exm-square-plus-one` (02:205-217) moved here: statement, Idea and prose solution verbatim, then **a derivation added** after the prose (§8 item 6), with the line "With the school fact as the premise:":
   ```
   1 ¬(x² < 0)            premise
   2 | x² + 1 = 0         assumption
   3 | x² < 0             algebra 2
   4 | ⊥                  ¬E 3, 1
   5 ¬(x² + 1 = 0)        ¬I 2–4
   ```
   (`\by{algebra}{2}` as in `thm-sqrt2-irrational`'s derivation; exempt (ii): the prose just above is its read-back.) **Quick check (new):** "In this derivation, which box does ¬I cite, and which statement opened it?" Solution: the box 2–4, opened by \( x^2 + 1 = 0 \), the unnegated statement; the conclusion is its negation, \( x^2 + 1 \ne 0 \).
6. `## First derivations with not-introduction`: 02:89 kept. `exm-double-negation-introduction`: (a) gains **two snapshots** (S1 line 1, gap, line 4 \( \neg\neg P \) unjustified; S2 box opened with 2 \( \neg P \), gap, line 3 \( \bot \) unjustified, line 4 ¬I 2–3), (b) gains **two snapshots** (S1 line 1, box 2 \( P \), gap, line 5 \( \bot \) unjustified, line 6 ¬I 2–5; S2 line 3 \( P \vee Q \) ∨I 2 written, gap, line 5 still unjustified). 02:134, 02:137 kept. Quick check 02:139-161 kept (its derivation exempt (vi)). 02:163 and `exm-triple-negation` (moved from before `exm-square-plus-one` to here, content verbatim), its Idea gaining **two snapshots** (S1 line 1, box 2 \( P \), gap, line 6 \( \bot \) unjustified, line 7 ¬I 2–6; S2 gap, line 5 \( \neg\neg P \) unjustified, line 6 ¬E 5, 1). 02:196 kept. Warning 02:199-201 → fold F2.2-a.
7. `## How the rule looks in a mathematical proof`: 02:221-223 kept. 02:225: its last sentence → "Making 'cannot go on for ever' precise needs a fact about the natural numbers that this book does not prove; here we take (L) as known." (fd2 01:148 and 02:162 say that Chapter 2 *claimed* this and *gave* the halving reason; both stay true.) `thm-sqrt2-irrational` with Idea (and *Before reading on*), proof, Quick check 02:243-249, 02:251, derivation 02:253-273 (exempt (ii)) **verbatim**. 02:275: first two sentences kept; the rest → "Two steps of the proof lie outside the derivation: choosing \( p \), \( q \) and \( m \), and passing from the arbitrary \( r \) to every rational number. Both are steps about 'some' and 'every', used as ordinary reasoning." 02:277: first two sentences kept; the third (*Analysis on the Real Line*) → the box. 02:279: kept to "…even though it is what everyone calls a proof by contradiction."; the last sentence ("Section 2.5 meets a second kind of box …") cut.
8. **Rule card** (replaces 02:281-289): rows ¬E, ⊥E, ¬I; 02:289's Lean sentence kept.
9. **Looking ahead:** "*Sets, Relations, and Cardinality*, Chapter 2 proves (L) from a fact about the natural numbers called well-ordering. *Analysis on the Real Line*, Chapter 1 uses this section's theorem in exactly the form proved here, as evidence that the rational numbers have a gap where \( \sqrt{2} \) should be."

**Folds.** F2.2-a `title="Edge cases of not-introduction"`: 02:49-62, 02:64, and warning 02:199-201 (as a bold lead-in paragraph: "**A box that never uses its assumption.**").

**Quick checks:** square-plus-one (new), \( \neg(P \vee Q) \vdash \neg P \) (kept), the ¬E step of the √2 proof (kept): three in ~2,300 words.

**Exercises.** A1 (key proof) kept. B2, B3 (frozen), B4, C1 (frozen), C2 kept.
- **B1** recast as the section's scaffolded B (content unchanged): "A search for \( P \to \neg Q \vdash Q \to \neg P \) has reached the stage below. *Name the move that opens each box, then complete it.*" Shown: line 1, a gap, line 7 \( Q \to \neg P \) unjustified. The solution 02:327-348 is kept verbatim (it names both moves and gives the 7-line derivation).
- **A2: Drill** (`exr-negation-and-contradiction-a2`):
  (a) Which statement opens the ¬I box for the goal \( \neg(P \vee Q) \)? — \( P \vee Q \).
  (b) A box opens with \( \neg P \) and ends with \( \bot \). What does ¬I write after it? — \( \neg\neg P \).
  (c) A box opens with \( P \) and its last line is \( \neg P \). May ¬I close it? — No: the last line must be \( \bot \); first write \( \bot \) by ¬E, citing the assumption and the line \( \neg P \).
  (d) For a real number \( x \), the goal is \( x \ne 3 \). Which statement opens the box? — \( x = 3 \).
  (e) "Suppose \( x^2 + 4 = 2x \) for a real \( x \). Then \( (x - 1)^2 = -3 < 0 \), which contradicts \( (x - 1)^2 \ge 0 \)." What may "Hence" write, and by which rule? — \( x^2 + 4 \ne 2x \), by ¬I (since \( x^2 + 4 - 2x = (x - 1)^2 + 3 \)).
  (f) Lines 1 \( \neg Q \); 2 | \( Q \); 3 | \( \bot \) ¬E 2, 1. What may line 4, just after the box, be by ¬I? — \( \neg Q \), the negation of the box's assumption; not \( Q \).
  (g) Find the illegal line: 1 \( P \to Q \); 2 \( \neg Q \); 3 | \( P \); 4 | \( Q \) →E 1, 3; 5 | \( \bot \) ¬E 4, 2; 6 \( \neg P \) ¬I 3–5; 7 \( Q \) →E 1, 3. — Line 7 cites line 3, inside the closed box 3–5.
  (h) Derive \( \neg P \vdash \neg(P \wedge Q) \). — 2 | \( P \wedge Q \); 3 | \( P \) ∧E 2; 4 | \( \bot \) ¬E 3, 1; 5 \( \neg(P \wedge Q) \) ¬I 2–4.
  (i) Derive \( P \to \neg P \vdash \neg P \). — 2 | \( P \); 3 | \( \neg P \) →E 1, 2; 4 | \( \bot \) ¬E 2, 3; 5 \( \neg P \) ¬I 2–4.
  (j) Derive \( P \wedge \neg Q \vdash \neg(P \to Q) \). — 2 | \( P \to Q \); 3 | \( P \) ∧E 1; 4 | \( Q \) →E 2, 3; 5 | \( \neg Q \) ∧E 1; 6 | \( \bot \) ¬E 4, 5; 7 \( \neg(P \to Q) \) ¬I 2–6.

**Sidecars:** A2(e) identity \( x^2 + 4 - 2x = (x - 1)^2 + 3 \).

### 4.3 Section 2.3: Derived Rules: Proved Sequents as New Rules (`03-derived-rules.md`)

**Budget:** main line ≤ 3,000 words (now 3,300); folds ≤ 500. Looking ahead: item 10.

**Changes, in the file's order.**
1. 03:3-15 kept.
2. `prp-modus-tollens`, statement and proof verbatim; its Idea gains **two snapshots** (S1 lines 1–2, box 3 \( P \), gap, line 5 \( \bot \) unjustified, line 6 ¬I 3–5; S2 gap, line 4 \( Q \) unjustified, line 5 ¬E 4, 2). 03:52-54 kept. `prp-contrapositive` verbatim, exempt (iii) (its Idea: "exactly where the proof of @prp-modus-tollens was"). 03:90: its last sentence → "The passage back, from \( \neg Q \to \neg P \) to \( P \to Q \), is a different matter (Common errors, below)." 03:92 kept.
3. `## What a derived rule is`: 03:96-98, `def-derived-rule` verbatim, 03:117, clauses 1–4 kept, except clause 2's last sentence ("Chapter 3 makes this replacement exact, under the name substitution.") → the box. 03:124 kept. **Figure (new; replaces the expansion argument on the main line):** two `nd` blocks side by side (`\qquad`), each under a bold caption line in prose above the figure: left, "With the derived rule": 1 \( P \to Q \); 2 \( \neg Q \); 3 \( \neg P \) MT 1, 2. Right, "Written out": the derivation of `prp-modus-tollens` (6 lines). Caption below (italic): *Line 3 on the left stands for lines 3–6 on the right: the same premises, the same last line.* Then one sentence: "A derived rule is shorthand for lines we could always write out, so it lets us prove nothing that the primitive rules could not." **Quick check (new):** "In the figure, which lines does line 3 on the left cite, and which lines on the right use those same two premises?" Solution: lines 1 and 2; on the right, line 4 cites line 1 and line 5 cites line 2. 03:126-141 → fold F2.3-a. Warning 03:143-145 kept. Givens/Goal sentence: "In the Givens/Goal table, a derived rule adds its conclusion to the Givens in one row, as an elimination rule does."
4. `## Disjunctive syllogism`: 03:149 and `prp-disjunctive-syllogism` verbatim (exempt (iii): "This is @exm-impossible-case with a simpler clash"); 03:185, 03:187 kept. `exm-derived-rules-in-use` kept; (a) gains **two snapshots** (S1 lines 1–3, gap, line 5 \( \neg P \) unjustified; S2 gap, line 4 \( \neg Q \) unjustified, line 5 MT 1, 4); its 11-line expansion is exempt (iii); (b) gains **two snapshots** (S1 lines 1–3, gap, line 5 \( R \); S2 gap, line 4 \( Q \) unjustified, line 5 →E 3, 4). Quick check 03:258-266 kept.
5. `## Modus tollens on numbers, and the green card`: `exm-modus-tollens-instance` kept. 03:282 rewritten as **a table and two sentences** (~140 words in all). Lead: "The claim of @exm-wason-selection (Section 1.3), for one card, is \( E \to R \), with \( E \): 'this card's number is even' and \( R \): 'its color side is red'."

   | The card shows | So we have | What a rule gives | Turn it? |
   |---|---|---|---|
   | \( 6 \) | \( E \) | →E: \( R \); the back must be red | yes: a green back would break the claim |
   | \( 7 \) | \( \neg E \) | nothing: no rule uses \( E \to R \) with \( \neg E \) | no |
   | red | \( R \) | nothing about \( E \): concluding \( E \) would be affirming the consequent | no |
   | green | \( \neg R \) | MT: \( \neg E \); the number must be odd | yes: an even number would break the claim |

   Then: "Turning the green card tests exactly the line MT wrote: an even number there gives \( E \), and with \( \neg R \) and \( E \to R \), →E and ¬E reach \( \bot \). Modus tollens is the step people skip." 03:284 kept from "\( \rulename{CP} \) turns the claim into its contrapositive …" to the end. **Quick check (new):** "Which card would MT settle if the claim were 'if a card's color side is red, then its number is even'?" Solution: the \( 7 \): the claim is \( R \to E \), the \( 7 \) shows \( \neg E \), and MT gives \( \neg R \), so its back must not be red; turn it.
6. `## How this rule looks in a mathematical proof`: 03:288 kept, then **the prose payoff (new, ~80 words)**: "Written the way a mathematician would write it, the proof is three sentences: *Suppose \( n^2 \) is even. Then \( n^2 \) is not odd, since no integer is both; so, by the contrapositive of (E3), \( n \) is not odd. As every integer is even or odd, \( n \) is even.* Each sentence after the first is one named step: ¬I with (E2), CP with →E, DS. The example below writes the same proof with every step tagged, and then as a derivation." Then `exm-square-even-via-contrapositive` **verbatim** (statement, Idea, tagged prose, derivation with line 11 "or commutes", 03:327; exempt (ii)). 03:330 → fold F2.3-b. 03:332 **moved** to 2.5 (it becomes the last two sentences of the x³ comparison, §4.5 item 11).
7. `## Common errors`: warnings 03:336-338 and 03:340-342 kept (the second: "Section 2.5 derives the passage back with a new rule." kept; the "true, but we state it without proof" sentence kept). Warning 03:344-346 **moved** to 2.5 (§4.5 item 11), rewritten there.
8. **Rule card** (replaces 03:348-356): rows ¬E, ⊥E, ¬I, MT, CP, DS.
9. 03:337's "Section 2.6 returns to the error in general" kept (in-chapter).
10. **Looking ahead:** "Chapter 3 makes exact the replacement of letters that a derived rule allows, under the name substitution."

**Folds.** F2.3-a `title="Why a derived rule adds no power"`: 03:126 ("Convenience, not power.") and 03:128-141 with their derivation, verbatim. F2.3-b `title="The two derivations of Even Square, line for line"`: 03:330 verbatim.

**Quick checks:** the figure (new), which derived rule (kept), the reversed card claim (new): three in ~3,000 words.

**Exercises.** A1, B1 (frozen), B2, C1 (frozen), C2, C3 (exit check) kept.
- **B3** recast as the section's scaffolded B, `[B3: Two refutations]` (content unchanged): "A search for \( (P \vee Q) \to R, \ \neg R \vdash \neg P \wedge \neg Q \) has reached the stage below. *Name the move, then complete it.*" Shown: lines 1–2, line 3 \( \neg(P \vee Q) \) MT 1, 2, a gap, line 12 \( \neg P \wedge \neg Q \) unjustified. The solution 03:473-498 kept verbatim.
- **A2: Drill** (`exr-derived-rules-a2`):
  (a) Lines 1 \( (A \wedge B) \to C \), 2 \( \neg C \). What does "MT 1, 2" write? — \( \neg(A \wedge B) \).
  (b) Lines 1 \( P \to \neg Q \), 2 \( Q \). Does MT apply? — Not yet: MT needs \( \neg\neg Q \); write it from \( Q \) by a ¬I box first, then MT gives \( \neg P \).
  (c) Lines 1 \( \neg P \vee Q \), 2 \( \neg\neg P \). What does "DS 1, 2" write? — \( Q \) (the letter \( P \) of DS replaced by \( \neg P \)).
  (d) Lines 1 \( P \vee Q \), 2 \( \neg Q \). Does DS, as stated, apply? — No: DS refutes the left disjunct; use the other form (Exercise B1 (a)) or exchange the disjuncts first.
  (e) What does CP write from \( (x > 0) \to (x^2 > 0) \)? — \( \neg(x^2 > 0) \to \neg(x > 0) \), that is, \( x^2 \le 0 \to x \le 0 \).
  (f) May a derivation of @prp-contrapositive use CP on one of its lines? — No: a derived rule may be used only after its sequent has been derived.
  (g) Written out with primitive rules, citing available lines directly, how many lines does one MT line become? — Four: an assumption, →E, ¬E, ¬I (the figure).
  (h) Find the illegal line: 1 \( P \to Q \); 2 \( \neg P \); 3 \( \neg Q \) MT 1, 2. — Line 3: MT needs the negation of the conclusion, \( \neg Q \), and gives \( \neg P \); from \( \neg P \) nothing follows about \( Q \). The form breaks at \( P \) false, \( Q \) true.
  (i) Derive \( P \to (Q \wedge R), \ \neg R \vdash \neg P \). — 3 | \( P \); 4 | \( Q \wedge R \) →E 1, 3; 5 | \( R \) ∧E 4; 6 | \( \bot \) ¬E 5, 2; 7 \( \neg P \) ¬I 3–6. (MT does not match: \( \neg(Q \wedge R) \) is not available.)
  (j) Derive \( P \vee Q, \ \neg P, \ \neg Q \vdash R \). — 4 \( Q \) DS 1, 2; 5 \( \bot \) ¬E 4, 3; 6 \( R \) ⊥E 5.
  (k) Derive \( \neg P \to Q, \ \neg Q \vdash \neg\neg P \) in one line. — 3 \( \neg\neg P \) MT 1, 2.

**Sidecars:** none new.

### 4.4 Section 2.4: Iff, Equivalence, and What a Definition Says (`04-biconditional-and-definitions.md`)

**Budget:** main line ≤ 3,300 words (now 3,685); folds ≤ 750. Looking ahead: item 10.

**Changes, in the file's order.**
1. 04:3: "Section 1.1 warned that 'if' means different things in a theorem and in a definition, and promised an explanation." → "Section 1.1 warned that 'if' means different things in a theorem and in a definition; this section explains why." (Chapter 1's R2 revision deleted the promise at old 01:101; ch01 01:113 now only warns.)
2. 04:7-53 kept (`def-rules-biconditional` verbatim, clauses 1–4). Givens/Goal sentence after clause 4: "In the Givens/Goal table, ↔I splits a row in two: \( \varphi \) added to the Givens with the goal \( \psi \), and \( \psi \) added with the goal \( \varphi \)."
3. 04:57 kept. `exm-iff-symmetric` (a) gains **two snapshots** (S1 line 1, gap, line 6 \( Q \leftrightarrow P \) unjustified; S2 boxes 2 \( Q \) … 3 \( P \) and 4 \( P \) … 5 \( Q \) opened, lines 3 and 5 unjustified, line 6 ↔I 2–3, 4–5); (b) exempt (iii) ("the derivation of @prp-modus-tollens with ↔E on line 4"). 04:110 kept. `prp-iff-two-implications` statement and proofs verbatim; its Idea gains **two snapshots for each derivation** (first: S1 line 1, gap, line 4 \( P \to Q \) unjustified, gap, line 7 \( Q \to P \) unjustified, line 8 ∧I 4, 7; S2 the boxes 2 \( P \) … 3 \( Q \) and 5 \( Q \) … 6 \( P \) opened, lines 4 and 7 →I. Second: S1 line 1, lines 2–3 by ∧E, gap, line 8 \( P \leftrightarrow Q \); S2 the boxes 4 \( P \) … 5 \( Q \) and 6 \( Q \) … 7 \( P \) opened, line 8 ↔I 4–5, 6–7). 04:168 kept. `exm-iff-negations` gains **two snapshots** (S1 line 1, box 2 \( \neg P \) … 6 \( \neg Q \), box 7 \( \neg Q \) … 11 \( \neg P \), gaps, line 12 ↔I 2–6, 7–11; S2 the inner boxes 3 \( Q \) … 5 \( \bot \) and 8 \( P \) … 10 \( \bot \) opened, lines 6, 11 ¬I, gaps where lines 4 and 9 go). **Quick check (new)** after it: "Which line does line 5 cite as \( \neg\varphi \), and why may it?" Solution: line 2, \( \neg P \), the assumption of the outer box, which is still open at line 5. 04:209 → "Its converse, \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \), is also derivable, with the rule of Section 2.5: in the box of \( P \) it must produce the **positive** statement \( Q \), and the natural box, on \( \neg Q \), closes to \( \neg\neg Q \), not \( Q \)." (The "true, but we state it without proof" sentence and "Section 2.5 sets the converse as an exercise" cut; 05:33 still finds this stall here.)
4. `## Provable equivalence`: 04:213-215, `def-provable-equivalence`, 04:223 kept. 04:225 → "A first example is \( P \wedge Q \dashv\vdash Q \wedge P \): @prp-and-commutes derives \( Q \wedge P \) from \( P \wedge Q \), and the same derivation with \( P \) and \( Q \) exchanged derives \( P \wedge Q \) from \( Q \wedge P \). By the same exchange, @exm-disjunction-first-derivations gives \( P \vee Q \dashv\vdash Q \vee P \), and part (a) of @exm-iff-symmetric gives \( P \leftrightarrow Q \dashv\vdash Q \leftrightarrow P \)." Its first sentence (\( P \dashv\vdash P \)) and 04:227 → fold F2.4-a. 04:229 and `prp-provable-equivalence-basics` (statement) kept, then the one-sentence meaning (italic, from 04:256): "*In words: one derivation of \( P \leftrightarrow Q \) from no premises is worth two derivations, one each way; and \( \dashv\vdash \) can be used like \( = \) in a calculation.*" Idea 04:242-244 and proof 04:246-254 → fold F2.4-b. 04:256 cut (its content is the meaning sentence). 04:258-270 kept. Warning 04:272-274: the parenthetical "(A derivation never leads … @thm-soundness.)" → "(Section 1.1's test: a choice of statements with the premise true and the conclusion false breaks the form.)" (§8 item 13).
5. `## Proving an iff: two directions`: 04:278-327 kept (`thm-odd-iff-square-odd`, `thm-squares-order` and its remark verbatim; prose proofs, no snapshots). 04:329: the parenthetical → "(That square roots of non-negative numbers exist is a school fact here.)". Quick check 04:331-343 and warning 04:345-347 kept.
6. `## What a definition says`: 04:351-357 kept; 04:359's last sentence ("The words 'for all real numbers \( x \) and \( y \)' are a quantifier, whose rules come in Chapter 4; here we use them informally.") cut (index note). `exm-strictly-increasing-both-ways` and 04:379 kept (ch05 01:226 cites the example). Warning 04:381-383 **replaced** (~80 words; school-level converse, §8 item 14): "The convention is for **definitions only**. In a theorem, 'if' means 'if', one direction. The theorem 'if \( 6 \mid n \), then \( n \) is even' is true for every integer \( n \): \( n = 6k = 2(3k) \). Its converse, 'if \( n \) is even, then \( 6 \mid n \)', breaks at \( n = 4 \). Reading a theorem's 'if' as 'iff' means proving its converse without a proof, which is the error of Argument B in Section 1.1." (\( d \mid n \) is defined at its first use in 1.3; NOTATION row 85.) The differentiability example of 04:382 → fold F2.4-c. **Quick check (new)** after the warning: "Write the converse of 'if a real number \( x \) satisfies \( x > 2 \), then \( x^2 > 4 \)', and break it." Solution: "if \( x^2 > 4 \), then \( x > 2 \)"; \( x = -3 \) breaks it (\( 9 > 4 \), and \( -3 > 2 \) fails).
7. `## Chains of equivalences`: 04:387-391 kept; `prp-equivalence-cycle` statement and proof verbatim, its Idea gaining **two snapshots** (S1 lines 1–3, gap, line 9 \( P \leftrightarrow Q \) unjustified; S2 boxes 4 \( P \) … 5 \( Q \) and 6 \( Q \) … 8 \( P \) opened, gaps, line 9 ↔I 4–5, 6–8). 04:429-457 kept (`exm-unit-interval-tfae` unchanged).
8. **Rule card** (replaces 04:459-466): rows ¬E, ⊥E, ¬I, MT, CP, DS, ↔I, ↔E; 04:461's first sentence ("The rows for this section's rules complete the table for the connectives; Section 2.6 collects the rules in one place.") and its Lean sentence kept.
9. Plain pointer check: 04:7's `@exr-statements-and-connectives-c1` stays (backward).
10. **Looking ahead:** "*Analysis on the Real Line*, Chapter 1 proves from its axioms that every non-negative real number has a square root, the school fact behind the square-root payoff above."

**Folds.** F2.4-a `title="Edge cases of provable equivalence"`: 04:225's first sentence, and 04:227 with its parenthetical "(It holds once Section 2.5 adds its rule; that it cannot hold without that rule is true, and Chapter 3 proves it: @thm-raa-independent.)" → "(It holds once Section 2.5 adds its rule; that it cannot hold without that rule is true, and nothing here uses it.)". F2.4-b `title="The proof: copying derivations"`: 04:242-254 verbatim (Idea and proof of `prp-provable-equivalence-basics`). F2.4-c `title="The same slip in calculus"`: 04:382 from "A familiar theorem of calculus" to "\( -1 \) for \( h < 0 \)", with ", proved in *Analysis on the Real Line*, Chapter 7," cut.

**Quick checks:** `exm-iff-negations` citation (new), one direction proved (kept), the converse (new): three in ~3,300 words.

**Exercises.** A1, B1, B2, C1, C2 kept.
- **B3** split into scaffolded parts (content and answer unchanged; the stem 04:544 kept): "(a) Apply @thm-squares-order with the roles of \( x \) and \( y \) exchanged. What does it say? (b) Use @exm-iff-negations as a derived rule on (a): with which statements in place of \( P \) and \( Q \), and what does it give? (c) Translate both sides of (b) with the fact quoted. (d) What have you proved?" Solution: 04:548 split along the parts.
- **B4** (new, scaffolded), `[B4: Both directions]`: "A search for \( P \leftrightarrow Q \vdash (P \wedge R) \leftrightarrow (Q \wedge R) \) has reached the stage below. *Name the move, then complete it.*" Shown: line 1, a gap, line 12 \( (P \wedge R) \leftrightarrow (Q \wedge R) \) unjustified. Answer: the move is *two boxes for an iff*; inside each, take the conjunction apart and cross with ↔E: 2 | \( P \wedge R \); 3 | \( P \) ∧E 2; 4 | \( R \) ∧E 2; 5 | \( Q \) ↔E 1, 3; 6 | \( Q \wedge R \) ∧I 5, 4; 7 | \( Q \wedge R \); 8 | \( Q \) ∧E 7; 9 | \( R \) ∧E 7; 10 | \( P \) ↔E 1, 8; 11 | \( P \wedge R \) ∧I 10, 9; 12 ↔I 2–6, 7–11.
- **A2: Drill** (`exr-biconditional-and-definitions-a2`):
  (a) Lines 1 \( P \leftrightarrow Q \), 2 \( Q \). What does "↔E 1, 2" write? — \( P \).
  (b) Lines 1 \( P \leftrightarrow Q \), 2 \( \neg P \). Does ↔E give anything? — No: ↔E needs \( P \) or \( Q \); \( \neg Q \) comes by a ¬I box (as in part (k)).
  (c) A box 2–4 runs from \( P \) to \( Q \); a box 5–7 from \( Q \) to \( P \), and line 6 cites line 3. Is "\( P \leftrightarrow Q \) ↔I 2–4, 5–7" correct? — No: line 6 cites line 3, inside the closed sibling box 2–4.
  (d) One box runs from \( P \) to \( Q \). What does it prove? — \( P \to Q \) (by →I); not \( P \leftrightarrow Q \).
  (e) Write "\( x^2 = 4 \) if and only if \( x = 2 \) or \( x = -2 \)" as two implications. Which begins "Suppose \( x^2 = 4 \)"? — \( (\Rightarrow) \) if \( x^2 = 4 \), then \( x = 2 \vee x = -2 \); \( (\Leftarrow) \) the converse. \( (\Rightarrow) \).
  (f) Definition: "an integer \( n \) is a **multiple of 3** if \( n = 3k \) for some integer \( k \)". From \( 12 = 3 \cdot 4 \), what follows, reading the definition which way? — \( 12 \) is a multiple of \( 3 \), reading it from the condition to the term (↔E).
  (g) True or false: \( P \dashv\vdash Q \) says that \( \vdash P \to Q \). — False: it says \( P \vdash Q \) and \( Q \vdash P \), two derivations (equivalently \( \vdash P \leftrightarrow Q \)).
  (h) A proof that (a), (b), (c) are equivalent proves (a) ⇒ (b), (b) ⇒ (a) and (b) ⇒ (c). Is it complete? — No: no arrow leaves (c); add (c) ⇒ (a) or (c) ⇒ (b).
  (i) Derive \( P \leftrightarrow Q, \ P \vdash Q \wedge P \). — 3 \( Q \) ↔E 1, 2; 4 \( Q \wedge P \) ∧I 3, 2.
  (j) Derive \( P \leftrightarrow Q, \ Q \leftrightarrow R, \ R \vdash P \). — 4 \( Q \) ↔E 2, 3; 5 \( P \) ↔E 1, 4.
  (k) Derive \( P \leftrightarrow Q, \ \neg P \vdash \neg Q \). — 3 | \( Q \); 4 | \( P \) ↔E 1, 3; 5 | \( \bot \) ¬E 4, 2; 6 \( \neg Q \) ¬I 3–5.

**Sidecars:** the warning (\( 6 \mid n \Rightarrow 2 \mid n \) on a range; \( 4 \) even, \( 6 \nmid 4 \)); the Quick check (\( x = -3 \)); A2(e) (\( x^2 = 4 \) exactly at \( \pm 2 \)).

### 4.5 Section 2.5: Proof by Contradiction and the Classical Rules (`05-reductio-and-classical-rules.md`)

**Budget:** main line ≤ 4,300 words (now 5,070); folds ≤ 1,700. Looking ahead: item 13.

**New order of material.**
1. 05:3 kept.
2. `## Two boxes that look alike`: 05:7-9 kept (the √2 proof is ¬I). 05:11 → "The second is about a real number." Then the **new example** (replaces `exm-raa-zero` here; `exm-raa-zero` moves to item 11):

   ::: {#exm-raa-at-most-one} [A number whose square is at most itself] "Let \( x \) be a real number with \( x^2 \le x \). Prove that \( x \le 1 \)." Solution (prose, ~60 words): "Suppose, for a contradiction, that \( x \le 1 \) fails, that is, \( x > 1 \). Then \( x > 0 \), and multiplying \( x > 1 \) by \( x \) gives \( x^2 > x \). This contradicts \( x^2 \le x \). Hence \( x \le 1 \)."

   05:25 kept with \( P \) now "\( x \le 1 \)" and its sentence → "If we tried to justify the last line by ¬I, we would get the negation of the box's assumption, \( \neg\neg P \): 'it is not the case that \( x \le 1 \) fails'." 05:23 **cut**.
3. `## Where the rules so far stop short`: 05:29 kept. Item 1 (05:31) → "Section 2.2 noted that a box opened with \( \neg(x > 0) \) and closed by ¬I gives \( \neg\neg(x > 0) \), and no rule so far gets from there to \( x > 0 \)." Item 2 (05:32) → "If you did Exercise C1 of Section 2.3, you met a second: @exr-derived-rules-c1 led from \( P \to Q \) and \( \neg P \to R \) to \( \neg(\neg Q \wedge \neg R) \), and not to \( Q \vee R \)." Item 3 (05:33) kept. 05:35 kept. 05:37 → "That no derivation of \( P \) from \( \neg\neg P \) exists with the rules so far is a claim about **all** derivations, which no search can settle; this section's Looking-ahead box says where it is proved. Here we name the missing step and add it as a rule." (The "other two stalls … without proof" sentence is cut; the ledger line goes.)
4. `## Reductio ad absurdum`: 05:41 and `def-rule-raa` verbatim. 05:63 → *"This rule has conditions that matter; read each one."* plus its first sentence; clauses 1–4 (05:65-68), 05:70 and the table 05:72-75 kept. 05:77 → one sentence: "The rows differ only in where the \( \neg \) sits, and that makes RAA different in kind: every other primitive rule is the introduction or elimination rule of one connective, while RAA applies to every statement, whatever its main connective, even a letter." 05:79 → fold F2.5-c. Givens/Goal sentence: "In the Givens/Goal table, RAA adds \( \neg\varphi \) to the Givens and makes \( \bot \) the goal." **The opening example as a derivation** (new, ~40 words of prose: "With the convention of Section 2.1, the argument of @exm-raa-at-most-one is this derivation."):
   ```
   1 x² ≤ x                 premise
   2 | ¬(x ≤ 1)             assumption
   3 | x > 1                algebra 2
   4 | ¬(x² ≤ x)            algebra 3
   5 | ⊥                    ¬E 1, 4
   6 x ≤ 1                  RAA 2–5
   ```
   (Line 3: "not at most 1" is "greater than 1"; line 4: \( x > 1 > 0 \), so \( x^2 = x \cdot x > x \), written \( \neg(x^2 \le x) \) by the convention.) Exempt (ii) (the prose of the example above is its read-back). Warning 05:81-83 kept. Quick check 05:85-91 kept. **Quick check (new):** "In this derivation, which line is the RAA step, which box does it cite, and what would ¬I have written there instead?" Solution: line 6, the box 2–5; ¬I would write \( \neg\neg(x \le 1) \).
5. `## The move: when stuck, assume the negation of the goal`: 05:95-99 kept. 05:101 → "The move is a last resort, not a first one; Section 2.6 explains why it never does harm and still comes last. Three of the derivations below reach the moment of being stuck, and their Ideas say where."
6. `## Derivations with the new rule` (retitled from "Five derivations with the new rule"): 05:105-124 (the degenerate case) → fold F2.5-a. `prp-double-negation` verbatim (both derivations exempt (iii): (a) repeats `exm-double-negation-introduction` (a), (b) the same box closed by the other rule); 05:179 kept; 05:181 → fold F2.5-a; 05:183 kept. 05:185 and `prp-contrapositive-converse` verbatim, its Idea gaining **two snapshots** (S1 line 1, box 2 \( P \), gap, line 6 \( Q \) unjustified, line 7 →I 2–6 (the stall at a letter); S2 inside box 2 a box opened with 3 \( \neg Q \), gap, line 5 \( \bot \) unjustified, line 6 RAA 3–5). 05:221: its first two sentences kept; the last → fold F2.5-c. 05:223 and `prp-excluded-middle` verbatim except the Idea's "(informally: \( P \) may be true or false; Chapter 3 makes this exact)" → "(each can be broken: \( P \) false breaks the first, \( P \) true the second)" (§8 item 20); its Idea gains **two snapshots** (S1 box 1 \( \neg(P \vee \neg P) \), gap, line 7 \( \bot \) unjustified, line 8 RAA 1–7; S2 gap, line 5 \( \neg P \) unjustified, line 6 \( P \vee \neg P \) ∨I 5, line 7 ¬E 6, 1). 05:260-262 kept.
   **Peirce's law, on the main line:** 05:264 and `prp-peirce` (statement) kept, then one sentence (italic): "*In words: a law with no \( \neg \) in it, whose derivation here still uses RAA. The derivation is in the fold below; Section 2.6 shows how the search finds it.*" 05:272-309 → fold F2.5-b.
7. `## De Morgan's laws`: 05:313, `prp-de-morgan` (key proof), Try it first 05:328, kept. Idea 05:331-334: the sentence "But neither follows from the premise alone: … and the rules never lead from true premises to a false conclusion (Chapter 3 proves this)." → "But the step from the premise to \( \neg P \) can be broken: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) false; and the step to \( \neg Q \) breaks with \( P \) false and \( Q \) true. So neither side is worth aiming at." (§8 item 21.) The rest of the Idea and the four proofs verbatim; the Idea gains snapshots: for (a) **two** (S1 line 1, gap, line 5 \( \neg P \) unjustified, gap, line 9 \( \neg Q \) unjustified, line 10 ∧I 5, 9; S2 boxes 2 \( P \) … 4 \( \bot \) and 6 \( Q \) … 8 \( \bot \) opened, lines 5, 9 ¬I); for (b) **two** (S1 lines 1–3, box 4 \( P \vee Q \), gap, line 9 \( \bot \) unjustified, line 10 ¬I 4–9; S2 inside, boxes 5 \( P \) … 6 \( \bot \) and 7 \( Q \) … 8 \( \bot \) opened, line 9 ∨E 4, 5–6, 7–8); (c) exempt (iii) ("the same shape as (b)"); for (d) **two** (S1 line 1, box 2 \( \neg(\neg P \vee \neg Q) \), gap, line 11 \( P \wedge Q \) unjustified, line 12 ¬E 11, 1, line 13 RAA 2–12; S2 gap, line 6 \( P \) unjustified, gap, line 10 \( Q \) unjustified, line 11 ∧I 6, 10, with the boxes 3 \( \neg P \) … 5 \( \bot \) and 7 \( \neg Q \) … 9 \( \bot \) opened). The snapshots sit after the Try-it-first prompt. 05:438-443 and Quick check 05:445-451 kept.
8. `## Implication as a disjunction`: 05:455-529 kept; (a) gains **two snapshots** (S1 line 1, box 2 \( \neg P \) … 6 \( P \to Q \), box 7 \( Q \) … 10 \( P \to Q \), gaps, line 11 ∨E 1, 2–6, 7–10; S2 the inner boxes 3 \( P \) … 5 \( Q \) and 8 \( P \) … 9 \( Q \) opened, lines 6 and 10 →I); (b) gains **two snapshots** (S1 line 1, line 2 LEM, box 3 \( P \) … 5, box 6 \( \neg P \) … 7, gaps, line 8 ∨E 2, 3–5, 6–7; S2 line 4 \( Q \) →E 1, 3 written, lines 5 and 7 \( \neg P \vee Q \) unjustified).
9. `## One principle in three forms`: 05:533 and 05:535 kept (the rule forms and "X derives Y" are used by the statement). `thm-classical-rules-interderivable` (statement) kept, then the one-sentence meaning (italic): "*In words: RAA, ¬¬E and LEM are one principle in three forms; adding any one of them to the other rules proves exactly what adding any other does.*" Then:
   - **Cycle diagram (new TikZ).** Three nodes at the corners of a triangle, labelled RAA, ¬¬E, LEM. Solid arrows: RAA → LEM labelled ① ("@prp-excluded-middle"), LEM → ¬¬E labelled ③ ("split on \( \varphi \vee \neg\varphi \)"), ¬¬E → RAA labelled ② ("close the box by ¬I, then ¬¬E"). A dashed arrow RAA → ¬¬E labelled ① ("@prp-double-negation (b)"). Caption: "An arrow from X to Y: X derives Y over the other primitive rules. Going round the solid cycle, each rule derives the other two." (Colour optional and never the only carrier; works in both themes; labels as `\text{}` in the TikZ, references in the caption prose, not in the picture.)
   - **② on the opening example** (new, ~120 words): "Part ② says that a step of RAA can be replaced by ¬I followed by ¬¬E, keeping the box. On the derivation of @exm-raa-at-most-one, line 6 becomes two lines:" — the derivation, lines 1–5 as before, 6 \( \neg\neg(x \le 1) \) ¬I 2–5, 7 \( x \le 1 \) ¬¬E 6. "Line 6 is correct by ¬I: the box opens with \( \neg(x \le 1) \), and \( \neg\neg(x \le 1) \) is the negation of that assumption. The box itself is unchanged: both rules ask for \( \bot \) as a line of the box, and differ only in what they write after it." (Exempt (iii).)
   - **③ on the same example** (new, ~100 words): "Part ③ replaces that ¬¬E line by a split on \( (x \le 1) \vee \neg(x \le 1) \), written by LEM:" — the derivation, lines 1–6 as in ②, 7 \( (x \le 1) \vee \neg(x \le 1) \) LEM; 8 | \( x \le 1 \) (a one-line box); 9 | \( \neg(x \le 1) \); 10 | \( \bot \) ¬E 9, 6; 11 | \( x \le 1 \) ⊥E 10; 12 \( x \le 1 \) ∨E 7, 8–8, 9–11. "The first case is the goal; the second clashes with line 6 and closes itself. Together, ② and ③ turned the one RAA line into steps of ¬I, LEM and the rules of the earlier sections: that is how LEM derives RAA." (Exempt (iii).)
   
   Then 05:600 kept to "…whichever of its three forms we write down."; its last sentence → the box. 05:543-547, 05:549-598 and 05:602 → fold F2.5-d. Remarks 05:604-606 and 05:608-610 → fold F2.5-e.
10. (The "How reductio looks" subsection follows.)
11. `## How reductio looks in a mathematical proof` (the single home of ¬I vs RAA): `exm-raa-zero` (05:13-21) **moved here verbatim** as the analysis showcase, with the lead sentence (replacing 05:614) "Here is an argument of a kind that analysis uses constantly; read it one sentence at a time, with the rule of each step in brackets." Its 7-step reading 05:616-622 kept, item 4's bracket → "[The hypothesis is about **every** \( \varepsilon > 0 \); applying it to one is a step about 'every', used as ordinary reasoning (the note at the start of this chapter).]" (ch04 09:700 is re-worded to match, §6.) Then **"¬I or RAA?" (new bold lead-in paragraph and display, ~260 words)**: "The phrase 'suppose not' covers two rules. Here is one statement proved both ways, for a real number \( x \): *if \( x^3 < 0 \), then \( x < 0 \).*"
    - **By the contrapositive (CP).** "We prove that if \( x \ge 0 \), then \( x^3 \ge 0 \). Suppose \( x \ge 0 \) [assumption for →I]. Then \( x^3 = x \cdot x \cdot x \ge 0 \) [algebra]. So if \( x \ge 0 \), then \( x^3 \ge 0 \) [→I], and by contraposition, if \( x^3 \) is not \( \ge 0 \), then \( x \) is not \( \ge 0 \) [CP]: that is, if \( x^3 < 0 \), then \( x < 0 \)."
    - **By contradiction (RAA).** "Suppose \( x^3 < 0 \) [assumption for →I]. Suppose, for a contradiction, that \( x < 0 \) fails, that is, \( x \ge 0 \) [an RAA box on \( \neg(x < 0) \)]. Then \( x^3 \ge 0 \), which contradicts \( x^3 < 0 \) [¬E]. Hence \( x < 0 \) [RAA], and so if \( x^3 < 0 \), then \( x < 0 \) [→I]."
    
    Then (adapted from 03:332 and 03:345): "The first proof never assumes a negation and closes it on the unnegated statement: every negation in it is introduced, none removed. The second does exactly that, at its RAA step. Which rule a 'suppose not' uses is decided by the lines as written: what the box assumes, and what is written after it (the table in 'Reductio ad absurdum'). For an order statement the convention of Section 2.1 lets the same argument be written either way: with the goal \( x < 0 \) written as \( \neg(x \ge 0) \), the box on \( x \ge 0 \) closes by ¬I. In @exm-raa-zero, as written, the box assumes \( x \ne 0 \) and the conclusion is \( x = 0 \), so the step is RAA." Then 05:624 kept to "…so it is ¬I." (its last sentence, on *Analysis on the Real Line*'s proof that ℕ is unbounded, cut). **Quick check (new):** "¬I or RAA? (i) 'Suppose \( 15 \) is prime. Then … contradiction. Hence \( 15 \) is not prime.' (ii) 'Suppose \( n \) is not odd. Then … contradiction. Hence \( n \) is odd.'" Solution: (i) ¬I, the box opens with the statement whose negation is concluded; (ii) RAA, the box opens with \( \neg \)(\( n \) odd) and the conclusion is \( n \) odd. Fold F2.5-c follows here. Warning 05:626-628: "Chapter 5 shows how to spot this costume in written proofs and take it off." → "It is a direct proof in costume." (the word "costume", which 06:78 and ch05 use, stays). Warning 05:630-632 kept.
12. **Rule card** (replaces 05:634-642): rows ¬E, ⊥E, ¬I, MT, CP, DS, ↔I, ↔E, RAA, ¬¬E, LEM. 05:636's "and the full dictionary is in Chapter 5" cut.
13. **Looking ahead:** "Chapter 3 proves that \( P \) cannot be derived from \( \neg\neg P \), nor Peirce's law from no premises, without RAA or one of its two equivalents. Chapter 5 tells the story of the mathematicians who declined the classical principle, and shows how to spot a proof by contradiction that is a direct proof in costume."

**Folds.** F2.5-a `title="Edge cases of reductio"`: 05:105-124 (the degenerate case, Idea, derivation and 05:124) and 05:181 (the nonexample by minimal change). F2.5-b `title="Peirce's law, derived"`: 05:272 (Try it first), 05:274-278 (Idea), 05:280-307 (proof), 05:309 without its last parenthetical ("(That every derivation of it must use RAA … that settles \( \neg\neg P \vdash P \).)"), all verbatim otherwise. F2.5-c `title="RAA is never needed to finish a negation"`: 05:79 verbatim, then 05:221's last sentence ("When \( Q \) is itself a negation, the inner goal is a negation, and by the paragraph after @def-rule-raa that RAA can be replaced by ¬I.") → "When \( Q \) is itself a negation, the inner goal in @prp-contrapositive-converse is a negation, and its RAA can be replaced by ¬I in this way." F2.5-d `title="The proof: replacing one rule by another"`: 05:543-547 (Idea with *Before reading on*), 05:549-598 (proof), 05:602 (the base list), verbatim. F2.5-e `title="Other books, and a rule we could drop"`: remark 05:604-606 verbatim; remark 05:608-610 with "the one Chapter 5 studies in its last section" cut ("We keep it so that the primitive rules other than RAA form a system of their own."; B3's solution 05:803 still points to it correctly).

**Cut outright:** 05:23; 05:37's last two sentences; 05:77's argument (to one sentence); 05:600's last sentence and 05:624's last sentence (pointers); 05:636's clause.

**Quick checks:** the opening derivation's RAA line (new), the box on \( \neg(x < 0) \) (kept), De Morgan without RAA (kept), ¬I or RAA (new): four in ~4,300 words.

**Exercises.** B1 (frozen), B2 (frozen), B3, C2 (frozen), C3 (exit check) kept.
- **A1** (key proofs): (a)–(d), (f) kept. (e)'s solution: "…and the rules never lead from true premises to a false conclusion (proved in Chapter 3, @thm-soundness)." → "…so each such step can be broken (Section 1.1's test), and a last line ∨I from it would rest on a step that can lead from a true premise to a false line." (g) → "In the instance of ② on the opening example (in 'One principle in three forms'), which rule justifies the line \( \neg\neg(x \le 1) \), and why does the box of lines 2–5 need no change?" Solution: 05:675's text with \( \varphi \) read as \( x \le 1 \) (¬I, since the box opens with \( \neg(x \le 1) \); both rules ask only for \( \bot \) as a line of the box itself).
- **A2: Drill** (`exr-reductio-and-classical-rules-a2`):
  (a) A box opens with \( \neg(P \wedge Q) \) and ends with \( \bot \). What may RAA write after it, and what may ¬I? — RAA: \( P \wedge Q \); ¬I: \( \neg\neg(P \wedge Q) \).
  (b) To prove \( Q \vee R \) by RAA, which statement opens the box? — \( \neg(Q \vee R) \), not \( \neg Q \vee R \).
  (c) To prove \( x \ge 2 \) by contradiction, what is assumed? — \( x < 2 \), that is \( \neg(x \ge 2) \); not \( x \le 2 \), which \( x = 2 \) satisfies together with the goal.
  (d) "Suppose \( 9 \) is prime. … This is impossible. Hence \( 9 \) is not prime." ¬I or RAA? — ¬I.
  (e) "Suppose \( n^2 \) is not even. … This is impossible. Hence \( n^2 \) is even." ¬I or RAA? — RAA.
  (f) Which of ¬¬I, ¬¬E, LEM, MT, DS are derived in this chapter with RAA? — ¬¬E and LEM; ¬¬I, MT and DS without.
  (g) Line 1 is \( \neg\neg(P \to Q) \). What does "¬¬E 1" write? — \( P \to Q \).
  (h) Find the illegal line: 1 \( \neg(P \wedge Q) \); 2 | \( \neg P \); 3 | | \( P \wedge Q \); 4 | | \( P \) ∧E 3; 5 | | \( \bot \) ¬E 4, 2; 6 | \( \neg(P \wedge Q) \) ¬I 3–5; 7 \( P \) RAA 2–5. — Line 7: lines 2–5 are not a box (the box opened at line 2 ends at line 6), and RAA needs \( \bot \) as a line of the box itself.
  (i) Derive \( \neg\neg P, \ P \to Q \vdash Q \). — 3 \( P \) ¬¬E 1; 4 \( Q \) →E 2, 3.
  (j) Derive \( \neg P \to P \vdash P \). — 2 | \( \neg P \); 3 | \( P \) →E 1, 2; 4 | \( \bot \) ¬E 3, 2; 5 \( P \) RAA 2–4.
  (k) Derive \( \neg P \to Q, \ \neg Q \vdash P \) in two lines. — 3 \( \neg\neg P \) MT 1, 2; 4 \( P \) ¬¬E 3.
- **B4** (label reused; new scaffolded item), `[B4: Stuck at a letter]`: "A search for \( (\neg P \to Q) \wedge (\neg P \to R), \ \neg(Q \wedge R) \vdash P \) has reached the stage below. *Name the move, then complete it.*" Shown: lines 1–2, a gap, line 10 \( P \) unjustified. Answer: the goal is a letter and both halves of the premise wait for \( \neg P \), which is nowhere: *when stuck, assume the negation of the goal*: 3 | \( \neg P \); 4 | \( \neg P \to Q \) ∧E 1; 5 | \( Q \) →E 4, 3; 6 | \( \neg P \to R \) ∧E 1; 7 | \( R \) →E 6, 3; 8 | \( Q \wedge R \) ∧I 5, 7; 9 | \( \bot \) ¬E 8, 2; 10 \( P \) RAA 3–9.
- **C1** `[C1: Challenge: Excluded middle does the work of reductio directly]`: stem and part (a) with its hints and solution kept; part (b) and its solution (05:882) cut (plan; it is bookkeeping on the folded proof).
- **C2** (frozen item): (c)'s solution "…and Chapter 3 proves that no derivation leads from true premises to a false conclusion (@thm-soundness). So citing a line of a sibling box is illegal in general, not just unlucky here." → "…so the move can carry a true premise to a false conclusion. So citing a line of a sibling box is illegal in general, not just unlucky here." (§8 item 33).

**Sidecars:** `exm-raa-at-most-one.py` (\( x^2 \le x \Rightarrow x \le 1 \) on a fine grid and exactly on \( [0, 1] \); \( x > 1 \Rightarrow x^2 > x \)); the x³ comparison (\( x \ge 0 \Rightarrow x^3 \ge 0 \)); A2(c) (\( x = 2 \)).

### 4.6 Section 2.6: How to Find a Derivation (`06-finding-derivations.md`)

**Budget:** main line ≤ 4,800 words (now 4,652, with ~750 words of new reference material: card, chart, named moves); folds ≤ 550. Looking ahead: item 14.

**New order of material.**
1. 06:3 kept.
2. `## The moves so far`: 06:7-23 kept (the moves table is the decision chart's source).
3. `## Partial derivations` **reordered**: first a snapshot, then the words, then the definition. Lead (~90 words, replacing 06:27): "Every section since Section 1.2 has shown derivations growing, as snapshots with a row \( \vdots \) between what is known and what is wanted. Here is the first snapshot of the first search below, for \( P \to \neg Q \vdash \neg(P \wedge Q) \wedge (Q \to \neg P) \):" — the schema snapshot of 06:113-120 (line 1, gap, line 7, gap, line 13, line 14 ∧I 7, 13), reprinted. Then (~60 words): "Each row \( \vdots \) is a **gap**. The written line just below a gap, here line 7 or line 13, is the gap's **current goal**; it has no justification yet. The lines available at that goal, here the premise, are the gap's **resources**. The definition says the same thing exactly." Then `def-partial-derivation` verbatim, 06:35 kept, 06:37 cut to its last two sentences ("The snapshots in the worked searches below are all partial derivations; a line carries the number it will have in the finished derivation, and a line whose place is not yet fixed carries no number. On paper you would number the lines at the end."). 06:39 → fold F2.6-a. Quick check 06:41-47 **moved** to after `exm-search-distribute` (item 5).
4. `## The method`: 06:51 kept. The algorithm block kept, except (§8 item 34): step 2's last bullet → "\( \psi \vee \chi \): **postpone**; do not choose a side yet (Section 1.5)."; step 4 gains, as its last sentence, "When the clash needs a disjunction whose negation is a resource, either side may be chosen to build it: once the disjunction is written, \( \bot \) follows." 06:72 kept, then **three bullets** replacing 06:74-78 (~150 words):
   - **Step 2 loses nothing.** If a gap with the goal \( \psi \to \chi \) can be filled at all, so can the gap inside a box on \( \psi \) with the goal \( \chi \); the same holds for \( \wedge \), \( \neg \) and \( \leftrightarrow \). So step 2 may be applied without thinking.
   - **Choosing a side of \( \vee \) can lose everything.** From \( P \vee Q \) the goal \( Q \vee P \) is derivable (@exm-disjunction-first-derivations), but neither side follows from \( P \vee Q \): with \( P \) true and \( Q \) false, \( P \vee Q \) is true and \( Q \) false, which breaks the step to \( Q \), and the step to \( P \) breaks the other way round. Choose a side only once the resources decide it, or to build a clash (step 4).
   - **Step 5 loses nothing either, and still comes last**: the goal \( \bot \) gives step 2 nothing to work with, a good statement to split on must be chosen, and a derivation that did not need the classical step reads worse with it (the costume of Section 2.5).
   
   Then fold F2.6-b. Quick check 06:80-93 kept (its (d) still uses LEM; its (b) solution unchanged).
5. `## Splitting the goal`: 06:97 and `exm-search-distribute` kept (snapshots already there). In "*Steps 3 and 4, second gap*" (06:154), after its first sentence, a **Givens/Goal table** (new):

   | Givens | Goal |
   |---|---|
   | \( P \to \neg Q \), \( \neg(P \wedge Q) \), \( Q \), \( P \) | \( \bot \) |
   | … and \( \neg Q \) (→E 1, 9) | \( \bot \) ✓ (\( Q \) and \( \neg Q \) clash) |

   06:183-186 kept. Then the **moved Quick check** 06:41-47 (now after the snapshots it asks about).
6. `## Cases must end in the goal`: `exm-search-cases` gains a **first snapshot** before 06:201 (lines 1–3, gap, line 8 \( R \) unjustified); the rest kept. 06:244-246 kept, 06:246 trimmed to its first three sentences.
7. `## Postponing a disjunction`: `exm-search-postpone-or` kept; 06:286's last parenthetical "(Chapter 3 turns such rows into proofs that no derivation exists: @cor-refuting-row.)" cut (the rows stay, as try-to-break). 06:344's last sentence (the 22-line route) kept. Warning 06:347-349 kept.
8. `## When nothing else works`: `exm-search-raa` kept. 06:439 **rewritten around two snapshots** (~170 words of prose), the search for Peirce's law: lead "The derivation of Peirce's law (@prp-peirce, in the fold of Section 2.5) adds one detail to step 5." **Snapshot S1, the stall** (a schema; only line 1 numbered, as in the dead end of `exm-search-postpone-or`): 1 | \( (P \to Q) \to P \) assumption; | | \( P \) assumption; gap; | | \( Q \); | \( P \to Q \) →I; | \( P \) →E; \( ((P \to Q) \to P) \to P \) →I. Prose: step 2 opened a box with the goal \( P \); step 3 made \( P \to Q \) a subgoal; step 2 opened a box on \( P \) with the goal \( Q \); there the search stalls, and assuming \( \neg Q \) at the stalled gap gives nothing new, since a clash with \( \neg Q \) needs \( Q \), the stalled goal itself. **Snapshot S2, one level out** (final numbers): 1 | \( (P \to Q) \to P \); 2 | | \( \neg P \); 3 | | | \( P \); gap; 5 | | | \( Q \) unjustified; 6 | | \( P \to Q \) →I 3–5; 7 | | \( P \) →E 1, 6; 8 | | \( \bot \) ¬E 7, 2; 9 | \( P \) RAA 2–8; 10 \( ((P \to Q) \to P) \to P \) →I 1–9. Prose: the new resource \( \neg P \) is available in every gap inside its box, including the stalled one, where it clashes with line 3; that is why step 5 says to try a goal further out. **Quick check (new):** "In S2, which two resources of the gap clash, and what does ⊥E then write?" Solution: lines 3 (\( P \)) and 2 (\( \neg P \)) give \( \bot \) by ¬E 3, 2 at line 4, and ⊥E 4 writes \( Q \), line 5.
9. `## A search that fails`: 06:443-460 kept. 06:462 **replaced by a table** (~150 words with its lead and close):

   | Attempt | What it needs | Why that goes round in a circle |
   |---|---|---|
   | step 3: →E on line 1 | \( P \) | \( P \) is the goal |
   | step 4: a clash | a negation among the resources | there is none |
   | step 5: RAA, a box on \( \neg P \) | \( P \), to clash with \( \neg P \) | \( P \) is the goal |
   | step 5: LEM on \( P \) | in the case \( \neg P \), the goal \( P \) | the same gap, one resource richer and no closer |
   | step 5: LEM on \( Q \) | in the case \( Q \), the goal \( P \) | that case is where we started (the case \( \neg Q \) clashes with line 2) |
   | step 5 further out: RAA on \( \neg(Q \to P) \) | \( Q \to P \), to clash | step 2 opens the same box on \( Q \) with the same goal \( P \) |

   Close: "Every row returns to one gap, '\( P \) from \( P \to Q \) and \( Q \)'. That is affirming the consequent (Section 1.3), the step that would repair Argument B, and Section 1.1 broke its form at \( n = 2 \)." **Quick check (new):** "Which row of the table would close the gap if affirming the consequent were a rule?" Solution: the first: →E's mirror image would give \( P \) from \( P \to Q \) and the resource \( Q \). 06:464 kept. 06:466 → "That is the question this chapter leaves open. *We show that something is derivable by exhibiting a derivation; how could we ever show that something is not?* Section 1.1's move already breaks the form: with \( P \) false and \( Q \) true, \( P \to Q \) is true and \( Q \to P \) false. What it cannot yet tell us is that **no derivation** leads from a premise to a conclusion that some choice of statements makes false." (The answer moves to the box.)
10. `## A mathematical goal`: `exm-skeleton-odd-product` kept; its skeleton paragraph gains a **Givens/Goal table** (new) after "*The skeleton.*":

    | Givens | Goal |
    |---|---|
    | the facts: every integer is even or odd, and not both; if \( m \) is even, then \( mn \) is even | if \( mn \) is odd, then \( m \) is odd and \( n \) is odd |
    | … and \( mn \) odd (→I) | \( m \) odd and \( n \) odd |
    | the same | \( m \) odd; \( n \) odd (∧I: two goals) |
    | … and \( mn \) not even, \( m \) not even (CP, →E) | \( m \) odd ✓ (DS); \( n \) odd by the same steps |

    06:487's last parenthetical ("(The phrase 'say \( m = 2k \)' names a witness … Chapter 4.)") cut (index note). Warning 06:490-492 kept.
11. `## The rules in one place` (06:494-689), the one-page reference, in this order:
    - **The rule card (new):** all thirteen primitive rules, columns Rule | Shape | You write | Lean: Chapter 1's seven rows exactly as on 1.6's card (∧I, ∧E, →E, →I, R, ∨I, ∨E), then ¬E, ⊥E, ¬I, ↔I, ↔E, RAA as in §1.7. Lead sentence: "Here are all the primitive rules of Chapters 1 and 2 on one card." Nothing depends on the Lean column (one sentence).
    - 06:496 and the schemas 06:498-655 kept (ch03 05:37 relies on "the primitive rules … collected in Section 2.6").
    - The derived-rules table 06:657-685 kept (rows unchanged; 06:685 kept).
    - **The decision chart (new)**, extending 1.6's three rows (copied verbatim from ch01 07: the \( \wedge \), \( \to \), \( \vee \) rows), with the lead "Each rule is also a move. Read by the goal's main connective, the introduction rules say how a goal is built; read by an available line's main connective, the elimination rules say how that line is used." New rows:
      | Main connective | As the goal (goal-directed) | As an available line (premise-directed) |
      |---|---|---|
      | \( \neg \) | open a box with the unnegated statement; the new goal is \( \bot \); close with ¬I | clash it by ¬E: make the unnegated statement a subgoal |
      | \( \leftrightarrow \) | two boxes, one each way; close with ↔I | cross with ↔E once one side is on a line |
      | \( \bot \) | find or manufacture a clash (¬E) | ⊥E writes the current goal |
      | stuck | RAA on the current goal, or LEM on a well-chosen statement | — |
    - Warning 06:687-689 kept.
    - `### Named moves`: the seven moves of the index (§4.0 item 6), with their sections.
12. **Looking ahead:** "Chapter 3 gives each statement a truth value and proves that the rules never lead from true premises to a false conclusion. Then one choice of truth values, such as \( P \) false and \( Q \) true for the failed search above, proves that no derivation exists." (ch03 05:3 and 05:278 are written to this.)

**Folds.** F2.6-a `title="A snapshot that is not a partial derivation"`: 06:39 verbatim. F2.6-b `title="Why the order loses nothing"`: 06:74-78, verbatim except in 06:76 "leaves a gap that cannot be filled (Chapter 3 makes 'cannot' exact, @cor-refuting-row)" → "leaves a gap whose goal does not follow from its resources: \( P \) true and \( Q \) false makes \( P \vee Q \) true and \( Q \) false" (§8 item 35).

**Cut outright:** 06:37's first three sentences, 06:462's paragraph (to the table), the pointers of 06:286, 06:466 and 06:487.

**Quick checks:** first goals (kept), the moved resources check (kept), Peirce's gap (new), the failed-search table (new): four in ~4,800 words, plus two Givens/Goal tables.

**Exercises.** A1 kept (its (b) solution's "(Naming \( n \) uses a rule for 'there exists', from Chapter 4.)" cut, index note). B1 (frozen), B2 (scaffolded; the faded triple's middle), B3, C1 (the faded triple's last), C2 (frozen except (b)'s `@cor-refuting-row` → plain "Chapter 3"), C3 (exit check), C4, R1, R2 kept; R3's solution "Chapter 3 proves that such a row rules out every derivation (@cor-refuting-row)" → without the `@ref`. C3's solution step 6: "(see the paragraph on choosing a side of ∨, after the method)" → "(step 4 allows either side when the disjunction is built for a clash with its own negation)".
- **A2: Drill** (`exr-finding-derivations-a2`):
  (a) The goal is \( \neg(P \vee Q) \). What does step 2 set up? — A box opened with \( P \vee Q \), with the goal \( \bot \).
  (b) The goal is \( (P \to Q) \wedge \neg R \). Which gaps does step 2 leave? — Two boxes: one on \( P \) with the goal \( Q \), one on \( R \) with the goal \( \bot \).
  (c) The goal is \( P \vee Q \), and the one resource is \( \neg P \to Q \). Which step does the work, and how? — Step 2 postpones; step 3 cannot fire (it needs \( \neg P \)); step 5: LEM on \( P \), the statement the resource waits for.
  (d) The goal is \( \bot \), and the resources are \( \neg(P \wedge Q) \), \( P \), \( Q \). What are the next two lines? — \( P \wedge Q \) by ∧I, then \( \bot \) by ¬E.
  (e) In a partial derivation the current goal is line 9, inside the boxes opened at lines 3 and 6; line 1 is a premise, and lines 4–5 form a box inside box 3 that has closed. Which of lines 1, 3, 4, 6 are resources? — 1, 3 and 6; not 4.
  (f) Which step of the method opens an RAA box, and when? — Step 5, when steps 2–4 give nothing.
  (g) True or false: a failed search shows that the sequent is not derivable. — False: it shows only that this search failed.
  (h) The goal is \( R \), and the resources are \( P \vee Q \), \( P \to R \), \( Q \to S \). Should the search be expected to succeed? — No: \( P \) false, \( Q \) true, \( R \) false, \( S \) true makes every resource true and \( R \) false, so the form is bad; in ∨E the case \( Q \) gives only \( S \).
  (i) Find a derivation of \( P \vee Q, \ \neg P \vdash Q \vee R \). — 3 \( Q \) DS 1, 2; 4 \( Q \vee R \) ∨I 3.
  (j) Find a derivation of \( (P \vee Q) \to R \vdash Q \to R \). — 2 | \( Q \); 3 | \( P \vee Q \) ∨I 2; 4 | \( R \) →E 1, 3; 5 \( Q \to R \) →I 2–4.
  (k) Find a derivation of \( P \to (Q \to R), \ P \wedge \neg R \vdash \neg Q \). — 3 \( P \) ∧E 2; 4 \( \neg R \) ∧E 2; 5 \( Q \to R \) →E 1, 3; 6 \( \neg Q \) MT 5, 4.

**Sidecars:** none new (all items are letters).

---

## 5. Budgets and the Time line

| Section | Main line now (before Exercises) | Main-line budget | Folds |
|---|---|---|---|
| 2.1 | 3,507 | ≤ 3,200 | ≤ 450 |
| 2.2 | 2,420 | ≤ 2,300 | ≤ 300 |
| 2.3 | 3,300 | ≤ 3,000 | ≤ 500 |
| 2.4 | 3,685 | ≤ 3,300 | ≤ 750 |
| 2.5 | 5,070 | ≤ 4,300 | ≤ 1,700 |
| 2.6 | 4,652 | ≤ 4,800 | ≤ 550 |
| total | 22,634 | ≤ 20,900 | ≤ 4,250 |

Every file stays under 5,000 main-line words. The whole-file advisory count of `check_structure.py` (with exercises) will stay above 5,000 in 2.1, 2.3, 2.4, 2.5 and 2.6, as now; it is advisory, and the binding budget is the main line.

Exercises after the revision: 6 A1, 6 A2 (drill banks, 65 parts, counted as about 16 exercises at one per four parts, STYLE §12.8), 22 B (3 new: 2.1 B4, 2.4 B4, 2.5 B4 (reused label); scaffolded: 2.1 B4, 2.2 B1, 2.3 B3, 2.4 B3 (parts) and B4, 2.5 B4, 2.6 B2 (existing)), 16 C (exit checks 2.3 C3, 2.5 C3, 2.6 C3; one Challenge, 2.5 C1), 3 R.

**Time (B1 formula: 15 min per 400 main-line words; 20–45 min per exercise; a drill bank counts as one exercise per four parts).** Core track = main line, all of A, one B and one non-Challenge C per section (the exit check where the section has one): reading 20,900 words ≈ 13.1 h; A1 6 × 25 min, A2 about 16 × 30 min, one B 6 × 30 min, one C 6 × 40 min ≈ 17.6 h; **≈ 30.7 h, so "About 30 hours on the core track"** (unchanged). Full track: main line plus folds ≈ 25,150 words ≈ 15.7 h; exercises A1 150 min, A2 about 490 min, 22 B × 30, 16 C × 40, 3 R × 40 ≈ 34.3 h; **≈ 50 h, so "about 50 hours for everything"** (up from 45: the six drill banks add about 8 hours). The plan's 25-hour core target is not reached: the drills cost what the cuts save. The drafter recomputes from the delivered text by the same rule (`check_structure.py --words`) and does not shade the number down (STYLE §11.9); §4.0 fixes no figure in advance.

---

## 6. Edits needed outside Chapter 2

No label moves, no section number changes, and no "Section 2.x" mention becomes false by number. These sentences describe text this revision changes, and are edited at step R6 (fd1) or reported to the coordinator:

| Where | Now says | Should say |
|---|---|---|
| ch04 09:700 | "…and the reading after it said that 'the hypothesis applies to it' is a rule for 'every' that Chapter 4 would make precise." | "…and the reading after it called 'the hypothesis applies to it' a step about 'every', used as ordinary reasoning until Chapter 4." |
| ch03 05:290 | "…because neither \( \neg P \) nor \( \neg Q \) follows from the premise alone, and it said 'the rules never lead from true premises to a false conclusion' as its reason. Now that reason is a theorem: …" | "…because the step from the premise to either disjunct can be broken, by a row that makes the premise true and the disjunct false. Now those rows are proofs: …" (the rest unchanged) |
| ch04 03:9-10 | `@exm-raa-zero` (Section 2.5) | unchanged (the example stays in 2.5, verbatim) |
| ch05 01:7, 01:108 | `@exm-square-even-via-contrapositive` reprinted, with its line 11 | unchanged (the example is kept verbatim) |
| ch05 07:417, 07:433 | a result of Section 2.2 that removes negations without ¬¬E (`@exm-triple-negation`) | unchanged (it stays in 2.2) |
| ch05 07:97 | the table in Section 2.2, after `@def-rules-negation` | unchanged (02:68-73 stays) |
| ch05 01:210 | "\( \neg(a \le b) \) by the order fact of Section 2.1" | unchanged (now the convention box of 2.1) |
| ch04 07:443 | MT, CP, DS have their rows in Section 2.3, ¬¬E and LEM in Section 2.5 | unchanged (the rule cards) |
| ch03 05:37, 05:310, 05:356; ch03 06:226, 06:558 | the primitive rules collected in Section 2.6; Section 2.5's promise about \( \neg\neg P \vdash P \); Peirce derived in Section 2.5; De Morgan (b), (c) without RAA | unchanged (the schemas stay in 2.6; 2.5's box keeps the promise; Peirce's derivation is in 2.5's fold; 05:438 stays) |
| ch04 04:426, 08:309-333 | "safe, in the sense of Section 2.6"; step 2 postpones ∨; step 4 clash | unchanged (the bullets keep the sense; ch04 08 restates step 2 and step 4 compatibly) |
| fd2 01:148, 02:162 | Chapter 2 claimed (L) and gave the halving reason | unchanged (02:225 keeps both) |
| fd2 ch01 02:134 | De Morgan (a) and (b) derived in Section 2.5 without RAA | unchanged |

**STATUS.md promise table** (coordinator, R6): row 64 (F1.2 soundness) loses §01 (the ⊥E remark now points back to 1.2's promise), §02, §03's "made exact" (now 2.3's box, substitution), the §04 warning, the §06 "cannot be filled" and C2 entries; it keeps §06's box (the failed search) and R3's plain pointer, and the index. Row 65 (\( \neg\neg P \vdash P \), Peirce) moves from §04/§05 prose to §05's Looking-ahead box only (04:227 and 05:37 no longer cite `thm-raa-independent`). Row 74 (¬P as P → ⊥; history) loses §02 (02:77's clause cut) and stays for §05's box. Row 75 (costume) stays, now carried by §05's box. Row 76 (quantifier steps) becomes "index note, F1.2" plus the three places that keep "used as ordinary reasoning" (§01 01:345, §02 02:275, §05 the reading of `exm-raa-zero`). Row 77 ((L), F2.2) is carried by §02's box. Row 80 (AN1.1) loses "the proof that ℕ is not bounded above is ¬I (§05)" (05:624's sentence cut) and gains §04's box (square roots). Row 81 (AN1.7) stays as a ledger source only (the fold names no volume).

**Downstream volumes.** fd2, fd3 and an1 cite 20 of this chapter's labels (§3.1); none changes content, and none is folded except `prp-peirce`, `prp-provable-equivalence-basics` and `thm-classical-rules-interderivable`, which no later volume cites. The R7 seam referee reads their "*Logic and Proof*, Chapter 2 / Section 2.x" mentions (fd2 01:157 Section 2.4's two paragraphs; fd2 02:134; fd3 03 01:181 Section 2.1; an1 01 index:7, 06:7, 07:424, 07:441, 07:459) against the new text; all describe kept content.

---

## 7. What stays exactly as it is

The motivating openings of every section (the novice report's "keep this"); the named moves and every Idea; the line-by-line table after `thm-square-even-implies-even` (01:332-343); the √2 proof with its *Before reading on* prompt, A1(e) and C2; the parity theorem proved three ways (2.1, 2.3, 2.4); the ¬I/RAA table (05:72-75) and the verdict that √2 is ¬I; the find-the-error items (2.1 C2, 2.3 C2, 2.5 C2 with true conclusions; 2.2 C2 with a false one); the proof-ordering item (2.3 B2); the faded triple of 2.6 (`exm-search-distribute`, B2, C1); the "What the method did" debriefs; the failed search's honest "a search that fails proves nothing"; the schemas and the derived-rules table of 2.6; both Try-it-first prompts (De Morgan (d), main line; Peirce, in its fold); the exit checks (2.3 C3, 2.5 C3, 2.6 C3) with their marking schemes; the hint ladders; the R group; every statement and proof of every label in §3.1 marked kept, kept (moved) or kept (folded).

---

## 8. S2a: every new or changed claim that needs blueprint verification

**Changed wording in cited or reviewed blocks:**
1. The global quantifier note (index) and the three places that now say "used as ordinary reasoning" (01:345, 02:275, 05:619): true descriptions of the steps; nothing rests on them; ch04 09:700's new wording matches.
2. `def-rules-negation`'s reading: clause 3 and 02:66 lose their soundness sentences; the block is verbatim. Check the 14 outside citations still hold (they cite the rule).
3. Fold F2.1-a: 01:60 reworded to point back to Section 1.2's promise (that promise covers "every rule of Chapters 1 and 2", which includes ⊥E and the rules passing ⊥ along).
4. The convention box of 2.1: the four order equivalences and \( a \ne b \) as \( \neg(a = b) \); "a derivation writes the negation out whenever ¬E or ¬I must see it" agrees with every kept derivation and reading (01:381, 01:524, 02:366, 05:616-621) and with Chapter 1's ≤/≥ box (1.5); ch05 01:210's "order fact of Section 2.1" still points to it.
5. The ⊥E intuition and "Why is this honest?" line (no forward pointer used as a reason; the claim is the informal one 01:60 already made).
6. `exm-square-plus-one`'s added derivation: lines 1–5 check with `check_fitch.py` (`\by{algebra}{2}`); the statement and prose solution unchanged; an1 01:117 still true.
7. 2.2's merged warning: "a box opened with \( \neg(x > 0) \) and closed by ¬I gives \( \neg\neg(x > 0) \)".
8. 2.2's Looking-ahead wording: (L) is proved in F2.2 from well-ordering (`lem-lowest-terms`); AN1.1 uses `thm-sqrt2-irrational` as stated (an1 06:7, 02:207…).
9. 2.3's figure and its claim "a derived rule … lets us prove nothing the primitive rules could not" (the fold F2.3-a keeps the argument; the figure's two derivations check).
10. 2.3's Wason table: each row's rule claim; the turned cards (6 and green) agree with `exm-wason-selection`'s solution in 1.3; the reversed-claim Quick check (the 7).
11. 2.3's prose payoff: three sentences, each step named (¬I with (E2), CP with →E, DS) matching `exm-square-even-via-contrapositive`.
12. 2.4's opening sentence (1.1 now warns and does not promise; ch01 01:113).
13. 2.4 warning 04:272-274 without soundness: "breaks the form" for \( P \vdash P \wedge Q \) at "2 > 1", "1 > 2".
14. 2.4's new converse warning: \( 6 \mid n \Rightarrow n \) even (\( n = 6k = 2(3k) \)); the converse broken at \( n = 4 \).
15. 2.4's Quick check: the converse of "\( x > 2 \Rightarrow x^2 > 4 \)" broken at \( x = -3 \).
16. 2.4's \( P \wedge Q \dashv\vdash Q \wedge P \) via `prp-and-commutes` with letters exchanged; fold F2.4-a's reworded parenthetical (no `@ref`; true: \( \neg\neg P \vdash P \) needs RAA, by `thm-raa-independent`).
17. 2.4's Looking ahead: AN1.1 proves square roots of non-negative reals exist (`thm-nth-root`).
18. `exm-raa-at-most-one`: true (\( x^2 \le x \iff 0 \le x \le 1 \)); its prose; its 6-line derivation checks (lines 3–4 `\by{algebra}`; line 4 written \( \neg(x^2 \le x) \) by the convention; line 5 cites 1 then 4).
19. 2.5's reworded items 1–2 of "Where the rules so far stop short" and 05:37's replacement (no claim beyond "no search can settle"; the promise is in the box).
20. `prp-excluded-middle`'s Idea: "\( P \) false breaks the first, \( P \) true the second" (forms with no premises: \( \vdash P \) and \( \vdash \neg P \)).
21. `prp-de-morgan`'s Idea: the two breaking rows; no claim that no derivation exists.
22. 2.5's one sentence replacing 05:77 (RAA belongs to no connective; ⊥E counts as ⊥'s elimination rule, R is a clause, as 05:77 said).
23. The cycle diagram: the arrows' directions and labels match ①②③ of the folded proof; the caption ("each rule derives the other two" by going round the solid cycle, chaining as 05:597 does).
24. ② on the opening example: line 6 ¬I 2–5, line 7 ¬¬E 6; "the box is unchanged".
25. ③ on the same example: lines 7–12 (LEM; one-line box; ¬E 9, 6 with \( \varphi = \neg(x \le 1) \); ⊥E; ∨E 7, 8–8, 9–11); "that is how LEM derives RAA" on this instance (② then ③, as the fold's chaining paragraph says).
26. The x³ comparison: both proofs correct; the CP route removes no negation; the RAA route's box opens with \( \neg(x < 0) \); "written with the goal \( x < 0 \) as \( \neg(x \ge 0) \), the box on \( x \ge 0 \) closes by ¬I" (true under the convention); "in `exm-raa-zero`, as written, the step is RAA" (no claim that RAA is needed). This replaces 03:345's "needs the rule of Section 2.5".
27. Fold F2.5-c's added last sentence (05:221's claim, applied to `prp-contrapositive-converse` with \( Q \) a negation).
28. 2.5's "¬I or RAA?" Quick check (15 prime: ¬I; "n not odd": RAA).
29. 2.5 Looking ahead: matches `thm-raa-independent` (states \( \neg\neg P \vdash P \) and \( \vdash P \vee \neg P \)) and the remark after it (Peirce); F1.5's history and costume examples exist (`exm-costume-direct`, `exm-costume-contrapositive`).
30. 2.6: the informal gap/goal/resources lead agrees with `def-partial-derivation`; the moved Quick check's answer (lines 1, 7, 8, 9) is unchanged.
31. 2.6's three bullets (step 2 loses nothing; the ∨ rows; step 5 last) and the Givens/Goal tables (search-distribute's second gap; the odd-product skeleton).
32. 2.6's Peirce snapshots (S1 stall; S2 with final numbers 1–10 matching `prp-peirce`'s derivation; the Quick check: ¬E 3, 2 at line 4, ⊥E 4 writes \( Q \)).
33. 2.5 C2 (c) and A1 (e) without `@thm-soundness` (the move "can carry a true premise to a false conclusion" is shown by the row given).
34. 2.6's algorithm: step 2 without the ∨ exception; step 4's new sentence ("either side may be chosen … once the disjunction is written, \( \bot \) follows"); C3's solution pointer reworded.
35. Fold F2.6-b: 06:76's reworded clause (a breaking row, not "cannot be filled").
36. 2.6's failed-search table: each row's need and circle; "Section 1.1 broke its form at \( n = 2 \)" (ch01 1.1's "Argument B, tried"); the Quick check (row 1).
37. 2.6's 06:466 rewrite: the form \( P \to Q \Rightarrow Q \to P \) breaks at \( P \) false, \( Q \) true; "what it cannot yet tell us is that no derivation…" (no claim either way).
38. 2.6's rule card (Shape and phrase for all thirteen rows, consistent with 1.6's card and §1.7) and decision chart (the ¬, ↔, ⊥, stuck rows agree with the method).

**New and changed exercise answers:**
39. 2.1 A2 (a)–(k), especially (f) (the written-out encoding) and (h); B4 (scaffold, 11 lines).
40. 2.2 A2 (a)–(j), (e)'s identity; B1 as a scaffold (shown lines; the kept solution).
41. 2.3 A2 (a)–(k), (h)'s breaking row, (i) (MT does not match); B3 as a scaffold.
42. 2.4 A2 (a)–(k); B3 split (each part's answer from 04:548); B4 (scaffold, 12 lines).
43. 2.5 A1 (e), (g) reworded; A2 (a)–(k), (h)'s range; B4 (new scaffold, 10 lines); C1 without (b).
44. 2.6 A2 (a)–(k), (h)'s breaking row; A1 (b)'s cut parenthetical; C2 (b), R3 without `@ref`s.

**Routes to confirm do not rest on removed or folded material:** every main-line statement whose proof is folded (`prp-provable-equivalence-basics`, `prp-peirce`, `thm-classical-rules-interderivable`) is cited later only as a statement; every A and B exercise is doable with the folds closed (2.5 A1(g) now asks about the main-line instance; B3's pointer to the remark after the theorem is in a solution); `exm-triple-negation` and `exm-square-even-via-contrapositive` stay on the main line for ch05; no main-line or fold sentence uses soundness as a reason.

---

## 9. Decisions this file makes against the plan's wording (for S2 and the author)

- **D1.** `exm-triple-negation` is not turned into a B exercise. ch05 07:433 uses its derivation as a result proved without RAA, and ch05 07:417's hint sends the reader to Section 2.2 for it; an exercise may not carry what a later proof rests on. It moves after `exm-square-plus-one` and \( P \vdash \neg\neg P \), so the section no longer opens with negation-stacking.
- **D2.** Disjunctive syllogism is not restated "for either disjunct", and the 13-line derivation of `exm-square-even-via-contrapositive` is not turned into an exercise. `prp-disjunctive-syllogism` is cited four times in fd1 with its left-disjunct content, and ch05 01:7 reprints the 13-line derivation, line 11 included. The plan's "prose-only payoff" is met by the three-sentence prose version placed before the kept example, and the other form of DS is already a named row of 2.6's table (B1 (a)).
- **D3.** The rule cards of 2.1–2.5 list Chapter 2's rules so far, with Chapter 1's seven on 1.6's card; 2.6's card is the full cumulative one. STYLE §12.6's "cumulative at the end of a run of rule sections" read with Chapter 2 as the run.
- **D4.** The x³ warning (03:345) is not moved verbatim: its claim that the box on \( x \ge 0 \) "needs the rule of Section 2.5" is false once the convention lets \( x < 0 \) be written \( \neg(x \ge 0) \). 2.5's single home says instead that the written lines decide the rule (§8 item 26).
- **D5.** 2.4's converse warning uses \( 6 \mid n \Rightarrow n \) even, not divisible-by-4: Chapter 1 now makes exactly the divisible-by-4 point at ch01 01:113.
- **D6.** The plan's "promote B4 into the text" is done twice over: old B4 (\( x^2 \le x \Rightarrow x \le 1 \)) becomes both 2.5's opening RAA example and the main-line instance of ②, and ③ is shown on the same example, so the reader follows one argument from RAA to ¬I + ¬¬E to LEM. The freed uncited label carries a new scaffold.
- **D7.** ¬E gets four bullets (STYLE §12.2 lists neither ¬E nor ⊥E; ¬E has an order and an exactness condition, as →E does); ⊥E three. ↔I/↔E keep their four one-line clauses.
- **D8.** The plan's 25-hour core target for Chapter 2 is not reached (≈ 30.7 h against 30 now): the main-line cuts save about 1.1 h of reading, and the six drill banks add about 8 h of exercises, all of A being on the core track. Nothing is shaded down.
