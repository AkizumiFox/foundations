# Chapter 2 — S7 re-referee recheck (round 1)

Fresh re-referee, 2026-09-28. Scope: the Resolution sections of `ch02-S5-A.md`, `ch02-S5-B.md` and `ch02-S6.md`, and the uncommitted diff `git diff -- src/ch02-negation-and-classical-logic verify/ch02 authoring/STATUS.md authoring/NOTATION.md`. Read-only on `src`. Each changed sentence was read in its surrounding text, not only in the diff.

## Gates (scratch copy `scratchpad/S7r-ch02/repo`)

- `check_fitch.py src/ch02-negation-and-classical-logic --notes`: 119 derivations (2 expect-invalid, 37 schema), **0 errors**. 03:319 now gives the note "line 11 justified by text (or commutes)". No derivation changed except that `\by` label.
- Every `verify/ch02/*.py` sidecar exits 0. `check_numbers.py 2`: 46 sidecars, 0 fatal, 0 advisory. That includes the edited `exr-biconditional-and-definitions-c2.py`, which quotes (−3, 1) and loops over every x < −y ≤ 0.
- `./build.py html` succeeds. `check_rendered.py`: 0 errors, 0 warnings. `check_forward_deps.py`: no proof cites a later section (378 labels).
- `check_structure.py`: 0 fatal. The only Ch 2 advisories are the word counts of §05 (7718) and §06 (7662), which the author allows.
- `check_notation.py`: 0 notes. `promises.py --reconcile`: 13 unrecorded promises, all from Ch 3 (another workflow). No Ch 2 promise is unrecorded.
- `ledger.py stale 2`: 0 stale before this stage's verdicts were written.

## Diff scope

Every hunk in `src/ch02-…` and `verify/ch02` matches a resolution row. I found no unlisted change.

The diff to NOTATION.md also contains rows that this stage did not write:
- the Ch 3 rows (atoms, `\circ`, `\hgt`, valuations, ⊨, …);
- the Ch 1 fixes (`\abs` "displayed in §07", "Section 1.5").

These belong to the concurrent Ch 1 and Ch 3 workflows. The four Ch 2 rows (`d \mid n`, `\dashv\vdash`, `\mathsf{X}`/`\mathsf{Y}`, φ/ψ/χ) are correct.

The STATUS.md Ch 2 rows were checked against the text: ¬¬P ⊢ P → Ch 3 (§04, §05); quantifier steps → Ch 4; (L) → Ch 7 (§02); differentiable ⇒ continuous → Ch 17 (§04); ¬P as P → ⊥ and the costume → Ch 5. Each is where the row says. The stale ch07 prime-divisor payment is correctly left to the coordinator, filed under "Blueprint deviations".

## Verdicts: S5 Referee A

| finding | verdict | evidence |
|---|---|---|
| 01:24 `def-rules-contradiction` (l.58, l.60) | fixed correctly | The new l.58 is true: the rules other than ¬E that can write a line ⊥ are ⊥E, →E, ∧E, ∨E, ↔E, R and RAA, and each needs a used line or box in which ⊥ already occurs. ¬E is the only rule whose conclusion is always ⊥. "Apart from being assumed" covers ⊥ as a premise or case assumption. The new l.60 now argues only for a ⊥ written by ¬E and hands the other rules to Ch 3. That is true, and it no longer rests on the false sentence. |
| 01:422 A1(c) | fixed correctly | 01:439: "⊥E needs a line ⊥ to start from. The rule that records a clash as ⊥ is ¬E …". True, and it answers "true or false, with a reason". |
| 03:290 "comm. of ∨" | fixed correctly | The `\by` and the prose tag now use the name "or commutes", which is the name in the §06 table (06:664). The table prints it in parentheses and `\by` prints it without, as with `\by{VI}`. That is typographic only. |
| 05:187 l.221 | fixed correctly | "needs no RAA" is true (`prp-contrapositive`). |
| 06:41 check (error); 06:99 l.154 | fixed correctly | Line 7 (¬I 2–6) is at top level above line 8, so it is available at line 11 by @def-derivation. The answer "1, 7, 8, 9" is right, and "this gap will not need it" is true (the gap closes with →E 1,9 and ¬E). 06:154 agrees. |
| 06:355 `exm-search-raa` title | fixed correctly | "A search that reaches step 5 at once" is true: 06:362 shows steps 2–4 have nothing to offer, and the title claims no necessity. |
| 06:1033 C3 scheme | fixed correctly | "our route with it then uses a second classical step" describes a route; it makes no necessity claim. The dependency-ledger comment was aligned (06:1251). |
| 06:462 failed search vs the step-5 clause | fixed correctly | Inside an RAA box on ¬(Q → P), with goal ⊥, step 4's only aim is Q → P. Step 2 then opens a box on Q with goal P, where the extra resource ¬(Q → P) again asks only for Q → P. So "every route returns to one gap" now covers the clause. The Ch 1 name fits: ch01 04:82 calls the pattern "affirming the consequent" and "the step that would repair Argument B". |
| 06:65–67 algorithm control flow | fixed correctly, but see N1 | Step 4 now ends "starting again at step 2 for that goal", which matches the worked searches (06:381, 06:1048). N1 below is a knock-on of this clause combined with S6 #5. |

