# Chapter 1 (connectives-and-derivations): S7 re-referee (fresh), round 1

**Scope:** the uncommitted diff to `src/ch01-connectives-and-derivations/`, `verify/ch01/`, `authoring/STATUS.md` and `authoring/NOTATION.md`, checked against every finding of `ch01-S5-A.md`, `ch01-S5-B.md` and `ch01-S6.md` and their Resolution sections. I had not written or reviewed Chapter 1 before this. `src` was only read. Verdicts are recorded in `authoring/ledger/ch01.yaml` (stage S7r, `--by rereferee`).

**Build copy:** `/tmp/claude-1000/-home-akizumi-coding-analysis/8d99e54f-c6f3-4bed-98e0-b546ef5dc565/scratchpad/S7r-ch01/repo` (rsync, with `.venv` and `_build` excluded).

**Gates re-run:**
- `check_fitch.py src/ch01-connectives-and-derivations`: 119 derivations (7 expect-invalid, 29 schema), 0 errors.
- `check_numbers.py 1`: 39 sidecars, 0 fatal, 3 advisory.
- All `verify/ch01/*.py` sidecars exit 0.
- `check_structure.py`: 0 fatal, 5 advisories. All five are word counts, which the author's direction exempts.
- `check_notation.py`: 0 advisories.
- `check_forward_deps.py`: 0 load-bearing forward citations. There are 2 dangling citations, both from Ch 3 (drafted concurrently) and neither from Ch 1.
- `./build.py html` succeeds.
- `check_rendered.py`: 0 errors, 0 warnings.
- `promises.py --reconcile`: no unrecorded pointer from Ch 1. The remaining pointers come from Ch 2 and Ch 3.
- `ledger.py stale 1`: 0 before I recorded my verdicts.
- The new derivation in the §06 A1 (d) answer (P, (P∨Q)→(R∧S) ⊢ S, 5 lines) also passes `check_fitch`.

**Critical check after the edits:**
- No changed or added line uses `\open`, `\ii`, `\oi` or `\oe`.
- §02–§04 still contain no `\open`.
- There is no negation, ⊥, ↔ or RAA rule macro anywhere in the chapter.
- The only new derivation-like content is §06 A1 (d), which uses ∨I, →E and ∧E. All three are available in §06.

**Earlier findings that must not come back:**
- v2 S8 row 3 (rule tags set several ways) is now fixed. No plain `\( \wedge \)E`-style tag is left in the chapter.
- The v2 "the one place" finding (06:247) is still fixed.

**Unintended changes:** none in `src` or `verify`.
- §03–§04: I paired every changed line with its old version after normalising `\rulename{…}`. Only five lines changed content: 03:100, 03:248, 03:376, the C1 scheme bullet, and a ledger re-filing. Each belongs to a finding. All 102 tag conversions are correct (`∧I/∧E` → `\rulename{\wedge I/E}`, `→E` → `\rulename{{\to}E}`).
- §01, §02, §05, §06, §07 and the four sidecars: every hunk belongs to a finding below.
- `NOTATION.md` also gains nine Ch 3 rows (atoms p, q, r; ∘; Γ, Δ; height, atoms, len, ex, nodes/neg; P(n)). They belong to the concurrent Ch 3 drafting, not to this revision. They are consistent with the new φ, ψ, χ row: from Ch 3 on, φ, ψ, χ are formula metavariables. So they are not a Ch 1 regression. I did not referee them.

**Counts:** 24 finding rows re-checked (S5-A 4 + 1 out-of-scope note; S5-B 13, rows 1–12 and 14; S6 6). The results:
- Fixed correctly: 21.
- Fixed with new problems: 1 row (S6 finding 5), which introduced two new minor problems, N1 and N2.
- Accepted deferrals outside what S7 may edit: 2 (S5-B row 14, S6 finding 6).
- Not fixed: 0.

There is one partial dispute (S6 finding 5, §05 A1 (e), the nesting half). I side with the reviser; see below.

## S5 Referee A

