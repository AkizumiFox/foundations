# Chapter 3 — S2a statement referee, re-check after the logic split

**Blueprint:** `authoring/blueprints/ch03.md` (Truth, Soundness and Completeness), as of 2026-09-28, before this re-check's edits. Every edit is marked "S2 recheck #n" in the blueprint.
**Why a re-check.** The blueprint was written and S2-reviewed when the logic block had one chapter before it. The author has since split that chapter into Chapter 1 (`connectives-and-derivations`) and Chapter 2 (`negation-and-classical-logic`). Their blueprints (`ch01.md`, `ch02.md`) and the drafted text in `src/ch01-connectives-and-derivations/` (§01–§07) and `src/ch02-negation-and-classical-logic/` (§01, §02, §03, §05) are now the authority for labels and rules.
**Brief.** PIPELINE S2a. Every statement, proof route, intended exercise answer and marking scheme was re-verified adversarially. Every label cited from Chapters 1–2 was checked for existence and for the meaning the blueprint assumes. Every derivation claimed was run through `tools/check_fitch.py`. The book.yaml entry for Chapter 3 was compared with the blueprint. Closeness to Huth & Ryan (§1.3–1.5 and Exercises 1.3–1.5, converted sections 008–021) was checked.

**Method.**
- **Labels.** Each label was grepped in `src/ch01-*`, `src/ch02-*` (the drafted `{#…}` ids) and in `ch01.md`/`ch02.md`, and the drafted block was read where one exists: `def-derivation` (05:203 defines length and context), `def-rules-implication`, `def-rules-disjunction` (the "line of that box itself" sentence inside the block), `def-rules-negation`, `def-rule-raa`, `prp-vacuous-implication` (01:170–176), `prp-contrapositive` (03:72–82), `prp-de-morgan`, `prp-double-negation`, `prp-excluded-middle`. `exm-search-postpone-or` and the Chapter 2 §06 items were checked against `ch02.md` and the archived pilot (`07-finding-derivations.md:207`, D36).
- **Derivations.** Every derivation the blueprint claims, and every replacement made here, is written out in the appendix (N1–N13). The appendix passes `python3 tools/check_fitch.py authoring/reviews/ch03-S2-recheck.md`: 21 derivations, 0 errors. Rows of `lem-connective-rows` and LEM are cited by `\by{…}`, so their shape is not checked.
- **Semantics.** A script (scratch `sem.py`, `sem2.py`) checked by exhaustion: every rule except RAA preserves the three-valued consequence of `thm-raa-independent` over all \( 3^4 \) values of \( (\min\Gamma, a, b, c) \); RAA fails at \( (1, \tfrac12) \); \( \neg\neg p \to p \) and \( p \vee \neg p \) take \( \tfrac12 \) at \( p = \tfrac12 \); Peirce takes \( \tfrac12 \) at \( (\tfrac12, 0) \). All the rows, equivalences, CNF/DNF claims, the majority connective's self-duality, the §02 sum formula (to \( n = 49 \)) and the \( 2^n \ge n^2 \) warning (fails only at \( n = 3 \) for \( n \le 11 \)) were checked.
- **Huth & Ryan.** Every sequent, formula and exercise in the blueprint was compared with H&R §1.3–1.5, their Theorem 1.31, Proposition 1.38, the completeness Steps 1–3, and Exercises 1.3, 1.4, 1.5 (the conversion truncates some items).
- **Gate.** `.venv/bin/python blueprint/check_blueprint.py 3`: 0 problems before and after the edits (one intermediate problem, a forward citation of Chapter 7's `exm-all-equal-induction` added by this re-check, was removed).

## 1. Findings

Verdicts: **correct** 21 · **minor** 18 · **gap** 4 · **error** 0 (43 rows). Every gap and minor finding below is **edited** in the blueprint, except #43, which belongs to Chapter 5's blueprint.

| # | Location | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | whole blueprint | Every label cited from Chapters 1–2 exists with the meaning assumed | correct | `def-rule-schema` (Ch 1 §02); `def-derivation` with context and length (Ch 1 §05, drafted 05:203); `def-rules-implication`, `def-rules-disjunction` (the "line of that box itself" sentence is inside both drafted blocks); `def-rules-negation` (Ch 2 §02), `def-rule-raa` (Ch 2 §05), both drafted with the same sentence; `def-rules-biconditional` (Ch 2 §04, blueprint only); `def-derived-rule` (Ch 2 §03); `prp-ex-falso` (no box), `prp-vacuous-implication` (5 lines, box 2–4), `prp-contrapositive` (7 lines, line 5 is ¬E), `prp-excluded-middle`, `prp-de-morgan` ((b), (c) without RAA), `exm-double-negation-introduction`, `prp-peirce`; `exm-search-postpone-or` is \( P \to (Q \vee R) \vdash (P \to Q) \vee (P \to R) \) (D36); Chapter 2 §06 C2 is \( \vdash (P \to Q) \vee (Q \to P) \); "a search that fails" is \( P \to Q \vdash Q \to P \). |
| 2 | header | "the proofs of soundness and completeness below follow a route of our own" | minor | False for completeness. `lem-truth-table-line` is H&R Proposition 1.38 (Kalmár's lemma), and gluing the \( 2^n \) lines with LEM is their Step 2 (conv. 012). Only the presentation differs (signed \( \varphi^{v} \); premises kept; splitting as a lemma plus induction). The header now says so and forbids the text from calling the route new. Soundness is genuinely different (H&R cut boxes open; conv. 011). **Edited.** |
| 3 | §01 Quick check | \( (\neg p \vee q) \leftrightarrow \neg(r \wedge p) \): height 4, eight subformulas | correct | Heights: \( p \) 1, \( \neg p \) 2, \( \neg p \vee q \) 3, \( r \wedge p \) 2, \( \neg(r \wedge p) \) 3, root 4. Subformulas \( p, q, r, \neg p, \neg p \vee q, r \wedge p, \neg(r \wedge p) \), the whole: 8. |
| 4 | §01 C1, "Why this definition" | 5 parse trees for \( p \to q \to r \to s \); \( p \wedge q \vee r \) has two trees with different values | correct | Catalan \( C_3 = 5 \). Row \( p = \mathrm{F} \), \( r = \mathrm{T} \): \( (p \wedge q) \vee r = \mathrm{T} \), \( p \wedge (q \vee r) = \mathrm{F} \). |
| 5 | §01 examples | book.yaml key example "parse trees of p → q → r under the right-associative convention and with brackets" | minor | Not placed. The shorthand example now names \( p \to q \to r \) and draws both groupings. **Edited.** |
| 6 | §02 | \( \sum_{k \le n} k(k+1) = n(n+1)(n+2)/3 \); the \( 2^n \ge n^2 \) warning | correct | Base \( 2 = 2 \); step adds \( (n+1)(n+2) \). \( 2n^2 \ge (n+1)^2 \) iff \( n \ge 1 + \sqrt 2 \), so for \( n \ge 3 \); the claim fails only at \( n = 3 \) (\( 8 < 9 \)), true at \( n = 2 \) and from \( n = 4 \). Neither is an H&R exercise (theirs: odd sum, Gauss sum, \( 2^n \ge n + 12 \), \( n^2 + 5n + 1 \)). |
| 7 | Induction, §02 | `ax-induction` → `thm-strong-induction` → `thm-structural-induction` (formation sequences) → `lem-parenthesis-count` → `thm-unique-readability` → `thm-structural-recursion` (symbol count) | correct | No step uses the height or unique readability before it is proved; the vacuous \( k < 1 \) case is handled; ℕ starts at 1 as Chapter 11 assumes. |
| 8 | §02 | `lem-parenthesis-count` (a)–(c) and the depth-one proof of `thm-unique-readability` | correct | (b) inductive: in \( (\varphi \circ \psi) \), a proper non-empty segment has excess \( 1 + (\ge 0) \) or \( 1 + 0 + (\ge 0) \). (c): inside \( \varphi \) depth \( \ge 1 + 1 \), inside \( \psi \) \( \ge 1 + 0 + 1 \), main connective depth 1. Tried on \( (\neg(p \wedge q) \wedge r) \): unique depth-1 connective is the second \( \wedge \). |
| 9 | §02 `lem-parenthesis-count` | presentation vs H&R | minor | (a) is H&R Theorem 1.31, also their first structural induction (by course-of-values on the **height**), and the non-strict (b) is their exercise 1.4.7(f). Standard facts; flagged so the drafter writes it our way (by `thm-structural-induction`, leading with (b), (c)). **Edited** (note). |
| 10 | §02 B1–B3 | \( 2^n \ge n+1 \); #subformulas ≤ #symbols; ≤ \( 2^h - 1 \) nodes | correct | B3: \( 2(2^{h-1} - 1) + 1 = 2^h - 1 \); \( \neg \) case \( 2^{h-1} \le 2^h - 1 \). |
| 11 | §05 `lem-context-inclusion` (b) | "if a closed box from \( a \) to \( b \) is available at \( k \), then \( \Gamma_b = \Gamma_k \cup \{\varphi_a\} \)" | **gap** | False as stated. `def-derivation` lets a box end on the same line as a box inside it (the drafted Ch 1 §07:326 says an outer box "would end inside the inner box" without an extra line). Counterexample: box 2–4 containing box 3–4, cited by nothing; at line 5 the box 2–4 is available, but \( \Gamma_4 \) contains the assumption on line 3 too. The blueprint's own reason ("every box rule requires …") only applies to a box **cited by a box rule**. Hypothesis changed to that; it is all the soundness proof uses. Chapter 4 §12 extends this (b) and is unaffected. **Edited.** |
| 12 | §02 C1, C2 | proper initial segments are not formulas; the even-parentheses find-the-error | correct | C1 by (a)+(b) for \( (\varphi\circ\psi) \), induction through \( \neg \); the second uniqueness proof works. C2: the step applies the hypothesis to \( \varphi \circ \psi \), not a formula; the counterexample to the step (property "no binary connective outside all parentheses", false of \( p \wedge q \)) is valid. |
| 13 | §05 `thm-soundness` step ④ | "its context is the premises", so \( \Gamma \models \psi \) | minor | `def-derivable` only asks that the premises **belong to** \( \Gamma \); one sentence on monotonicity of \( \models \) was missing. **Edited.** |
| 14 | §05 `cor-refuting-row` | pays "affirming the consequent is not a rule" | minor | Chapter 1 §01 and §04 promise that \( P \to Q, Q \vdash P \) **cannot be derived** (ch01.md: "not one of the rules is visible, and is not what Chapter 3 proves"). Now paid explicitly by the row \( p = \mathrm{F} \), \( q = \mathrm{T} \). **Edited.** |
| 15 | §03 C1 | the rows of \( \to \) are forced by \( \to \)E, \( \to \)I | correct | \( \to \)E at \( p = \mathrm{T}, q = \mathrm{F} \) forces (T,F)↦F; \( \to \)I with \( \Gamma \) empty, \( \varphi = \psi = p \) forces (T,T), (F,F)↦T; \( \Gamma = q \), \( \varphi = p \), \( \psi = q \) forces (F,T)↦T. No \( \to \) occurs in \( \Gamma, \varphi, \psi \), so the candidate is not used circularly. |
| 16 | §03 | `lem-coincidence`; B2 (atom occurrences = binary connectives + 1); C2 (all-T find-the-error, reason false for \( p \to q \)) | correct | Checked. C2's step counterexample (the stated reason "\( v(\varphi) = \mathrm{F} \)" is false for \( p \to q \) under all-T) meets STYLE §11.3. |
| 17 | §05 `thm-raa-independent` (optional) | Gödel three-valued semantics: every rule except RAA preserves \( \min\Gamma \le v(\psi) \) | correct | Exhaustive check (Method). A remark was added that the same values refute Peirce (\( \tfrac12 \) at \( (\tfrac12, 0) \)); they cannot refute De Morgan (d) or \( (p \to q) \vee (q \to p) \), as Chapter 2 says. The statement and Chapter 2's promise are unchanged. **Edited** (remark). |
| 18 | §04 | Quick checks, B2, C2, the warnings' rows, the non-equivalence | correct | \( p \to q, \neg p \not\models \neg q \) at \( p = \mathrm{F}, q = \mathrm{T} \); \( p \leftrightarrow q \equiv (p \wedge q) \vee (\neg p \wedge \neg q) \); \( (p \to q) \to r \) vs \( p \to (q \to r) \) differ at \( p = r = \mathrm{F} \); replacement fails at \( p = \mathrm{T}, q = \mathrm{F} \); \( q \to p \) not a tautology. C2 (≡ preserved by uniform substitution) is true by the route given. |
| 19 | §06 `lem-connective-rows`, B1 | "the Chapter 1–2 result or two-line derivation that gives it"; B1 "derive three rows not written in the text" | **gap** | "Two-line" is false for most rows (checked lengths: 4, 5, 6, 7, 9 lines). Worse, B1 implies the text omits some rows, so a lemma used by the key proof `lem-truth-table-line` would rest on an exercise. Now every row has a citation (\( \wedge \)I, \( \vee \)I, `prp-vacuous-implication`, `exm-double-negation-introduction` (a), `prp-de-morgan` (b)/(c)) or a printed short derivation (N9, N13). B1 now derives from the primitive rules the three rows the table gets from De Morgan. **Edited.** |
| 20 | §06 | "none of these [rows] needs RAA" | correct | Every row derived without RAA (N9, N13); De Morgan (b), (c) are Chapter 2's RAA-free parts. |
| 21 | book.yaml vs blueprint | exit checks | **gap** | book.yaml's three exit checks (structural induction: nodes > negations; decide \( P \to (Q \to R) \models (P \to Q) \to R \); CNF/DNF of \( (P \to Q) \to (\neg Q \to R) \)) were absent, with no deviation note (Chapters 1–2 record theirs). The second is answered in print by Chapter 2 §06 R3; the third is §07's worked example. Added §02 C3 (literal, marking scheme; proof checked), §07 C4 (adapted, \( (p \to q) \to (q \wedge r) \), answer checked), mapped the second to §07 C3, and wrote "Deviation from book.yaml". The two key-proof exit checks (§05 C2, §06 C2) are kept; the author may demote them. **Edited.** |
| 22 | §06 Aftermath | book.yaml key examples De Morgan (d) and Peirce by table, "⊢ found via completeness, then by hand" | minor | Absent. Placed in the Aftermath, with "the derivations there use RAA" (not "need"). **Edited.** |
| 23 | §06 | `lem-weakening-cut`, `lem-truth-table-line`, `lem-atom-splitting`, `thm-completeness` (Claim, step ③ on \( m = n - j + 1 \), case \( n = 0 \)), `cor-derivable-iff-valid`, worked example (three splittings in two rounds), Quick check | correct | The list \( p_1, \dots, p_n \) "includes" the atoms, which the induction needs (without it, \( p \nvdash q \)). The Claim's false-premise case: \( p^{v} \vdash \neg\gamma \), then ¬E and ⊥E. The step \( j \to j-1 \) applies case \( j \) to the two valuations differing at \( p_j \). Quick check: \( p, q \vdash \neg(p \to \neg q) \) via \( q \vdash \neg\neg q \). |
| 24 | §06 B3 | \( \neg(p \leftrightarrow q) \vdash \neg p \leftrightarrow q \): "needs RAA for \( \neg p \to q \)"; 12 / 22 lines | minor | Counts correct (N1, N2). "Needs" is true (two worlds \( w_0 \le w_1 \), \( p \) nowhere, \( q \) at \( w_1 \) only: \( w_0 \) forces \( \neg(p \leftrightarrow q) \) and \( \neg p \), not \( q \)), but the book cannot prove it; the solution states it without proof, as Chapter 2 does. The rows cited are named. **Edited.** |
| 25 | §04 | the two relations "feed §06 and §07" | minor | §06's proof uses neither. Now "feeds §07". **Edited.** |
| 26 | §07 `thm-dnf` | empty-disjunction convention "\( \bot \), or \( p \wedge \neg p \)" | minor | \( \bot \) is not a literal, and `thm-adequate-connectives` reuses the construction inside \( \{\neg, \wedge, \vee\} \), where \( \bot \) is unavailable. Fixed to \( p \wedge \neg p \). **Edited.** |
| 27 | §07 `thm-adequate-connectives` | \( \{\wedge, \vee, \to\} \) not adequate "(the §03 C2 fact, now proved correctly)" | minor | Ambiguous: a text proof may not rest on an exercise's solution. Now the structural induction is written in the text. **Edited.** |
| 28 | §07 | worked example \( \equiv p \vee q \vee r \) (7 conjuncts, 1 clause); Quick check; B3 (4 conjuncts); C1; C2 (majority, flipped rows) | correct | All checked by table. M is self-dual, so every \( \{\neg, \mathsf{M}\} \) formula is; \( p \wedge q \) is F on (T,F) and (F,T). |
| 29 | §07 C3 (d) | \( p \wedge (q \to r) \vdash (p \to q) \to r \) (7 lines) | **gap** | This is Chapter 2 §06 B1(a) (`exr-finding-derivations-b1`), whose answer is printed; in an exit check it tests recall. Replaced by \( (p \vee q) \wedge \neg p \vdash q \vee r \) (9 lines, no RAA, N5; not in H&R). **Edited.** |
| 30 | R1 | \( p \to (q \to r) \vdash (p \wedge \neg r) \to \neg q \) | minor (copying) | H&R's exercise sequent \( q \to (p \to r), \neg r, q \vdash \neg p \) with \( p, q \) swapped and two premises curried into the goal: the pattern Chapter 2's S2 removed (its §06 B3). Replaced by \( p \vee q, \neg(p \wedge r), r \vdash q \) (9 lines, no RAA, N7). **Edited.** |
| 31 | R3 | \( (p \to q) \wedge (q \to r) \to (p \to r) \) derivable without RAA | minor | Chapter 1 §05 prints \( (P \to Q) \wedge (Q \to R) \vdash P \to R \) (Remark on `prp-implication-transitive`); one \( \to \)I closes it. Replaced by \( (p \wedge (q \vee r)) \to ((p \wedge q) \vee r) \) (10 lines, no RAA, N12). **Edited.** |
| 32 | Promises | "pilot STATUS rows … → Ch 5", "→ Ch 3 final section" | minor | Out of date. STATUS rows targeting Ch 3 are: soundness (with length and context), unique readability, substitution, ¬¬P ⊢ P, Chapter 11 induction. Each is now mapped to its paying label or place; Chapter 1's and Chapter 2's non-derivability promises are listed. **Edited.** |
| 33 | Coverage check | `originality.py 2` | minor | That is Chapter 2. Now `3`; HR is in `sources.yaml` and book.yaml lists HR.1, CH.3, VDL.1, VEL.1. **Edited.** |
| 34 | §07 C3 (a)–(c) | (a) derivable in 10 lines, no RAA; (b), (c) refuting rows | correct | N3. (b) at \( p = \mathrm{T}, q = r = \mathrm{F} \): premise T, conclusion F. (c) at \( p = q = \mathrm{T}, r = \mathrm{F} \). (a) is not an H&R sequent (theirs is the \( \wedge \) version). |
| 35 | §05 Quick check, B1 | \( p \to r \nvdash (p \vee q) \to r \) at F, T, F; the trap is `exm-search-postpone-or` | correct | Checked; D36 derives it (14 lines). |
| 36 | §05 A1 | contexts on the five lines of `prp-vacuous-implication` | correct | Drafted 01:170–176: box 2–4; contexts \( \neg P \); \( \neg P, P \) ×3; \( \neg P \). |
| 37 | §06 B2 | "write the derivation it produces" | minor | No answer or length given; it is 21 lines (N11), beyond the usual limit. The answer and "exempt from the limit" are now in the item, with the comparison to the 3-line \( \to \)E derivation. **Edited.** |
| 38 | Marking schemes | §05 C2, §06 C2, §07 C3 | correct | Each sums to 10 and names fatal errors. The new §02 C3 and §07 C4 schemes also sum to 10. |
| 39 | §05 Quick check | "Which case handles line 5 of `prp-contrapositive`?" | minor | No answer given. Answer added (¬E, a one-step rule; contexts by (a)). **Edited.** |
| 40 | §04 `def-satisfiable` | defined for a formula; "\( \Gamma \) unsatisfiable" is used | minor | Extended to lists. **Edited.** |
| 41 | all must-prove items | each hypothesis needed | correct | `lem-truth-table-line`: "include all atoms" (else \( p \nvdash q \)). `lem-atom-splitting`: both premises (\( \Delta = \emptyset \), \( \psi = p \)). `lem-coincidence`: agreement on atoms. `lem-replacement`: equivalence (the warning). `lem-substitution`: uniformity (the warning). `thm-unique-readability`: "not an atom or ⊥". `lem-context-inclusion` (b): now "cited by a box rule" (#11). `thm-raa-independent`: without RAA. `thm-completeness`: finite \( \Gamma \) (infinitely many atoms otherwise). |
| 42 | later blueprints | Chapters 4, 5, 7, 8 cite `ax-induction`, `thm-strong-induction`, `thm-structural-induction`, `thm-structural-recursion`, `cor-refuting-row`, `thm-soundness`, `lem-context-inclusion`, `def-valid-argument`, `def-tautology` | correct | All created here with the meaning those blueprints assume; Chapter 7 lists `exm-all-equal-induction` as the full version of §02's pointer. |
| 43 | Ch 5 blueprint (outside this stage) | §02 B1 \( 2^n \ge n+1 \) | minor | Chapter 5's phrase table (ch05.md:86) uses the same inequality as its induction example. Harmless (it cites the method, not the item), but the coordinator may want different numbers there. **Not edited** (not this stage's file). |

## 2. Open items for the author

1. **Exit checks** (#21): five items now carry "Exit check" titles (§02 C3, §05 C2, §06 C2, §07 C3, §07 C4). book.yaml has three; keep five, or demote §05 C2 and §06 C2 to C items with their marking schemes. The two adaptations are recorded in "Deviation from book.yaml"; the literal book.yaml items can be restored by changing the worked example of §07 instead.
2. **H&R closeness of the completeness proof** (#2): the lemma and the LEM gluing are H&R's (and every textbook's). The blueprint now says so and asks the text not to claim novelty. Nothing is copied.
3. **`def-rules-biconditional`** (Chapter 2 §04, not yet drafted) must contain the "line of that box itself" sentence inside its block, as `lem-context-inclusion` (b) cites it; the drafted `def-rules-negation` and `def-rule-raa` already do.

## 3. Appendix: derivations checked (N1–N13)

`python3 tools/check_fitch.py authoring/reviews/ch03-S2-recheck.md`: 21 derivations, 0 errors (rows of `lem-connective-rows` and LEM cited by `\by{…}`: availability checked, shape not).

### N1 §06 B3, rows cited (12)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {P \leftrightarrow Q} \by{row}{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {P}
  \have {9} {P \leftrightarrow Q} \by{row}{8,7}
  \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\neg P} \ni{8-10}
  \close
  \have {12} {\neg P \leftrightarrow Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

### N2 §06 B3, primitive (22)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {\neg Q}
  \open
  \hypo {4} {P}
  \have {5} {\bot} \ne{4,2}
  \have {6} {Q} \be{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {\bot} \ne{7,3}
  \have {9} {P} \be{8}
  \close
  \have {10} {P \leftrightarrow Q} \bi{4-6,7-9}
  \have {11} {\bot} \ne{10,1}
  \close
  \have {12} {Q} \raa{3-11}
  \close
  \open
  \hypo {13} {Q}
  \open
  \hypo {14} {P}
  \open
  \hypo {15} {P}
  \have {16} {Q} \r{13}
  \close
  \open
  \hypo {17} {Q}
  \have {18} {P} \r{14}
  \close
  \have {19} {P \leftrightarrow Q} \bi{15-16,17-18}
  \have {20} {\bot} \ne{19,1}
  \close
  \have {21} {\neg P} \ni{14-20}
  \close
  \have {22} {\neg P \leftrightarrow Q} \bi{2-12,13-21}
\end{nd}$
\end{center}
```

### N3 §07 C3 (a) (10)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \vee (P \to R)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {P \to Q}
  \have {4} {Q} \ie{3,2}
  \have {5} {Q \vee R} \oi{4}
  \close
  \open
  \hypo {6} {P \to R}
  \have {7} {R} \ie{6,2}
  \have {8} {Q \vee R} \oi{7}
  \close
  \have {9} {Q \vee R} \oe{1,3-5,6-8}
  \close
  \have {10} {P \to (Q \vee R)} \ii{2-9}
\end{nd}$
\end{center}
```

### N4 §07 C3 (d) as written (7) = Ch 2 §06 B1(a)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
  \hypo {2} {P \to Q}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ie{2,3}
  \have {5} {Q \to R} \ae{1}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {(P \to Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

### N5 §07 C3 (d) replacement (9)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \wedge \neg P}
  \have {2} {P \vee Q} \ae{1}
  \have {3} {\neg P} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {\bot} \ne{4,3}
  \have {6} {Q \vee R} \be{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {Q \vee R} \oi{7}
  \close
  \have {9} {Q \vee R} \oe{2,4-6,7-8}
\end{nd}$
\end{center}
```

### N6 R1 as written (10)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \wedge \neg R}
  \have {3} {P} \ae{2}
  \have {4} {\neg R} \ae{2}
  \open
  \hypo {5} {Q}
  \have {6} {Q \to R} \ie{1,3}
  \have {7} {R} \ie{6,5}
  \have {8} {\bot} \ne{7,4}
  \close
  \have {9} {\neg Q} \ni{5-8}
  \close
  \have {10} {(P \wedge \neg R) \to \neg Q} \ii{2-9}
\end{nd}$
\end{center}
```

### N7 R1 replacement (9)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg (P \wedge R)}
  \hypo {3} {R}
  \open
  \hypo {4} {P}
  \have {5} {P \wedge R} \ai{4,3}
  \have {6} {\bot} \ne{5,2}
  \have {7} {Q} \be{6}
  \close
  \open
  \hypo {8} {Q}
  \close
  \have {9} {Q} \oe{1,4-7,8-8}
\end{nd}$
\end{center}
```

### N8 R3, no RAA (8)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \wedge (Q \to R)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \have {6} {R} \ie{3,5}
  \close
  \have {7} {P \to R} \ii{4-6}
  \close
  \have {8} {((P \to Q) \wedge (Q \to R)) \to (P \to R)} \ii{1-7}
\end{nd}$
\end{center}
```

### N9 connective rows (no RAA)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg (P \wedge Q)} \ni{2-4}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P \vee Q}
  \open
  \hypo {4} {P}
  \have {5} {\bot} \ne{4,1}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {\bot} \ne{6,2}
  \close
  \have {8} {\bot} \oe{3,4-5,6-7}
  \close
  \have {9} {\neg (P \vee Q)} \ni{3-8}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \r{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P \to Q}
  \have {4} {Q} \ie{3,1}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (P \to Q)} \ni{3-5}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P \leftrightarrow Q}
  \have {4} {Q} \bie{3,1}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (P \leftrightarrow Q)} \ni{3-5}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \hypo {2} {Q}
  \open
  \hypo {3} {P \leftrightarrow Q}
  \have {4} {P} \bie{3,2}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg (P \leftrightarrow Q)} \ni{3-5}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\bot}
  \close
  \have {2} {\neg \bot} \ni{1-1}
\end{nd}$
\end{center}
```

### N10 atom splitting instance: Delta = Q; Q, P |- Q and Q, not P |- Q pasted

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {Q} \r{1}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {Q} \r{1}
  \close
  \have {7} {Q} \oe{2,3-4,5-6}
\end{nd}$
\end{center}
```

### N11 §06 B2 method output for P, P -> Q |= Q (21)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \have {3} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {4} {P}
  \have {5} {Q \vee \neg Q} \by{LEM}{}
  \open
  \hypo {6} {Q}
  \close
  \open
  \hypo {7} {\neg Q}
  \have {8} {\neg (P \to Q)} \by{row}{4,7}
  \have {9} {\bot} \ne{2,8}
  \have {10} {Q} \be{9}
  \close
  \have {11} {Q} \oe{5,6-6,7-10}
  \close
  \open
  \hypo {12} {\neg P}
  \have {13} {Q \vee \neg Q} \by{LEM}{}
  \open
  \hypo {14} {Q}
  \have {15} {\bot} \ne{1,12}
  \have {16} {Q} \be{15}
  \close
  \open
  \hypo {17} {\neg Q}
  \have {18} {\bot} \ne{1,12}
  \have {19} {Q} \be{18}
  \close
  \have {20} {Q} \oe{13,14-16,17-19}
  \close
  \have {21} {Q} \oe{3,4-11,12-20}
\end{nd}$
\end{center}
```

### N12 R3 replacement: |- (P and (Q or R)) -> ((P and Q) or R) (10)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge (Q \vee R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \vee R} \ae{1}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{2,4}
  \have {6} {(P \wedge Q) \vee R} \oi{5}
  \close
  \open
  \hypo {7} {R}
  \have {8} {(P \wedge Q) \vee R} \oi{7}
  \close
  \have {9} {(P \wedge Q) \vee R} \oe{3,4-6,7-8}
  \close
  \have {10} {(P \wedge (Q \vee R)) \to ((P \wedge Q) \vee R)} \ii{1-9}
\end{nd}$
\end{center}
```

### N13 connective rows: iff rows and not-not

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \r{2}
  \close
  \open
  \hypo {5} {Q}
  \have {6} {P} \r{1}
  \close
  \have {7} {P \leftrightarrow Q} \bi{3-4,5-6}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,1}
  \have {5} {Q} \be{4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {\bot} \ne{6,2}
  \have {8} {P} \be{7}
  \close
  \have {9} {P \leftrightarrow Q} \bi{3-5,6-8}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {\neg\neg P} \ni{2-3}
\end{nd}$
\end{center}
```
