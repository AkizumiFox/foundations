# Chapter 3 — S7 re-referee recheck (round 1)

Fresh re-referee, 2026-09-28. I had not seen the chapter before this stage. Scope:
- the Resolution sections of `ch03-S5-A.md`, `ch03-S5-B.md` and `ch03-S6.md`;
- every change to `src/ch03-semantics-soundness-completeness`, `verify/ch03`, `authoring/STATUS.md` and `authoring/NOTATION.md` since the refereed text.

I read each changed sentence in its surrounding text, not only in the diff. I was read-only on `src`.

**How the diff was obtained.** `src/ch03-…` and `verify/ch03` are untracked, so `git diff` shows nothing for them. The Ch 3 rows of NOTATION.md and most of the Ch 3 rows of STATUS.md were swept into HEAD by the Chapter 2 commit (232dfd7), so `git diff` shows only 3 lines of STATUS.
- The S5-A, S5-B and S6 scratch copies (`S5a-ch03-refA/src`, `ch03-refB/repo/src`, `ch03-S6/tree/src`) are byte-identical, so they are the refereed text.
- I diffed the live tree against `ch03-S6/tree`: `src/…`, `verify/ch03`, NOTATION.md and STATUS.md.
- `verify/ch03`: no change.
- `src`: 7 files changed, `index.md` unchanged, 344 diff lines.

## Gates (fresh scratch copy `scratchpad/ch03-S7-recheck/repo`)

- `./build.py html` (whole book) succeeds. `./build.py pdf` succeeds for all seven Ch 3 sections.
- `check_rendered.py`: 0 errors, 102 warnings. All 102 are the mdframed "Overfull box … at line 2028" loop in `06-completeness.log`, at the §06 B3 solution; see Referee B row 4 (b) below. The 0.95pt §07 overfull line is gone.
- `check_structure.py 3`: 0 fatal, 0 advisory. `check_notation.py`: 0 notes.
- `check_forward_deps.py`: clean (378 labels). `check_optional.py`: no proof rests on `thm-raa-independent`.
- `check_fitch.py src/ch03-…`: 31 derivations, 20 tables, 0 errors. No `nd` block or table was edited in this round (checked in the diff), so the capital-letter re-run of S5-A/S6 still certifies the derivations.
- `check_numbers.py 3`: 60 sidecars, 0 fatal, 0 advisory.
- `promises.py --reconcile`: 0 not recorded.
- `ledger.py stale 3`: 0 before this stage's verdicts.

## Diff scope

Every src hunk matches a resolution row, with one exception: 05:43 ("Recall from Section 1.5, just after @def-derivation"). That hunk is the Ch 1/Ch 2 seam item that the S5-B resolution mentions under 04:242/03:268, so it is also accounted for.

The dependency-ledger edits are:
- the three stale "drafted in parallel" notes removed;
- the 03 ledger line aligned to "uses RAA";
- the R2 source changed to Ch 7.

I found no unlisted change. In NOTATION.md, only the three new Ch 3 rows (`v_T`, `φ^v`, NAND/NOR/M) belong to this chapter. The `\dashv\vdash` "Ch 2 §04" edit is Ch 2's.

## Verdicts: S5 Referee A