| Finding | Verdict | Evidence |
|---|---|---|
| 03:100, goal \(a<d\) | fixed correctly | Now "from the goal \(u<z\) of part (c) of @exm-chaining-derivation". Part (c) has premises \(u<v, w<z, v<w\) and goal \(u<z\), and it is the backward search in §02. |
| 05:157, "exactly the boxes containing" (a box contains itself) | fixed correctly | Now "the boxes other than itself that contain it are **exactly** the boxes containing line \(k\)". This agrees with every worked availability check (05:244, the curry note at 05:427, 07:198). It also matches how Ch 3 uses it: ch03 05-soundness:83–85 reads "the boxes containing \(B\)" as excluding \(B\) ("\(C = B\), or \(C\) is one of the boxes containing \(B\)"). The paraphrase at 05:190–198 still matches. *Note for the coordinator (optional):* ch03 05:83 could quote the new wording. |
| 06:100, \(Q \nvdash P\) with no pointer | fixed correctly | Now "with \(P\) false and \(Q\) true, a derivation would lead from a true premise to a false conclusion, and Chapter 3 proves that no derivation does." This is true, the pointer is prose only, and it matches the flag at 07:625. |
| 06:204, "no rule can take \(R\) out of them" | fixed correctly | The letter argument is gone. The box would need \(R\) "from the premise \(P\to Q\) and the assumption \(P\) alone". Those are the only lines available in (c)'s box (lines 1 and 2). The instance \(x = 2.5\) with \(P: x>2\), \(Q: x>1\), \(R: x>3\) makes \(P\to Q\) and \(P\) true and \(R\) false, so the non-derivability claim is now justified semantically, with a Ch 3 pointer. |
| Out of scope: pre-split sidecars in `verify/ch01/` | fixed correctly | `verify/ch01/` holds only Ch 1 labels. `check_numbers` finds no orphan. |

## S5 Referee B

| Row | Verdict | Evidence |
|---|---|---|
| 1 (gap), STATUS promise table | fixed correctly | `--reconcile` reports no unrecorded Ch 1 pointer. I spot-checked the new Ch 1 → Ch 2 row: `prp-vacuous-implication` is at ch02 01:154 (Section 2.1), `def-derived-rule` at 03:100 (2.3), `def-provable-equivalence` at 04:217 (2.4), `thm-square-even-implies-even` at 01:283, and "finding derivations" is §06 (2.6). The re-filed Ch 2 rows (¬¬P, ¬P as P→⊥, lowest terms, differentiable ⇒ continuous) are no longer credited to Ch 1. The new rows point to targets that deliver: Ch 7 even/odd, Ch 16 EVT, and Ch 3 induction and completeness. The pilot paragraph (l.19–24) now says the pilot was split and no longer exists. |
| 2, 02:3 "ended with a slogan" | fixed correctly | "The previous section stated a slogan". True: 01:253. |
| 3, 06:3 / 07:3 "ends with a goal" | fixed correctly | "Near its end it meets a goal …" / "The previous section met a goal …". True: the stall at 06:259 is followed only by two short subsections and the exercises. |
| 4, 03:376 "one row in each section" | fixed correctly | "the table grows with each new rule". True for §04–§07, including §05's two rows (→I, R). |
| 5, 01:269 "one rule, or one half of a pair" | fixed correctly | Now "introduces **one** rule, except that Section 1.3 introduces the pair of rules for 'and' …". §05 also adds R, but the chapter itself counts R apart from the rules ("six rules … and R", 07:478; R is clause (D3) of `def-derivation`). So the sentence agrees with the chapter's own count. index:15 ("the first two rules") is consistent with it. |
| 6, 01:276 "adds its rule to both" | fixed correctly | "adds its rule to one of them: an introduction rule answers the first question, an elimination rule the second". True for §04 (→E), §05 (→I), §06 (∨I) and §07 (∨E). It matches 03:100 and the table at 07:565–569. |
| 7, 06:204 | fixed correctly | See the S5-A row. |
| 8, rule-name typesetting in §03–§04 | fixed correctly | All 102 occurrences are converted, and the normalised pairing shows no content change. A grep for the plain forms over the chapter returns nothing. The HTML check reports no raw TeX. |
| 9, §01 A1 has seven parts | fixed correctly | (a) and (b) are merged into one "is it a statement" part. The item now has six parts, and the solutions (a)–(f) match the parts. The old (g) answer is now (f) and still answers the connective-table part. The source list numbers are `1. 3. 4. 5. 6. 7.` (a gap left by the merge), but `filters/enumerate.lua` numbers the items from the start value in order, so the rendered labels are (a)–(f). Source hygiene only; not a finding. |
| 10, NOTATION rows | fixed correctly | (a) The φ, ψ, χ row says "introduced Ch 1 §02 after `def-rule-schema`". True (02:82). (b) `\dashv\vdash` → Ch 2 `def-provable-equivalence` (ch02 04:217). (c) `\mathsf{X}` → Ch 2 §05 (the only Ch 2 file that uses it). (d) `def-derivation` is in Section 1.5. (e) \(\abs{x}\) is displayed in §07 (07:9). (f) `d \mid n` first used in Ch 2 §04 C1: 04:556 is C1, and no earlier Ch 2 file uses `\mid`. |
| 11, ledger keys that are not labels | fixed correctly | Re-keyed to `def-statement`, `def-main-connective` and `exm-not-a-derivation`, each "(example)" with a locating phrase. The §03 warning instance is now under `def-rules-conjunction`, where the warning sits. Format is `<label> (<kind>): …`. |
| 12, facts without an `@ref` | fixed correctly | 07 C2 (a) now cites "shown in the solution of @exr-disjunction-and-cases-c1". C1's solution proves \(\abs{-a} = \abs{a}\) at 07:752, and C1 comes before C2. The §01 A1 ledger line "x² − 1 = 0 exactly when x = ±1; 0² − 1 = −1" is added. |
| 14, mdframed split warnings | accepted deferral | This is engine-side (`latex/`, `filters/`) and outside what S7 may edit. `check_rendered` on the HTML is clean. It stays on the coordinator's engineering list. |