## Verdicts: S5 Referee B

| # / item | verdict | evidence |
|---|---|---|
| 1 STATUS promises (gap) | fixed correctly | Ch 2 rows are present and accurate (see "Diff scope"). `--reconcile` shows no unrecorded Ch 2 promise. |
| 2 NOTATION rows | fixed correctly (already present) | l.56, 92–94 as described. |
| 3 "comm. of ∨" | fixed correctly | As in A 03:290. |
| 4 blueprint deviation | fixed correctly | STATUS "Blueprint deviations" has a Ch 2 entry for `exm-search-raa` and the step-5 clause. |
| 11(a) "(converse of CP)" wrap | fixed correctly | 06:679 now reads "(CP, converse)", so no ")" follows the math. The name is descriptive, not used in any `\by`. |
| 11(b) Idea and argument run together | dispute accepted | Confirmed in `templates/html/styles.css` l.869–896. In print, `.foldable.is-folded > :not(.fold-head)` is reverted to visible while `.foldable.is-folded > .fold-head { margin: 0 }` still applies. The problem is in the engine (coordinator), not the source. |
| 12 missing ledger | fixed correctly | `authoring/ledger/ch02.yaml`: 120 items, 0 stale. |
| 06:42–46, 06:154 (error) | fixed correctly | As in A. |
| 06:462 "converse error" | fixed correctly | As in A. The warning at 06:491 still uses "converse error" in Ch 1's other sense (opening the box at the wrong end). That use is correct. |
| 06:353, 356, 436 `exm-search-raa` | fixed correctly | The derivation uses ↔I (step 2), plus ∨I, ¬E and ⊥E (the step-4 manufacture and close), and RAA. "Steps 2 and 4" is exactly right. |
| 06:1044, 06:1084 C3 step 3 | fixed correctly | "Nothing can be eliminated … only in a clash (step 4)" matches the method (06:65–66) and 06:362. The scheme reads "steps 3 and 4". |
| 06:244 "every" | fixed correctly | This matches ch01 07:322, "Almost every proof by cases". |
| 06:1085, 06:1140, 05:333 unmarked necessity | fixed correctly | All three now describe our route: "our route with it then uses", "our derivation reaches Q with the classical rule instead", "each gets a small RAA box". None claims necessity. |
| 05:958 C3 primitive list | fixed correctly | ↔I and ↔E are added. The list now matches the reference sheet's primitive rules. |
| 05:624 Ch 11 quotation | fixed correctly | The quotation is now a paraphrase with no quotation marks. It is true of the Ch 11 proof, which opens "Suppose, for contradiction, that ℕ is bounded above". |
| 05:830 B4 (d) | fixed correctly | It now matches (a)'s naming of the assumption. |
| 02:469 C1 scheme | fixed correctly | The clause is dropped. The item's "use only" and the scheme now agree. No hint points to the mod-3 route. |
| 01:58, 60, 439 | fixed correctly | As in A. |