| finding | verdict | evidence |
|---|---|---|
| 02:257 `lem-parenthesis-count` (02:249, 02:269) | fixed correctly | The proof of `thm-unique-readability` (02:333–335) uses only (a) and (c), so "(c), with (a), is what the unique readability theorem needs" is true. C1 (a) (02:531) is "no proper initial segment of a formula is a formula", and it rests on (b) with (a). "The steps for (b) and (c) use (a) for the parts" is true: (b) uses (a) for φ in the third and fourth kinds, and (c) uses (a) for φ in the ψ-case. The following paragraph (02:303, "the three parts were proved together for a reason") still agrees with it. 02:249 "one that the next theorem needs, and one that Exercise C1 uses" is consistent with this. |
| 04:162 `prp-standard-equivalences` (04:242) | fixed correctly | Ch 2 states the necessity for De Morgan (d) without proof (ch02 05:443, ledger 05:1009). ¬¬P ⊢ P is the optional `thm-raa-independent` in Section 3.5. "Some directions with derivations that use RAA or LEM" is now a claim about the printed derivations, and it is true. "The tables do not see that difference" still reads correctly: tables see neither use nor need. |
| 05:323 `thm-raa-independent` | fixed correctly | The new first sentence of the proof reduces derived rules derived without RAA to pasted primitive non-RAA derivations. It does this as Step 1 of `thm-soundness` does, and it matches the statement's parenthesis "(and derived rules derived from those)". The expansion (ch02 03:126) copies the rule's own derivation, which by hypothesis has no RAA. |
| 06:30 `lem-weakening-cut` (06:42, 06:68) | fixed correctly | 06:42: part (c) chains derivations whose last lines lie in no box, so "outside every box" is exact. "Section 2.3's expansion" is ch02 03:126, which repeats the cited lines by (D3) and then pastes. 06:68 correctly splits the cases: a line in no box is covered by the lemma, and a line in a box by `def-derived-rule`, "where the cited lines are repeated inside the box first", which is what 03:126 says. The rows cited inside boxes at 06:480–500 and 06:698–766 are now covered by the stated reason. |
| 07:132 `thm-cnf` (07:160) | fixed, with a new minor problem (N1) | Replacing ⊥ by p ∧ ¬p is right: both are F in every row, and afterwards pushing ¬ inward and distributing yields literals only. For example, p ∨ ⊥ ↦ (p ∨ p) ∧ (p ∨ ¬p), and ¬⊥ ↦ ¬p ∨ p. But the unchanged next sentence says "the equivalences are those of @prp-standard-equivalences", and ⊥ ≡ p ∧ ¬p is not among (a)–(h) (04:168–175). See N1. |
| 07:162 `exm-normal-forms-two-routes` | fixed correctly | φ = (p → q) → (¬q → r) has three arrows. The first displayed line applies (c) three times. The second applies (b) and removes ¬¬q, and the third removes ¬¬p, so "(d) twice" is right. |
| Tooling (check_fitch reads only capital atoms) | not a Ch 3 change | Correctly left to the coordinator. No derivation or table changed, so the upper-case re-runs of S5-A and S6 stand. |

## Verdicts: S5 Referee B

| finding | verdict | evidence |
|---|---|---|
| Row 1 (gap): 13 unrecorded promises; 07:724 source | fixed correctly | `promises.py --reconcile`: 0 not recorded. STATUS l.62–67 contains the six new Ch 3 rows. Each row's content matches the pointers Referee B listed (→ Ch 4, 5, 6, 7 with `exm-all-equal-induction`, 9, 11 paid). The R2 ledger source now names Ch 7 and "every integer is even or odd, and not both", which is exactly STATUS l.56 (target Ch 7). |
| Row 2: NOTATION rows; `u` with two meanings | fixed correctly | `grep` finds no all-T `u` left in §03 or §07; the all-T valuation is `v_T` in §03 C2 (claim, proof, solution, scheme), `thm-adequate-connectives` (b) and §07 C2 (a). `u` remains only the three-valued valuation of §05. The three new NOTATION rows are accurate about their scope. `check_notation.py`: 0 notes. |
| Row 3: ledger file; stale notes | fixed correctly | `authoring/ledger/ch03.yaml` exists. The three "drafted in parallel" notes (03, 04, 05 ledgers) are removed. |
| Row 4: rendering | (a) fixed correctly; (b) dispute upheld; (c) fixed | (a) 05:83 and 05:87 are reworded, and both sentences are still true. (b) I rebuilt `06-completeness.pdf` and inspected p. 18. The B3 solution (table, search, 12-line derivation, closing remark) is complete and unclipped, and C1 starts cleanly below it. The warnings are the splitter's search loop, and there is nothing on the page to fix. (c) `07-normal-forms.log` has no overfull line now. |
| Row 5: blueprint deviations | fixed correctly (recorded) | The STATUS "Blueprint deviations" Ch 3 entry lists all four points and the false blueprint l.87 claim. It correctly says the §05/§06 exit checks are "now marked 'write from memory'". |
| Row 6: 2ⁿ ≥ n + 1 in the ch05/ch07 blueprints | fixed correctly (recorded) | Recorded for the coordinator in the same STATUS entry. Other chapters' blueprints are outside S7. |
| 07:261 `exm-cnf-validity-glance` (b) | fixed correctly | The proof of `prp-cnf-validity` (07:234) sets every atom not in the clause to T, so it names p = T. "In fact either value of p works" is true, because p is not in the clause ¬s ∨ ¬r ∨ q. |
| 06:42, 06:68 | fixed correctly | See Referee A's `lem-weakening-cut` row. |
| 05:3 opening frame | fixed correctly | `exm-affirming-the-consequent` (04:86–93) uses the row p = F, q = T. There p → q = T, and q → p = T → F = F. The sentence no longer says that Section 3.4 evaluated q → p. |
| 04:242, 03:268 | fixed correctly | 03:268 "derived the way back with a derivation that uses RAA" is true, since ch02 05:221 says "our derivation of the way back uses one RAA". The ledger line (03:569) says "visible in its printed derivation". For 04:242, see Referee A. The STATUS annotations "(Applied at Ch 3 S7 round 1 …)" and "(these three settled …)" are accurate. |
| 03:113 "four columns" | fixed correctly | The first subsection (03:7–45) reads off exactly ∧, ⊥ (always F), ¬ and →, and leaves ∨ and ↔ to the reader. |
| 03:533 §03 C2 | fixed correctly | See S6 finding 1. |
| 02:249, 02:269 | fixed correctly | See Referee A's first row. |
| (seam item) 05:43 | fixed correctly | ch01 05:205 defines the context in the discussion that follows the `def-derivation` block (157–194), in the same subsection. "In Section 1.5, just after @def-derivation" is accurate. |