## S6

| Finding | Verdict | Evidence |
|---|---|---|
| 1 (gap), `check_numbers` fails | fixed correctly | The three QUOTED strings now occur verbatim in the text: 06:249, the §06 product fact, and 06:361. `check_numbers 1` gives 0 fatal. The retired and Ch 2 sidecars are gone from `verify/ch01/`. |
| 2, B2 (e)/(f) answered in the prose | fixed correctly | The prose now works from \(y<5\). Each of its claims is true of Sh (\(a<b \Rightarrow a+c<b+c\)): \(y+1<5+1\) and \(y+x<5+x\) are instances; \(y+1<5+2\) is not (c inconsistent); \(y+1<6\) is a different string. B2 (premise \(x<3\), candidates \(x+1<3+2\), \(x+y<3+y\)) is no longer printed in the prose, and B2 itself is unchanged. |
| 3, C1 scheme rewards one route | fixed correctly | The first bullet now also accepts the argument that goes down the derivation line by line. The premise case still gets its own bullet ("rules out a premise"), so the scheme still sums to 10 and covers both routes fairly. |
| 4, C4 Hint 2 gives the move | fixed correctly | Hint 2 now asks "What can you do with the one disjunction available?" and no longer states the split. It is close to Hint 1, but it adds the current goal \(S\) and the fact that nothing gives \(S\) at once. The ladder is weak but no longer does the move for the reader (STYLE §11.7). |
| 5, comprehension parts answered in the prose | **fixed, with two new minor problems** (§05 A1 (e), §06 A1 (d)); the rest fixed correctly | **03 A1 (d):** 03:248 now states only the general rule ("every line must come after each line it cites"). This is true, and the part now needs the reader to find the citation. **07 A1 (c):** the new part is fair and correct. The quoted "proof" treats only even \(n\). \(n = 1\) gives \(n^2 = 1\) odd, so the conclusion is false. The sidecar asserts this, and the ledger lists \(1^2 = 1\). **05 A1 (e), availability half: new minor N2** (below). **05 A1 (e), nesting half (partial dispute):** I side with the reviser. The blueprint mandates this part (ch01.md §05 A1), and the blueprint binds this stage. It is an A-level recall part. No further escalation is needed unless the coordinator wants one. **06 A1 (d): new minor N1** (below). |
| 6, check_fitch ∧I citation order (tooling) | accepted deferral | This is in `tools/` and outside S7. The verifier's order-strict run passes every Ch 1 derivation, so the text needs no change. It stays on the coordinator's list. |

## New problems introduced by the fixes