## Verdicts: S6

| finding | verdict | evidence |
|---|---|---|
| 1 §04 C1 scheme | fixed correctly | The 4-point bullet accepts any correct combination. The route n = 3n − 2n = 6a − 6b is a proof of "2 ∣ n and 3 ∣ n ⇒ 6 ∣ n", so it does not hit the fatal-error clause. |
| 2 §04 C2 (a) | fixed correctly | The new (a) is correct and fair. The (⇐) proof at 04:320 uses y ≥ 0 exactly twice (x > y ≥ 0 gives x > 0, and y < x times y ≥ 0 gives y² ≤ xy). Its other multiplication is by the derived x > 0, so x ≥ 0 is never used. x = −3, y = 1 refutes (⇒) and differs from the remark's pair. The sidecar checks the whole family x < −y ≤ 0. Note, no finding: (a) is now a comprehension task, and (b) carries the C-level work. |
| 3 §05 C1 (b) | fixed correctly | Recounted. After the given box, ② + ③ add 7 lines: ¬¬φ; LEM; [φ]; [¬φ, ⊥, φ]; ∨E. The fragment adds 4: LEM; [φ]; ⊥E appended to the box; ∨E. So 3 lines are saved: ¬¬φ, and ③'s k + 2 and k + 3. The labels k + 2, k + 3, k + 4 match ③'s schema at 05:576–588. "In ③" disambiguates them from the k of (a)'s fragment. |
| 4 §06 C2 Hint 2 | fixed correctly | The hint names both forms of step 5 and asks the reader to choose, without doing the step. The RAA route stays credited by the scheme. |
| 5 §06 C3 side choice vs `exm-search-raa` | fixed, with a new minor problem (N1) | The new clause at 06:76 is true: if the resources contain ¬(A ∨ B) and derive A ∨ B, they derive ⊥, and then A by ⊥E, so choosing a side loses nothing. C3 step 6 cites it correctly. The new wording at 06:381 is consistent with it. But see N1. |
| 6 "comm. of ∨" | fixed correctly | As in A 03:290. |

## New findings

| # | file:line | verdict | evidence and fix |
|---|---|---|---|
| N1 | 06:62, 06:66 (algorithm block) | minor | Two round-1 fixes combine badly. Step 4 now sends a manufactured χ to "step 2 for that goal", and step 2 says of a ∨ goal "postpone; do not choose a side yet". Followed literally in C3's box (χ = P ∨ ¬Q), that route postpones, finds nothing in steps 3–4, and returns to step 5 on the same goal: a loop. The exception that allows C3 step 6 to choose ¬Q exists only in the prose paragraph at 06:76, outside the algorithm. The moves table (06:15, "choose a side only when it is in hand") records Section 1.6's move and can stay. **Fix (one clause):** in step 2's ∨ bullet, write "postpone; do not choose a side yet, unless the disjunction is being manufactured for a clash with its own negation (step 4), when either side may be chosen (see below)". Alternatively, add the same clause to the new end of step 4. |

## Earlier reviews (ch01v2-*) regressions

I spot-checked the items the S5/S6 referees listed as fixed:
- 05:79, last-step RAA claim;
- 03:126, iteration clause;
- 04:209, marked converse;
- 04:326, remark unchanged apart from C2's reference to it;
- 06:711, A1(a);
- 05:920, "part (d) below";
- 05:262, LEM aftermath;
- 04:227, pointer to Ch 3;
- 04:591, C1 cites B3 (a);
- 06:1030, C2 scheme accepts RAA.

The diff touched none of them, and none has returned.

## Critical checks (re-confirmed on the changed text)

- **Rule order.** No change introduces a rule before its section. The new §01 sentences name ⊥E, →E and ¬E, all of which are available in §01 (→E from Ch 1). §04 and §05 changes use only rules available by then.
- **Necessity claims.** Every changed "needs" or "must" sentence either describes a route or is true and proved on the page (05:221 "needs no RAA" is `prp-contrapositive`). No new unmarked non-derivability claim was added.
- **Search method.** The step-5 clause is now exercised by the failed search (06:462) and justified at 06:78 and 06:439. The new side-choice exception is sound. N1 is the one remaining seam.
- **Derived-rule name.** "or commutes" is the name in 03:299, 03:319 and 06:664.