## Verdicts: S6

| finding | verdict | evidence |
|---|---|---|
| 1. §03 C2, elided step in (2)–(4) | fixed correctly | The added sentence licenses the induction hypothesis for the parts. It is the same step as `thm-adequate-connectives` (b) ("then so are α and β"), and it is true by unique readability. Lines (1)–(3) are now correct, and the only error is (4)'s reason "v_T(φ) = F", which contradicts its own hypothesis. The solution and scheme are unchanged except for the rename, and still name line (4) alone. STYLE §11.3 is now met. |
| 2. §01 C1 (a) "two-level tree" | fixed correctly | In node-counting height (`def-height`), q → (r → s) and p → (q → r) have height 3, and p → q has height 2. The sentence is now consistent with "two trees of height 2". |
| 3. §04 C1 "seven clauses" | fixed correctly | Atoms, ⊥, ¬, and ∧, ∨, →, ↔, \| make 1 + 1 + 1 + 5 = 8 cases, and the solution treats each. |
| 4. §05 B2 constraints | fixed correctly | (ii) "Hence v(χ) = T in either case" is the only line that uses (v)'s split and both (viii) and (iv). (viii) and (iv) are conditionals and use only (iii), (vii) and (i). The dependency sentence now agrees with the constraint list, and both stated orders are admissible. |
| 5. §04 C2 idle second part | fixed correctly | The item now posits a hypothetical: (b) checked only for atoms, with the instance ¬(p ∧ q) ≡ ¬p ∨ ¬q named. That instance is the first half of (b) (04:169). The first part (σφ ≡ σψ) is then genuinely used: with σ(p) = r → s and σ(q) = ¬t, the two sides become ¬((r → s) ∧ ¬t) and ¬(r → s) ∨ ¬¬t. The scheme's "2: the instance, with the substitution named" fits the new solution. The item is still fair: it is one line once the first part is proved. |
| 6. Missing schemes §06 C1, §07 C1 | fixed correctly | §06 C1: 4 + 4 + 1 + 1 = 10. It matches the solution: (∨1) and (∨2) use one hypothesis, (∨3) both, and each ↔ case both; "Chaining" is `lem-weakening-cut` (c). §07 C1: 3 + 3 + 1 + 3 = 10. It matches the solution, and `thm-adequate-connectives` (a) covers {¬, ∧} and {¬, ∨} (07:295). Both fatal lists name real fatal errors. The HTML and PDF render `\mathbin{|}` correctly in the list. |
| 7. §05 C2, §06 C2 answered by printed proofs | fixed correctly (option (i)) | Each now opens "*Close the section first, and write from memory.*". This is the lightest option the finding offered, and it keeps the frozen blueprint's exit checks. The phrasing matches the book's other "from memory" items. |
| Notes, tooling | no change needed | Notes only; tooling left to the coordinator. |

## New finding

| # | file:line | verdict | evidence and fix |
|---|---|---|---|
| N1 | 07:160 (paragraph after `thm-cnf`, "Alternatively … rewriting") | minor | The S7 fix correctly adds a first step, replacing ⊥ by p ∧ ¬p. The next, unchanged sentence says: "Each step replaces a part of the formula by an equivalent one: the equivalences are those of @prp-standard-equivalences". ⊥ ≡ p ∧ ¬p is not one of (a)–(h). Its equivalence is given only by the new clause "both are false in every row". This is an overstated meta-claim of the kind S5-B flagged elsewhere in the chapter; the mathematics is right. **Fix (a few words):** "the equivalences are ⊥ ≡ p ∧ ¬p and those of @prp-standard-equivalences, which hold for arbitrary formulas". |

## Summary (round 1)

- Of the 7 S5-A, 13 S5-B (6 chapter-level, 7 item) and 7 S6 findings, all are fixed. One S5-B sub-item (row 4 (b)) is a dispute that I uphold after inspecting the page.
- One fix, 07:160 (S5-A `thm-cnf`), leaves an adjacent sentence that now overclaims: **N1, minor**.
- There is no error or gap. No derivation, table or sidecar changed, and no unintended change was found.
- Chapter 1 and 2 changes needed: none.