| # | file:line | verdict | problem | suggested fix |
|---|---|---|---|---|
| N1 | 06:363 / 06:374, `exr-disjunction-introduction-a1` (d) | minor | (i) **The stem is false as worded.** "Why is that rule used, although neither the goal nor any statement on the way to it is a disjunction?" But the line the part asks for, line 3, \(P \vee Q\), is a statement on the way to the goal, and it is a disjunction. (ii) **It pre-solves C2.** The new sequent \(P, (P\vee Q)\to(R\wedge S) \vdash S\) is `exr-disjunction-introduction-c2` (a), \((P\vee Q)\to(R\wedge S) \vdash P\to S\), with the box's assumption promoted to a premise. It has the same premise and the same move, and C2 (c)'s "could you have predicted …" is answered in A1 (d)'s solution. An A part should not work a C item two items later. | Word the stem "…, although the goal is not a disjunction?" Use a sequent C2 does not use, e.g. \(Q \wedge T,\ (P \vee Q) \to R \vdash R\): it needs ∧E, then ∨I by the second schema, then →E. |
| N2 | 05:525, `exr-proving-an-implication-a1` (e)/(f) | minor | The new stem of (e) begins "line 5 cites line 4". That hands over half of (f)'s answer ("which rule produces line 5, and which lines does it cite?", answer: →E, lines 1 and 4). The (e) solution itself is correct: line 4 lies in the boxes 2–6 and 3–5, and both contain line 5. The prose at 05:427 explains line 4's own citations, not line 4's availability at line 5, so the rest of the fix works. | Ask only "Why is line 4 available at line 5?", or put (f) before (e). |

Both are minor. Neither touches a derivation, a rule-order constraint or a proof. Round 2 needs to re-check only these two parts.

## Resolution (S7, reviser, round 2, 2026-09-28)

Only the two new problems were open; every other row was verified fixed or accepted as deferred above. Ledger: `exr-disjunction-introduction-a1` and `exr-proving-an-implication-a1`, stage S7 `--by reviser`, 0 stale.

| # | Resolution |
|---|---|
| N1, §06 A1 (d) | **Fixed.** (i) The stem now reads "…, although the goal is not a disjunction?", which is true. (ii) The sequent is now \( Q, \ (P \vee Q) \to (Q \to R) \vdash R \): line 3 \( P \vee Q \) by \( \rulename{\vee I} \) 1 (second schema), line 4 \( Q \to R \) by \( \rulename{{\to}E} \) 2, 3, line 5 \( R \) by \( \rulename{{\to}E} \) 4, 1. I did not take the suggested \( Q \wedge T, (P \vee Q) \to R \vdash R \): its second premise is C2 (b)'s premise, and its derivation is C2 (b)'s alternative route (take \( Q \) from a conjunction, second schema, \( \rulename{{\to}E} \)) with the box removed, so it would still pre-solve C2 (b). The new sequent shares no premise with C2 (a) or (b), needs no box, no \( \rulename{\wedge E} \) and no conjunction, and still has \( \rulename{\vee I} \) as the first line after the premises. The solution no longer argues that the need for \( \rulename{\vee I} \) could be predicted from the premise's shape alone (C2 (c)); it only names the hypothesis that \( \rulename{{\to}E} \) needs. |
| N2, §05 A1 (e) | **Fixed** as suggested. The stem is now "In the first derivation in the proof of @prp-curry, why is line 4 available at line 5? And why is the inner box closed before the outer one?" It no longer says that line 5 cites line 4, so (f) is not half answered. The (e) solution is unchanged and still correct. |

**Gates** (clean copy in `scratchpad/ch01-S7r2/repo`): `./build.py html` and `pdf` (all eight Ch 1 pages) succeed; `./build.py check` passes (378 labels, 1221 references; warnings only spelling and two "Triangle Inequality" name hints, as before); `python3 -m pytest tests -q` 295 passed, 5 skipped; `check_fitch` on Ch 1: 119 derivations, 0 errors; `check_structure 1`: 0 fatal, 0 advisory; `check_numbers 1`: 39 sidecars, 0 fatal; `check_rendered`: 0 errors, 102 warnings, all the known mdframed split in §05 C1's hint box (S5-B row 14, deferred to the engine); `blueprint/originality.py 1`: 0 shared 8-grams; `promises.py --reconcile`: no unrecorded Ch 1 promise (the 13 unrecorded ones are Ch 3's, outside this stage).

## S7 re-referee (fresh), round 2, 2026-09-28

**Scope:** the two problems round 1 left open (N1, N2) and their fixes, plus a check that nothing else in the scoped diff moved since round 1. I had not seen the chapter or round 1 before this pass. `src` was only read. Verdicts are recorded in `authoring/ledger/ch01.yaml` (stage S7r, `--by rereferee`).

**Build copy:** `scratchpad/S7r2-ch01/repo` (rsync, with `.venv` and `_build` excluded).