## Summary

33 resolution rows were checked: 32 fixed correctly (including the accepted dispute of B 11(b)) and 1 fixed with a new minor problem (S6 #5, via N1). There is no error or gap and no unintended change. Every edited derivation passes check_fitch, and the changed exercises (§02 C1, §04 C1, §04 C2, §05 C1, §05 C3, §06 C2, §06 C3, §06 C4) are correct and fair. Round 2 needs only the one-clause fix of N1 in the §06 algorithm block.

Chapter 1 changes needed: none. Every Ch 1 sentence the new text leans on says what is claimed: ch01 04:82 "affirming the consequent … would repair Argument B", ch01 07:322 "Almost every proof by cases", and `exm-disjunction-first-derivations`.

## Resolution (S7, reviser, round 2)

- **N1 (from S6 #5; 06:62, 06:66).** Fixed as proposed. Step 2's ∨ bullet now reads "postpone; do not choose a side yet (Section 1.6), unless the disjunction is being manufactured for a clash with its own negation (step 4), when either side may be chosen (see below)". Step 4's route back to step 2 therefore no longer loops in C3's RAA box, and C3 step 6's side choice follows the algorithm block itself, with 06:76 as the justification. The moves table (06:15) is unchanged, as the recheck advised. No other text changed.

# Round 2 — S7 re-referee recheck

Fresh re-referee (had not seen the chapter), 2026-09-28. I read the S5-A, S5-B and S6 reviews with their Resolution sections, the round-1 recheck above and its round-2 Resolution. I also read every hunk of `git diff -- src/ch02-negation-and-classical-logic verify/ch02 authoring/STATUS.md authoring/NOTATION.md`, each in its surrounding text. I was read-only on `src`.

## Gates (fresh scratch copy `scratchpad/S7r2-ch02/repo`)

- `check_fitch.py src/ch02-… --notes`: 119 derivations (2 expect-invalid, 37 schema), **0 errors**.
- All 46 `verify/ch02` sidecars pass. `check_numbers.py 2`: 0 fatal, 0 advisory.
- `build.py html` succeeds. `check_rendered.py`: 0 errors, 0 warnings. `check_forward_deps.py`: no proof cites a later section.
- `check_structure.py`: 0 fatal. The only Ch 2 advisories are the lengths of §05 (7718 words) and §06 (7685 words), which the author allows.
- `check_notation.py`: 0 notes. `ledger.py stale 2`: 0 before this round's verdicts.

## N1 (round-1 new finding): fixed correctly

06:62, the step-2 ∨ bullet, now reads: "postpone; do not choose a side yet (Section 1.6), unless the disjunction is being manufactured for a clash with its own negation (step 4), when either side may be chosen (see below)".

- **The algorithm no longer loops.** Step 4 (06:66) sends a manufactured χ back to step 2. In C3's RAA box, χ = P ∨ ¬Q is manufactured against the resource ¬(P ∨ ¬Q). Step 2 now allows a side there, so C3 step 6 (06:1047), which chooses ¬Q, follows the algorithm block itself.
- **The exception is sound.** Let Γ be the resources, containing ¬(ψ ∨ χ). If Γ ⊢ ψ ∨ χ, then Γ ⊢ ⊥ by ¬E, and then Γ ⊢ ψ and Γ ⊢ χ by ⊥E. So choosing a side never turns a derivable gap into an underivable one. "(see below)" points to the paragraph at 06:76, which gives exactly this argument.
- **The worked searches still agree with the method.**
  - `exm-search-raa` step 4 (06:381) says aiming at P ∨ Q "leads back to the start". Under the new step 2 this is literally true: step 4 restarts step 2 at the goal P ∨ Q, which is the chapter's starting goal. "No side in hand" correctly gives the reason not to prefer that route, even though step 2 permits it.
  - The failed search (06:462) contains no disjunction goal, so the new exception does not bear on it.
- **The moves table is unchanged.** Line 06:15 still reads "choose a side only when it is in hand". That is Section 1.6's move, and it is correctly left alone.
- **Nothing else changed.** Every other hunk in the diff matches a round-1 resolution row.

## Re-check of the round-1 verdicts (independent)

I re-derived the substantive points instead of relying on round 1:

- **05 C1(b), line count.** Replacing the RAA line by ② and then ③ adds 7 lines: ¬¬φ, LEM, the box on φ, and the box ¬φ, ⊥, φ, followed by ∨E. The fragment of (a) adds 4: LEM, the box on φ, ⊥E appended to the given box, and ∨E. So it saves exactly 3 lines: ¬¬φ, k + 2 and k + 3. Line k + 4 survives. The text is correct.
- **04 C2(a).** The proof at 04:320 uses y ≥ 0 twice: to get x > 0 from x > y ≥ 0, and to get y² ≤ xy. Its other multiplication is by the derived x > 0. The pair x = −3, y = 1 refutes (⇒) and differs from the remark's pair (−2, 1). The sidecar checks the whole family x < −y ≤ 0. The remark's wording, "(⇐) used only y ≥ 0", supports the item's "the remark … says that (⇐) survives".
- **06 check 1 / `exm-search-distribute`.** Line 7 is at top level above lines 8–11, so it is available. "1, 7, 8, 9" is right.
- **06 failed search.** "Step 5 at the goal further out" is true. The RAA box on ¬(Q → P) asks only for Q → P, and step 2 reopens the box on Q with goal P. "Affirming the consequent (Section 1.4), the step that would repair Argument B" matches ch01 04:82 verbatim in substance. The warning at 06:491 keeps "converse error" in Ch 1's sense (ch01 05:686). That usage is correct.
- **Other round-1 items.** 03:299/319 and 06:664 now use one name, "or commutes". 05:221 "needs no RAA" is correct (`prp-contrapositive`). The 05 C3 primitive list now includes ↔I and ↔E. 06 C2 Hint 2 names both forms of step 5 without executing either. 06 C4 now describes our route and makes no necessity claim.
- **NOTATION and STATUS rows.** `d \mid n` first appears at ch02 04:556. The Ch 2 promise rows are accurate.

I agree with every round-1 verdict except one refinement, N2 below.

## New finding

| # | file:line | verdict | evidence and fix |
|---|---|---|---|
| N2 | 01:58 (`def-rules-contradiction`, reading paragraph) | minor | The S5 fix says: "Apart from being assumed, the only way \( \bot \) first appears is by \( \rulename{\neg E} \)". Read literally, this is false: from a line P, ∨I (@def-rule-disjunction-introduction, whose second disjunct is "any statement") writes P ∨ ⊥, so ⊥ appears without ¬E and without being assumed. The claim is true of a **line** \( \bot \). The sentence's own gloss says so ("whose new line is always ⊥"), and so does the next paragraph ("A line ⊥ can stand only…"), so this is a matter of precision, not of substance. **Fix (two words):** "the only way a line \( \bot \) first appears is by \( \rulename{\neg E} \)". |

## Earlier reviews (ch01v2-*)

The round-2 edit touched only 06:62. None of the round-1 spot-checked items has returned: 05:79, 03:126, 04:209, 04:326, 06:711, 05:920, 05:262, 04:227, 04:591 and 06:1030.

## Critical checks (on the round-2 text)

- **Rule order.** The step-2 clause uses ∨I, ¬E and ⊥E, all of which are available by §06.
- **Necessity claims.** No new claim that something needs RAA or is not derivable.
- **Search method.** The step-5 clause, the side-choice exception, `exm-search-raa` and C3 are mutually consistent.
- **Derived-rule name.** §03 and the §06 table both say "or commutes".

## Summary (round 2)

- N1 is fixed correctly.
- The 32 round-1 "fixed correctly" verdicts are confirmed on independent re-derivation.
- There is one new `minor` finding, N2: a two-word precision fix at 01:58.
- There is no error or gap, and no unintended change.
- Chapter 1 changes needed: none.