Ledger: S7r verdicts (`--by rereferee`) recorded on the 25 items the reviser touched: `correct` on 24, and `minor` on `thm-cnf` (N1).

## Resolution (S7, reviser, round 2)

| finding | resolution |
|---|---|
| N1, 07:160 (minor) | Fixed as proposed: "the equivalences are \( \bot \equiv p \wedge \neg p \) and those of @prp-standard-equivalences, which hold for arbitrary formulas, and @lem-replacement says the whole formula stays equivalent". |

Ledger: S7 `correct` by reviser on `thm-cnf`. STATUS promise table reconciled (206 promises, 0 unrecorded); NOTATION unchanged. Gates re-run in `scratchpad/ch03-S7r2/repo`: `./build.py html`, `pdf` (all ch03 sections), `check` (378 labels, 1225 references), pytest (295 passed, 5 skipped), check_fitch (31 derivations, 20 tables, 0 errors), check_structure (0 fatal), check_numbers (60 sidecars, 0 fatal), check_rendered (0 errors), promises (0 unrecorded). originality.py 3 lists 24 shared 8-grams, all truth-table value rows (t/f strings) and one roman-numeral list, none of them prose; this round changed no table.

---

# Chapter 3 — S7 re-referee recheck (round 2)

Fresh re-referee, 2026-09-28. I had not seen the chapter before this round. I read the S5-A, S5-B and S6 reviews with their Resolution sections, round 1 above, and its round-2 Resolution. I was read-only on `src`.

**How the diff was obtained.** `src/ch03-…` and `verify/ch03` are still untracked, so I diffed the live tree against the round-1 recheck copy (`scratchpad/ch03-S7-recheck/repo`). I diffed `src/ch03-…`, `verify/ch03`, `authoring/NOTATION.md`, `authoring/STATUS.md` and `authoring/blueprints/ch03.md`. `git diff` on STATUS and NOTATION shows only the two round-1 STATUS annotations that round 1 already checked.

## Diff scope

Since round 1, exactly one line has changed in the scope: `07-normal-forms.md:160`. The change inserts "\( \bot \equiv p \wedge \neg p \) and" before "those of @prp-standard-equivalences". Nothing changed in `verify/ch03`, NOTATION.md, STATUS.md or the blueprint, and there are no other `src` changes.

## Gates (fresh scratch copy `scratchpad/ch03-S7-recheck2/repo`)

- `./build.py html` succeeds (whole book), and `./build.py pdf` succeeds for §07.
- `check_rendered.py` gives 0 errors and 0 warnings, and `07-normal-forms.log` has no overfull box.
- `check_fitch.py src/ch03-…` finds 31 derivations and 20 tables, with 0 errors. No derivation or table was edited.
- `check_structure.py 3` gives 0 fatal and 0 advisory. `check_notation.py` gives 0 notes, and `check_forward_deps.py` is clean over 378 labels.
- `check_numbers.py 3` runs 60 sidecars with 0 fatal. `promises.py --reconcile` reports 206 promises with 0 not recorded.
- `ledger.py stale 3` shows 0 stale verdicts. The edit lies in the paragraph after the `thm-cnf` block, so the item hash is unchanged.

## Verdicts

| finding | verdict | evidence |
|---|---|---|
| N1, 07:160 (minor) | fixed correctly | The sentence now names every equivalence the rewriting route uses. ⊥ ≡ p ∧ ¬p is justified in the same paragraph ("both are false in every row"). The ↔ step is (e), the → step (c), the De Morgan pushes (b), the ¬¬ removal (d) and the distribution (g) of `prp-standard-equivalences` (04:168–175). "which hold for arbitrary formulas" attaches to the standard equivalences, as 04:160 states. ⊥ ≡ p ∧ ¬p holds for the atom p, which is all the step uses. The DNF variant in the next sentence uses the same list plus the other half of (g), so it stays covered. The rendered HTML shows the new math correctly. |
| All round-1 verdicts (S5-A, S5-B, S6) | stand | No other text in the scope has changed since round 1, so round 1's evidence still applies. |

## New findings

None. Beyond the N1 fix itself, the diff contains no changed sentence, derivation or exercise.

Observation (not a finding): the dependency-ledger line for `thm-cnf` (07:724) lists `prp-standard-equivalences` and `lem-replacement`, but not ⊥ ≡ p ∧ ¬p. That fact is proved in place by (V1)–(V3) in the sentence that introduces it, so it is not an uncited external fact.

## Summary (round 2)

- N1 is fixed correctly. No finding is open: error 0, gap 0, minor 0.
- No unintended change was found.
- Chapter 1 and 2 changes needed: none.

Ledger: an S7r verdict (`--by rereferee`) is recorded on `thm-cnf`: `correct`.