**What changed since round 1.** Only `05-proving-an-implication.md` and `06-disjunction-introduction.md` have a later modification time than every other file in the scoped diff. Their current hunks against HEAD are the round-1 hunks already accepted (the 05:162 scope rule, the 06:3, 06:100 and 06:204 sentences) plus the two round-2 edits: 05:525 with its (e) solution at 05:539, and 06:363 with its (d) solution at 06:374. The §06 sidecar is the one round 1 accepted. §01–§04, §07, `verify/ch01`, `STATUS.md` and `NOTATION.md` were not touched again. No unintended change.

| # | Verdict | Evidence |
|---|---|---|
| N1, §06 A1 (d) (`exr-disjunction-introduction-a1`) | **fixed correctly** | (i) The stem now says "although the goal is not a disjunction". That is true: the goal is \( R \). (ii) The sequent \( Q,\ (P\vee Q)\to(Q\to R) \vdash R \) is valid, and the solution's derivation is correct: 3 \( P\vee Q \), \( \vee \)I 1, by the **second** schema (\( \varphi \) on the right, 06:36); 4 \( Q\to R \), \( \to \)E 2, 3; 5 \( R \), \( \to \)E 4, 1. The citation order (implication first) matches 06:230. I wrote the derivation out and `check_fitch` passes it. The control run with the first schema (\( Q \vee P \) at line 3) is rejected at line 4, as it should be, so "second schema" in the answer is right. Every claim in the solution is true in context. \( R \) occurs only in premise 2. \( \to \)E fires on it only when \( P\vee Q \) is on a line. Only \( Q \) is in hand. The move is the same as in `exm-or-hypothesis-split`. Uses only \( \vee \)I and \( \to \)E, both available by §06, and needs no box. **No pre-solving:** the sequent shares no premise with C2 (a) \( (P\vee Q)\to(R\wedge S) \) or C2 (b) \( (P\vee Q)\to R \). It needs no \( \wedge \)E and no \( \to \)I. The answer no longer argues C2 (c)'s "could you have predicted" point. It also does not duplicate B1–B3 or any worked example: a grep for \( (P \vee Q) \to (Q \) finds only this item in Ch 1. The part is fair at A level. |
| N2, §05 A1 (e) (`exr-proving-an-implication-a1`) | **fixed correctly** | The stem is now "why is line 4 available at line 5? And why is the inner box closed before the outer one?". It no longer mentions a citation, so (f) (\( \to \)E citing 1 and 4) is not half answered. The (e) answer is true of the `prp-curry` derivation (05:407–419): line 4 lies in the boxes 2–6 and 3–5, both contain line 5, and 4 < 5. The proof prose at 05:422 works the analogous question for a *different* pair (line 4 citing 1, 2, 3), so the reader applies the scope rule rather than recalling a printed answer. That was S6 finding 5's request. The nesting half is unchanged (round 1 accepted the partial dispute). |

**Notes (not findings):**
- *Blueprint wording.* `authoring/blueprints/ch01.md` §06 A1 (d) still reads "in `exm-or-hypothesis-split`, why is \( \vee \)I used …". The delivered part asks the same question of a fresh sequent, to resolve S6 finding 5, and its solution cites that example. The skill tested is the one the blueprint names. The coordinator may want to update the blueprint line to match (outside S7's remit).
- *"Which rule writes the first line after the premises"* assumes the natural derivation. A pedant could write a detour first (R 1, or \( \wedge \)I 1, 1). The "why" half of the question makes the intended reading clear, so I don't count this as a defect.

**Gates re-run (clean copy):**
- `check_fitch` on Ch 1: 119 derivations (7 expect-invalid, 29 schema), 0 errors.
- The §06 A1 (d) derivation passes separately, and the first-schema control fails as expected.
- `check_numbers 1`: 39 sidecars, 0 fatal, 3 advisory.
- All `verify/ch01` sidecars exit 0.
- `check_structure 1`: 0 fatal, 0 advisory.
- `check_notation`: 0 advisories.
- `check_forward_deps`: no proof cites a later section.
- `./build.py html` succeeds.
- `check_rendered`: 0 errors, 0 warnings.
- `promises.py --reconcile`: the 13 unrecorded promises are all Ch 3's; none is from Ch 1.
- `ledger.py stale 1`: 0 before and after recording.

**Round 2 result:** both open problems are fixed correctly. No new problem was introduced and no finding is open. Counting the round-1 table, the 24 finding rows now stand at 22 fixed correctly (with N1 and N2 closed) and 2 accepted deferrals (S5-B row 14 and S6 finding 6, both engine or tooling work for the coordinator). None is left unfixed. S7 exit is met for Chapter 1.
